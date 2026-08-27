<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Conformance and Falsification Vectors

This directory is reserved for **public, released** ICTS vectors.

## Bootstrap rule

No internal preregistered Run #2 attack corpus is included in the bootstrap.

That separation is deliberate: the engineering candidate and a preregistered adversarial suite must not be silently co-authored by the same actor when a blind-engineering claim is intended.

Future vector releases must identify:

- vector-set version;
- criteria/profile version;
- expected disposition;
- coverage/falsifier mapping;
- canonical bytes/digest;
- whether the vector was known to the implementation actor before candidate freeze.
