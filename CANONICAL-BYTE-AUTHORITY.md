<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Canonical Byte Authority

## Rule

For raw repository artifacts, the **exact bytes identified by an immutable Git commit or tag** are the canonical byte authority.

Human-readable filenames, Dropbox mirrors, chat attachments, generated previews, and local working copies are not canonical merely because they contain logically similar text.

## Raw artifacts

For a raw source artifact:

`artifact_digest = SHA-256(exact bytes stored for the identified Git tree object)`

Git normalization rules for this repository are defined in `.gitattributes`. Text is committed with LF line endings.

## Structured logical objects

Cross-implementation identities for structured objects require a separately specified canonical serialization.

A raw-file hash and a logical-object hash answer different questions and must not be substituted for one another.

## Publication archives

Publication workflow should be:

**immutable Git tag → reproducible release bundle → release manifest/digests → publication archive (for example Zenodo)**

The publication archive should identify the source Git tag/commit from which it was produced.

## Working mirrors

Dropbox may be used for collaboration, review, and evidence exchange. It is not the release byte authority unless a future specification explicitly says otherwise.

## Corrections

A corrected release receives a successor identity. The predecessor tag and release artifacts remain part of the historical record.
