#!/usr/bin/env python3
"""Verify kernel files only import from the pinned allowlist.

Uses AST parsing (not grep) to extract all import statements from
kernel-scope files and checks them against the allowlist defined in
spec/kernel_import_allowlist_v1.json.

Usage:
    python3 spec/verify_kernel_imports.py
"""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ALLOWLIST_PATH = REPO_ROOT / "spec" / "kernel_import_allowlist_v1.json"


def extract_imports(filepath: Path) -> list[tuple[int, str]]:
    """Return list of (line_number, module_name) for all imports in file."""
    source = filepath.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(filepath))

    imports: list[tuple[int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append((node.lineno, alias.name.split(".")[0]))
        elif isinstance(node, ast.ImportFrom):
            if node.module is not None:
                imports.append((node.lineno, node.module.split(".")[0]))
    return imports


def main() -> None:
    with ALLOWLIST_PATH.open("r", encoding="utf-8") as f:
        config = json.load(f)

    allowed = set(config["allowed_modules"])
    scope_files = config["scope"]

    passed = 0
    failed = 0

    for rel_path in scope_files:
        filepath = REPO_ROOT / rel_path
        if not filepath.exists():
            print(f"  [SKIP] {rel_path} -- file not found")
            continue

        imports = extract_imports(filepath)
        file_ok = True

        for lineno, module in imports:
            # Allow self-imports (aaa_eal importing from aaa_eal)
            if module == "aaa_eal":
                continue
            if module not in allowed:
                print(f"  [FAIL] {rel_path}:{lineno} -- disallowed import: {module}")
                file_ok = False
                failed += 1

        if file_ok:
            print(f"  [PASS] {rel_path}")
            passed += 1

    print()
    print(f"Kernel import allowlist: {passed} passed, {failed} violations")

    if failed > 0:
        print("Kernel files must only import from:", sorted(allowed))
        sys.exit(1)


if __name__ == "__main__":
    main()
