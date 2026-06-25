# Stage 3 — Draft

> Turn a high-fit atom into an application **draft**, into a queue — **never auto-sent.**

**Status: planned.** Depends on Stage 2 producing high-fit candidates.

---

## What a draft is

A draft is a complete-as-possible application package, assembled from **reusable narrative
components** plus the specifics of one funder:

- **Reusable components** (write once, reuse everywhere): mission statement, statement of
  need, the program model, organizational background, theory of change, budget narrative
  skeleton. These are the highest-leverage thing quaestor can build *before* formation, since
  every application reuses them.
- **Per-funder specifics**: the funder's required questions, word limits, priorities,
  required attachments, and the tailoring of the narrative to *their* language.

Drafts are runtime output, **git-ignored** (`drafts/`). The repo holds the *templates and
the drafting logic*, never a filled-in application with org/financial details.

## Drafting rules (hard)

1. **Never auto-send.** A draft is a file in a queue with status `needs-human-review`. The
   drafter has no submit capability — see Stage 4.
2. **No fabricated facts.** Budgets, outcomes, headcounts, financials, and credentials are
   **placeholders** a human fills, never invented. A grant application with invented numbers
   is fraud; quaestor must structurally refuse to manufacture them. Placeholders are marked
   `[HUMAN: …]`.
3. **No authoritative claims.** Anything that reads as a legal/tax/eligibility assertion is
   marked `confirm-with-counsel`.
4. **Cite the funder's own words.** Required questions and limits are quoted from the
   opportunity, not guessed.
5. **Honesty about formation.** While Cind & Sol is pre-formation, drafts say so plainly
   ("in formation," "planned") — never imply an entity or track record that doesn't exist.

## Quality, not volume

A bad draft wastes a human's review time and can burn a funder relationship for years.
quaestor optimizes for **few strong drafts**, tightly matched, with the human's reusable
voice — not a flood. (This pairs with the high-fit-only default in Stage 2.)

## Output for the human

Each queued draft carries a short cover note for the reviewer:

- which atom / funder, the deadline, the ask amount,
- the fit score and *why* it scored that way,
- every `[HUMAN: …]` placeholder that still needs a real value,
- every `confirm-with-counsel` flag,
- a one-line honest read: "strong fit / borderline / stretch."

Then it goes to the **human-review gate** (Stage 4) — and stops there until a person acts.

---
*Owned by: `scriba` (scribe). Authored 2026-06-25. Drafts are not legal/financial advice and contain no invented facts — confirm everything with a grant professional.*
