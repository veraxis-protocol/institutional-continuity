<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# ICI Architecture Constitution

**Field / category:** Open Institutional Computation
**Architecture:** Institutional Continuity Infrastructure

**Status:** PRE-1.0 normative design baseline, v0.2
**Supersedes:** `spec/CATEGORY-CONSTITUTION.md` (ICI Category Constitution, v0.1)

## Change record

Required by [CHANGE-CONTROL.md](CHANGE-CONTROL.md).

1. **Predecessor identity.**
   Path `spec/CATEGORY-CONSTITUTION.md`, blob
   `514ad07939635978ba82e69adac2575c5ce88c63`, at commit
   `549430974b9511261e997f8f67febb7ad99b503a`. Titled "ICI Category Constitution",
   PRE-1.0 normative design baseline. **Preserved, not deleted, not edited in place.**

2. **Successor identity.**
   This document, `spec/ICI-ARCHITECTURE-CONSTITUTION-v0.2.md`, PRE-1.0 normative design
   baseline v0.2, issued under CAT-ALIGN-001B.

3. **Rationale.**
   Open Institutional Computation is the parent field/category. Institutional Continuity
   Infrastructure is the reference end-to-end continuity architecture within that field.
   The predecessor presented ICI as the category itself, which made ICI read as a competing
   parent category on public surfaces and obscured the field the architecture belongs to.

4. **Exact semantic change.**
   **CATEGORY RELATIONSHIP ONLY.** ICI is restated as an architecture within Open
   Institutional Computation rather than as the parent category. Nothing else changes.

5. **Compatibility impact.**
   None. No canonical-chain change. The nine-node chain, the joins, the full-continuity
   rule, the non-collapse rules, bounded-satisfaction semantics, falsifiability and
   implementation neutrality are carried forward unchanged in substance below.

6. **Benchmark impact.**
   None. No change to eligibility, vectors, expected dispositions, schemas, ICTS
   methodology or pass conditions. No implementation gains or loses a score.

7. **Formal-obligation impact.**
   None. No proof obligation in `formal/` is added, removed or altered.

8. **Migration impact.**
   Public references to the ICI constitution should point to this successor. The
   predecessor remains valid historical normative evidence and remains addressable at its
   path and blob.

9. **Claim-ceiling impact.**
   None. Every claim ceiling in `CLAIMS.md` and `STATUS.md` continues to apply unchanged.
   This document makes no maturity, production, benchmark, adoption or legal-effect claim,
   and broadens none.

10. **Owner / design-authority approval.**
    CAT-ALIGN-001B / Arkadiy Miteiko / 2026-09-08.

## Position within the field

Open Institutional Computation is the field concerned with how institutional authority and
institutional meaning become computable: how governing sources, authorized interpretation
and admission produce machine-operational control state that a runtime may act on, and how
that relationship remains examinable afterward.

ICI is the reference end-to-end continuity architecture within that field. It is not a
competing parent category. It defines the canonical chain, the joins, the invariants and the
conformance methodology by which a continuity claim can be falsified.

The controlling category source is [THESIS.md](../THESIS.md).

## Definition

**Institutional Continuity Infrastructure (ICI) is infrastructure for preserving and independently verifying the continuity of institutional authority and meaning from authoritative source through machine consequence and later examination.**

## Canonical chain

> **SOURCE → ADMITTED MEANING → WARRANTED CONTROL → RUNTIME AUTHORITY → EXACT ACTION → CONSEQUENCE → INDEPENDENT OBSERVATION → RECONCILIATION → EXAMINATION**

## Full-continuity rule

A claim of **full Institutional Continuity** requires every mandatory canonical join J1–J8 to be established under the applicable pinned profile and evidence requirements.

A profile may bound **how** a required join is established. It may not redefine full ICI by removing a required join.

`NOT_APPLICABLE` does not satisfy a required join for a full-ICI claim.

`ESTABLISHED_BOUNDED` may satisfy a join only where the exact pinned profile explicitly permits bounded satisfaction for that exact join and states the bound.

## Non-collapse rules

1. source existence ≠ source authority;
2. represented/extracted meaning ≠ admitted meaning;
3. logical warrant ≠ external truth;
4. control eligibility ≠ execution authorization;
5. identity ≠ institutional standing;
6. authorization ≠ execution;
7. execution ≠ consequence;
8. consequence receipt ≠ independent observation;
9. record integrity ≠ population completeness;
10. causal authority ≠ evidentiary authority;
11. correction ≠ historical erasure;
12. vendor availability ≠ historical verifiability.

## Falsifiability

If any required material edge cannot be established, the system must not claim full Institutional Continuity. It may claim the narrower property actually established.

## Implementation neutrality

ICI is larger than any one Veraxis product stack.

Independent systems may implement the same interfaces and joins. Conformance is determined by pinned evidence and benchmark rules, not vendor identity.

## Note on the successor identifier

`spec/` filenames in this repository are otherwise unversioned, and `VERSIONING.md` carries
versions through tags (`ici/vMAJOR.MINOR.PATCH`) and the component-state table in `STATUS.md`,
where the ICI category model is recorded as a v0.1 design baseline.

This successor nonetheless carries `-v0.2` in its filename because `CHANGE-CONTROL.md` requires
the predecessor to be preserved rather than overwritten, so predecessor and successor must
coexist under distinct paths. An unversioned second constitution would leave two similarly
named normative documents with no filename-level indication of which supersedes which. The
version increment follows `VERSIONING.md`'s MINOR semantics: a compatible normative change
during PRE-1.0, with a change-control record, and no incompatible semantic, eligibility or
join-boundary change.
