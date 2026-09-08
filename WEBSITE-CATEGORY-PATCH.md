<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# veraxis.io Category Patch — to be applied later

**Work order:** CAT-ALIGN-001
**Controlling source:** [THESIS.md](THESIS.md) — Veraxis Category Thesis v1.0
**Status:** NOT APPLIED. Prepared for later application by someone with access to the site source.

## Why this document exists instead of a website change

Work order CAT-ALIGN-001 section IX authorizes a website patch **if and only if** the source that
deploys veraxis.io is available and clearly identified. It is not, for two independent reasons:

1. **No website source exists in the reachable repository set.** All 14 repositories the executing
   account can access were enumerated and searched for `index.html`, any `.html`, `CNAME`,
   `_config.yml`, `netlify.toml`, `vercel.json`, `next.config.*`, `astro.config.*`, and for
   GitHub Pages deployment workflows (`actions/deploy-pages`, `peaceiris/actions-gh-pages`,
   `github-pages`). **Zero matches.** The site is deployed from somewhere outside this set — a
   hosted site builder, a private repository, or an account this session cannot reach.
2. **The live site could not be read.** A fetch of `https://veraxis.io` was refused by the network
   egress policy (`EGRESS_BLOCKED`). Per the proxy contract that denial was reported, not retried
   or routed around.

Consequently the "current copy" column below **cannot be filled in from evidence** and is left
explicitly empty rather than reconstructed from memory or assumption. The proposed copy is exact
and owner-specified; the current copy must be captured by whoever holds site access before the
diff is applied.

No unrelated repository was modified as a substitute.

## What must change, structurally

The failure being corrected is ordering, not accuracy. The site currently makes evidence and
Authorization Evidence Packs easier to recognize than the upstream institutional-authority
computation that gives them meaning. Two external events demonstrated it: an independent
AI-assisted evaluation of VEIP that centered on the Authorization Evidence Pack, and an executive
discussion that opened on authority/permission computation and drifted to AEP security and
evidence.

So the requirement is a placement requirement: **the authority statement must appear above the
first evidence/AEP-heavy explanation on the page.** Adding the text lower down does not fix it.

## Block 1 — the missing computation

**Location:** immediately above the first evidence-, receipt-, or AEP-oriented explanation on the
page. If the hero already carries an evidence-first message, this replaces the hero's leading
explanation and the evidence message moves below it.

**Current copy:** _(not captured — see above; fill in before applying)_

**Proposed copy, exact:**

> The missing computation is authority.
>
> Enterprise policy is written for humans. Before an agent can act on it, an institution must
> establish what the governing source means, who may admit that meaning, where it applies, whether
> it remains current, and what exact machine action it authorizes.

## Block 2 — evidence in its place

**Location:** immediately after Block 1, before or alongside the existing evidence explanation.

**Current copy:** _(not captured — fill in before applying)_

**Proposed copy, exact:**

> Evidence comes downstream. VEIP preserves and binds machine-operational authority into runtime;
> Evidence Packs record the resulting authorization and execution relationship. They do not create
> the institutional authority being proved.

## Block 3 — the architecture sequence

**Location:** wherever the site shows a product or architecture diagram. If none exists, add one.

The sequence must read, in this order:

```
source
  → admission
  → OIC
  → authority/control state
  → VEIP
  → enforcement/runtime
  → exact action
  → Evidence Pack
  → consequence/examination
```

Any existing diagram that begins at the runtime, the gate, or the Evidence Pack is the specific
defect this work order exists to correct.

## Claim constraints on the applied copy

These bind whoever applies the patch. They are not optional stylistic guidance.

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

## Acceptance

Once applied, run the seven-question gate in
[governance/CATEGORY-PERCEPTION-GATE.md](governance/CATEGORY-PERCEPTION-GATE.md) against the live
page as the sole artifact, and record the result with the page URL and retrieval date. The page
passes only if a reader given nothing but that page answers "Open Institutional Computation" to
question 1 and "no" to questions 6 and 7.

## Open item for the owner

The location of the veraxis.io source is unresolved. Identifying it — repository, hosting platform,
or site builder — is a prerequisite for applying this patch, and is the single blocking dependency
recorded against the website portion of CAT-ALIGN-001.
