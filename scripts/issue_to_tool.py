#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

from common import ROOT, TOOLS_DIR, load_vocab, reverse_label_maps, slugify

LABELS = {
    "name": "Tool name",
    "primary": "Best link for the tool",
    "summary": "What does the tool do?",
    "resource_types": "What kind of resource is it?",
    "primary_function": "What is its main function?",
    "secondary_functions": "Other functions",
    "platforms": "Which analytical platforms does it support?",
    "interfaces": "How do researchers use it?",
    "access": "How is it accessed?",
    "role": "What is your relationship to the tool?",
    "publication": "Primary publication or DOI",
    "additional_links": "Additional links",
    "contact": "Name or ORCID for attribution",
    "notes": "Anything else we should know?",
}

LINK_KEYS = {
    "homepage": "homepage",
    "web app": "web_app",
    "web application": "web_app",
    "repository": "repository",
    "source": "repository",
    "source code": "repository",
    "documentation": "documentation",
    "docs": "documentation",
    "download": "download",
    "tutorial": "tutorial",
    "issue tracker": "issue_tracker",
    "biotools": "biotools",
    "bio.tools": "biotools",
    "workflowhub": "workflowhub",
}


def parse_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current: str | None = None
    lines: list[str] = []
    for line in body.splitlines():
        if line.startswith("### "):
            if current is not None:
                sections[current] = "\n".join(lines).strip()
            current = line[4:].strip()
            lines = []
        elif current is not None:
            lines.append(line)
    if current is not None:
        sections[current] = "\n".join(lines).strip()
    return sections


def clean(value: str | None) -> str:
    value = (value or "").strip()
    return "" if value in {"_No response_", "No response"} else value


def selected(value: str) -> list[str]:
    value = clean(value)
    if not value:
        return []
    items: list[str] = []
    for line in value.splitlines():
        line = re.sub(r"^[-*]\s+", "", line.strip())
        if line:
            items.extend(item.strip() for item in line.split(",") if item.strip())
    return list(dict.fromkeys(items))


def map_values(values, mapping, field):
    missing = [value for value in values if value not in mapping]
    if missing:
        raise ValueError(f"Unknown {field} selection(s): {', '.join(missing)}")
    return [mapping[value] for value in values]


def parse_additional_links(text: str) -> dict[str, str]:
    links: dict[str, str] = {}
    for line in clean(text).splitlines():
        match = re.match(r"\s*([^:]+):\s*(https?://\S+)\s*$", line)
        if not match:
            continue
        label, href = match.groups()
        key = LINK_KEYS.get(label.strip().lower())
        if key:
            links[key] = href.rstrip(".,")
    return links


def parse_contact(text: str):
    text = clean(text)
    orcid_match = re.search(
        r"0000-000[0-9]-[0-9]{4}-[0-9]{3}[0-9X]", text
    )
    email_match = re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text)
    cleaned = text
    if orcid_match:
        cleaned = cleaned.replace(orcid_match.group(0), "")
    if email_match:
        cleaned = cleaned.replace(email_match.group(0), "")
    name = cleaned.strip(" ;,|-")
    return (
        name or None,
        orcid_match.group(0) if orcid_match else None,
        email_match.group(0) if email_match else None,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True)
    args = parser.parse_args()

    event = json.loads(Path(args.event).read_text(encoding="utf-8"))
    issue = event["issue"]
    sections = parse_sections(issue.get("body", ""))

    def value(key: str) -> str:
        return clean(sections.get(LABELS[key], ""))

    vocab = load_vocab()
    reverse = reverse_label_maps(vocab)
    name = value("name")
    if not name:
        raise ValueError("Tool name is missing")
    slug = slugify(name)
    path = TOOLS_DIR / f"{slug}.yml"
    if path.exists():
        raise ValueError(
            f"An entry already exists at {path}. Use the update form instead."
        )

    summary = value("summary")
    if len(summary) > 500:
        summary = summary[:497].rstrip() + "..."
    primary = value("primary")
    date_created = issue.get("created_at", str(date.today()))[:10]

    resource_types = map_values(
        selected(value("resource_types")),
        reverse["resource_types"],
        "resource type",
    )
    primary_function = map_values(
        [value("primary_function")],
        reverse["functions"],
        "primary function",
    )[0]
    secondary = map_values(
        selected(value("secondary_functions")),
        reverse["functions"],
        "secondary function",
    )
    secondary = [item for item in secondary if item != primary_function]
    platforms = map_values(
        selected(value("platforms")), reverse["platforms"], "platform"
    )
    interfaces = map_values(
        selected(value("interfaces")), reverse["interfaces"], "interface"
    )
    access = map_values(
        [value("access")], reverse["access_models"], "access model"
    )[0]
    role = map_values(
        [value("role")], reverse["submission_roles"], "submitter role"
    )[0]

    links = {"primary": primary}
    links.update(parse_additional_links(value("additional_links")))
    host = urlparse(primary).netloc.lower()
    if "github.com" in host and "repository" not in links:
        links["repository"] = primary
    elif "docs" in host and "documentation" not in links:
        links["documentation"] = primary
    elif "homepage" not in links:
        links["homepage"] = primary

    publications = []
    publication = value("publication")
    if publication:
        doi = re.search(r"10\.\d{4,9}/\S+", publication, flags=re.I)
        if doi:
            publications.append(
                {"doi": doi.group(0).rstrip(".,;)"), "type": "primary"}
            )
        else:
            publications.append({"citation": publication, "type": "primary"})

    submitter_name, submitter_orcid, _email = parse_contact(value("contact"))
    provenance = {
        "submitted_by": role,
        "source_issue": issue["html_url"],
        "developer_verified": False,
    }
    if submitter_name:
        provenance["submitter_name"] = submitter_name
    if submitter_orcid:
        provenance["submitter_orcid"] = submitter_orcid
    notes = [item for item in [value("notes")] if item]
    if notes:
        provenance["notes"] = "\n".join(notes)[:1000]

    record = {
        "$schema": "../../schemas/tool.schema.json",
        "slug": slug,
        "name": name,
        "summary": summary,
        "links": links,
        "resource_types": resource_types,
        "functions": {
            "primary": primary_function,
            "secondary": secondary,
            "capabilities": [],
        },
        "platforms": platforms,
        "analysis_types": [],
        "interfaces": interfaces,
        "access": {"model": access},
        "publications": publications,
        "common_uses": [],
        "scope": {},
        "acquisition": {},
        "related_tools": [],
        "maintenance": {
            "status": "unclear",
            "last_checked": date_created,
        },
        "credits": [],
        "provenance": provenance,
        "status": {
            "entry": "stub",
            "review": "unreviewed",
            "created_at": date_created,
            "updated_at": date_created,
            "last_verified": date_created,
        },
    }
    if submitter_name and role in {"developer", "maintainer"}:
        credit = {"name": submitter_name, "role": role}
        if submitter_orcid:
            credit["orcid"] = submitter_orcid
        record["credits"].append(credit)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(
            record,
            sort_keys=False,
            allow_unicode=True,
            width=1000,
        ),
        encoding="utf-8",
    )

    output = os.getenv("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"path={path.relative_to(ROOT).as_posix()}\n")
            handle.write(f"slug={slug}\n")
            handle.write(f"name={name}\n")
            handle.write("type=tool\n")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
