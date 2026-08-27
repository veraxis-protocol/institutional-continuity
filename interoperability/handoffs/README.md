<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Handoff Contracts

A handoff contract specifies what must be true when evidence/control crosses an ICI join.

A complete contract should define:

- producer role;
- consumer role;
- object identity;
- version/currentness;
- required authority/warrant fields;
- uncertainty behavior;
- integrity binding;
- refusal behavior;
- correction/supersession semantics;
- evidence references;
- verifier expectations.

Product-specific transport is not itself the institutional meaning of the handoff.
