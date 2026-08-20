#!/usr/bin/env python
from __future__ import annotations

import sys
from pathlib import Path

import yaml

from common import ROOT, load_vocab, label_maps

FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "submit-tool.yml"

EXPECTED = {
    "resource-types": "resource_types",
    "primary-function": "functions",
    "secondary-functions": "functions",
    "platforms": "platforms",
    "interfaces": "interfaces",
    "access-model": "access_models",
    "submitter-role": "submission_roles",
}


def main():
    form = yaml.safe_load(FORM.read_text(encoding="utf-8"))
    body = {item.get("id"): item for item in form.get("body", []) if item.get("id")}
    labels = label_maps(load_vocab())
    failed = False
    for field_id, vocab_key in EXPECTED.items():
        actual = body[field_id]["attributes"]["options"]
        expected = list(labels[vocab_key].values())
        if actual != expected:
            failed = True
            print(f"ERROR: {field_id} options differ from controlled vocabulary")
            print("  expected:", expected)
            print("  actual:  ", actual)
    if failed:
        return 1
    print("Submission-form options match the controlled vocabulary.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
