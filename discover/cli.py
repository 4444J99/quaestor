"""CLI: ``quaestor-discover`` (see ``discover/__main__.py`` for ``python -m discover``).

A bounded, read-only poll of free grant sources. Writes new normalized atoms to
the git-ignored ``atoms/`` store. Nothing here submits, registers, or pays.
"""

from __future__ import annotations

import argparse
import json
import sys

from .runner import FREE_SOURCES, DiscoveryRunner


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="quaestor-discover",
        description="QS-010: read-only grant discovery (free sources first). Never submits or pays.",
    )
    p.add_argument(
        "--source",
        action="append",
        dest="sources",
        metavar="NAME",
        help=f"source to poll (repeatable); default all free: {sorted(FREE_SOURCES)}",
    )
    p.add_argument("--keyword", default="", help="search keyword / focus term")
    p.add_argument("--limit", type=int, default=25, help="max opportunities per source (bounded)")
    p.add_argument("--atoms-dir", default="atoms", help="git-ignored output dir (default: atoms/)")
    p.add_argument("--per-source-cap", type=int, default=50, help="hard per-source cap (loop safety)")
    p.add_argument("--delay", type=float, default=1.0, help="polite seconds between source polls")
    p.add_argument("--dry-run", action="store_true", help="poll + normalize but write nothing")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    runner = DiscoveryRunner(
        atoms_dir=args.atoms_dir,
        per_source_cap=args.per_source_cap,
        polite_delay=args.delay,
    )
    summary = runner.run(
        sources=args.sources,
        keyword=args.keyword,
        limit=args.limit,
        dry_run=args.dry_run,
    )
    json.dump(summary, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
