# Stage 5 — Track

> Deadlines, decisions, awards, and reporting obligations — so nothing is dropped.

**Status: planned.** This stage closes the loop: discoveries become deadlines, submissions
become outcomes, awards become reporting obligations.

---

## What gets tracked

| Thing | Why it matters |
|-------|----------------|
| **Upcoming deadlines** | A grant missed by a day is a year lost. The single highest-value, lowest-tech win quaestor offers. |
| **Submission state** | per opportunity: `discovered → matched → drafting → needs-review → approved → submitted → decision`. |
| **Decisions** | awarded / declined / no-response — feeds back into fit-scoring (which funders actually say yes). |
| **Reporting obligations** | an **award creates duties**: interim/final reports, fund-use restrictions, renewal windows. These are deadlines too, and missing them risks the relationship and future funding. |

## Deadline surfacing

Deadlines are surfaced where a human will see them, ranked by urgency × fit. The mechanism
(a surface page like the decisions board, a digest, a calendar push) is an implementation
choice for the wiring issue (QS-008). Tracking data is runtime (`data/`) and **git-ignored**.

## The feedback loop

Outcomes are the organ's learning signal:

- **Awarded** → that funder/profile pairing scores higher next time; reusable narrative that
  won gets reinforced.
- **Declined / ignored** → lower that pairing; if a whole source yields nothing, question
  whether it's worth polling.

This is the "evolve" half of the lifecycle: quaestor gets better at fit over time and asks
the human to review fewer, better-targeted drafts.

## Still no money, still no auto-submit

Tracking an *award* is a record-keeping act. **Receiving** the award, spending it, and
filing the reports are **human hand** (reports may assert facts and trigger payments).
quaestor reminds and drafts; humans act. (QS-015, QS-016.)

---
*Owned by: `tabularius` (registrar). Authored 2026-06-25. Reporting obligations are legal duties — confirm with a grant professional.*
