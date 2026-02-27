# Canonicalization Rules (Determinism)

These rules define how report hashes are computed for conformance checks.

## Report Canonical Form

1. Serialize report object as canonical JSON with sorted keys and compact form.
2. Use UTF-8 encoding.
3. Do not include trailing newline in canonical byte stream.
4. Compute SHA-256 over canonical bytes.

Shell reference:

```bash
canonical=$(jq -cS '.expected_report' conformance/fixtures/T1_VALID.json | tr -d '\n')
hash=$(printf '%s' "$canonical" | shasum -a 256 | awk '{print $1}')
```

## Conformance Rule

For each fixture:

- `expected_report_sha256` MUST equal SHA-256 of canonicalized `expected_report`.
- `classification`, `primary_reason_code`, and `reason_codes` MUST match expected
  report exactly.

## Stability Rule

A fixture hash change is a contract change. Any update to `expected_report` must
be accompanied by:

1. revised `expected_report_sha256`
2. explicit changelog note
3. compatibility decision (`non-breaking` or `breaking`)
