# SPDX-FileCopyrightText: 2026 Veraxis Protocol
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import json
import re
import sys

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

# All Markdown should carry an SPDX identifier.
for p in ROOT.rglob("*.md"):
    txt = p.read_text(encoding="utf-8")
    if "SPDX-License-Identifier:" not in txt[:500]:
        errors.append(f"missing SPDX identifier: {p.relative_to(ROOT)}")

# Internal Markdown links must resolve to repository paths.
md_link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for p in ROOT.rglob("*.md"):
    txt = p.read_text(encoding="utf-8")
    for target in md_link.findall(txt):
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        rel_target = target.split("#", 1)[0].split("?", 1)[0]
        if not rel_target:
            continue
        destination = (p.parent / rel_target).resolve()
        try:
            destination.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"internal link escapes repository: {p.relative_to(ROOT)} -> {target}")
            continue
        if not destination.exists():
            errors.append(f"broken internal link: {p.relative_to(ROOT)} -> {target}")

# Release-manifest schema must accept an ordinary 40-hex Git SHA shape.
release_schema_path = ROOT / "releases/RELEASE-MANIFEST.schema.json"
try:
    release_schema = json.loads(release_schema_path.read_text(encoding="utf-8"))
    commit_pattern = release_schema["properties"]["commit_sha"]["pattern"]
    if commit_pattern != r"^[0-9a-f]{40}$":
        errors.append(f"release commit_sha pattern drift: {commit_pattern!r}")
    if re.fullmatch(commit_pattern, "a" * 40) is None:
        errors.append("release commit_sha pattern rejects valid 40-hex SHA")
    if re.fullmatch(commit_pattern, "a" * 39) is not None:
        errors.append("release commit_sha pattern accepts 39-hex SHA")
    if release_schema["properties"]["artifacts"].get("minItems") != 1:
        errors.append("release manifest must require at least one artifact")
except Exception as exc:
    errors.append(f"release manifest schema invalid: {exc}")

# Evaluation joins must be canonical J1..J8, exactly once and in canonical order.
eval_schema_path = ROOT / "benchmark/schemas/icts-evaluation.schema.json"
try:
    eval_schema = json.loads(eval_schema_path.read_text(encoding="utf-8"))
    joins = eval_schema["properties"]["joins"]
    prefix = joins.get("prefixItems", [])
    if len(prefix) != 8 or joins.get("items") is not False:
        errors.append("evaluation joins schema must use exactly eight closed prefixItems")
    else:
        observed = []
        for item in prefix:
            const = item["allOf"][1]["properties"]["id"]["const"]
            observed.append(const)
        if observed != EXPECTED_JOINS:
            errors.append(f"evaluation join order drift: {observed}")
except Exception as exc:
    errors.append(f"evaluation schema invariant check failed: {exc}")

# Bounded satisfaction permission must be explicit for each J1..J8.
profile_schema_path = ROOT / "benchmark/schemas/icts-profile.schema.json"
try:
    profile_schema = json.loads(profile_schema_path.read_text(encoding="utf-8"))
    bounded = profile_schema["properties"]["bounded_permitted"]
    if bounded.get("required") != EXPECTED_JOINS:
        errors.append("bounded_permitted must explicitly require J1-J8")
    if bounded.get("additionalProperties") is not False:
        errors.append("bounded_permitted must reject unknown join keys")
except Exception as exc:
    errors.append(f"profile schema invariant check failed: {exc}")

# Mixed repository licensing must not be flattened into a false CFF single-license claim.
cff_path = ROOT / "CITATION.cff"
if cff_path.exists():
    cff = cff_path.read_text(encoding="utf-8")
    if re.search(r"(?m)^license:\s", cff):
        errors.append("CITATION.cff must not flatten component-specific licensing into one SPDX license")
    if "license-url:" not in cff:
        errors.append("CITATION.cff must point to the repository licensing map")

if errors:
    print("REPOSITORY VALIDATION: FAIL")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)

print("REPOSITORY VALIDATION: PASS")
print(f"required files: {len(REQUIRED)}")
print("canonical joins: J1-J8")
print("canonical chain: exact")
print("internal markdown links: resolved")
print("release/evaluation/profile schema invariants: enforced")
print("mixed licensing metadata: bounded")
