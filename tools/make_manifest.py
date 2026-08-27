# SPDX-FileCopyrightText: 2026 Veraxis Protocol
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import hashlib, json, datetime

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {
    "BOOTSTRAP-SHA256SUMS.txt",
    "BOOTSTRAP-MANIFEST.json",
}

records = []
for p in sorted(ROOT.rglob("*")):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT).as_posix()
    if rel in EXCLUDE or rel.startswith(".git/"):
        continue
    b = p.read_bytes()
    records.append({
        "path": rel,
        "size": len(b),
        "sha256": hashlib.sha256(b).hexdigest(),
    })

manifest = {
    "manifest_type": "working-bootstrap-manifest",
    "canonical_git_commit": None,
    "canonical_git_tag": None,
    "note": "This manifest describes the local bootstrap bytes before Git canonical freeze. Regenerate after the canonical commit/tag.",
    "artifacts": records,
}
(ROOT / "BOOTSTRAP-MANIFEST.json").write_text(
    json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n"
)
(ROOT / "BOOTSTRAP-SHA256SUMS.txt").write_text(
    "".join(f"{r['sha256']}  {r['path']}\n" for r in records),
    encoding="utf-8", newline="\n"
)
print(f"wrote manifest for {len(records)} artifacts")
