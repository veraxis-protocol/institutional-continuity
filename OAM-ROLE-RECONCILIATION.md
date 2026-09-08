<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# OAM Role Reconciliation

**Work order:** CAT-ALIGN-001B
**Date:** 2026-09-08
**Status:** CONFLICT FOUND — OWNER AUTHORIZATION REQUIRED
**Controlling source:** [THESIS.md](THESIS.md) — Veraxis Category Thesis v1.0

## Why this record exists

CAT-ALIGN-001B requires the controlling thesis to name each Veraxis reference primitive's role.
For OAM it forbids inventing or silently selecting a canonical expansion or role, and requires a
census of currently maintained public definitions first, because public surfaces have used
materially different descriptions over time.

That census found a genuine conflict. It is recorded here rather than resolved by editorial
preference.

## Census scope

Every repository reachable by the executing account under `veraxis-protocol` (14 total) was
searched for `OAM` and `Open Audit Mission` across Markdown, text, JSON, Python, Go and CFF files.

## Definitions found

### 1. Institutional Continuity Infrastructure — README reference table

- **Repository / file:** `veraxis-protocol/institutional-continuity` — `README.md`, line 171
- **Blob:** `fc28bdc9db7f044344f4034a4cce70dd9ceb1416` (at `origin/main`
  `549430974b9511261e997f8f67febb7ad99b503a`)
- **Expansion:** Open Audit Mission
- **Exact role stated:**

  > | **OAM — Open Audit Mission** | Standing/examination workflow where appropriate. |

- **Reading:** a downstream, examination-side role. Standing to examine, and the workflow by which
  examination happens. It constrains nothing at runtime.

### 2. Open Institutional Compiler — admission contract

- **Repository / file:** `veraxis-protocol/Institutional-Compiler` —
  `design/admission-boundary-001/ADMISSION-CONTRACT-v0.1.md`, line 112
- **Blob:** `1128bdbcc42dc47a355551fa230bab6f7420accc` (at `main`
  `c3d986229e2d7874a30a318981f5045e3f793236`); last touched by commit
  `fbb90d950f378e16928426e429e29ba2fbe650e8`
- **Expansion:** none given
- **Exact role stated:**

  > A later OCE/runtime stage may compute consequences; OAM/ZTL may constrain operational
  > authority; and VEIP may record or verify execution consequences. None is designed or
  > implemented here.

- **Reading:** an authority-constraining role. Constraining operational authority is a control-side
  function that acts on what a runtime may do, not an examination of what it did.

### 3. AuthContract — component mention

- **Repository / file:** `veraxis-protocol/AuthContract` — `README.md`, line 1101
- **Blob:** `22e8cb43684ae6631f68e20b61146d14cbcc6b5d` (at `origin/main`
  `6c677aec730bff79dfc60a88d1721564000ad111`)
- **Exact role stated:**

  > The Veraxis research stack uses components including OIC, ZTL, OAM, VEIP, and AEP to reason
  > about parts of this chain.

- **Reading:** names OAM as a stack component but assigns it no role. Not in conflict; not a
  definition either.

### 4. Institutional Compiler Review Ledger — operational usage

- **Repository:** `veraxis-protocol/Institutional-Compiler-Review-Ledger` at
  `713381f866798a950e02cf19c3270e145af94369`
- **Files:** `owner-decisions/AUTHORIZE-M1-S2-LEDGER-NATIVE-EXECUTION-001.md`,
  `owner-decisions/AUTHORIZE-M1-CLOSURE-ENV-001-CONDITIONAL-R1-001.md`, and evidence transcripts
  under `stage-m1-closure/evidence/r1/`
- **Exact usage:** `OAM` appears only as an identifier prefix on audit gates and reports —
  `OAM-GATE-SAR-05-CDC-PROFILE-AUDIT-003`, `OAM-GATE-SAR-05-CDC-AUDIT-INDEX.json`,
  `OAM-CDC-PROFILE-CORRECTION-…-INDEPENDENT-REVIEW-RETURN-001.md`
- **Reading:** operationally an audit and gate-governance function. Consistent with the
  examination reading of definition 1, but expressed as gates that a candidate must satisfy, which
  is closer to a control than to a post-hoc examination. No prose role statement exists.

### 5. The repository named for it

- **Repository:** `veraxis-protocol/Open-Audit-Mission`
- **State:** **empty — no commits.** The clone reported `your current branch 'main' does not have
  any commits yet`.
- **Consequence:** the repository that carries the name holds no definition at all. The canonical
  home for an OAM definition is currently vacant.

## Do the definitions conflict?

**Yes.** Definitions 1 and 2 are materially different, not two phrasings of one role:

| | ICI README | OIC admission contract |
|---|---|---|
| Function | standing and examination workflow | constrains operational authority |
| Position | downstream of consequence | upstream of, or at, runtime |
| Effect on a runtime decision | none | binding |
| ICI plane | evidentiary authority | causal / institutional authority |

`spec/AUTHORITY-PLANES.md` in this repository holds that collapsing institutional, causal and
evidentiary authority produces false assurance. The two OAM definitions sit on opposite sides of
exactly that distinction, so this cannot be reconciled by choosing softer wording.

Definition 4's gate usage does not settle it. Audit gates that a candidate must pass read as
constraining, which leans toward definition 2, while the naming and the audit vocabulary lean
toward definition 1.

## Recommended canonical role

**Recommendation: definition 1 — the examination-side role — with an explicit exclusion.**

Proposed wording, for owner approval and not adopted anywhere yet:

> **OAM — Open Audit Mission.** Standing and examination workflow: who is entitled to examine a
> continuity claim, and the process by which that examination is conducted and recorded. OAM does
> not constrain operational authority at runtime and does not originate institutional authority.

Reasons:

1. It matches the only public surface that actually defines OAM with an expansion and a role.
2. It keeps OAM on the evidentiary-authority plane, preserving the non-collapse rule.
3. It leaves the constraint function to ZTL, which the same OIC sentence already pairs with OAM
   and which the ICI README independently defines as bounded logical warrant.
4. It is the narrower claim. If OAM later needs a control-side role, adding one is a deliberate
   expansion with its own authorization, whereas starting broad and retreating is a claim
   reduction on a published surface.

**Consequence if adopted:** the OIC admission contract's sentence becomes inaccurate as to OAM.
That file is preregistered design evidence carrying its own claim ceiling and
`NOT SELF-ADJUDICATED` marker. It should not be edited in place to agree with a later decision;
correcting it is a successor-record operation in that repository, under that repository's
governance.

## Is owner authorization required?

**Yes.** This is a semantic conflict between two published Veraxis surfaces, one of which is
preregistered design evidence in a claim-controlled repository. CAT-ALIGN-001B forbids resolving
it by editorial preference, and THESIS.md's own change-control rule requires an owner-authorized
successor for any change to a component's architectural relationship.

Until the owner decides, THESIS.md states only that OAM's exact canonical role is subject to this
record, and no component README may infer an OAM role from the thesis.

## Open questions for the owner

1. Adopt the recommended examination-side role, adopt the control-side role, or define OAM as
   carrying both under explicitly separated planes?
2. Should `veraxis-protocol/Open-Audit-Mission` become the canonical home for the definition, given
   that it is currently empty?
3. Does the `OAM-GATE-*` identifier family in the review ledger reflect an intended control
   function, or is it naming convention only?
4. Who corrects the OIC admission contract's OAM sentence, and under which successor record?
