# Hard problems — an honest accounting

> A grant-machine sounds clean on a diagram. Here is what is genuinely hard, where it can
> fail, and how quaestor mitigates each. No hand-waving.

---

## 1. Eligibility before formation

**The problem.** quaestor's richest lane — US foundation and federal grants for Cind & Sol —
mostly requires an **established 501(c)(3)**, often with SAM.gov registration and a few years
of Form 990 history. Cind & Sol doesn't exist yet. So the highest-value applications can't be
submitted at all until formation (registry QS-017 ↔ Cind & Sol CS-004).

**Mitigation.** Do the work that *doesn't* need formation: build read-only discovery,
map/rank funders, pre-draft reusable narrative, and specifically hunt **fiscal-sponsorship**
and **international/community-led** funders (IAF, IDB, direct-to-grassroots foundations) that
accept pre-formation or sponsored applicants. Be honest in every draft about formation status.

## 2. Application quality

**The problem.** Foundations reject most applications. A generic, AI-flavored, or off-target
application is worse than none — it can sour a funder for years. Good grant-writing is a
craft: funder-specific, evidence-backed, in a credible institutional voice.

**Mitigation.** Optimize for **few strong drafts**, not volume. Reuse a human-vetted
narrative library. Quote the funder's own questions and limits. Mark every fact a human must
supply as `[HUMAN: …]`. Keep the human-review gate mandatory — a person always makes it real
before it goes out.

## 3. Deadline tracking

**The problem.** Grants are deadline-driven and the deadlines are scattered across dozens of
portals, PDFs, and emails. A grant missed by a day is a year lost. Awards then create *more*
deadlines (interim/final reports, renewals).

**Mitigation.** Treat deadlines as the highest-value, lowest-tech output (Stage 5). Normalize
every atom's deadline, surface ranked by urgency × fit, and track post-award reporting duties
as first-class deadlines.

## 4. Avoiding low-fit spam

**The problem.** It is easy to generate hundreds of "matches" that are technically grants but
a poor fit — wasting human review time and funder goodwill. Volume is a vanity metric.

**Mitigation.** Hard **disqualify** on eligibility and mission mis-fit (not just a low score),
**high-fit-only** as the default threshold (QS-012), and a transparent fit score the human can
inspect. Refuse to manufacture drafts to "look busy" on idle beats.

## 5. API access & cost

**The problem.** The best foundation data (Candid / Foundation Directory) and the best
match/track tooling (Instrumentl) are **paid subscriptions**. Free sources (Grants.gov,
ProPublica 990) are shallower or lag 1–2 years. Paid usage is spend, which is human hand.

**Mitigation.** Free sources first (Grants.gov, ProPublica Nonprofit Explorer). Gate paid
sources behind an explicit cost decision (QS-012 covers aggressiveness; a paid-source spend is
human hand). The Candid MCP connector exists in this environment but is **not invoked** until
that decision is made. Evaluate build-vs-buy honestly: if Instrumentl already does match+track
well, buying it may beat rebuilding it.

## 6. Mission drift via the money

**The problem.** Chasing whatever is fundable can quietly bend a mission toward the grants
instead of the goal — e.g. pursuing clinical/research money for a campus that is explicitly
**peer support, not clinical care**.

**Mitigation.** Encode the beneficiary's `explicitly_not` list as a **disqualifying filter**
(Stage 2), not a soft penalty. quaestor finds money *for the mission as defined*, and refuses
fits that would distort it. The human, not the funding landscape, sets the mission.

## 7. Trust, fraud, and authority

**The problem.** Applications assert facts about a real organization and real money. Inventing
a budget number or a track record is fraud. An LLM stating eligibility as settled fact is a
liability.

**Mitigation.** Structural refusal to fabricate facts (placeholders only). Everything that
reads as a legal/tax/eligibility assertion is marked `confirm-with-counsel`. Submission and
money are permanent human-hand gates. quaestor is an assistant to a human's judgment, never an
authority.

---
*Owned by: `quaestor` (treasury steward). Authored 2026-06-25. None of this is legal/financial advice — confirm with a nonprofit attorney / grant professional.*
