# Stage 4 — Human review & submit

> The mandatory gate. **A person reviews. A person submits. Always.**

**Status: invariant.** This is not a feature to be optimized away — it is the line the
machine never crosses. Registry items **QS-013** (decision: confirm always-on),
**QS-015** (permanent gate: submit), **QS-016** (permanent gate: money).

---

## The review gate (between draft and submit)

Every draft stops at `needs-human-review`. To advance it, a human must:

1. Read the draft and its cover note (fit, placeholders, flags).
2. Fill every `[HUMAN: …]` placeholder with real, true values.
3. Resolve every `confirm-with-counsel` flag (or accept the risk knowingly).
4. Explicitly mark it `approved-to-submit`.

quaestor **cannot** mark a draft approved. There is no code path, flag, or "confidence
threshold" that auto-approves. If the gate could be bypassed, it would not be a gate.

## Submission is human hand

Even after approval, **the human submits** — on the funder's own portal (Grants.gov,
a foundation's application system, email to a program officer). quaestor does not:

- log into funder portals,
- upload or transmit an application,
- e-sign anything,
- create accounts that bind an entity or a person.

quaestor's job ends at *"here is an approved package and the link to submit it."* It then
records the submission *after the human reports it back* (Stage 5).

## Why always-on (QS-013 recommendation)

The recommendation is **always-on, no exceptions**:

- A wrong submission can disqualify an applicant or sour a funder for years.
- Applications assert facts about a real organization and real money — only a person can
  vouch for those.
- "Auto-submit the easy ones" has no safe boundary; the first mistake is unrecoverable.

The decision card asks Anthony to confirm always-on. The default, until he says otherwise,
**is** always-on.

## Money is never touched

Receiving an award, moving funds, payroll, vendor payment — **none** of it runs through
quaestor. The organ finds and drafts; humans and the proper financial/legal rails handle
money. This is permanent (QS-016).

## Not authoritative advice

The reviewer is encouraged — for any non-trivial application, eligibility question, or
fund-use restriction — to **confirm with a nonprofit attorney or grant professional.**
quaestor's read is an input, not a ruling.

---
*Owned by: `arbiter` (keeper of choices). Authored 2026-06-25. Submission and money are human hand, always.*
