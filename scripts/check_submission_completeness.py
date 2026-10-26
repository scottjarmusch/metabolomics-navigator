"""Read-only submission checks derived from the current GitHub issue forms."""
import argparse
import json
import os
import re
from pathlib import Path
import yaml
from issue_to_tool import parse_sections

ROOT = Path(__file__).resolve().parents[1]


def submission_kind(issue):
    labels = {x.get("name", "") if isinstance(x, dict) else x for x in issue.get("labels", [])}
    title = issue.get("title", "").lower()
    kinds = [kind for kind in ("tool", "strategy")
             if f"{kind}-submission" in labels or f"[{kind} submission]:" in title]
    if len(kinds) != 1:
        raise ValueError("Submission type is missing or ambiguous; use exactly one submission label or title marker.")
    return kinds[0]


def normalize(text):
    return " ".join(text.split())


def missing_fields(issue, kind):
    form = yaml.safe_load((ROOT / f".github/ISSUE_TEMPLATE/submit-{kind}.yml").read_text(encoding="utf-8"))
    sections = parse_sections(issue.get("body") or "")
    missing = []
    for field in form["body"]:
        attributes = field.get("attributes", {})
        label = attributes.get("label")
        value = sections.get(label, "").strip()
        if field.get("validations", {}).get("required") and value.lower() in ("", "_no response_", "no response"):
            missing.append(label)
        if field["type"] == "checkboxes":
            checked = {normalize(m.group(1)) for m in re.finditer(r"^\s*- \[x\] (.+)$", value, re.M | re.I)}
            for option in attributes.get("options", []):
                if option.get("required") and normalize(option["label"]) not in checked:
                    missing.append(f"{label}: required confirmation not checked")
    return missing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", required=True, type=Path)
    args = parser.parse_args()
    payload = json.loads(args.event.read_text(encoding="utf-8"))
    issue = payload.get("issue", payload)
    try:
        kind = submission_kind(issue)
        missing = missing_fields(issue, kind)
    except ValueError as error:
        print(str(error))
        return 1
    report = [f"Submission completeness: {kind}"]
    report += [f"Missing: {label}" for label in missing] if missing else ["All required fields and confirmations are present."]
    report.append("This checks presence, not scientific accuracy, scope, URL validity or editorial quality.")
    print("\n".join(report))
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
            handle.write("\n".join(report) + "\n")
    if not missing and os.getenv("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            handle.write(f"type={kind}\nlabel={kind}-submission\n")
    return int(bool(missing))


if __name__ == "__main__":
    raise SystemExit(main())
