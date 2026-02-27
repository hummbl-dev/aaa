#!/usr/bin/env python3
"""Verify EAL conformance fixtures deterministically.

Checks:
- report schema validity
- primary_reason_code equals first reason_codes entry
- reason_codes order follows precedence
- expected_report_sha256 matches canonical expected_report bytes
"""

from __future__ import annotations

import glob
import hashlib
import json
from pathlib import Path

from jsonschema import validate


PRECEDENCE = [
    "E_INPUT_MALFORMED",
    "E_CONTRACT_VERSION_COLLISION",
    "E_SIG_INVALID",
    "E_HASH_MISMATCH",
    "E_EVIDENCE_MISSING",
    "E_EPOCH_AMBIGUOUS",
    "E_ACTION_OUT_OF_SPACE",
    "E_BOUNDARY_MISMATCH",
    "E_LOG_CHAIN_BREAK",
    "E_LOG_SEQUENCE_GAP",
    "E_REPLAY_DETECTED",
    "E_EPOCH_INVALIDATED",
    "E_OK_VALID",
]
PRECEDENCE_INDEX = {code: idx for idx, code in enumerate(PRECEDENCE)}


def canonical_json_bytes(obj: dict) -> bytes:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return payload.encode("utf-8")


def verify_fixture(path: Path, schema: dict) -> None:
    with path.open("r", encoding="utf-8") as fh:
        fixture = json.load(fh)

    report = fixture["expected_report"]
    validate(instance=report, schema=schema)

    reason_codes = report["reason_codes"]
    primary = report["primary_reason_code"]

    if reason_codes[0] != primary:
        raise ValueError(
            f"{path.name}: primary_reason_code ({primary}) does not match reason_codes[0] ({reason_codes[0]})"
        )

    if sorted(reason_codes, key=lambda code: PRECEDENCE_INDEX[code]) != reason_codes:
        raise ValueError(f"{path.name}: reason_codes are not in precedence order")

    digest = hashlib.sha256(canonical_json_bytes(report)).hexdigest()
    declared = fixture["expected_report_sha256"]
    if digest != declared:
        raise ValueError(f"{path.name}: hash mismatch {digest} != {declared}")


def main() -> int:
    base = Path(__file__).resolve().parent
    schema_path = base / "validation_report.schema.json"
    with schema_path.open("r", encoding="utf-8") as fh:
        schema = json.load(fh)

    fixture_paths = sorted(Path(p) for p in glob.glob(str(base / "fixtures" / "*.json")))
    if not fixture_paths:
        raise ValueError("no fixtures found")

    for fixture_path in fixture_paths:
        verify_fixture(fixture_path, schema)
        print(f"PASS {fixture_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
