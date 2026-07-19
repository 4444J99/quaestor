"""Grants.gov adapter — US federal grant opportunities (free, no account).

Uses the public **Search2** REST endpoint. No 501(c)(3) is required to *search*
(most awards require an eligible entity, which the match stage/QS-017 handles).
The search result does not carry award amounts or full eligibility text, so
those atom fields stay ``None``/empty rather than being guessed — a detail fetch
or the match stage fills them later.
"""

from __future__ import annotations

from typing import Any

from ..atom import GrantAtom
from .base import Source

SEARCH2_URL = "https://api.grants.gov/v1/api/search2"


def _iso_date(mmddyyyy: str | None) -> str | None:
    """Normalize Grants.gov ``MM/DD/YYYY`` to ISO ``YYYY-MM-DD`` (or None)."""
    if not mmddyyyy:
        return None
    parts = mmddyyyy.strip().split("/")
    if len(parts) != 3:
        return None
    mm, dd, yyyy = parts
    if not (mm.isdigit() and dd.isdigit() and yyyy.isdigit()):
        return None
    return f"{int(yyyy):04d}-{int(mm):02d}-{int(dd):02d}"


class GrantsGov(Source):
    name = "grants.gov"
    paid = False

    def search(self, *, keyword: str = "", limit: int = 25) -> list[GrantAtom]:
        payload: dict[str, Any] = {
            "rows": max(1, min(limit, 1000)),
            "keyword": keyword or "",
            # "posted" = currently open opportunities; forecasted are upcoming.
            "oppStatuses": "forecasted|posted",
        }
        data = self._fetch(SEARCH2_URL, payload=payload)
        hits = ((data or {}).get("data") or {}).get("oppHits") or []
        atoms: list[GrantAtom] = []
        for hit in hits[:limit]:
            opp_id = str(hit.get("id") or hit.get("number") or "").strip()
            if not opp_id:
                continue
            number = hit.get("number") or opp_id
            atoms.append(
                GrantAtom(
                    id=f"grants.gov:{opp_id}",
                    source="grants.gov",
                    funder=hit.get("agency") or hit.get("agencyCode") or "US federal agency",
                    title=hit.get("title") or number,
                    url=f"https://www.grants.gov/search-results-detail/{opp_id}",
                    deadline=_iso_date(hit.get("closeDate")),
                    # Search results carry no eligibility prose or amounts; leave
                    # honest empties for the match stage / detail fetch to fill.
                    eligibility_raw="",
                    geography=["US"],
                    focus=[],
                    requires_501c3=None,
                )
            )
        return atoms
