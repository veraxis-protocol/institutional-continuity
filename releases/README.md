<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Releases

A release should be produced from an immutable Git commit/tag.

## Required release metadata

- component/version;
- commit SHA;
- tag;
- release UTC time;
- claim ceiling;
- supersedes / superseded-by relationship where applicable;
- exact artifact digests;
- criteria/profile/vector identities where applicable;
- toolchain identity where applicable;
- licensing inventory.

## Publication archive

When a release is deposited to a publication archive, the archive metadata should cite the exact Git tag/commit and carry a matching release manifest.

Do not generate canonical publication artifacts from a mutable Dropbox working copy.
