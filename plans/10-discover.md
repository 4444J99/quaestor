# Stage 1 — Discover

> Poll funding sources **read-only**, emit one normalized **grant atom** per opportunity.

**Status: planned.** No source has been queried and no account created. Building the
adapters is the work of registry item **QS-010** (`status:ready`). This plan is what that
work builds against.

---

## The grant atom (normalized output)

Every source adapter emits the same shape, so downstream stages don't care where an
opportunity came from:

```json
{
  "id": "src:opportunity-id",
  "source": "grants.gov | candid | propublica | instrumentl | nih | nsf | intl",
  "funder": "name of foundation / agency",
  "title": "program / opportunity title",
  "url": "canonical link to the opportunity",
  "amount": { "min": null, "max": null, "currency": "USD" },
  "deadline": "ISO date or 'rolling' or null",
  "eligibility_raw": "verbatim eligibility text from the funder",
  "geography": ["US", "Panama", "international"],
  "focus": ["mental health", "community development", "housing", "..."],
  "requires_501c3": true,
  "fetched_at": "ISO timestamp",
  "fit_score": null
}
```

Atoms are runtime data and are **git-ignored** (`atoms/`). The repo holds the *plan* and the
*adapters*, never the harvested data.

## Sources (cited)

| Source | What it gives | Access | Cost | Notes |
|--------|---------------|--------|------|-------|
| **Grants.gov** | US **federal** grant opportunities (all agencies) | Public REST API (Search2) + bulk XML extract | Free | The canonical federal feed. No 501(c)(3) needed to *search*; most awards require eligible entity status. |
| **ProPublica Nonprofit Explorer** | Form **990** data on ~1.8M US nonprofits (incl. private foundations + their grants) | Public REST API | Free | Best free way to see *who funds what* — read a foundation's past grantees off its 990. Lags ~1–2 yrs. |
| **Candid** (Foundation Directory / GrantSpace, formerly Foundation Center + GuideStar) | Foundation profiles, grant histories, RFPs | API + web; Candid MCP connector available | **Paid** (FDO subscription); some free tiers via library access (FDO Free at partner libraries) | The deepest foundation dataset. Gate on cost — see QS-012. |
| **Instrumentl** | Curated, matched grant opportunities + deadlines for nonprofits | Web app | **Paid** (subscription) | Does much of match/track itself; evaluate build-vs-buy in `90-hard-problems.md`. |
| **NIH** (RePORTER / Grants) | Federal **health research** funding | Public API | Free | Relevant only if a fleet venture is research-shaped; **not** a fit for a peer-support campus (no clinical/research line — see Cind & Sol guardrails). |
| **NSF** | Federal **science/education** funding | Public API | Free | Same caveat as NIH — only if a venture is genuinely research/education. |
| **International / Panama funders** | Healing-campus-relevant funders outside the US | Mostly manual / web | Free–varies | e.g. Inter-American Foundation (IAF, US gov, funds Latin-American community-led development), Inter-American Development Bank (IDB) community grants, private global-health/wellbeing foundations, Panama-based corporate foundations. Many fund **community-led** work directly — a path that does **not** require a US 501(c)(3). |

> The **Candid MCP connector** is available in this environment (`mcp__claude_ai_Candid__*`)
> but is **not invoked now** — querying it is part of QS-010, and any paid usage is gated on
> the cost decision (QS-012). This plan only records that the door exists.

## What requires the 501(c)(3) to exist first

- **Grants.gov / most federal**: applicant must be a registered eligible entity (SAM.gov
  registration, often 501(c)(3) status). → blocked on Cind & Sol formation (QS-017 ↔ CS-004).
- **Most US private foundations** (read via Candid/990): typically fund established 501(c)(3)s,
  often with 990 history. → blocked on formation.
- **Paths that do NOT require it first** (pursue these while formation is pending):
  - **Fiscal sponsorship** — apply *through* an existing 501(c)(3) sponsor.
  - **International/community-led funders** (IAF, IDB, some global foundations) that fund
    grassroots groups directly.
  - **Pre-formation narrative work** — drafting reusable mission/need/model components.

## Adapter rules (hard)

1. **Read-only.** Adapters search and read. They never submit, register, or pay.
2. **Respect terms + rate limits.** Use official APIs; honor ToS, robots, and quotas. No
   scraping a source that forbids it. Cache politely.
3. **Secrets stay out of git.** API keys live in env / the secret store, never committed
   (`.gitignore` already blocks `.env`, `*.key`, `secrets/`).
4. **Cost is gated.** Paid sources (Candid, Instrumentl) are not wired until QS-012 is
   decided. Free sources first.
5. **No accounts now.** Creating any funder/portal/API account is deferred to QS-010 and,
   where it implies spend or identity, is human hand.

---
*Owned by: `explorator` (scout). Authored 2026-06-25. Not legal/financial advice — confirm eligibility with a grant professional.*
