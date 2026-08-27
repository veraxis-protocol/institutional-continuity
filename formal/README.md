<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Formalization

ICI formalization exists to make key non-collapse and continuity obligations machine-checkable.

## Claim discipline

A file containing Lean/Coq/TLA+/Tamarin/etc. text is not proof merely because it parses.

A formal claim should identify:

- exact model;
- theorem/property statement;
- assumptions;
- abstraction boundary;
- toolchain/kernel;
- exact artifact bytes;
- reproducible check;
- what real-world claim is **not** established by the model.

## Current bootstrap state

The bootstrap publishes formal obligations, not a claim of a fully kernel-checked ICI implementation.
