# `discover/` — QS-010 read-only grant-discovery adapters

Stage 1 of the pipeline (`plans/10-discover.md`): **poll funding sources
read-only, emit one normalized [grant atom](../plans/10-discover.md#the-grant-atom-normalized-output)
per opportunity.** Free sources first; paid sources are gated on QS-012.

## What it is

| File | Role |
|------|------|
| `atom.py` | The normalized `GrantAtom` — the single output shape (exact schema from `plans/10-discover.md`). |
| `sources/base.py` | Read-only `Source` contract + a zero-dependency stdlib HTTP fetcher (injectable, so tests never touch the network). |
| `sources/grants_gov.py` | **Grants.gov** Search2 adapter — US federal opportunities (free, no account). |
| `sources/propublica.py` | **ProPublica Nonprofit Explorer** adapter — free 990 funder leads (who-funds-what). |
| `runner.py` | POLL + ATOMIZE: polls enabled free sources, dedupes, appends atoms to the git-ignored `atoms/` store. Bounded per the loop contract. |
| `cli.py` | `quaestor-discover` / `python -m discover`. |

## Run it (read-only)

```bash
pip install -e '.[test]'
python -m pytest -q                        # hermetic tests (no network)
python -m discover --keyword "mental health" --limit 5 --dry-run   # preview, writes nothing
python -m discover --keyword "mental health" --limit 25            # writes new atoms to atoms/
```

Atoms land in `atoms/atoms.jsonl` — **git-ignored runtime data**, never committed
(the repo holds the plan and the adapters, never the harvested data).

## The hard rules (enforced in code, per `plans/10-discover.md`)

1. **Read-only.** Adapters only search/read. There is no submit/register/pay code path.
2. **Respect terms + rate limits.** Official APIs, a descriptive User-Agent, a polite
   inter-source delay, and a hard per-source cap (`--per-source-cap`).
3. **Secrets stay out of git.** Free sources need no key; nothing here reads or writes one.
4. **Cost is gated.** Requesting a paid source (`candid`, `instrumentl`) raises
   `PaidSourceGated` until the QS-012 decision — it is not wired.
5. **No accounts.** Nothing here creates a funder/portal/API account.

## What is deliberately *not* here yet

- **Amounts / full eligibility text / thematic focus** for Grants.gov opportunities — the
  search endpoint doesn't return them, so those atom fields stay `null`/empty (honest) for a
  later detail-fetch or the match stage (QS-004) to fill, rather than being guessed.
- **Paid sources** (Candid, Instrumentl) — gated on QS-012.
- **The heartbeat wiring** (QS-008) — this module is the POLL/ATOMIZE the loop calls;
  wiring it into the live limen daemon is QS-008's job.
