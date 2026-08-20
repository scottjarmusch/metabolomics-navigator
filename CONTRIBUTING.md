# Contributing

## Submit a tool

Use the **Submit a tool** issue form. Only the basic information needed to create and categorize a stub is required.

## Improve an existing entry

Use the **Update an existing tool** form or edit the corresponding YAML file in `content/tools/` and open a pull request.

## Editorial expectations

- Use neutral, factual language.
- Link claims about performance to a publication or benchmark.
- Disclose when you are a developer or maintainer.
- Avoid rankings, promotional slogans, and unsupported superlatives.
- Separate tool capabilities from independent evidence about performance.
- Do not copy substantial text from software websites or publications.

## Validation

Run before opening a pull request:

```bash
pip install -r requirements.txt
python scripts/validate_tools.py
python scripts/check_form_sync.py
python scripts/build_site.py
```

## Review labels

- **Developer submitted** describes provenance.
- **Developer verified** means a named developer reviewed the entry.
- **Editorially reviewed** means a catalogue editor checked categorization, links, and neutral presentation.
- **Independently benchmarked** appears only when an independent benchmark publication is recorded.
