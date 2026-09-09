# v4 upgrade: Tools + Strategies

This release turns Strategies into a first-class Navigator content type and enriches tool pages with capabilities, acquisition metadata, factual scope/considerations, freshness, and provenance.

## Upgrade an existing GitHub repository

1. Upload the contents of the **v4 root update** package to the repository root, replacing files when GitHub asks.
2. Open the existing `.github` directory in GitHub and upload the contents of the **v4 GitHub helper** package there.
3. If a dummy Navigator test tool is still present, delete its YAML file from `content/tools/` (for example `navigatortest.yml`).
4. Commit the root update to `main`. Validation and Pages deployment should run automatically.
5. Confirm the live site now has **Find tools**, **Strategies**, **Browse**, **Contribute**, and **Submit** navigation items.
6. Open **Issues → New issue** and confirm both **Submit a metabolomics tool** and **Submit a metabolomics strategy** are available.
7. Test a strategy submission with a fake strategy. The workflow should create an automated draft pull request, just as it does for tools.

## What should appear after deployment

- 12 seeded tool entries
- 2 seeded strategy entries
- Native MS metabolomics ↔ MZmine/GNPS/MassIVE cross-links
- Reverse metabolomics ↔ MSMS-Chooser/MASST/ReDU/GNPS/MassIVE cross-links
- Tool pages with capabilities, acquisition mode, scope/considerations, version freshness, and verification metadata
- Strategy pages with workflow steps, connected tools, reusable resources, publication details, and scope/considerations
- JSON exports for tools, strategies, and the combined catalogue
