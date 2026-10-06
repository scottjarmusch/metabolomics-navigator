#!/usr/bin/env python
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas" / "tool.schema.json").read_text(encoding="utf-8"))
HANDOFF = ROOT / "handoff" / "enveda-review-2026-09-23" / "validated"

def main() -> int:
    validator = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
    files = sorted(HANDOFF.glob("batch-*/tools/*.yml"))
    failed = False
    seen_slugs: dict[str, Path] = {}

    for path in files:
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(record), key=lambda e: list(e.absolute_path))
        for error in errors:
            failed = True
            loc = ".".join(str(p) for p in error.absolute_path) or "<root>"
            print(f"ERROR: {path.relative_to(ROOT)}: {loc}: {error.message}")

        slug = record.get("slug")
        if slug:
            if slug in seen_slugs:
                failed = True
                print(f"ERROR: duplicate handoff slug {slug}: {seen_slugs[slug]} and {path}")
            seen_slugs[slug] = path

    if failed:
        return 1
    print(f"Validated {len(files)} Enveda handoff tool drafts successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
