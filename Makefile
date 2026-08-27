# SPDX-FileCopyrightText: 2026 Veraxis Protocol
# SPDX-License-Identifier: Apache-2.0

.PHONY: validate manifest

validate:
	python3 tools/validate_repo.py

manifest:
	python3 tools/make_manifest.py
