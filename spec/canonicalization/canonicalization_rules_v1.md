# Canonicalization Rules v1 (Normative)

**Ruleset ID:** `aaa-canonical-json-v1`
**Version:** 1.0.0
**Status:** Normative. This is the single authoritative source for AAA v1 canonicalization.

---

## Rules

1. **Serialization format:** JSON (RFC 8259).
2. **Object key ordering:** Lexicographic sort by Unicode codepoint (Python: `sort_keys=True`).
3. **Nested objects:** Recursively sorted by the same rule.
4. **Arrays:** Preserve original order (no reordering).
5. **Whitespace:** None. Compact separators only (`,` between elements, `:` between key-value).
6. **Strings:** UTF-8 encoded. No Unicode NFC/NFD normalization applied. Non-ASCII characters preserved as-is (`ensure_ascii=False`).
7. **Numbers:** Integers preserved as-is. Floats SHOULD be avoided; if present, they MUST use the serializer's default representation with no trailing zeros added or removed.
8. **Booleans:** Lowercase `true`/`false` per JSON spec.
9. **Null:** Lowercase `null` per JSON spec.
10. **Trailing newline:** MUST NOT be included in the canonical byte stream.
11. **Encoding:** Exact UTF-8 bytes. No BOM.
12. **Hash algorithm:** SHA-256 over the canonical byte stream.

## Reference Implementation

```python
import json
import hashlib

def canonical_json_bytes(obj: dict) -> bytes:
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")

def sha256_hex(obj: dict) -> str:
    return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
```

## Verification

For any input object, the canonical byte stream MUST be identical across:

- Different machines
- Different locales
- Different Python versions (3.8+)
- Different JSON libraries implementing these rules

Any implementation producing different bytes for the same logical object is non-conformant.
