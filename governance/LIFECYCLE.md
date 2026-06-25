# Lifecycle — how work moves through this organ

The full GitHub lifecycle, run by the tasked roles in `ROLES.md`.

```
idea ─▶ issue ─▶ branch ─▶ PR ─▶ review ─▶ merge ─▶ registry log ─▶ (metabolize next beat)
        │                                    │
        └── discussion (open questions) ─────┘
```

## 1. Issue
Every work item is an issue. It carries:
- an `owner:<role>` label (the standing owner from `ROLES.md`),
- a `type:` label (`plan` · `adapter` · `pipeline` · `surface` · `landing` · `governance`),
- a `status:` label (`status:ready` · `status:blocked` · `status:human-hand`).

Items needing a human get `status:human-hand` and are mirrored to `surfaces/decisions.html`
so they show up where Anthony actually looks (the design dictum: hanging choices live on a
surface with options + pathways, never buried in chat).

## 2. Branch
One branch per organ area, named `organ/<role-or-area>` (e.g. `organ/discover`,
`organ/match`). The owning role works only inside its own files.

## 3. Discussion
Open questions, vision threads, and aesthetic/name calls go to GitHub **Discussions**
(enabled on this repo) — not chat. Resolved discussions become issues.

## 4. PR
The owning role opens a PR from its branch. Body states: **what changed**, **owner role**,
**which issue it closes**, and **what a human still needs to decide** (if anything).

## 5. Merge
Green, reviewed PRs that don't break a live surface merge without further asking (standing
merge authority). **Anything that would submit an application, move money, publish public
content, or create an external account waits for an explicit human yes** — these never
merge-and-go.

## 6. Log + metabolize
On merge, the registrar appends the item to `registry.json`. Each heartbeat the organ
metabolizes the ledger: reaps done items, surfaces blocked ones, advances the pipeline
(discover → match → draft → review-gate), and — when the backlog goes dry — generates the
next bounded work item (a new source to add, a fit-scoring improvement) so the lifeform
keeps breathing. The review-gate and money are **never** crossed by the loop.

---
*Owned by: `tabularius` (registrar). Authored 2026-06-25.*
