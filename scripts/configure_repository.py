#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml

from common import ROOT


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Configure repository URLs after copying the starter project."
    )
    parser.add_argument(
        "repository",
        help="GitHub repository in OWNER/REPOSITORY format.",
    )
    args = parser.parse_args()

    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repository):
        raise SystemExit("Repository must use OWNER/REPOSITORY format.")

    owner, repo = args.repository.split("/", 1)
    repository_url = f"https://github.com/{owner}/{repo}"
    pages_base = "" if repo.lower() == f"{owner.lower()}.github.io" else f"/{repo}"
    pages_url = f"https://{owner.lower()}.github.io{pages_base}/"

    site_path = ROOT / "config" / "site.yml"
    site = yaml.safe_load(site_path.read_text(encoding="utf-8"))
    site["repository_url"] = repository_url
    site_path.write_text(
        yaml.safe_dump(site, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )

    citation_path = ROOT / "CITATION.cff"
    citation = yaml.safe_load(citation_path.read_text(encoding="utf-8"))
    citation["repository-code"] = repository_url
    citation["url"] = pages_url
    citation_path.write_text(
        yaml.safe_dump(citation, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )

    schema_path = ROOT / "schemas" / "tool.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    schema["$id"] = f"{pages_url}schemas/tool.schema.json"
    schema_path.write_text(
        json.dumps(schema, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Configured {args.repository}")
    print(f"Repository: {repository_url}")
    print(f"Pages URL:  {pages_url}")


if __name__ == "__main__":
    main()
