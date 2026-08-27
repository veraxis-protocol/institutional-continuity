<!-- SPDX-FileCopyrightText: 2026 Veraxis Protocol -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Bootstrap Push Procedure

This package is intended to become one coherent initial repository commit.

## Before pushing

1. Confirm repository visibility is the intended state.
2. Complete the IP/public-disclosure gate.
3. Inspect `LICENSE.md`, `PATENTS.md`, and `TRADEMARKS.md`.
4. Run:

```bash
python3 tools/validate_repo.py
python3 tools/make_manifest.py
git status --short
```

5. Confirm no private review corpus, secrets, unpublished patent-sensitive implementation material, or credentials are present.

## Recommended first commit

From the extracted directory:

```bash
git init
git branch -M main
git remote add origin https://github.com/veraxis-protocol/institutional-continuity.git
git add .
git commit -s -m "bootstrap: establish Institutional Continuity Infrastructure category repository"
git push -u origin main
```

If the remote already contains a commit, do **not** force-push blindly. Fetch and inspect first.

## Canonical freeze

After the first push, record the exact commit:

```bash
git rev-parse HEAD
git show --no-patch --format=fuller HEAD
```

Do not create the first immutable release tag until the owner has approved the exact committed bytes.

## Release tag example

```bash
git tag -a ici/v0.1.0 -m "ICI category model v0.1.0"
git push origin ici/v0.1.0
```

A later ICTS release should receive its own `icts/...` tag.
