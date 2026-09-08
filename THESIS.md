<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Veraxis Category Thesis

STATUS: OWNER-AUTHORIZED CONTROLLING CATEGORY SOURCE
VERSION: 1.0
OWNER: Arkadiy Miteiko
DATE: 2026-09-08

APPLIES TO:
- all Veraxis public repositories;
- README category positioning;
- veraxis.io;
- decks and pre-reads;
- partner and customer engagements;
- public technical explanations;
- proposals and commercialization materials;
- AI-generated summaries derived from Veraxis public artifacts.

## Precedence

This document governs category positioning and component relationships.
Component repositories may define their own implementation scope, status,
interfaces, and claim ceilings, but may not redefine their architectural
role in the Veraxis category hierarchy without an owner-authorized successor
to this document.

## 1. Category definition

The category is **Open Institutional Computation**.

Open Institutional Computation is the open, falsifiable study and engineering of
how institutional authority and institutional meaning become computable — how a
human institution's governing sources, its authorized interpreters, and its
admission acts produce machine-operational control state that a runtime may act
on, and how that relationship remains examinable afterward.

It is a field, not a product. Multiple independent implementations, including
non-Veraxis implementations, may occupy it.

## 2. Missing-computation definition

The central missing computation is **institutional authority computation**:

> the governed transformation through which human institutional sources,
> authorized interpretation/admission, currentness, scope, delegation,
> conditions, exceptions, and required evidence become machine-operational
> authority/control state.

### The critical distinction

Permission checking asks:

> "Does this action satisfy this rule?"

Institutional authority computation asks:

> "Why is this the rule entitled to govern this action now?"

The first question is well served by existing policy engines, authorization
services, and enforcement runtimes. The second question is the one that is not
reliably machine-operational today, and it is the question this category is
organized around.

## 3. Canonical architecture

```
HUMAN GOVERNING SOURCES
        ↓
AUTHORIZED INTERPRETATION / ADMISSION
        ↓
OIC
        ↓
MACHINE-OPERATIONAL AUTHORITY / CONTROL STATE
        ↓
VEIP
        ↓
CAGE / OPA / AGENT RUNTIME
        ↓
EXACT CONSEQUENTIAL ACTION
        ↓
EVIDENCE PACK / AEP
        ↓
CONSEQUENCE / OBSERVATION / EXAMINATION
```

Position in this architecture is an architectural statement. It is not a
statement that any component currently performs its role in production. See
section 10.

## 4. Exact OIC role

**OIC — Open Institutional Compiler.**

OIC is the upstream institutional-compilation component.

Its architectural role is:

> governing source
> → source-grounded candidate meaning
> → explicit uncertainty
> → authorized institutional admission
> → machine-operational control/authority state.

OIC does **not** create institutional authority. Institutional authority remains
externally constituted, and admission remains an institutional act performed by
parties with the required standing. Machine extraction may propose meaning;
authorized institutional admission is required before proposed meaning becomes
admitted meaning.

OIC makes admitted institutional meaning computationally usable. It operates
upstream of VEIP and upstream of runtime enforcement.

## 5. Exact VEIP role

**VEIP — Veraxis Execution Integrity Protocol.**

VEIP is the execution-integrity and interoperability protocol downstream of
institutional authority/control formation.

VEIP consumes externally established or admitted machine-operational authority
or control state, and binds and preserves that state across the boundary to an
exact proposed action, a runtime disposition, an execution transition, and
verifiable evidence.

VEIP does **not**:

- interpret governing documents as institutional truth;
- perform institutional admission;
- originate institutional authority.

A VEIP deployment that is functioning perfectly still says nothing about whether
the upstream institutional meaning it is preserving was correctly interpreted or
validly admitted. That is the upstream problem, and it belongs to OIC.

## 6. Exact Evidence Pack / AEP role

An **Authorization Evidence Pack / Evidence Pack** is an **artifact**.

It records or proves the relationship among:

- authority/control state;
- exact action;
- runtime decision;
- execution/evidence state.

An Evidence Pack is **not** the category. It is **not** VEIP itself. It does
**not** create institutional authority. A cryptographically valid Evidence Pack
establishes only the bounded cryptographic and structural integrity properties
actually verified under the applicable schema/profile. It does not by itself
establish truth, completeness, institutional validity, correct upstream
interpretation, consequence occurrence, or observation coverage.

Normative schema terminology is preserved as published. Where a specification
says "Evidence Pack," it is not renamed to "AEP" for messaging purposes.
Terminology in a normative specification changes only through that
specification's own governance process.

## 7. Enforcement / runtime role

**CAGE, OPA, and other agent runtimes are enforcement consumers.**

They evaluate or enforce machine-operational control state. They are not the
origin of institutional authority. An enforcement decision inherits whatever
institutional warrant its inputs carry; it does not manufacture warrant that the
inputs lack.

## 8. ICI role

**ICI — Institutional Continuity Infrastructure.**

ICI is the end-to-end continuity architecture and examination framework under the
broader field of Open Institutional Computation. It defines the canonical chain,
the joins, the invariants, and the ICTS conformance methodology by which a
continuity claim can be falsified.

ICI is a reference end-to-end continuity architecture within the broader field of
Open Institutional Computation. It is not a competing parent category.

## 8a. Reference primitive roles

This section exists so that fixing the category does not silently redefine or erase
components that already exist. Each entry states an architectural role only. None is
a capability, maturity or readiness claim; each component's own repository governs
what may be claimed about it.

**OIC — Open Institutional Compiler.**
Upstream institutional compilation: source-grounded candidate meaning → explicit
uncertainty → authorized institutional admission → machine-operational control state.

**ZTL — Zero-Trust Logic.**
Bounded logical warrant: tests what conclusions follow from admitted grounds without
silently converting absence, uncertainty, provenance, or external authority into facts
that have not been established.

**VEIP — Veraxis Execution Integrity Protocol.**
Execution-integrity/interoperability boundary: binds and preserves applicable
machine-operational authority/control and warrant state to exact proposed actions and
runtime transitions, producing verifiable downstream evidence.

**OAM.**
OAM is an existing Veraxis reference primitive whose exact canonical role is subject to
the OAM role-reconciliation record. No component README may infer a new OAM role from
this thesis.

See [OAM-ROLE-RECONCILIATION.md](OAM-ROLE-RECONCILIATION.md). That census found a
material conflict between two published surfaces — one defining OAM as a standing and
examination workflow, another as constraining operational authority — and it is
recorded for owner decision rather than resolved by editorial preference.

**ICI — Institutional Continuity Infrastructure.**
End-to-end continuity architecture and falsification/examination framework within Open
Institutional Computation.

**AuthContract.**
Developer-facing reference artifact and control boundary where applicable. It is not a
parent category and does not create institutional authority.

**Runtime Admissibility.**
Research and runtime-currentness primitive where applicable. It is not a parent
category.

Primitives named on other Veraxis surfaces but without a reachable repository in the
censused set — including VICCP, RegSpine and CAGE — are deliberately not assigned roles
here. Assigning one from an unreachable surface would be the same defect this record
exists to prevent.

## 9. Terminology distinctions

| Term | Meaning |
|---|---|
| **Policy** | Human/institutional statement of intended governance. |
| **Institutional authority** | Externally constituted entitlement by which a person, office, source, rule, delegation, or institutional process may govern a consequence. |
| **Admission** | Institutional act accepting bounded meaning/control for a stated scope/use. |
| **Permission** | Bounded authorization for a specific action under applicable authority/control. |
| **Warrant** | Machine-verifiable basis for relying on a particular authority/control state. |
| **VEIP** | Execution-integrity protocol preserving/binding relevant state across runtime boundaries. |
| **Evidence Pack / AEP** | Evidence artifact describing/proving a bounded authorization/execution relationship. |
| **Enforcement** | Runtime evaluation or action based on machine-operational control state. |
| **Institutional Continuity** | End-to-end preservation/examination of the warranted chain from source through consequence and later reliance/examination. |

## 10. Claim-control rule

**Role statements are architecture statements, not implementation claims.**

This document places components in a hierarchy. It does not assert that any
component has achieved, demonstrated, or validated the capability implied by its
position.

This document preserves, and does not override:

- repository-specific `STATUS`;
- `CLAIMS.md`;
- capability matrices;
- benchmark status;
- validation scope;
- research claim ceilings.

Where a repository's own documentation establishes a narrower demonstrated
scope, that narrower scope governs what may be claimed about that repository.

No sentence in this document may be read as asserting that OIC currently
performs production institutional compilation or production runtime
authorization. Its repository does not establish that, and this document does
not extend it. Where implementation status requires it, external wording uses
"is developing" rather than "produces."

## 11. External engagement rule

Every new external technical or commercial pre-read SHOULD identify:

```
GOVERNING CATEGORY THESIS:
Veraxis Category Thesis v1.0
<canonical commit SHA after merge>
```

External explanations should establish the following sequence before discussion
centers on implementation artifacts:

1. **Missing computation:** institutional authority is not reliably
   machine-operational from human governing sources.
2. **OIC:** governed source-to-admitted-control transformation.
3. **VEIP:** runtime execution-integrity/interoperability boundary.
4. **Evidence Pack/AEP:** downstream evidence artifact.

If an engagement focuses on AEP security, cryptography, signing, replay, tamper
resistance, registry, or retention, those discussions are valid but must not
redefine AEP as the source of institutional authority.

### Canonical external summary

> Veraxis is making institutional authority computable for machines.
> OIC produces machine-operational institutional control state.
> VEIP binds and preserves that state into runtime.
> Enforcement systems act on it.
> Evidence Packs record what happened.

Use wording carefully where implementation status requires "is developing"
rather than "produces."

## 12. Perception test

The category-perception gate for this thesis is maintained at
[governance/CATEGORY-PERCEPTION-GATE.md](governance/CATEGORY-PERCEPTION-GATE.md).

Given only the artifact being evaluated, a reader — human or AI — should be able
to answer:

1. What category is Veraxis proposing?
2. What is the primary missing computation?
3. What does OIC do?
4. What does VEIP do?
5. What is an Evidence Pack/AEP?
6. Does VEIP originate institutional authority?
7. Does an Evidence Pack prove its own upstream institutional validity merely by
   being cryptographically valid?

An artifact that leads a competent reader to answer "Veraxis is primarily an
Evidence Pack company" has failed this test regardless of its technical
accuracy.

## 13. Change-control rule

Any future public change that materially changes:

- OIC ↔ institutional authority
- OIC ↔ admission
- VEIP ↔ authority/control state
- VEIP ↔ Evidence Pack/AEP
- Evidence Pack ↔ evidence
- ICI ↔ category
- CAGE/runtime ↔ enforcement

requires an owner-authorized successor to this document **first**.

Component READMEs inherit the category hierarchy. They do not independently
redefine it.

This document does not itself change any normative specification. Where a
normative specification in any repository states a category or role differently,
that specification is changed only through its own governance process, and this
document does not silently override it.
