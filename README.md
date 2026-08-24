# Metabolomics Tool Atlas

A community-maintained, GitHub-native atlas of **metabolomics tools** and **published, transferable protocols**.

The Atlas is designed around two linked questions:

- **Tools:** What software, database, spectral library, repository, service, or workflow can I use?
- **Protocols:** How have researchers combined experimental and computational steps to solve a reusable metabolomics problem?

## Repository structure

- `content/tools/` — one YAML record per tool
- `content/protocols/` — one YAML record per protocol
- `schemas/` — JSON Schemas for both content types
- `data/controlled-vocabulary.yml` — controlled categories and tags
- `templates/` + `assets/` — static website templates and styling
- `scripts/` — validation, issue parsing, cross-linking, and site generation
- `.github/ISSUE_TEMPLATE/` — simple researcher submission/update forms
- `.github/workflows/` — validation, submission-to-PR automation, and GitHub Pages deployment

## Community contribution model

Researchers can submit either a tool or a protocol through a GitHub Issue Form. The automation converts the form into a structured YAML draft and opens a pull request. A maintainer reviews the proposed entry; schema validation protects the live catalogue; merging to `main` automatically rebuilds GitHub Pages.

Protocol and tool records are cross-linked. A protocol can list the tools it uses, while a tool page automatically lists protocols that use it. Tool-to-tool relationships are stored once where possible and safe inverse relationships are generated automatically.

## Local validation and build

```bash
python -m pip install -r requirements.txt
python scripts/validate_catalogue.py
python scripts/check_form_sync.py
python scripts/build_site.py --strict
```

The generated static site is written to `dist/` and is intentionally not committed.

## Licenses

Code is licensed under `LICENSE-CODE`. Catalogue prose and structured content are licensed under `LICENSE-CONTENT` unless otherwise noted.

## Pre-population hardening

The v5.3 information model supports tool aliases and an automatically inverted relationship graph, protocol sample types, biological contexts, organisms, disease-state and host–microbe objectives, explicit editorial inclusion/verification rules, and automated collision checking. The legacy `sample_contexts` field has been retired. A synthetic 500-tool stress test is available in `scripts/stress_test.py`; see `docs/scaling-test.md`.
