# Master Plan — quaestor, the money-finding organ

> *"Find the money that is already out there, match it, draft it, and put it in a human's hand to send."*

**Status: scaffolding / planned.** This describes a grant-machine that does not yet run.
No grant APIs have been queried and no accounts created. This plan is the blueprint the
tasked adapter-agents build against.

> ✅ **"MPO" resolved (2026-06-25):** = NPO / "Non-Profit Organization" — Anthony's spoken
> term, apposed to "the non-profit"; found in zero written text. The nonprofit = Cind & Sol;
> **quaestor** = its money-finding engine. Name kept. This repo owns the concept. Reversible
> via `surfaces/decisions.html` (QS-009).

---

## What quaestor is (and is not)

quaestor finds **external money** — grants from foundations, governments, and international
funders — and walks each opportunity down a pipeline until a human can submit it. It is the
**outside-money** complement to the fleet's **inside-money** organs:

| Organ | Money it finds |
|-------|----------------|
| `organvm/the-invisible-ledger` | internal **product** revenue |
| limen **revenue-backlog** organ | internal **idle-capacity** revenue work |
| **quaestor** (this organ) | **external grant** revenue — foundations, government, international |

quaestor does **not** duplicate the two above. If a task is "monetize a product we built,"
that is the-invisible-ledger's lane. If a task is "find a foundation that funds healing
campuses," that is quaestor's.

## Who it feeds, in order

1. **Cind & Sol Foundation first** — the Panama healing & reintegration campus
   (`organvm-vi-koinonia/cind-and-sol-foundation`). It is the clearest grant-eligible
   mission in the fleet once its 501(c)(3) exists.
2. **The wider fleet second** — other organs/ventures with a grant-shaped need.

## The pipeline (the whole machine)

```
discover ─▶ match-eligibility ─▶ draft ─▶ [ HUMAN REVIEW ] ─▶ submit (HUMAN HAND) ─▶ track
```

| Stage | Plan | One line |
|-------|------|----------|
| **discover** | `10-discover.md` | Poll funding sources read-only; emit a grant *atom* per opportunity. |
| **match-eligibility** | `20-match-eligibility.md` | Score each atom against a beneficiary profile; drop low-fit. |
| **draft** | `30-draft.md` | Draft an application into a queue — never auto-sent. |
| **human review** | `40-review-and-submit.md` | A person reads the draft. **Mandatory gate.** |
| **submit** | `40-review-and-submit.md` | **HUMAN HAND.** A person submits on the funder's portal. |
| **track** | `50-track.md` | Deadlines, decisions, awards, reporting obligations. |

The **per-heartbeat loop** that drives this is `60-autopoietic-loop.md` (declared, not yet
wired). The **honest list of what is genuinely hard** is `90-hard-problems.md`.

## The two permanent gates (never crossed by the machine)

1. **Submitting any application is human hand.** The organ drafts and surfaces; a person
   reviews and submits. No "high-confidence auto-submit." Ever.
2. **Moving or receiving any money is human hand.** quaestor never touches funds, accounts,
   or payment rails.

These are not Phase-Zero caveats that relax later — they are permanent invariants
(registry items QS-015, QS-016) and they live in the README, the manifest, and a decision
card.

## Not authoritative advice

Nothing here is **financial, tax, or legal advice**. Eligibility reads and entity-structure
notes are drafts to *bring to* a nonprofit attorney or grant professional. Every such
artifact carries that disclaimer. quaestor's confidence is an input to a human's judgment,
never a substitute for counsel.

## Formation gates eligibility

Most US foundation and federal grants require an **established 501(c)(3)** (often with a few
years of Form 990 history and audited financials). So quaestor's highest-value lane —
US grants for Cind & Sol — is **blocked until Cind & Sol forms** (registry QS-017, tied to
Cind & Sol's CS-004). Until then, quaestor can still:

- build and harden the **read-only discovery adapters** (no formation needed to *read*),
- map and rank the funder landscape,
- pre-draft narrative components (mission, need, model) that any application reuses,
- find the few funders open to **fiscal-sponsorship** or pre-formation applicants.

## How a stage advances

A stage is not "done" when code exists — it is done when **the next stage can stand on it**:
discover is done when match has real atoms to score; match is done when draft has high-fit
candidates; draft is done when a human has something worth reviewing. The loop only advances
*up to* the human-review gate on its own.

---
*Owned by: `quaestor` (treasury steward). Authored 2026-06-25.*
