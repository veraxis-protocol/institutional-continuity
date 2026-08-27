<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# ICTS Specification — Methodology Baseline

**Status:** PRE-1.0 normative design baseline for methodology. Reference implementation is not included in the bootstrap.

## 1. Evaluation object

A pinned evaluation identifies at minimum:

- subject/system identity and version;
- ICI/ICTS criteria version;
- compatibility profile identity/version;
- evidence references;
- applicable join results;
- applicable invariant results;
- environment/runner identity when executable evaluation is used;
- exact canonical artifact identities/digests required by the profile.

## 2. Join set

Full ICI requires exactly J1–J8.

A structurally incomplete, duplicated, unknown, or otherwise malformed join set is not a valid full-ICI evaluation input.

Malformed/unevaluable input should result in a typed **REFUSED** verifier disposition, not a substantive `NOT_CONTINUOUS` judgment.

## 3. Join statuses

Substantive join statuses are defined by `spec/STATUS-VOCABULARY.md`.

For full ICI:

- `ESTABLISHED` satisfies a required join;
- `ESTABLISHED_BOUNDED` satisfies it only when the exact pinned profile permits bounded satisfaction for that exact join;
- `NOT_ESTABLISHED`, `REFUTED`, `NOT_EVALUATED`, `NOT_APPLICABLE`, and `INDETERMINATE` do not satisfy the join.

## 4. Cross-cutting invariants

Mandatory invariant classification comes from benchmark-controlled criteria/profile state, not from the evaluated subject's self-assertion.

A mandatory invariant failure blocks a full-ICI success.

## 5. Dispositions

A verifier may expose three aggregation dispositions:

- `CONTINUOUS`
- `NOT_CONTINUOUS`
- `REFUSED`

`REFUSED` means the input could not be validly evaluated under the pinned contract.

## 6. Evidence

Every positive result must reference evidence sufficient for the exact scope claimed.

A valid cryptographic object may establish integrity or binding without establishing institutional warrant, real-world consequence, independent observation, or population completeness.

## 7. Reproducibility

Measured evaluations should identify exact:

- criteria/profile/vector set;
- candidate/system version;
- runner/toolchain;
- environment;
- result artifact;
- digests/identities;
- timestamps;
- preserved stdout/stderr or equivalent evidence where relevant.

## 8. Claim ceiling

An ICTS PASS establishes only the properties and versioned experiment actually tested.

It does not by itself establish regulatory compliance, complete real-world coverage, universal correctness, or end-to-end ICI beyond the tested evidence.
