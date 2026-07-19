"""The normalized grant atom — the single output shape every adapter emits.

Schema is fixed by ``plans/10-discover.md`` so downstream stages
(match-eligibility, draft) never care which source an opportunity came from.
"""

from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from typing import Any


def _now_iso() -> str:
    return datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class GrantAtom:
    """One normalized funding opportunity (or funder lead).

    ``id`` is the stable dedupe key, always ``"<source>:<opportunity-id>"``.
    Unknown numeric/temporal fields are ``None`` rather than guessed — honesty
    over false precision (e.g. amount is rarely in a search result, so it stays
    null until a detail fetch or the match stage fills it).
    """

    id: str
    source: str
    funder: str
    title: str
    url: str
    amount_min: float | None = None
    amount_max: float | None = None
    currency: str = "USD"
    deadline: str | None = None  # ISO date, "rolling", or None
    eligibility_raw: str = ""
    geography: list[str] = field(default_factory=list)
    focus: list[str] = field(default_factory=list)
    requires_501c3: bool | None = None
    fetched_at: str = field(default_factory=_now_iso)
    fit_score: float | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize to the exact JSON shape declared in plans/10-discover.md."""
        return {
            "id": self.id,
            "source": self.source,
            "funder": self.funder,
            "title": self.title,
            "url": self.url,
            "amount": {"min": self.amount_min, "max": self.amount_max, "currency": self.currency},
            "deadline": self.deadline,
            "eligibility_raw": self.eligibility_raw,
            "geography": list(self.geography),
            "focus": list(self.focus),
            "requires_501c3": self.requires_501c3,
            "fetched_at": self.fetched_at,
            "fit_score": self.fit_score,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "GrantAtom":
        amount = d.get("amount") or {}
        return cls(
            id=d["id"],
            source=d["source"],
            funder=d.get("funder", ""),
            title=d.get("title", ""),
            url=d.get("url", ""),
            amount_min=amount.get("min"),
            amount_max=amount.get("max"),
            currency=amount.get("currency", "USD"),
            deadline=d.get("deadline"),
            eligibility_raw=d.get("eligibility_raw", ""),
            geography=list(d.get("geography", [])),
            focus=list(d.get("focus", [])),
            requires_501c3=d.get("requires_501c3"),
            fetched_at=d.get("fetched_at", _now_iso()),
            fit_score=d.get("fit_score"),
        )
