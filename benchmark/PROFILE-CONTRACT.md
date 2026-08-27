<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# ICI / ICTS Compatibility Profile Contract

A compatibility profile declares the scoped continuity claim and the evidence interfaces by which it can be evaluated.

## Required concepts

A profile should identify:

- profile ID;
- version;
- ICI version;
- ICTS version;
- subject/system class;
- fixed required full-ICI join set J1–J8 for any full-ICI claim;
- per-join bounds;
- per-join permission for `ESTABLISHED_BOUNDED`, if any;
- applicable invariants and their criteria-controlled mandatory/advisory classification;
- evidence requirements;
- observation and coverage model;
- offline-examination requirement;
- canonicalization/digest profile where structured identities are used;
- expiry/currentness rules.

## Bounded satisfaction

Bounded satisfaction is not “optional join.”

A profile can say, for example, that J5 is established only for a declared payment rail and consequence class. That can be a legitimate `ESTABLISHED_BOUNDED` result when the profile permits it.

A profile cannot remove J5 and still call the result full Institutional Continuity.

## Trust boundary

Fields that determine whether an invariant is mandatory must be derived from benchmark-controlled criteria/profile state. They must not be accepted merely because the evaluated system says they are non-mandatory.
