# Phase 3 — drug, food and microbial-context readouts

Reviewed 10 September 2026. The preceding query-app batch (`23456ab`) passed validation and deployed successfully (Pages run 34448559786).

Added Drug Readout, Food Readout and CMMC Dashboard, bringing the catalogue to **90 Tools and 13 Strategies**. All three appear in the interpretation guide and link to MetaboApps and FBMN. CMMC Dashboard also links to CMMC-KB and microbeMASST.

Each record now describes its actual inputs, outputs and interpretation limits. Food Readout requires matching quantification and metadata tables alongside the task identifier. CMMC Dashboard requires both enrichment and FBMN results. Drug Readout distinguishes analogue evidence and column exclusion from stronger identification or quality-control claims. These are research-context dashboards, not independent confirmations of exposure or microbial origin.

Direct implementation documentation provides the evidence citation; no standalone app paper was verified or inferred from the papers of the parent resources:

- [Drug Readout](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapp_Drug_Readout/)
- [Food Readout](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapp_Food_Readout/)
- [CMMC Dashboard](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapp_CMMC_dashboard/)

Validation passes: catalogue/schema, editorial baseline, form sync, strict build, catalogue JavaScript tests, terminology regression and both audits. The generated site contains 120 pages, 4,099 checked local links/fragments and 217 checked declared/parent-child relationship links. Nine desktop/tablet/mobile page checks pass with documentation citations, parent navigation, keyboard skip link, no overflow and no browser errors. No remote scientific jobs were run.

Phase 3 remains incomplete. Continue the GNPS2 inventory; preserve one canonical page for MS2LDA and enrich it after the child apps. Phase 4, full relationship review and Ask Navigator remain later work.
