"""ProPublica Nonprofit Explorer adapter — free 990 data, no account.

The best free way to see *who funds what*: read foundation/nonprofit profiles
off IRS Form 990 data. This adapter emits **funder-lead atoms** (each matched
organization becomes a lead to research), not dated opportunities — so
``deadline`` and ``amount`` stay null. Focus/geography derive from the org's
NTEE code and state. Data lags ~1-2 years (a documented source caveat).

API: https://projects.propublica.org/nonprofits/api/v2/search.json?q=<query>
"""

from __future__ import annotations

import urllib.parse

from ..atom import GrantAtom
from .base import Source

SEARCH_URL = "https://projects.propublica.org/nonprofits/api/v2/search.json"
ORG_URL = "https://projects.propublica.org/nonprofits/organizations"


class ProPublica(Source):
    name = "propublica"
    paid = False

    def search(self, *, keyword: str = "", limit: int = 25) -> list[GrantAtom]:
        query = urllib.parse.urlencode({"q": keyword or ""})
        data = self._fetch(f"{SEARCH_URL}?{query}")
        orgs = (data or {}).get("organizations") or []
        atoms: list[GrantAtom] = []
        for org in orgs[:limit]:
            ein = str(org.get("ein") or "").strip()
            if not ein:
                continue
            name = org.get("name") or f"EIN {ein}"
            ntee = org.get("ntee_code") or org.get("raw_ntee_code")
            state = org.get("state")
            subsection = org.get("subseccd")
            elig_bits = []
            if ntee:
                elig_bits.append(f"NTEE {ntee}")
            if subsection is not None:
                elig_bits.append(f"IRS 501(c)({subsection})")
            atoms.append(
                GrantAtom(
                    id=f"propublica:{ein}",
                    source="propublica",
                    funder=name,
                    title=f"Nonprofit/foundation profile: {name}",
                    url=f"{ORG_URL}/{ein}",
                    # 990 profile: no opportunity deadline or committed amount.
                    deadline=None,
                    eligibility_raw="; ".join(elig_bits),
                    geography=[state] if state else ["US"],
                    focus=[ntee] if ntee else [],
                    # It's a funder lead, not an opportunity for us to apply to.
                    requires_501c3=None,
                )
            )
        return atoms
