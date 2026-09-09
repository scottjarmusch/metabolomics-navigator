# Metabolomics Navigator

An open, community-maintained guide to **MS-based metabolomics tools** and **published, transferable strategies**, with practical scope, data requirements, documentation and scientific sources.

**Public website:** [Metabolomics Navigator](https://scottjarmusch.github.io/metabolomics-navigator/).

The homepage offers six task categories, each opening a dedicated guide. The searchable catalogue remains available under Tools.

The current beta contains **79 tools and resources** and **13 strategies**. See the [September expansion and sources](docs/expansion-50-2026-09.md).

Metabolomics Navigator is designed around two linked questions:

- **Tools:** What software, database, spectral library, repository, service, or workflow can I use?
- **Strategies:** How have researchers combined experimental and computational steps to solve a reusable metabolomics problem?

## Repository structure

- `content/tools/` — one YAML record per tool
- `content/strategies/` — one YAML record per strategy
- `schemas/` — JSON Schemas for both content types
- `data/controlled-vocabulary.yml` — controlled categories and tags
- `templates/` + `assets/` — static website templates and styling
- `scripts/` — validation, issue parsing, cross-linking, and site generation
- `.github/ISSUE_TEMPLATE/` — simple researcher submission/update forms
- `.github/workflows/` — validation, submission-to-PR automation, and GitHub Pages deployment

## Community contribution model

Researchers can submit either a tool or a strategy through a GitHub Issue Form. The automation converts the form into a structured YAML draft and opens a pull request. A maintainer reviews the proposed entry; schema validation protects the live catalogue; merging to `main` automatically rebuilds GitHub Pages.

- [Submit a tool or resource](https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=submit-tool.yml)
- [Update an existing tool](https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=update-tool.yml)
- [Submit a published strategy](https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=submit-strategy.yml)
- [Update an existing strategy](https://github.com/scottjarmusch/metabolomics-navigator/issues/new?template=update-strategy.yml)

A free GitHub account is required. Update forms open correction requests for editorial review; they do not automatically change an entry. New-entry automation requires GitHub Actions permissions to create pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md).

Strategy and tool records are cross-linked. A strategy can list the tools it uses, while a tool page automatically lists strategies that use it. Tool-to-tool relationships are stored once where possible and safe inverse relationships are generated automatically.

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

The v5.3 information model supports tool aliases and an automatically inverted relationship graph, strategy sample types, biological contexts, organisms, disease-state and host–microbe objectives, explicit editorial inclusion/verification rules, and automated collision checking. The legacy `sample_contexts` field has been retired. A synthetic 500-tool stress test is available in `scripts/stress_test.py`; see `docs/scaling-test.md`.

## Tool editorial baseline

See [the tool editorial model](docs/tool-editorial-model.md) for the completion checklist, source trail, representative entries and validation commands.

## Current analytical scope

The Navigator currently covers mass-spectrometry-based metabolomics. NMR-only and other non-MS-only resources are outside scope. Shared databases, statistical tools and platforms remain eligible where they support MS metabolomics; entries describe their relevant use. The September expansion and publication-audit documents are historical snapshots. See [the MS scope update](docs/ms-scope-2026-09-08.md).
