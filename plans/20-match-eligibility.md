# Stage 2 — Match eligibility

> Score each grant atom against a **beneficiary profile**; keep high-fit, drop the rest.

**Status: planned.** Depends on Stage 1 emitting atoms. The aggressiveness of the cut
(high-fit only vs. wide net) is a human decision — **QS-012**.

---

## Beneficiary profiles

A profile describes who we are applying *for*. The first profile is **Cind & Sol**:

```json
{
  "id": "cind-and-sol",
  "legal_status": "pre-formation (US 501c3 + Panama entity planned)",
  "geography": ["Panama", "US-fundraising-side"],
  "mission_focus": ["community healing", "reintegration", "peer support",
                    "grief/transition", "community development", "regenerative food"],
  "explicitly_not": ["clinical/medical treatment", "research", "outcome claims"],
  "annual_budget": null,
  "990_history_years": 0,
  "can_receive_via_fiscal_sponsor": "TBD (human)"
}
```

> The `explicitly_not` list matters: Cind & Sol is **community & peer support, not clinical
> care** (its own guardrail). quaestor must **not** chase health-research or clinical-service
> grants for it — that would be a mis-fit that distorts the mission. This is a fit *filter*,
> not just a score.

## The fit score

Each atom gets a 0–1 `fit_score` from transparent, inspectable signals:

| Signal | Direction |
|--------|-----------|
| geography overlap (funder ↔ profile) | + |
| focus-area overlap | + |
| funder's past grantees resemble us (from 990 data) | + |
| amount in a useful range (not too small to bother, not implausibly large) | + |
| deadline far enough out to draft a real application | + |
| **eligibility hard-fail** (requires 501c3 we don't have, wrong country, wrong entity type) | **disqualify** |
| **mission mis-fit** (clinical/research for a peer-support campus) | **disqualify** |

Hard-fails **disqualify** (atom is parked with a reason), they don't just lower the score —
this is how we avoid low-fit spam.

## Aggressiveness — the human knob (QS-012)

- **High-fit only** (recommended default): only atoms above a high threshold reach the draft
  queue. Fewer, better applications; protects human review time and funder relationships.
- **Wide net**: lower threshold, more drafts surfaced. Higher volume, higher noise, more
  human review load, and risk of annoying funders with off-target asks.

Default to **high-fit only** until Anthony chooses otherwise (reversible knob).

## Eligibility is drafted, not decided

A computed "eligible" is a **hypothesis**, never a ruling. Borderline eligibility (fiscal
sponsorship, foreign-applicant rules, fund-use restrictions) is flagged
`confirm-with-counsel` and surfaced — it does **not** auto-advance to drafting as if settled.

---
*Owned by: `iudex` (eligibility judge). Authored 2026-06-25. Not legal/financial advice — confirm eligibility with a nonprofit attorney / grant professional.*
