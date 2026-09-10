# Phase 3 — conjugate explorer and resumable inventory

Reviewed 10 September 2026. The readout batch `fb675b2` deployed successfully (Pages run 34448896568, validation run 34448896573).

Added **Conjugated Metabolome Explorer**, bringing the catalogue to **91 Tools and 13 Strategies**. Its public-data guide link and MetaboApps relationship are present. The entry uses the documented SMILES input and frequency setting and distinguishes direct spectral evidence from delta-mass inference. It does not imply that a putative conjugate establishes a reaction site or enzyme.

The source is the [direct GNPS2 app documentation](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapp_Conjugated_Metabolome_Explorer/). The [app endpoint](https://conjugated-metabolome.gnps2.org/) returns a Streamlit shell. Documentation states no login is required; no search was submitted. No standalone app paper was verified, so the entry uses a documentation citation.

All required automated checks pass: schema/catalogue, form sync, editorial coverage, strict build, catalogue JavaScript tests, terminology regression and both audits. Link checks cover 4,135 local links/fragments across 121 pages and 220 declared/parent-child relationship links. Desktop/tablet/mobile page checks pass, including citation rendering, parent-link discovery, keyboard skip link, no overflow and no browser errors.

`docs/phase-3-inventory-status.md` reconciles the full supplied GNPS2 child inventory: **12 of 32 added, 20 pending**. This includes the two MassQL interfaces missed by the earlier parent-only filter. Review the additional in-development tissueMASST inventory mention before closing Phase 3, then update the existing MS2LDA page. Remaining phases have not begun.

Across this session, ten new Tools were curated and validated, and dense related-tool lists now retain every link in an expandable section. No scientific tool execution or developer verification is claimed.
