<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# veraxis.io Category Patch — to be applied later

**Work order:** CAT-ALIGN-001, updated under CAT-ALIGN-001B
**Controlling source:** [THESIS.md](THESIS.md) — Veraxis Category Thesis v1.0
**Status:** NOT APPLIED. The website has **not** been modified. This is an exact patch
specification for later application by someone with access to the site source.

## Provenance of the current copy recorded here

- **Reviewed surface:** `https://veraxis.io` — homepage; the category/hero statement, the "why is
  this the rule" framing, the OIC card, and the VEIP card.
- **Date reviewed:** 2026-09-08.
- **Read by:** the owner, independently, and supplied to this record in work order CAT-ALIGN-001B.
  **Not read by the executing session.** A fetch of `https://veraxis.io` from this environment was
  refused by the network egress policy (`EGRESS_BLOCKED`) and was not retried or routed around, so
  the copy below is quoted as supplied rather than transcribed from the live page. Anyone applying
  this patch should re-verify the exact current strings against the live page first.

## Website source: still unresolved

All 14 repositories reachable by the executing account were searched for `index.html`, any
`.html`, `CNAME`, `_config.yml`, `netlify.toml`, `vercel.json`, `next.config.*`, `astro.config.*`
and GitHub Pages deployment workflows. **Zero matches.** The site is deployed from outside that
set — a hosted site builder, a private repository, or an account this session cannot reach.

Identifying the source remains the blocking dependency for the website portion of this work.

## What is already correct — KEEP

The homepage does **not** need a wholesale rewrite. The category framing is already right, and
these elements should be preserved as they stand:

| Element | Current live copy | Disposition |
|---|---|---|
| Category / hero | "The next $1T AI market is Open Institutional Computation." | **KEEP.** Names the field correctly and first. |
| Missing-computation framing | "Policy engines can execute a rule. The harder question is: why is this the rule?" | **KEEP.** This is the permission-checking vs institutional-authority-computation distinction, stated well. |
| OIC card | source anchoring → candidate meaning → ambiguity → institutional admission → machine-operational control → lineage | **KEEP.** Correct upstream sequence, correctly attributed to OIC. |
| Evidence limitation statement | the site's explicit statement that execution evidence alone does not establish consequence, observation coverage, or later examinability | **KEEP. Do not weaken or remove.** This is one of the strongest claim-control statements on any Veraxis surface. |

The earlier version of this document proposed inserting a "missing computation is authority"
block above the first evidence-heavy explanation. That proposal is **withdrawn**: the live page
already leads with the category and the authority question. Adding it would duplicate correct copy.

## The one demonstrated defect — the VEIP card

The VEIP card currently foregrounds a primary label materially equivalent to:

> **Portable execution evidence**

and asks whether another system can verify what happened.

That makes the evidence artifact the headline for the component whose actual job is the
authority-to-execution binding. It is the specific surface that lets a reader — or an AI
summarizing the page — conclude that VEIP *is* the Evidence Pack. That is the perception failure
this work order exists to correct, and it is the only homepage element that requires a change.

### Proposed replacement card

**Current primary label:** "Portable execution evidence"

**Proposed primary role:** "Execution integrity" (or "Authority-to-execution integrity")

**Proposed card, exact:**

```
### Veraxis Execution Integrity Protocol
Execution integrity

Can a runtime bind the exact action it is about to take to the current
machine-operational authority and warrant state it is entitled to rely on?

VEIP

Authority/control state → exact action → runtime disposition →
execution-integrity binding → verifiable evidence.

Evidence Packs are downstream artifacts. They do not create the institutional
authority they record.
```

Evidence stays on the card — it is genuinely part of what VEIP produces — but it moves to the end
of the sequence, where it belongs, instead of serving as the component's name.

## Claim constraints on the applied copy

These bind whoever applies the patch.

- **Do not claim current functionality beyond repository evidence.** OIC's repository establishes a
  bounded reference implementation; production compilation and runtime authorization remain
  unestablished and its broader production semantic gate remains BLOCKED. Where implementation
  status requires it, use "is developing" rather than "produces".
- All eight preregistered OIC-Bench rows remain `TARGET — NOT MEASURED`, and the comparative target
  remains `PROVISIONAL TARGET — NOT MEASURED — NOT CALIBRATED`. The site must not report a
  benchmark result.
- Do not assert that Google Cloud, Backbase, Fujitsu, or any other party has adopted OIC or VEIP.
- Do not present an Evidence Pack / AEP as the category, as VEIP itself, or as a source of
  institutional authority.
- Do not assert that CAGE, OPA, any runtime, or OIC autonomously creates institutional authority.
- Preserve the exact component names: Open Institutional Compiler (OIC), Veraxis Execution
  Integrity Protocol (VEIP).
- A cryptographically valid Evidence Pack establishes only the bounded cryptographic and
  structural integrity properties actually verified under the applicable schema/profile. It does
  not by itself establish truth, completeness, institutional validity, correct upstream
  interpretation, consequence occurrence, or observation coverage.

## Acceptance

Once applied, run the seven-question gate in
[governance/CATEGORY-PERCEPTION-GATE.md](governance/CATEGORY-PERCEPTION-GATE.md) against the live
page as the sole artifact, and record the result with the page URL and retrieval date. The page
passes only if a reader given nothing but that page answers "Open Institutional Computation" to
question 1 and "no" to questions 6 and 7.
