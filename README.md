# quaestor — the money-finding organ

> *"Find the money that is already out there, match it, draft it, and put it in a human's hand to send."*

**quaestor** (Roman magistrate of the public treasury) is an autopoietic **grant-machine**:
a self-keeping organ that continuously **discovers external funding** — foundation,
government, and international grants — **matches eligibility**, **drafts applications**,
**tracks deadlines**, and **surfaces** each opportunity for a human to submit.

It feeds the **Cind & Sol Foundation** first (the Panama healing-campus nonprofit), the
wider fleet second. It is **external money**: grants and funders out in the world. It does
**not** duplicate Anthony's internal product-revenue machinery
(`organvm/the-invisible-ledger`, the limen revenue-backlog organ) — those mine *product*
revenue; quaestor finds *grant* revenue.

> ⚠️ **Name not yet confirmed.** Anthony called this "**the MPO**." I do not know what that
> stands for, so I did **not** assume. The working name is **quaestor**. A decision card
> (`surfaces/decisions.html`) asks him to confirm what "MPO" means and whether to keep
> `quaestor` or rename. **Until he answers, treat the name as provisional.**

---

## The hard line: the organ drafts, a human sends

Two things are **always human hand** — never automated, ever:

1. **Submitting any grant application.** quaestor drafts and surfaces; a human reviews and
   submits.
2. **Moving or receiving any money.** quaestor never touches funds, accounts, or payment
   rails.

There is a **mandatory human-review gate** between *draft* and *submit*. Nothing leaves
this organ as an external application without a person saying yes. Nothing in this repo is
**financial, tax, or legal advice** — every eligibility read or structuring note is marked
*"confirm with a nonprofit attorney / grant professional."*

---

## This repo is an autopoietic lifeform

It is not a folder of documents — it is a self-keeping organ in the `organvm-iii-ergon`
("work / labor") organism. It is **owned and run by tasked agents**, not by any single chat
session:

- **`organ/manifest.json`** — what this organ is and how the fleet metabolizes it each beat.
- **`governance/ROLES.md`** — the agent roles that own each stage of the pipeline.
- **`governance/LIFECYCLE.md`** — how work flows: issue → branch → discussion → PR → merge → log.
- **`governance/registry.json`** — the live work-item ledger (mirrored to GitHub issues).

## The pipeline

```
discover ─▶ match-eligibility ─▶ draft ─▶ [ HUMAN REVIEW ] ─▶ submit (HUMAN HAND) ─▶ track
   │              │                 │            ▲                                      │
   └─ poll funders└─ score fit      └─ draft     └── gate: nothing submits without a yes │
      each beat      vs. profile       queue                                            │
                                                                  deadlines + outcomes ◀┘
```

Each stage has its own plan in `plans/`. The loop is **declared, not yet wired** to the live
limen daemon — wiring is a seeded `status:ready` issue, not done.

## Map of the repo

| Path | What it is | Owner role |
|------|-----------|-----------|
| `README.md` | Vision, the human-hand line, repo map | `quaestor` |
| `plans/00-master-plan.md` | The pipeline, grounded + honest, ties to Cind & Sol | `quaestor` |
| `plans/10-discover.md` | Funding sources (cited) + read-only adapters | `explorator` |
| `plans/20-match-eligibility.md` | Eligibility matching + fit scoring | `iudex` |
| `plans/30-draft.md` | Application drafting (queue, never auto-send) | `scriba` |
| `plans/40-review-and-submit.md` | The human-review gate + submission (human hand) | `arbiter` · `quaestor` |
| `plans/50-track.md` | Deadlines, outcomes, reporting obligations | `tabularius` |
| `plans/60-autopoietic-loop.md` | The per-heartbeat loop (declared, not wired) | `vigil` |
| `plans/90-hard-problems.md` | Honest accounting of what is genuinely hard | `quaestor` |
| `site/index.html` | In-formation landing — the *form* / lure (built, unpublished) | `faber-liminis` |
| `surfaces/decisions.html` | Hanging Anthony choices, with options + pathways | `arbiter` |
| `governance/` | Roles, lifecycle, the ledger, labels | `tabularius` · `vigil` |

## Status

🟡 **Private / scaffolding.** The vision, pipeline plans, landing, and governance are stood
up. **No grant APIs have been queried and no accounts created** — those are seeded as
`status:ready` issues for tasked adapter-building agents. Three things stay in human hands
and are surfaced, never auto-executed:

- **Submitting any application** (`status:human-hand`).
- **Moving or receiving any money** (`status:human-hand`).
- **Publishing the landing** publicly.

See `surfaces/decisions.html` (or GitHub issues labelled `status:human-hand`) for what
currently needs a human.

---
*Form vs. operation: this private repo is the **operation** (the moat). `site/index.html`
is the **form** (the lure) — publish it only when there is something to point people to.*

*Owned by: `quaestor` (treasury steward). Authored 2026-06-25.*
