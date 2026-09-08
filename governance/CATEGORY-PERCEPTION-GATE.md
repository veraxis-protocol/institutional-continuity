<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Category Perception Gate

**Controlling source:** [THESIS.md](../THESIS.md) — Veraxis Category Thesis v1.0

This gate exists because category perception has failed in observed practice.
External readers, including AI systems asked to summarize Veraxis public
artifacts, have centered their analysis on Evidence Packs and evidence
infrastructure rather than on the upstream institutional-authority computation
that gives those artifacts meaning.

The gate is a **manual, reproducible evaluation**. It is not an automated
AI-dependent CI requirement, and it must not be made one without owner
authorization.

## How to run the gate

1. Select one artifact: a repository README, a deck, a pre-read, a landing page,
   or an AI-generated summary derived from Veraxis public material.
2. Give a competent reader — or an AI system — **only that artifact**. Do not
   supply THESIS.md, and do not supply context from other Veraxis surfaces.
3. Ask the seven evaluation questions below.
4. Compare each answer against PASS semantics.
5. Record the result, the artifact identity (repo, path, commit SHA or URL and
   retrieval date), and any FAIL indicator observed.

An artifact passes only if every answer is materially equivalent to its PASS
semantics. A single FAIL indicator fails the artifact.

## Evaluation questions

Given ONLY the artifact being evaluated:

1. What category is Veraxis proposing?
2. What is the primary missing computation?
3. What does OIC do?
4. What does VEIP do?
5. What is an Evidence Pack/AEP?
6. Does VEIP originate institutional authority?
7. Does an Evidence Pack prove its own upstream institutional validity merely by
   being cryptographically valid?

## PASS semantics

| # | Required answer |
|---|---|
| 1 | Open Institutional Computation. |
| 2 | Institutional authority / admitted institutional meaning becoming machine-operational. |
| 3 | Upstream source-to-admitted-control institutional compilation. |
| 4 | Downstream execution-integrity / binding / interoperability. |
| 5 | Evidence artifact, not category or authority source. |
| 6 | No. |
| 7 | No. |

## FAIL indicators

An answer materially equivalent to any of the following fails the artifact:

- Veraxis is primarily an Evidence Pack company.
- VEIP is itself an Authorization Evidence Pack.
- AEP is the core category.
- VEIP autonomously creates institutional authority.
- A signature makes institutional meaning valid.
- CAGE/OPA/runtime originates institutional authority.

## Optional deterministic lexical check

The following is a **supporting** check only. Passing it does not establish
category perception, and failing it does not by itself fail an artifact. It
exists to catch the most common mechanical omission: a public surface that
positions a component without naming the field it sits in.

For a repository README that carries category positioning, check that it:

- contains the exact string `Open Institutional Computation`;
- contains a link to the canonical `THESIS.md`;
- where it names Evidence Packs or AEP, does not describe them as the category;
- where it describes a downstream component, states what must already exist
  upstream.

This check is lexical. It is not a substitute for the seven-question gate.

## Recording results

A gate result should record:

- artifact identity (repository and path with commit SHA, or URL with retrieval
  date);
- evaluator (human or named AI system and version);
- the seven answers as given, not as paraphrased into compliance;
- PASS or FAIL;
- each FAIL indicator observed;
- the remediation, if any, and the resulting artifact identity.

Answers must be recorded as actually given. Rewriting an evaluator's answer to
match PASS semantics destroys the only signal this gate produces.

## Claim boundary

This gate measures how an artifact is *perceived*. It measures nothing about
implementation maturity, validation status, or demonstrated capability. An
artifact may pass this gate while its repository's `STATUS`, `CLAIMS.md`, and
capability documentation establish a narrow demonstrated scope. Those documents
govern what may be claimed; this gate governs only whether the category is
legible.
