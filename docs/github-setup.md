# GitHub setup

This repository is configured for `scottjarmusch/metabolomics-navigator`.

## Required repository settings

1. **Settings → Pages → Source:** GitHub Actions.
2. **Settings → Actions → General → Workflow permissions:** Read and write permissions.
3. Enable **Allow GitHub Actions to create and approve pull requests**.

## Labels

The submission workflow now creates/refreshes these automatically when a tool or strategy submission arrives:

- `tool-submission`
- `tool-update`
- `strategy-submission`
- `strategy-update`
- `needs-triage`
- `automated-draft`

They may also be created manually under **Issues → Labels**.

## Test the contribution routes

### Tool
Open **Issues → New issue → Submit a metabolomics tool**. A successful submission should create a structured draft pull request automatically.

### Strategy
Open **Issues → New issue → Submit a metabolomics strategy**. A successful submission should create a structured strategy draft and cross-link tool names that already exist in the Navigator.

Validation runs on every pull request. Merging a valid entry into `main` automatically rebuilds GitHub Pages.
