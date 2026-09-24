"""The discovery runner — POLL + ATOMIZE steps of the autopoietic loop.

Polls enabled **free** source adapters, normalizes results into grant atoms,
dedupes against atoms already on disk, and appends new atoms to a JSONL store
under the git-ignored ``atoms/`` directory. Bounded per the loop contract
(``plans/60-autopoietic-loop.md``): a hard cap per source and a polite delay
between calls. It never crosses the submit/money gates and never wires a paid
source.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from .atom import GrantAtom
from .sources import GrantsGov, ProPublica
from .sources.base import HttpError, PaidSourceGated, Source

# Free sources, wired now. Paid sources (candid, instrumentl) are deliberately
# NOT registered here — they stay gated on the QS-012 cost decision.
FREE_SOURCES: dict[str, type[Source]] = {
    "grants.gov": GrantsGov,
    "propublica": ProPublica,
}

DEFAULT_ATOMS_DIR = Path("atoms")
ATOMS_FILE = "atoms.jsonl"


class DiscoveryRunner:
    def __init__(
        self,
        *,
        atoms_dir: Path | str = DEFAULT_ATOMS_DIR,
        per_source_cap: int = 50,
        polite_delay: float = 1.0,
        sleep=time.sleep,
    ) -> None:
        self.atoms_dir = Path(atoms_dir)
        self.per_source_cap = per_source_cap
        self.polite_delay = polite_delay
        self._sleep = sleep

    # ------------------------------------------------------------------ store
    @property
    def store_path(self) -> Path:
        return self.atoms_dir / ATOMS_FILE

    def _load_seen_ids(self) -> set[str]:
        path = self.store_path
        if not path.exists():
            return set()
        seen: set[str] = set()
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict):
                continue
            record_id = record.get("id")
            if isinstance(record_id, str) and record_id:
                seen.add(record_id)
        return seen

    def _append(self, atoms: list[GrantAtom]) -> None:
        self.atoms_dir.mkdir(parents=True, exist_ok=True)
        with self.store_path.open("a", encoding="utf-8") as fh:
            for atom in atoms:
                fh.write(json.dumps(atom.to_dict(), ensure_ascii=False) + "\n")

    # ------------------------------------------------------------------- poll
    def build_source(self, name: str, fetch=None) -> Source:
        name = name.strip().lower()
        if name in FREE_SOURCES:
            return FREE_SOURCES[name](fetch=fetch)
        # A recognized-but-paid source fails loudly and specifically.
        if name in {"candid", "instrumentl"}:
            raise PaidSourceGated(
                f"source '{name}' is a PAID source, gated on the QS-012 cost decision; not wired"
            )
        raise KeyError(f"unknown source '{name}' (free sources: {sorted(FREE_SOURCES)})")

    def run(
        self,
        *,
        sources: list[str] | None = None,
        keyword: str = "",
        limit: int = 25,
        dry_run: bool = False,
        fetch=None,
    ) -> dict:
        """Poll ``sources`` (default: all free), atomize, dedupe, persist.

        Returns a summary dict. ``dry_run`` performs the full poll+normalize but
        writes nothing to disk (safe preview).
        """
        names = sources or list(FREE_SOURCES)
        seen = self._load_seen_ids()
        new_atoms: list[GrantAtom] = []
        per_source: dict[str, int] = {}
        errors: dict[str, str] = {}
        run_seen: set[str] = set()

        for i, name in enumerate(names):
            try:
                source = self.build_source(name, fetch=fetch)
            except PaidSourceGated as exc:
                errors[name] = str(exc)
                continue
            cap = min(limit, self.per_source_cap)
            try:
                atoms = source.search(keyword=keyword, limit=cap)
            except HttpError as exc:  # a dead source never kills the run
                errors[name] = str(exc)
                atoms = []
            added = 0
            for atom in atoms:
                if atom.id in seen or atom.id in run_seen:
                    continue
                run_seen.add(atom.id)
                new_atoms.append(atom)
                added += 1
            per_source[name] = added
            if self.polite_delay and i < len(names) - 1:
                self._sleep(self.polite_delay)

        if new_atoms and not dry_run:
            self._append(new_atoms)

        return {
            "sources_polled": [n for n in names if n not in errors],
            "new_atoms": len(new_atoms),
            "per_source": per_source,
            "errors": errors,
            "dry_run": dry_run,
            "store": str(self.store_path),
            "atoms": [a.to_dict() for a in new_atoms] if dry_run else [],
        }
