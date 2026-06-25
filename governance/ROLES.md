# Roles — who owns this lifeform

quaestor is run by **tasked organ-agents**, not by any single interactive session. Each
role owns a stage of the pipeline end-to-end: it authors, it keeps current, and it
opens/closes its own issues, branches, and PRs. The interactive session (Claude in chat)
only *orchestrates* and *surfaces decisions* — it does not own the work.

> Convention: every artifact this organ produces names its **owning role** in a footer, and
> every governance issue carries an `owner:*` label. That is what "owned by tasked agents"
> means in practice — traceable authorship + a standing owner for the upkeep.

| Role | Latin handle | Owns | Surfaces / artifacts |
|------|--------------|------|----------------------|
| **Treasury steward** | `quaestor` | The vision, master plan, the human-hand line, hard-problems honesty | `README.md`, `plans/00-master-plan.md`, `plans/90-hard-problems.md` |
| **Scout** | `explorator` | Funding-source map + **read-only** discovery adapters; the grant-atom feed | `plans/10-discover.md` |
| **Eligibility judge** | `iudex` | Eligibility matching + fit scoring (high-fit vs. wide-net) | `plans/20-match-eligibility.md` |
| **Scribe** | `scriba` | Application drafting into a queue — **never auto-sent** | `plans/30-draft.md` |
| **Keeper of choices** | `arbiter` | The decisions surface + the **human-review gate** before any submission | `surfaces/decisions.html`, `plans/40-review-and-submit.md` |
| **Door-builder** | `faber-liminis` | The in-formation landing (the *form* / lure) | `site/index.html` |
| **Registrar** | `tabularius` | The work-item ledger; deadline + outcome tracking; logs, owners, reaps | `governance/registry.json`, `plans/50-track.md`, GitHub issues |
| **Heartbeat** | `vigil` | Wiring this organ into the live limen daemon; metabolize/run/evolve each beat | `organ/manifest.json`, `plans/60-autopoietic-loop.md` |

## Human hands (never auto-executed — surfaced only)

- **Submit** — submitting *any* grant application. The organ drafts and surfaces; a human
  reviews at the mandatory gate and submits. No exceptions, no "low-risk" auto-submit.
- **Money** — receiving or moving *any* funds. The organ never touches accounts or rails.
- **Publish** — making the landing public.

## Not authoritative advice

No role in this organ gives **financial, tax, or legal advice**. Eligibility reads,
entity-structure notes, and deadline interpretations are drafts to *bring to* a nonprofit
attorney or grant professional — never a substitute for one. Every such artifact carries
that disclaimer.

See `LIFECYCLE.md` for how issues → branches → discussions → PRs flow, and
`registry.json` for the live ledger.

---
*Owned by: `tabularius` (registrar). Authored 2026-06-25.*
