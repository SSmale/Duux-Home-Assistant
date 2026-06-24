#!/usr/bin/env python3
"""Reorder manifest.json keys to match the order hassfest expects.

domain and name come first; all other keys follow alphabetically.
"""
import json
import sys
from pathlib import Path

MANIFEST = Path("custom_components/duux/manifest.json")


def sorted_manifest(data: dict) -> dict:
    priority = ["domain", "name"]
    rest = sorted(k for k in data if k not in priority)
    return {k: data[k] for k in priority + rest if k in data}


def main() -> int:
    original = MANIFEST.read_text()
    data = json.loads(original)
    reordered = sorted_manifest(data)
    fixed = json.dumps(reordered, indent=2) + "\n"
    if fixed == original:
        return 0
    MANIFEST.write_text(fixed)
    print(f"Fixed key order in {MANIFEST}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
