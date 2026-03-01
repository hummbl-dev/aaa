#!/usr/bin/env python3
"""Verify SHA-256 integrity of all pinned normative artifacts.

Usage:
    python3 spec/verify_pinned_artifacts.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "spec" / "PINNED_ARTIFACTS_v1.json"


def main() -> None:
    with MANIFEST.open("r", encoding="utf-8") as f:
        manifest = json.load(f)

    artifacts = manifest["artifacts"]
    passed = 0
    failed = 0

    for rel_path, expected_sha256 in artifacts.items():
        full_path = REPO_ROOT / rel_path
        if not full_path.exists():
            print(f"  [FAIL] {rel_path} -- file not found")
            failed += 1
            continue

        actual_sha256 = hashlib.sha256(full_path.read_bytes()).hexdigest()
        if actual_sha256 == expected_sha256:
            print(f"  [PASS] {rel_path}")
            passed += 1
        else:
            print(f"  [FAIL] {rel_path}")
            print(f"         expected: {expected_sha256}")
            print(f"         actual:   {actual_sha256}")
            failed += 1

    print()
    print(f"Pinned artifact verification: {passed} passed, {failed} failed")

    if failed > 0:
        print("WARNING: Pinned artifact hash mismatch. If this is intentional,")
        print("update spec/PINNED_ARTIFACTS_v1.json with new hashes.")
        sys.exit(1)


if __name__ == "__main__":
    main()
