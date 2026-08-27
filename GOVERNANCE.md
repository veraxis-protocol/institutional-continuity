<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Governance

## 1. Purpose

This repository governs the open category architecture, benchmark methodology, interoperability surfaces, and conformance language of **Institutional Continuity Infrastructure (ICI)**.

Governance exists to protect four properties:

1. semantic stability;
2. falsifiability;
3. implementation neutrality;
4. preserved historical provenance.

It is not designed to maximize the number of features or to privilege any one implementation.

## 2. PRE-1.0 governance model

During PRE-1.0 category formation, the repository uses an **owner-controlled design-authority model with public technical review**.

### Design Authority

The Design Authority:

- owns the canonical category boundary;
- approves normative category and benchmark changes;
- resolves vocabulary conflicts;
- enforces claim ceilings;
- determines whether a change is editorial, compatible, or epoch/version changing;
- cannot retroactively rewrite frozen historical evidence.

The current Design Authority is maintained by Veraxis Protocol.

### Maintainers

Maintainers may:

- triage issues and pull requests;
- review editorial and technical proposals;
- maintain schemas, examples, tooling, and CI;
- recommend normative changes.

Maintainer status does not independently authorize a category-breaking normative change.

### Contributors

Contributors may propose:

- corrections;
- interoperability profiles;
- implementation mappings;
- falsification vectors;
- formal obligations or proofs;
- benchmark improvements;
- evidence-language corrections.

### Evaluators

Evaluators execute or reproduce benchmark work under the evidence-class and independence conditions declared for the specific evaluation. A reviewer must not be described as independent merely because a review occurred.

## 3. Normative vs non-normative material

A file is normative only when it explicitly says so or resides in a path designated normative by a frozen release manifest.

The following are intended normative surfaces after release freeze:

- `spec/`
- `benchmark/ICTS-SPEC.md`
- `benchmark/PROFILE-CONTRACT.md`
- frozen benchmark schemas and registries identified by release manifest
- formal obligations explicitly incorporated by the category constitution

Examples, landscape mappings, explanatory diagrams, and implementation notes are non-normative unless promoted through change control.

## 4. Change classes

### Editorial

No intended semantic effect: spelling, formatting, broken links, explanatory clarification that does not change obligations.

### Compatible normative

Adds a requirement or precision without changing the meaning of already-valid conformant behavior, as demonstrated by compatibility analysis.

### Material normative

Changes eligibility, status semantics, a canonical join, invariant, profile interpretation, evidence requirement, failure behavior, or conformance result.

Material normative changes require a version increment and successor artifact.

### Category/epoch change

Changes the canonical chain, authority model, or meaning of full Institutional Continuity.

These changes require explicit Design Authority approval, published rationale, compatibility analysis, benchmark impact report, and a new category epoch/version.

## 5. Required record for normative change

A normative change proposal must include:

1. problem statement;
2. proposed normative text;
3. rationale;
4. compatibility analysis;
5. benchmark impact;
6. claim-ceiling impact;
7. security/abuse analysis where relevant;
8. migration or successor plan;
9. evidence supporting the change;
10. owner approval for material changes.

## 6. Non-rewrite rule

Frozen releases and relied-upon historical evidence are immutable in meaning.

Corrections must:

- preserve the predecessor;
- issue a successor;
- record lineage;
- state what was corrected;
- state whether prior conclusions remain valid.

This repository applies ICI-F6 to itself.

## 7. Implementation neutrality

No Veraxis implementation receives privileged benchmark treatment.

A non-Veraxis implementation may satisfy an ICI interface or join. The category definition must not be altered merely to preserve a commercial implementation's advantage.

Likewise, category language must not be broadened merely to award a favored implementation credit.

## 8. Conformance labels

Public conformance designations require the exact evidence required by the applicable profile and benchmark release.

Repository maintainers may reject or correct misleading compatibility language.

Potential future program labels such as `ICI Conformant` or `ICTS Verified` do not become valid merely because a project self-describes that way. See [TRADEMARKS.md](TRADEMARKS.md).

## 9. External standards work

Future IETF, W3C, ISO, regulatory, or other standards submissions are separate governance events and may create additional intellectual-property or contribution obligations. No repository contribution is automatically a submission to an external standards body.

## 10. Post-1.0 direction

The intended long-term direction is broader multi-stakeholder governance once:

- the canonical semantics are stable;
- conformance is independently reproducible;
- change control is battle-tested;
- implementation-neutral interoperability exists;
- capture resistance can be designed without weakening the category's falsifiability.

Any transition will itself be a versioned governance change.
