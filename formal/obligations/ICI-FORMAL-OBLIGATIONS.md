<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Formal Obligations

The formal program should refine the category invariants into machine-checkable properties.

Priority obligations:

- **FO-01:** fixed full-ICI join set J1–J8;
- **FO-02:** malformed/unevaluable input cannot produce success;
- **FO-03:** unknown/indeterminate cannot construct established fact;
- **FO-04:** profile-bounded satisfaction cannot escape its declared bound;
- **FO-05:** unadmitted widening invalidates continuity;
- **FO-06:** authority cannot increase solely by downstream transformation;
- **FO-07:** correction creates successor lineage and preserves predecessor identity;
- **FO-08:** full continuity requires a witness for every required join;
- **FO-09:** self-produced consequence records cannot alone establish population completeness;
- **FO-10:** mode-equivalence claims require preservation of the declared semantic path;
- **FO-11:** material dependency change invalidates affected currentness;
- **FO-12:** verifier errors are disjoint from success.

Formalization must state assumptions rather than hiding them in implementation conventions.
