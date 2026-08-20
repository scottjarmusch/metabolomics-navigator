from __future__ import annotations

import json
import os
import re
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote, urlencode

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "content" / "tools"
VOCAB_PATH = ROOT / "data" / "controlled-vocabulary.yml"
SCHEMA_PATH = ROOT / "schemas" / "tool.schema.json"


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_vocab():
    return load_yaml(VOCAB_PATH)


def load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_tools():
    records = []
    for path in sorted(TOOLS_DIR.glob("*.y*ml")):
        record = load_yaml(path)
        record["_path"] = path
        records.append(record)
    return records


def validator():
    return Draft202012Validator(load_schema(), format_checker=FormatChecker())


def slugify(value: str) -> str:
    import unicodedata
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value or "tool"


def label_maps(vocab):
    sections = {
        "resource_types": "resource_types",
        "functions": "functions",
        "capabilities": "capabilities",
        "platforms": "platforms",
        "analysis_types": "analysis_types",
        "interfaces": "interfaces",
        "access_models": "access_models",
        "maintenance_statuses": "maintenance_statuses",
        "entry_statuses": "entry_statuses",
        "review_statuses": "review_statuses",
        "submission_roles": "submission_roles",
        "operating_systems": "operating_systems",
        "common_data_formats": "common_data_formats",
        "common_data_types": "common_data_types",
    }
    return {key: {item["id"]: item["label"] for item in vocab[src]} for key, src in sections.items()}


def reverse_label_maps(vocab):
    return {key: {label: ident for ident, label in values.items()} for key, values in label_maps(vocab).items()}


def derive_base_path(explicit: str | None = None) -> str:
    if explicit is not None:
        value = explicit.strip()
    elif os.getenv("BASE_PATH") is not None:
        value = os.getenv("BASE_PATH", "").strip()
    elif os.getenv("GITHUB_REPOSITORY"):
        owner, repo = os.environ["GITHUB_REPOSITORY"].split("/", 1)
        value = "" if repo.lower() == f"{owner.lower()}.github.io" else f"/{repo}"
    else:
        value = ""
    if value in {"", "/"}:
        return ""
    return "/" + value.strip("/")


def record_date(record, key, default="0000-00-00"):
    value = record.get("status", {}).get(key, default)
    if isinstance(value, date):
        return value.isoformat()
    return str(value or default)


def date_display(value):
    if not value:
        return "Not recorded"
    if isinstance(value, date):
        value = value.isoformat()
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").strftime("%d %B %Y").lstrip("0")
    except ValueError:
        return str(value)


def counts_for(tools, field):
    counter = Counter()
    for tool in tools:
        value = tool
        for part in field.split("."):
            value = value.get(part, {}) if isinstance(value, dict) else None
        if isinstance(value, list):
            counter.update(value)
        elif value:
            counter[value] += 1
    return counter
