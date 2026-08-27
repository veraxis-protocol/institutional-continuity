<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Versioning

ICI versions its major artifact families independently.

Recommended tags:

- `ici/vMAJOR.MINOR.PATCH`
- `icts/vMAJOR.MINOR.PATCH`
- `profile/vMAJOR.MINOR.PATCH`
- `formal/vMAJOR.MINOR.PATCH`

## Semantics

- **PATCH** — editorial or fully compatible correction with no intended material semantic change.
- **MINOR** — compatible normative expansion or new optional capability.
- **MAJOR** — incompatible semantic, eligibility, or category boundary change.

During PRE-1.0, incompatible changes may use a MINOR increment where conventional semantic-versioning practice permits it, but every material change still requires explicit change-control records.

## Releases

Every release should identify:

- component version(s);
- commit and tag;
- criteria/profile identities where applicable;
- vector-set identity where applicable;
- toolchain identity where applicable;
- claim ceiling;
- supersession relationship;
- exact artifact digests.
