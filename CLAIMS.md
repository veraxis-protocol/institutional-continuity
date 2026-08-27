<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Claims and Evidence Discipline

ICI uses explicit claim classes so that architecture, implementation, experiment, proof, and deployment evidence do not collapse into one another.

## Claim classes

### Category claim

A category claim states what ICI defines: a canonical continuity chain, joins, invariants, evidence boundaries, failure semantics, and conformance methodology.

A category claim does **not** establish that a specific implementation satisfies the model.

### Specification claim

A specification claim states what a versioned normative artifact requires.

A specification claim does **not** establish implementation conformance.

### Implementation claim

An implementation claim states what exact frozen software purports to implement.

An implementation claim does **not** establish that the implementation behaves correctly.

### Evaluation claim

An evaluation claim states the observed result of a pinned experiment against a pinned criteria/vector set and environment.

An evaluation claim is bounded to that experiment.

### Formal claim

A formal claim is permitted only when the exact formal model, theorem statement, trusted kernel/toolchain identity, and reproducible check are identified.

A theorem over an abstraction does not automatically establish the corresponding real-world property.

### Operational claim

An operational claim requires evidence from the actual deployed environment and remains bounded by observation and coverage limitations.

## Evidence classes

The project uses the following vocabulary:

- **E1 — frozen primary specification or artifact**
- **E2 — reproducible executable experiment**
- **E3 — kernel-checked formal proof**
- **E4 — independent reproduction**
- **E5 — independently controlled operational observation**
- **E6 — deployment evidence**
- **E7 — analyst inference, search absence, or author-directed/machine-assisted review where stronger classes are not established**

The class describes the evidence source, not the importance of the claim.

## Status vocabulary

The principal evaluation statuses are:

- `ESTABLISHED`
- `ESTABLISHED_BOUNDED`
- `NOT_ESTABLISHED`
- `REFUTED`
- `NOT_EVALUATED`
- `NOT_APPLICABLE`
- `INDETERMINATE`

`NOT_EVALUATED` is not evidence of failure.  
`NOT_ESTABLISHED` is not automatically a factual negation.  
`REFUTED` requires evidence against the stated claim.  
`ESTABLISHED_BOUNDED` requires the bound to be explicit and pinned.

## Prohibited inference patterns

The following inference patterns are invalid without additional evidence:

- source existence → source authority;
- extraction → institutional admission;
- logical verdict → external fact;
- warranted control → execution authorization;
- identity → institutional standing;
- authorization → execution;
- execution → consequence;
- consequence receipt → independent observation;
- record integrity → population completeness;
- causal authority → evidentiary authority;
- correction → permission to erase predecessor history;
- vendor availability → historical verifiability.

## Public claim ceiling

Unless a release explicitly supplies stronger evidence, do not claim:

- regulatory or legal compliance;
- universal correctness;
- universal completeness;
- market adoption;
- standards-body endorsement;
- full ICI conformance by a named vendor;
- independent validation;
- production readiness;
- uniqueness or freedom from prior art.

Claims should be reproducible, pinned, falsifiable, and no stronger than the weakest material link in the evidence chain.
