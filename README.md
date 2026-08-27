<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Institutional Continuity Infrastructure

**An open architecture for proving that institutional authority survives from governing source to machine consequence and independent examination.**

> **SOURCE → ADMITTED MEANING → WARRANTED CONTROL → RUNTIME AUTHORITY → EXACT ACTION → CONSEQUENCE → INDEPENDENT OBSERVATION → RECONCILIATION → EXAMINATION**

[![Status: PRE-1.0](https://img.shields.io/badge/status-PRE--1.0-orange)](STATUS.md)
[![Category: ICI](https://img.shields.io/badge/category-Institutional%20Continuity%20Infrastructure-blue)](spec/CATEGORY-CONSTITUTION.md)
[![Benchmark: ICTS](https://img.shields.io/badge/benchmark-ICTS-informational)](benchmark/README.md)
[![Docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey)](LICENSE.md)

**Agent authorization is necessary. It is not sufficient.**

A machine can be correctly authorized to execute the wrong institutional meaning.  
A cryptographically valid receipt can exist without proving that the claimed consequence occurred.  
A perfectly intact record can still fail to establish that every consequential event that should have been captured was actually observed.

**Institutional Continuity Infrastructure (ICI)** defines a falsifiable architecture for preserving and independently examining institutional meaning, warrant, authority, action, consequence, observation, reconciliation, and historical evidence across that entire chain.

## Current status

**PRE-1.0 / CATEGORY FORMATION / NO IMPLEMENTATION CURRENTLY SCORED**

ICI is presently a category architecture, vocabulary, invariant set, interoperability model, and benchmark methodology under active hardening. It is **not** a claim that Veraxis—or any other system—has established full Institutional Continuity.

The public claim ceiling is deliberately strict:

- a documented architecture is not an implementation;
- an implementation is not a validated implementation;
- a valid authorization is not proof of exact execution;
- a valid execution receipt is not proof of consequence completeness;
- an intact record is not proof that all eligible events were captured;
- a benchmark PASS establishes only the scope actually tested.

See [CLAIMS.md](CLAIMS.md) and [STATUS.md](STATUS.md).

## The continuity problem

Modern agent and automation stacks often solve important middle-layer problems: identity, delegation, policy enforcement, authorization, tool invocation, receipts, or audit storage. Those capabilities matter. But consequential institutional systems require a stronger question:

> **Can an independent examiner reconstruct an unbroken, warranted path from the institution's governing source to the machine consequence without semantic widening, authority inflation, silent uncertainty collapse, or unwitnessed material transition?**

ICI treats that question as an infrastructure problem rather than an application feature.

## The canonical chain

| Node | Meaning |
|---|---|
| **Source** | Authoritative material from which institutional meaning may be derived. |
| **Admitted Meaning** | Meaning explicitly accepted through a valid institutional admission process. |
| **Warranted Control** | A machine-operational control whose relationship to admitted meaning is bounded by declared warrant and evidence. |
| **Runtime Authority** | Current authority eligible to govern a particular runtime decision. |
| **Exact Action** | The action actually authorized for execution, including material parameters. |
| **Consequence** | The externally relevant effect produced by the action. |
| **Independent Observation** | Observation not controlled solely by the same actor or mechanism that caused the consequence. |
| **Reconciliation** | Comparison between continuity evidence and independent observation, including unmatched and indeterminate cases. |
| **Examination** | Later reconstruction and verification by an examiner who was not required to trust the original runtime. |

The canonical chain is frozen at the category level. Product-specific stages may exist inside a join, but they do not silently redefine the chain.

## The eight joins

ICI evaluates the **joins**, not feature counts.

| Join | Boundary | Core question |
|---|---|---|
| **J1** | Source → Admitted Meaning | Was this represented meaning actually admitted by a party with the required standing, against the pinned source state? |
| **J2** | Admitted Meaning → Warranted Control | Did the control preserve material meaning, uncertainty, scope, exceptions, temporal state, and authority boundaries without unadmitted widening? |
| **J3** | Warranted Control → Runtime Authority | Did runtime eligibility bind the exact current warranted control under the applicable authority and profile? |
| **J4** | Runtime Authority → Exact Action | Did the authority bind the exact action and material parameters that were executed? |
| **J5** | Exact Action → Consequence | Is the claimed consequence connected to that exact action rather than merely to an executor assertion? |
| **J6** | Consequence → Independent Observation | Was the consequence independently observable under a declared observation/coverage model? |
| **J7** | Independent Observation → Reconciliation | Were continuity records reconciled against the relevant observed population, including missing, extra, excluded, and indeterminate cases? |
| **J8** | Reconciliation → Examination | Can an independent party reconstruct and verify the historical chain later, including offline where the profile requires it? |

> **No weighted feature score can compensate for a missing mandatory join in a claim of full Institutional Continuity.**

A component may be excellent at one or more joins without claiming full ICI. That is expected and desirable.

## Core invariants

The current category invariants include:

1. **No unadmitted semantic widening.**
2. **No downstream authority inflation.**
3. **Unknown does not silently become established fact.**
4. **Runtime action binds the exact warranted control.**
5. **Consequence evidence cannot self-certify population completeness.**
6. **Correction never rewrites relied-upon history.**
7. **Historical examination remains possible under the declared availability model, including offline where required.**
8. **Every eligible full-continuity consequence has an unbroken witness path to admitted institutional meaning.**
9. **Causal authority and evidentiary authority remain distinguishable.**
10. **Error or inability to evaluate cannot silently become success.**
11. **Shadow, replay, preflight, and enforcement do not silently use materially different semantic paths.**
12. **Material change invalidates dependent eligibility until required re-establishment occurs.**

The normative formulation lives in [spec/INVARIANTS.md](spec/INVARIANTS.md).

## ICTS — Institutional Continuity Test Suite

**ICTS** is the open falsification and conformance framework for evaluating claims made against the ICI model.

ICTS is designed around four principles:

- **joins over feature counts;**
- **bounded claims over marketing labels;**
- **typed refusal over silent coercion;**
- **the same rubric for Veraxis and non-Veraxis systems.**

A system receives no credit for “authorization” if upstream warrant cannot be established. It receives no credit for “auditability” merely because records exist. It receives no completeness credit when the only evidence of coverage is produced by the same mechanism whose completeness is being asserted.

See [benchmark/README.md](benchmark/README.md) and [benchmark/ICTS-SPEC.md](benchmark/ICTS-SPEC.md).

## Current evaluated implementations

**No implementation currently has a public ICTS score in this repository.**

| System / family | Current public status |
|---|---|
| Veraxis reference stack | **NOT_EVALUATED** |
| EMILIA-family protocols | **NOT_EVALUATED** |
| AC2-family agent signing/delegation | **NOT_EVALUATED** |
| MCP-based agent stacks | **NOT_EVALUATED** |
| Cloud-agent platforms | **NOT_EVALUATED** |
| Other implementations | **NOT_EVALUATED** |

`NOT_EVALUATED` is not a negative score. It means the required pinned evaluation has not been published here.

## Reference implementations, not mandatory dependencies

Veraxis maintains reference machinery that maps into the ICI model:

| Reference primitive | Principal ICI role |
|---|---|
| **OIC — Open Institutional Compiler** | Source representation, admission-supporting compilation, institutional control production. |
| **VICCP — Veraxis Institutional Control Compiler Protocol** | Portable institutional-control semantics and semantic-conservation interchange. |
| **AuthContract** | Explicit approved machine-control object. |
| **ZTL — Zero-Trust Logic** | Bounded logical warrant without collapsing logical result into external fact. |
| **VEIP — Veraxis Execution Integrity Protocol** | Runtime/exact-action execution-integrity boundary and evidence. |
| **RegSpine** | End-to-end continuity, consequence linking, reconciliation, and examination substrate. |
| **OAM — Open Audit Mission** | Standing/examination workflow where appropriate. |

**A system does not need to use Veraxis software to implement the Institutional Continuity model.**

A non-Veraxis component may replace a reference primitive if it satisfies the applicable handoff contracts and benchmark obligations. In that sense:

> **RegSpine is the spine, not the monopoly.**

## How to map your stack into ICI

If you build:

- **identity or delegation** — you likely provide inputs to J3/J4;
- **policy-as-code or rules-as-code** — you may occupy J1/J2, depending on admission and semantic-conservation evidence;
- **capability or authorization receipts** — you likely occupy J3/J4;
- **execution integrity** — you likely occupy J4/J5;
- **outcome attestation** — you likely occupy J5/J6;
- **event reconciliation or evidence completeness** — you likely occupy J6/J7;
- **audit/replay/examination infrastructure** — you likely occupy J7/J8.

The recommended integration mechanism is an **ICI Compatibility Profile**: a pinned declaration of the joins you claim, their bounds, evidence interfaces, versions, and applicable conformance requirements.

See [interoperability/profiles/README.md](interoperability/profiles/README.md).

## Compatibility is not endorsement

ICI is intentionally designed for multiple independent implementations.

> **A stronger implementation of any join strengthens the continuity ecosystem.**

A vendor may implement J3–J5 well while making no claim about J1–J2 or J6–J8. That is a precise statement, not a deficiency. What is prohibited is converting a partial claim into a full-chain claim without the missing evidence.

## Authority is not one thing

ICI distinguishes at least three authority planes:

- **Institutional authority** — who may determine or admit the governing institutional meaning;
- **Causal authority** — who or what can make the consequential action/effect happen;
- **Evidentiary authority** — who or what controls the authoritative account used to establish what happened.

Collapsing these planes produces false assurance. See [spec/AUTHORITY-PLANES.md](spec/AUTHORITY-PLANES.md).

## Formalization

The formal program is organized around explicit proof obligations and claim ceilings.

No theorem is described as kernel-checked unless the repository contains the exact formal artifact, toolchain identity, and reproducible verification evidence for the cited release.

See [formal/README.md](formal/README.md).

## Evidence and historical continuity

ICI applies its history-preservation rule to itself.

Corrections are issued as successors; relied-upon historical artifacts are not silently rewritten. Historical evidence may therefore contain failed experiments, superseded specifications, and negative results.

See [evidence/README.md](evidence/README.md).

## Repository governance

This repository is governed as open category infrastructure, not as a product backlog.

Normative changes require explicit rationale, compatibility analysis, benchmark impact, claim-ceiling review, and a versioned successor where the change is material.

The current PRE-1.0 design authority is documented in [GOVERNANCE.md](GOVERNANCE.md). The intended direction is progressively broader multi-stakeholder governance after the semantics, evidence model, and conformance process are stable enough to resist capture by implementation-specific interests.

## Byte authority and releases

For raw repository artifacts:

> **The exact bytes at an identified immutable Git commit/tag are the canonical byte authority.**

Dropbox, chat attachments, and working directories are not canonical release authorities. Zenodo or other archives should be generated from the exact frozen Git release and carry the corresponding commit/tag identity and release manifest.

See [CANONICAL-BYTE-AUTHORITY.md](CANONICAL-BYTE-AUTHORITY.md) and [releases/README.md](releases/README.md).

## Licensing

The repository uses **component-specific licensing**:

- normative specifications, category documentation, schemas, benchmark methodology, and public conformance materials: **CC BY 4.0**, unless a file says otherwise;
- executable reference software and tooling: **Apache License 2.0** only where the file is explicitly marked `SPDX-License-Identifier: Apache-2.0`;
- trademarks, certification/conformance designations, and patent rights are addressed separately and are **not** granted merely by the documentation license.

See [LICENSE.md](LICENSE.md), [PATENTS.md](PATENTS.md), and [TRADEMARKS.md](TRADEMARKS.md).

## Contributing

Contributions are welcome, including competing implementations and critical falsification work.

Normative proposals should aim to make claims **more precise, more falsifiable, and more interoperable**, not merely broader.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

Until a release DOI is assigned, cite the repository and the exact Git tag/commit used. See [CITATION.cff](CITATION.cff).

## Security

Do not disclose suspected security vulnerabilities in a public issue. Follow [SECURITY.md](SECURITY.md).

---

**Category sentence:**  
**Agent authorization is only one link. Institutional Continuity Infrastructure is the open continuity architecture for preserving warranted institutional meaning from source to machine consequence and independent examination.**
