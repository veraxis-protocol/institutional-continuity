<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Category Perception Results — 2026-09-08

**Work order:** CAT-ALIGN-001B section 6
**Gate:** [governance/CATEGORY-PERCEPTION-GATE.md](CATEGORY-PERCEPTION-GATE.md)
**Controlling source:** [THESIS.md](../THESIS.md)

## Method

Ten surfaces, three independent fresh evaluations each: **30 evaluations**. Each evaluator was a
separate cold session given exactly one artifact path and the seven gate questions. Each was
instructed to read that file only, to search nothing, to use no prior knowledge of the
organization, and to say so explicitly where the artifact did not answer a question.

**Evaluators were never told the expected answers.** They were additionally asked, in their own
words, what they would say the organization's primary business or product is — the question that
actually detects the failure this work order exists to correct.

Rounds 1 and 2 ran against the surfaces as they stood after CAT-ALIGN-001. Round 3 ran after the
two corrections below, and therefore doubles as post-fix verification.

## Headline result

**Zero FAIL indicators across all 30 evaluations.**

Not one evaluator, on any surface, in any round, identified Veraxis primarily as an Evidence Pack,
receipt, or audit-record company. None described VEIP as an Evidence Pack, treated AEP as the
category, or said that VEIP or a runtime originates institutional authority, or that cryptographic
validity establishes institutional meaning.

- **Q1 (category):** "Open Institutional Computation" — **30/30**.
- **Q6 (does VEIP originate authority):** "No" wherever the artifact addressed it — no evaluator
  ever answered yes.
- **Q7 (does cryptographic validity prove upstream validity):** "No" wherever addressed — no
  evaluator ever answered yes.

## Defects found in rounds 1–2, and fixed

### 1. The "OIC" abbreviation collided with the field name

Three evaluators, on three different surfaces, independently reported the abbreviation collapsing
two distinct things. Verbatim:

- *"Two senses appear. As a category, 'Open Institutional Computation.' As a component, 'OIC —
  Open Institutional Compiler'."* (veip-verifier-core, round 1)
- *"the acronym is also used for the category name 'Open Institutional Computation'"*
  (runtime-admissibility, round 1)
- *"it is both the category name … and the named upstream reference path"* (veip-sdk, round 1)

**Fix:** THESIS.md section 9 now carries an explicit abbreviation rule — the field is always
written out and never abbreviated; "OIC" unqualified always means the Open Institutional Compiler.

**Round 3 verification, THESIS.md, asked directly whether the abbreviation is used ambiguously:**
*"No — Section 9 explicitly establishes an abbreviation rule."*

### 2. VEIP was undefined on two of its own downstream surfaces

- veip-registry, round 1: *"VEIP: Never expanded or defined … What VEIP does is not stated."*
  Q6 answered *"unstated for VEIP."*
- veip-registry, round 2: *"The README doesn't spell out VEIP's function directly."*
- veip-verifier-core, round 1: *"The README never defines its function directly."*

**Fix:** both role blocks now expand the acronym and state VEIP's role and its three non-roles.

**Round 3 verification:**

- veip-registry: *"VEIP (Veraxis Execution Integrity Protocol) is the execution-integrity and
  interoperability boundary that binds already-established machine-operational authority/control
  state … does not interpret governing documents, perform institutional admission, or originate
  institutional authority."* Q6: *"No."*
- veip-verifier-core: Q4 answered in full; Q6: *"No. Line 15 explicitly states VEIP 'does not
  originate institutional authority'."*

Both defects are closed.

## Per-surface result

| Surface | R1 | R2 | R3 | Verdict |
|---|---|---|---|---|
| THESIS.md | PASS | PASS | PASS | **PASS** — strongest surface; all seven answered from the text |
| institutional-continuity README | PASS | PASS | PASS | **PASS** — field/architecture distinction read correctly every time |
| veip-spec README | PASS | PASS | PASS | **PASS** |
| veip-sdk README | PASS | PASS | PASS | **PASS** — Q2 answered as the SDK's own boundary, with the upstream gap correctly flagged |
| veip-verifier-core README | PASS, Q4 weak | PASS, Q4 weak | PASS | **PASS after fix** |
| veip-registry README | PASS, Q4/Q6 weak | PASS, Q4/Q6 weak | PASS | **PASS after fix** |
| Institutional-Compiler README | PASS | PASS | PASS | **PASS** — Evidence Pack/AEP absent by design; OIC is upstream of them |
| AuthContract README | PASS | PASS | PASS | **PASS** |
| runtime-admissibility README | PASS | PASS | PASS | **PASS** — VEIP/Evidence Pack absent by design; see accepted limitation below |
| website proposed copy | PASS | PASS | PASS | **PASS** |

## Disagreements, preserved

The gate requires disagreements to be recorded rather than smoothed over.

1. **What the business *is* — genuine divergence.** On veip-spec, rounds 1 and 2 read a
   "standards-and-certification business", noting the spec is given away under CC BY 4.0 while
   certification marks are retained under trademark; round 3 read it plainly as "publishing an open
   technical specification". Same text, materially different commercial inference. Similar split on
   veip-sdk: "a self-declared standards/certification-registry play" (R1) versus "a minimal
   reference implementation SDK" (R3). Neither reading is a FAIL indicator, and the surfaces do not
   have to resolve it, but the ambiguity is real and is recorded.

2. **Q2 varies by surface, as expected.** Component READMEs name their own component's problem
   rather than the field's missing computation. THESIS.md, the ICI README, the OIC README and the
   website copy all name institutional authority computation correctly. Component surfaces are not
   expected to restate the field thesis, and this is not scored as a miss.

3. **An observation several evaluators volunteered.** Multiple independent readers noted that the
   surfaces disclaim a great deal and demonstrate comparatively little — "the actual product is the
   category itself", "pre-product research and governance scaffolding", "the disclaimers about what
   a PASS does not establish are longer than the description of what it does". This is a direct
   consequence of the claim ceilings these repositories deliberately enforce, and it is the correct
   trade at this stage. It is recorded because it is what a careful outside reader actually takes
   away, and the owner should know that.

## Accepted limitations, not defects

- **runtime-admissibility README** mentions neither VEIP nor Evidence Packs, in all three rounds.
  That is correct for its scope: it is a research repository about the runtime
  currentness/admissibility boundary. Adding VEIP vocabulary to make a gate question answerable
  would widen the artifact for the test's benefit rather than the reader's. Q4/Q5/Q7 are recorded
  as unanswerable there by design.
- **Institutional-Compiler README** does not mention Evidence Pack or AEP. Also correct: OIC sits
  upstream of both.

## Claim boundary

This gate measures perception. It establishes nothing about implementation maturity, validation
status or demonstrated capability, and no result here changes any repository's `STATUS`,
`CLAIMS.md`, capability matrix or benchmark position.
