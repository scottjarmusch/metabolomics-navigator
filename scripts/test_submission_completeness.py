import unittest
import yaml
from check_submission_completeness import ROOT, missing_fields, submission_kind


def complete_issue(kind="tool"):
    form = yaml.safe_load((ROOT / f".github/ISSUE_TEMPLATE/submit-{kind}.yml").read_text(encoding="utf-8"))
    parts = []
    for field in form["body"]:
        a = field.get("attributes", {})
        if "label" not in a:
            continue
        value = "Example" if field.get("validations", {}).get("required") else "_No response_"
        if field["type"] == "checkboxes":
            value = "\n".join("- [x] " + o["label"] for o in a.get("options", []) if o.get("required"))
        parts.append("### " + a["label"] + "\n\n" + value)
    return {"title": f"Example[{kind.title()} submission]:", "body": "\n\n".join(parts)}


class CompletenessTests(unittest.TestCase):
    def test_nonstandard_title_is_detected(self):
        self.assertEqual(submission_kind(complete_issue()), "tool")

    def test_label_without_title_marker(self):
        self.assertEqual(submission_kind({"title": "Example", "labels": [{"name": "strategy-submission"}]}), "strategy")

    def test_ambiguous_type_fails(self):
        with self.assertRaises(ValueError):
            submission_kind({"title": "[Tool submission]:", "labels": ["strategy-submission"]})

    def test_optional_fields_do_not_block(self):
        for kind in ("tool", "strategy"):
            self.assertEqual(missing_fields(complete_issue(kind), kind), [])

    def test_empty_required_summary_is_named(self):
        issue = complete_issue()
        issue["body"] = issue["body"].replace("### What does the tool do?\n\nExample", "### What does the tool do?\n\n_No response_")
        self.assertIn("What does the tool do?", missing_fields(issue, "tool"))

    def test_unchecked_consent_fails(self):
        issue = complete_issue()
        issue["body"] = issue["body"].replace("- [x] I consent", "- [ ] I consent")
        self.assertTrue(any("attribution and privacy" in x for x in missing_fields(issue, "tool")))

    def test_unrelated_checkbox_is_not_consent(self):
        issue = complete_issue()
        issue["body"] = issue["body"].replace("- [x] I consent", "- [x] Some other statement\n- [ ] I consent")
        self.assertTrue(missing_fields(issue, "tool"))

    def test_uppercase_checked_boxes(self):
        issue = complete_issue(); issue["body"] = issue["body"].replace("[x]", "[X]")
        self.assertEqual(missing_fields(issue, "tool"), [])


if __name__ == "__main__":
    unittest.main()
