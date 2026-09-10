# Phase 3 — search, GC-MS processing and structure classification

Reviewed 10 September 2026. Phase 3 remains in progress; Phase 4 and Ask Navigator have not started.

Added three dedicated Tools, bringing the catalogue to **84 Tools and 13 Strategies**:

- **MS2Query**: exact-match candidates and analogue retrieval from MS/MS, with Python and GNPS2 interfaces. Added its MS2DeepScore integration alongside Spec2Vec. Kept the direct 2023 tool paper only.
- **MSHub-GC**: GC-MS alignment/deconvolution. Distinguished the launchable processing workflow from downstream networking in the wider published system. Verified CDF, mzML and mzXML inputs from the current workflow definition, including one format per input folder.
- **NPClassifier**: classification from supplied structures, explicitly distinguished from prediction directly from spectra. Documented the SMILES interface, JSON output, software/model licensing and hosted query logging; removed the unsupported draft CSV-output claim.

All three have requirements, interpretation limits, access notes and GNPS parent relationships. Their task-guide links are in place. No scientific analysis jobs were submitted or benchmarked. GNPS2 workflow launch URLs resolved to HTTP 200 login pages; that establishes routing, not successful analysis execution.

## Navigation regression found during QA

The builder silently truncated every related-tool list at eight, hiding new GNPS children. All declared relationships are now rendered, with entries after the first eight inside a native keyboard-accessible disclosure. This is a bounded discovery fix needed for the new entries; the wider Phase 5 relationship and page-quality review remains outstanding.

The site-link checker now verifies declared relationships and parent-to-child discovery, in addition to checking that existing links resolve. It checks 186 relationship links in this build.

## Evidence

- [MS2Query GNPS2 documentation](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/ms2query_doc/), [implementation and license](https://github.com/iomega/ms2query), [direct paper](https://doi.org/10.1038/s41467-023-37446-4).
- [MSHub-GC documentation](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/mshub-gc_doc/), [current input definition](https://github.com/Wang-Bioinformatics-Lab/mshub-gc_workflow/blob/master/workflowinput.yaml), [direct paper](https://doi.org/10.1038/s41587-020-0700-3).
- [NPClassifier repository, interface and licenses](https://github.com/mwang87/NP-Classifier), [hosted interface](https://npclassifier.gnps2.org/), [direct paper](https://doi.org/10.1021/acs.jnatprod.1c00399).
- [GNPS2 hosted-access guidance](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/).

## Validation

Catalogue/schema, form sync, editorial coverage, strict Pages build, catalogue JavaScript tests, terminology regression tests and both terminology audits pass. The generated site has 114 pages and 3,857 checked local links/fragments. Nine new-Tool route/viewport checks (1280, 640, 390 px) pass without horizontal overflow or browser errors. Publications render, GNPS reveals all three links using the keyboard, and the skip link remains the first keyboard stop. No software benchmark or full Phase 7 accessibility certification is implied.

Next: remaining GNPS2 workflows and MetaboApps, scientific web apps, then MS2LDA 2.0 enrichment. Consult the full inventory, including MassQL Analysis/Playground outside the preliminary parent filter. Do not advance phases until the inventory is reconciled and validated.
