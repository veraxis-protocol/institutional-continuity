<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Security Policy

## Scope

Security reports may concern:

- reference verification software;
- schemas whose ambiguity can create unsafe acceptance;
- signature/digest or replay handling;
- fail-open behavior;
- parser differentials;
- benchmark logic that can incorrectly grant stronger status;
- supply-chain or release-integrity issues.

## Reporting

**Do not open a public GitHub issue for an undisclosed vulnerability.**

Preferred channel:

1. use GitHub Private Vulnerability Reporting / Security Advisories for this repository when enabled;
2. if that is unavailable, use the private contact channel published by Veraxis Protocol at `veraxis.io`.

Include:

- affected commit/tag;
- affected file/component;
- reproduction steps;
- expected vs observed behavior;
- impact;
- whether public disclosure has already occurred.

## Response model

Security handling should preserve the same historical-continuity rule as other corrections:

- preserve the affected release identity;
- issue a successor;
- describe impact accurately;
- do not rewrite the predecessor and pretend it never existed.

## Benchmark findings

A benchmark failure is not automatically a security vulnerability. A security report should explain the plausible exploit or assurance failure.

## No bounty promise

This file does not create a bug-bounty, payment, or disclosure-reward obligation.
