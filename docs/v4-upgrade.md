# v4 upgrade: Tools + Protocols

This release turns Protocols into a first-class Atlas content type and enriches tool pages with capabilities, acquisition metadata, factual scope/considerations, freshness, and provenance.

## Upgrade an existing GitHub repository

1. Upload the contents of the **v4 root update** package to the repository root, replacing files when GitHub asks.
2. Open the existing `.github` directory in GitHub and upload the contents of the **v4 GitHub helper** package there.
3. If a dummy Atlas test tool is still present, delete its YAML file from `content/tools/` (for example `atlastest.yml`).
4. Commit the root update to `main`. Validation and Pages deployment should run automatically.
5. Confirm the live site now has **Find tools**, **Protocols**, **Browse**, **Contribute**, and **Submit** navigation items.
6. Open **Issues → New issue** and confirm both **Submit a metabolomics tool** and **Submit a metabolomics protocol** are available.
7. Test a protocol submission with a fake protocol. The workflow should create an automated draft pull request, just as it does for tools.

## What should appear after deployment

- 12 seeded tool entries
- 2 seeded protocol entries
- Native MS metabolomics ↔ MZmine/GNPS/MassIVE cross-links
- Reverse metabolomics ↔ MSMS-Chooser/MASST/ReDU/GNPS/MassIVE cross-links
- Tool pages with capabilities, acquisition mode, scope/considerations, version freshness, and verification metadata
- Protocol pages with workflow steps, connected tools, reusable resources, publication details, and scope/considerations
- JSON exports for tools, protocols, and the combined catalogue
