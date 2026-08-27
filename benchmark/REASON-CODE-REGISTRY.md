<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# ICTS Reason-Code Registry — Initial Namespace

**Status:** PRE-1.0 design registry. A released verifier must pin the exact registry version it implements.

Reason codes make refusal and substantive failure machine-addressable.

## Refusal class

- `REFUSED_MALFORMED_INPUT`
- `REFUSED_JOIN_SET_INVALID`
- `REFUSED_STATUS_TOKEN_INVALID`
- `REFUSED_PROFILE_MISSING`
- `REFUSED_PROFILE_UNRESOLVED`
- `REFUSED_PROFILE_VERSION_MISMATCH`
- `REFUSED_PROFILE_DIGEST_MISMATCH`
- `REFUSED_REQUIRED_IDENTITY_MISSING`
- `REFUSED_INTEGRITY_IDENTITY_MISMATCH`
- `REFUSED_INTERNAL_EVALUATION_ERROR`

## Substantive not-continuous class

- `NOT_CONTINUOUS_JOIN_NOT_ESTABLISHED`
- `NOT_CONTINUOUS_JOIN_REFUTED`
- `NOT_CONTINUOUS_JOIN_NOT_EVALUATED`
- `NOT_CONTINUOUS_JOIN_NOT_APPLICABLE`
- `NOT_CONTINUOUS_JOIN_INDETERMINATE`
- `NOT_CONTINUOUS_BOUNDED_NOT_PERMITTED`
- `NOT_CONTINUOUS_MANDATORY_INVARIANT_FAILED`

## Success class

- `CONTINUOUS_ALL_REQUIRED_JOINS_SATISFIED`

## Rule

Reason codes are evidence about the verifier's disposition, not a substitute for the underlying evidence that supports the join result.
