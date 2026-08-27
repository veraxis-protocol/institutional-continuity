<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# ICTS — Institutional Continuity Test Suite

ICTS is the open falsification and conformance framework associated with ICI.

## What ICTS measures

ICTS measures whether a pinned system/profile/evidence package establishes declared properties at canonical joins and satisfies applicable cross-cutting invariants.

It does not award a generic “governance score.”

## Full-ICI condition

A full-ICI claim requires J1–J8.

Profiles may bound how a join is established. They do not remove required joins from the meaning of full ICI.

## Benchmark philosophy

- **fail closed on malformed/unevaluable input;**
- **typed refusal is distinct from substantive failure;**
- **unknown does not become established;**
- **bounded establishment requires explicit permission and scope;**
- **no vendor gets privileged treatment;**
- **negative evidence and failed runs are preserved.**

## Bootstrap boundary

This bootstrap intentionally does **not** publish:

- the internal preregistered Run #2 adversarial corpus;
- a measured ICTS v0.2 reference aggregation kernel;
- an external independent reproduction.

Those artifacts follow their own freeze and evidence process.

The absence is deliberate and must not be interpreted as a hidden PASS.
