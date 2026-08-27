<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Status Vocabulary

The category uses explicit status tokens.

## ESTABLISHED

The stated property is established under the exact declared scope and evidence requirements.

## ESTABLISHED_BOUNDED

The property is established only within an explicit bound permitted by the pinned profile.

The bound must be machine-identifiable or otherwise unambiguous.

## NOT_ESTABLISHED

Available evidence does not establish the stated property.

This status must not be silently interpreted as proof of the factual opposite.

## REFUTED

Evidence establishes that the stated claim fails under the declared scope.

## NOT_EVALUATED

The required evaluation has not been performed or no result is being asserted.

## NOT_APPLICABLE

The evaluated component declares that the property does not apply to its scoped component claim.

For **full ICI**, a mandatory canonical join marked NOT_APPLICABLE does not satisfy the full-chain condition.

## INDETERMINATE

The available evidence does not permit a determinate disposition.

## Refusal vs substantive status

Malformed or unevaluable inputs should be represented as a typed verifier refusal, not converted into a substantive continuity status.
