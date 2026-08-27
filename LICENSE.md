<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Licensing Map

This repository uses **component-specific licensing**. The license applicable to a file is determined by its SPDX identifier and this map.

## 1. Documentation, specifications, schemas, and public benchmark materials

Unless a file explicitly states otherwise, original Veraxis-authored material in these categories is licensed under:

**Creative Commons Attribution 4.0 International (`CC-BY-4.0`)**

This includes, when marked accordingly:

- category and normative specification documents;
- benchmark methodology;
- public schemas and interoperability profiles;
- public conformance/evaluation templates;
- explanatory documentation.

The full license text is in [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt).

CC BY 4.0 permits broad reuse subject to its conditions. It does **not** grant patent or trademark rights. See [PATENTS.md](PATENTS.md) and [TRADEMARKS.md](TRADEMARKS.md).

## 2. Executable software and tooling

Executable code is licensed under the **Apache License, Version 2.0 (`Apache-2.0`) only when the file is explicitly marked**:

`SPDX-License-Identifier: Apache-2.0`

The full license text is in [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt).

The bootstrap repository contains tooling under Apache-2.0. A future reference verifier or benchmark kernel is **not** automatically Apache-2.0 merely because it is stored in this repository; the actual file must carry the identifier and be included in a released licensing manifest.

Apache-2.0 includes patent terms that apply according to that license. Publication of specifications under CC BY 4.0 does not by itself create an Apache patent grant.

## 3. Third-party material

Third-party material, if introduced, must preserve its own applicable license and attribution. It must not be assumed to inherit the repository's default license.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## 4. Trademarks and conformance designations

No license in this repository grants rights to Veraxis names, logos, trade dress, or reserved conformance/certification designations except for nominative or descriptive use allowed by applicable law.

See [TRADEMARKS.md](TRADEMARKS.md).

## 5. Patents

Patent rights are not granted by the CC BY 4.0 documentation license. Apache-2.0 software carries only the patent rights, if any, stated in Apache-2.0.

See [PATENTS.md](PATENTS.md).

## 6. Contributions

By submitting a contribution for inclusion, you represent that you have the right to submit it and agree that accepted contributions are made available under the license designated for the target file/path, unless a separate written agreement applies.

Contributors must use Developer Certificate of Origin sign-off as described in [CONTRIBUTING.md](CONTRIBUTING.md).

## 7. No implied license to excluded machinery

This repository does not include or license proprietary Veraxis machinery merely because that machinery may implement or produce objects described by the open specifications.

Examples of potentially excluded implementation domains include proprietary semantic derivation, institutional compilation, admission assistance, graph reconstruction, proprietary adapters, managed reconciliation, and other non-published implementation methods.

## 8. Legal review

This file is an operational licensing map, not legal advice. Rights holders and implementers should obtain appropriate counsel for patent, trademark, standards, and commercial-use questions.
