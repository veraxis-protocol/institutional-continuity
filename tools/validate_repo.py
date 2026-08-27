# SPDX-FileCopyrightText: 2026 Veraxis Protocol
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import json, sys, re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "STATUS.md",
    "CLAIMS.md",
    "GOVERNANCE.md",
    "LICENSE.md",
    "PATENTS.md",
    "TRADEMARKS.md",
    "CANONICAL-BYTE-AUTHORITY.md",
    "spec/CATEGORY-CONSTITUTION.md",
    "spec/CANONICAL-CHAIN.md",
    "spec/INVARIANTS.md",
    "spec/ONTOLOGY.json",
    "benchmark/ICTS-SPEC.md",
    "benchmark/PROFILE-CONTRACT.md",
    "LICENSES/Apache-2.0.txt",
    "LICENSES/CC-BY-4.0.txt",
]

CHAIN = "SOURCE → ADMITTED MEANING → WARRANTED CONTROL → RUNTIME AUTHORITY → EXACT ACTION → CONSEQUENCE → INDEPENDENT OBSERVATION → RECONCILIATION → EXAMINATION"
EXPECTED_JOINS = [f"J{i}" for i in range(1, 9)]

errors = []

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

for rel in ["README.md", "spec/CATEGORY-CONSTITUTION.md", "spec/CANONICAL-CHAIN.md"]:
    p = ROOT / rel
    if p.exists() and CHAIN not in p.read_text(encoding="utf-8"):
        errors.append(f"canonical chain drift/missing: {rel}")

op = ROOT / "spec/ONTOLOGY.json"
if op.exists():
    try:
        obj = json.loads(op.read_text(encoding="utf-8"))
        ids = [j.get("id") for j in obj.get("joins", [])]
        if ids != EXPECTED_JOINS:
            errors.append(f"ontology joins must be exactly {EXPECTED_JOINS}, got {ids}")
        req = obj.get("full_ici_required_joins")
        if req != EXPECTED_JOINS:
            errors.append("full_ici_required_joins drift")
    except Exception as exc:
        errors.append(f"ontology JSON invalid: {exc}")

# Normative docs must not contain common drafting placeholders.
normative = [
    ROOT / "spec/CATEGORY-CONSTITUTION.md",
    ROOT / "spec/INVARIANTS.md",
    ROOT / "benchmark/ICTS-SPEC.md",
    ROOT / "benchmark/PROFILE-CONTRACT.md",
]
placeholder = re.compile(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b")
for p in normative:
    if p.exists() and placeholder.search(p.read_text(encoding="utf-8")):
        errors.append(f"drafting placeholder in normative file: {p.relative_to(ROOT)}")

# All generated Markdown should carry an SPDX identifier.
for p in ROOT.rglob("*.md"):
    txt = p.read_text(encoding="utf-8")
    if "SPDX-License-Identifier:" not in txt[:500]:
        errors.append(f"missing SPDX identifier: {p.relative_to(ROOT)}")

if errors:
    print("REPOSITORY VALIDATION: FAIL")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)

print("REPOSITORY VALIDATION: PASS")
print(f"required files: {len(REQUIRED)}")
print("canonical joins: J1-J8")
print("canonical chain: exact")
