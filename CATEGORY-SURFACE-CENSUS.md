<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Category Surface Census — CAT-ALIGN-001

**Controlling source:** [THESIS.md](THESIS.md) — Veraxis Category Thesis v1.0
**Date:** 2026-09-08
**Scope:** every repository reachable by the executing account under `veraxis-protocol` (14 total,
enumerated from the account's repository list; the listing reported no further pages).

## Method

For each repository: the working tree was cloned and inspected — `README.md`, category and
architecture documents, terminology documents, and public landing documentation — and searched
case-insensitively across all Markdown and text files for the terms `category`,
`Institutional Computation`, `Institutional Continuity`, `AI governance`, `governance layer`,
`authority`, `authorization`, `Evidence Pack`, `AEP`, `VEIP`, `OIC`, `protocol`, and `trust`.

Repositories were then classified:

- **A — CORE:** receives the standard role block now.
- **B — SUPPORTING:** links to THESIS.md where category positioning appears.
- **C — HISTORICAL/EXPERIMENTAL:** history preserved; historical claims not rewritten for consistency.
- **D — IRRELEVANT/FORK:** no action.

No repository was rewritten merely for consistency.

## Census

| Repo | Class | Current positioning before CAT-ALIGN-001 | Conflict found? | Change made? | Reason | PR | Claim-impact assessment |
|---|---|---|---|---|---|---|---|
| `institutional-continuity` | A | Badge read `Category: ICI`, positioning ICI as the parent category | **Yes** — competing parent category | Yes — added THESIS.md and the perception gate; replaced the category badge with a field badge plus an architecture badge; added a placement section | Controlling source lives here; ICI must read as an architecture within the field, not as the field | [#2](https://github.com/veraxis-protocol/institutional-continuity/pull/2) | None. Nine-node chain, eight joins, invariants, ICTS and all claim ceilings unchanged; every implementation remains `NOT_EVALUATED` |
| `veip-spec` | A | Deterministic execution-control standard; execution authorization and evidence packaging foregrounded | Yes — no upstream boundary stated; readable as originating authority | Yes — role block plus an architectural-position subsection | Highest-risk surface for category collapse toward Evidence Packs | [#1](https://github.com/veraxis-protocol/veip-spec/pull/1) | None. Normative spec, scope, licensing, schemas, invariants, versioning untouched; "Evidence Pack" schema terminology preserved |
| `veip-sdk` | A | Architecture model began at `AI System → Action Proposal → VEIP Authorization Gate` | Yes — chain started at the gate, nothing stated what must be true upstream | Yes — role block plus an Upstream Boundary section before the architecture model | An authority envelope is an input; the SDK does not originate it | [#1](https://github.com/veraxis-protocol/veip-sdk/pull/1) | None. Existing scope sections, invariants and version bindings preserved |
| `veip-verifier-core` | A | Careful about what it is not, but silent on what a PASS establishes | Yes — a PASS was over-readable as upstream validation | Yes — role block plus "What a PASS does and does not establish" | Verifier output is the easiest artifact in the stack to over-read | [#1](https://github.com/veraxis-protocol/veip-verifier-core/pull/1) | Restrictive only. Existing verifier claim ceiling preserved, not widened |
| `veip-registry` | A | Already stated it is not a governance authority and not a centralized global registry | Partial — correct boundaries, no upstream reason given | Yes — role block plus the registry authority boundary | Custody of evidence is not legitimacy of authority | [#1](https://github.com/veraxis-protocol/veip-registry/pull/1) | None; restrictive in effect |
| `Institutional-Compiler` | A | Opened on status, bootstrap date and governing design; field never named | Yes — the upstream component was the least placeable surface | Yes — role section near the top | Inverted dependency: downstream surfaces were easier to recognize than the upstream one | [#44](https://github.com/veraxis-protocol/Institutional-Compiler/pull/44) | None. `BOUNDED_REFERENCE_IMPLEMENTATION`, Gate F/G figures, twelve exclusions, OIC-Bench `TARGET - NOT MEASURED` rows, STATUS/CLAIMS/capability matrix all unchanged |
| `AuthContract` | A | Developer-workflow framing under an owner-approved language freeze | Partial — receipt behavior over-readable as originating authority | Yes — role block placed **after** `Current status`, below `## Quick start` | `docs/DEVELOPER-LANGUAGE.md` and `tests/test_veip.py` forbid deep ontology vocabulary before Quick start; placement moved rather than changing the test | [#16](https://github.com/veraxis-protocol/AuthContract/pull/16) | None. TRL 4 / experimental status and the full "does not currently claim" list preserved verbatim |
| `runtime-admissibility-experiment` | A | Static authorization vs runtime admissibility, formally stated | Partial — `RA(x,t)` over-readable as defining institutional authority | Yes — role block stating `A_t` is an input | Research into the runtime currentness/admissibility boundary inside the field | [#1](https://github.com/veraxis-protocol/runtime-admissibility-experiment/pull/1) | None. No equation, predicate, scenario or result altered |
| `RAED` | B | Semantic memory substrate; core invariant is a field-level non-collapse rule | No conflict | Yes — role block plus thesis link | Category positioning appears ("It is the layer that…"), so the link applies | [#1](https://github.com/veraxis-protocol/RAED/pull/1) | None. CLAIMS, LIMITATIONS, CONFORMANCE, benchmarks, design targets untouched |
| `Veraxis-Memory-Admissibility-Management-MAM-` | B | "Memory is part of the authority path"; AEP appears in the custody chain | Partial — authority-path sentence over-readable as memory creating authority | Yes — role block bounding the authority-path claim and placing AEP downstream | AEP terminology and authority positioning appear here | [#1](https://github.com/veraxis-protocol/Veraxis-Memory-Admissibility-Management-MAM-/pull/1) | None. Production invariants, benchmark envelope and release notes unchanged |
| `Institutional-Compiler-Review-Ledger` | C | Adjudication and diagnostic evidence records; zero category-term hits | No | **No** | Frozen evidence ledger. Rewriting historical records for messaging consistency is forbidden by this work order | — | None; untouched |
| `white-papers` | C | Single released PDF (`Veraxis White Paper v1.2.pdf`); no editable Markdown surface | Not assessable — binary released artifact | **No** | Released artifact; not rewritten. Any category correction belongs in a successor paper version | — | None; untouched |
| `Open-Audit-Mission` | D | Repository is empty (clone reported no commits) | No | **No** | No surface to patch | — | None |
| `awesome-mcp-servers` | D | Upstream fork, not Veraxis positioning | No | **No** | Fork of third-party content | — | None |

**Totals:** 14 censused, 10 modified, 4 not modified.

## Remaining known inconsistencies

These are recorded rather than fixed, each for a stated reason.

1. **`spec/CATEGORY-CONSTITUTION.md` is titled "ICI Category Constitution".** With the README now
   presenting ICI as an architecture within Open Institutional Computation, the normative spec still
   uses "category" for ICI. Reconciling it is a **material normative change** under
   [spec/CHANGE-CONTROL.md](spec/CHANGE-CONTROL.md) and requires a successor artifact with a full
   change record. It was deliberately not changed by README-adjacent prose, per the work order's
   guardrail against altering released specs by prose alone. **Owner decision required.**
2. **veraxis.io source is unresolved.** Not present in any reachable repository, and the live site
   is unreachable from this environment. See [WEBSITE-CATEGORY-PATCH.md](WEBSITE-CATEGORY-PATCH.md).
3. **`veip-spec` CI is red on `main`, pre-existing.** `make check` requires both `LICENSE` and
   `LICENSE.md`; only `LICENSE` exists. Unrelated to category positioning and outside this work
   order's bounded documentation scope, so not fixed. Expect the veip-spec PR to inherit that
   failure.
4. **`veip-registry` README ends mid-sentence.** The "Relationship to veip-spec" section reads
   "The canonical Evidence Pack schema originates in:" with nothing following. Pre-existing and
   unrelated to category positioning; not fixed.
5. **`white-papers` v1.2 PDF has not been assessed against the thesis.** Binary released artifact;
   assessing and, if needed, correcting it belongs to a successor paper version, not to this work
   order.
6. **Component names `VICCP`, `ZTL`, `RegSpine`, `CAGE` and `OAM`** appear in the ICI README's
   reference-primitive table but have no reachable repository in this account. Their public
   surfaces, if any exist elsewhere, were not censused.
