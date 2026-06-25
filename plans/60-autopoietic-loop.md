# The autopoietic loop

> How quaestor breathes once it is wired to the live limen daemon.

**Status: declared — NOT yet wired.** Wiring this organ into the heartbeat is registry item
**QS-008** (`status:ready`). This plan describes the loop the wiring builds.

---

## One heartbeat

Each beat, the organ metabolizes (past), runs (present), and — when idle — evolves (future):

```
per beat:
  1. POLL     each enabled source adapter (read-only, rate-limited, free sources first)
  2. ATOMIZE  new opportunities → grant atoms (dedupe against what's already seen)
  3. MATCH    score new atoms vs. active beneficiary profiles; disqualify hard-fails
  4. DRAFT    for high-fit atoms with no draft yet → enqueue a draft (status: needs-review)
  5. SURFACE  upcoming deadlines + drafts-awaiting-review to the human surface
  6. METABOLIZE  fold state into governance/registry.json; reap done; surface blocked
  7. EVOLVE   if the queue is dry → generate ONE bounded work item
              (add a source, refine fit-scoring, draft a reusable narrative component)

  NEVER, on any beat:
    - submit an application        (human hand — QS-015)
    - move or receive money        (human hand — QS-016)
    - cross the review gate         (only a human marks approved-to-submit)
    - create a paid account / spend (gated; human hand)
```

## Bounded, never runaway

The loop obeys the fleet's bounded-work contract:

- **Caps per beat** — a max number of source polls, new atoms, and drafts, so one beat can't
  fan out unboundedly or blow an API quota or token budget.
- **Cheap-first** — free sources before paid; cheap model tiers for triage, escalate only to
  draft high-fit candidates.
- **Idle is fine** — a beat with nothing new is a valid beat (no busywork; don't manufacture
  low-fit drafts to look busy).
- **Stop criteria** — every generated work item states its objective, scope, and done-proof.

## Wiring (QS-008)

To go live, the heartbeat needs:

1. an entry in the limen daemon's organ rotation (declared in `organ/manifest.json`),
2. the read-only adapters built and tested (QS-010),
3. cadence-aware polling (respect each source's reset/quota, like the fleet's vendor
   cadences),
4. the surface destination chosen for deadlines + review queue.

Until then the loop is **declared, not running**. Nothing polls, nothing drafts, on its own
yet — by design.

---
*Owned by: `vigil` (heartbeat). Authored 2026-06-25.*
