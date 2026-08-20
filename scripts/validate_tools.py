#!/usr/bin/env python
from __future__ import annotations

import sys
from collections import Counter

from common import load_tools, validator


def format_path(path):
    return ".".join(str(p) for p in path) or "<root>"


def main():
    tools = load_tools()
    check = validator()
    failed = False
    slugs = []
    names = []
    for record in tools:
        path = record["_path"]
        clean_record = {key: value for key, value in record.items() if key != "_path"}
        errors = sorted(check.iter_errors(clean_record), key=lambda e: list(e.absolute_path))
        if errors:
            failed = True
            print(f"ERROR: {path}")
            for error in errors:
                print(f"  {format_path(error.absolute_path)}: {error.message}")
        slugs.append(record.get("slug"))
        names.append((record.get("name") or "").casefold())
    for label, values in (("slug", slugs), ("name", names)):
        duplicates = [value for value, count in Counter(values).items() if value and count > 1]
        if duplicates:
            failed = True
            print(f"ERROR: duplicate {label}(s): {', '.join(duplicates)}")
    known = set(slugs)
    for record in tools:
        path = record["_path"]
        for related in record.get("related_tools", []):
            if related["slug"] not in known:
                failed = True
                print(f"ERROR: {path}: related tool '{related['slug']}' does not exist")
    if failed:
        return 1
    print(f"Validated {len(tools)} tool records successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
