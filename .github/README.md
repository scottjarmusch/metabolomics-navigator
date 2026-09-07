# Metabolomics Navigator

An open, community-maintained guide to **metabolomics tools** and **published, transferable protocols**, with practical scope, data requirements, documentation and scientific sources.

**Public website:** [Metabolomics Navigator](https://scottjarmusch.github.io/metabolomics-navigator/).
The repository and site use the `metabolomics-navigator` name. The repository was renamed from `metabolomics-tool-atlas`; use the website link above for the current GitHub Pages address.

The current beta contains **31 tools and resources** and **13 protocols**. See the [September expansion and sources](https://github.com/scottjarmusch/metabolomics-navigator/blob/main/docs/expansion-2026-09.md).

Metabolomics Navigator is designed around two linked questions:

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

- [Submit a tool or resource](https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=submit-tool.yml)
- [Update an existing tool](https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=update-tool.yml)
- [Submit a published protocol](https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=submit-protocol.yml)
- [Update an existing protocol](https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=update-protocol.yml)

A free GitHub account is required. Update forms open correction requests for editorial review; they do not automatically change an entry. New-entry automation requires GitHub Actions permissions to create pull requests. See [CONTRIBUTING.md](https://github.com/scottjarmusch/metabolomics-navigator/blob/main/CONTRIBUTING.md).

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

## Tool editorial baseline

See [the tool editorial model](https://github.com/scottjarmusch/metabolomics-navigator/blob/main/docs/tool-editorial-model.md) for the completion checklist, source trail, representative entries and validation commands.
