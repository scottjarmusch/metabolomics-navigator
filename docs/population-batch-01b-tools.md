# Content Batch 01B — GNPS, SIRIUS, and MZmine ecosystem completion

Date reviewed: 2026-08-24

This is a tools-only content batch. No Protocol records are added or modified.

## Inclusion rule used for ecosystem components

A component receives its own Tool entry when it has a distinct scientific function, a stable recognizable name, a maintained interface/documentation/repository, is reusable across studies, and is something researchers may reasonably search for independently. Small utilities and individual workflow buttons remain capabilities of the parent ecosystem rather than separate Atlas records.

## New GNPS/GNPS2 ecosystem entries

- FASST / FASST Records — accelerated indexed tandem-MS repository search infrastructure
- StructureMASST — structure/substructure-centric pan-repository searching
- microbeMASST — microbial monoculture taxonomic contextualization
- plantMASST — plant chemotaxonomic contextualization and explorer
- foodMASST — food and beverage contextualization
- microbiomeMASST — microbiome metadata-network contextualization (preprint-backed)
- ModiFinder — structural modification-site localization from paired MS/MS
- GNPS Dashboard — interactive browser-based raw/public MS-data visualization
- CMMC-KB — community-curated microbial metabolite knowledgebase (preprint-backed)
- MetaboApps — maintained collection of modular downstream GNPS2 applications

## Expanded GNPS/GNPS2 entries

- GNPS/GNPS2 — reframed as the parent ecosystem and linked to the first-class subresources above
- MASST — updated for the accelerated GNPS2 implementation and FASST-era searching
- Pan-ReDU — updated from the older ReDU-only description to the current pan-repository infrastructure
- MassQL — expanded with the 2025 Nature Methods publication, current web/API/Nextflow ecosystem, and cross-software implementations

## New SIRIUS entries

- CSI:FingerID — structure-database search through predicted molecular fingerprints
- CANOPUS — database-independent compound-class prediction
- MSNovelist — de novo structure generation; current implementation is in SIRIUS 6 and the historic standalone repository is archived

## Expanded SIRIUS entry

The SIRIUS parent page now includes current SIRIUS 6 functionality: LC-MS feature detection/alignment, identity and analog spectral-library searching, custom databases, SIRIUS/ZODIAC molecular-formula analysis, CSI:FingerID/COSMIC structure search, CANOPUS class prediction, and MSNovelist de novo generation.

## Expanded MZmine entry

The MZmine page now includes current multimodal processing and analysis capabilities: LC-MS/MS DDA/DIA, LC-IMS-MS, GC-MS, imaging, lipid annotation, local molecular networking, learned spectral-similarity models, dashboards/statistics, library generation, and current GNPS/SIRIUS integrations. Current access language reflects the academic Community program and separate commercial packages shown by the project website.

## Key sources reviewed

### GNPS/GNPS2
- Current GNPS2 documentation and tool index
- GNPS2 MASST, plantMASST, API, metadata, and dashboard documentation
- GNPS domainMASST repositories on GitHub
- Mongia et al., Nature Biotechnology (2024), DOI 10.1038/s41587-023-01985-4
- Zuffa et al., Nature Microbiology (2024), DOI 10.1038/s41564-023-01575-9
- Gomes et al., bioRxiv (2024), DOI 10.1101/2024.05.13.593988
- West et al., npj Science of Food (2022), DOI 10.1038/s41538-022-00137-3
- StructureMASST, Nature Biotechnology (2026), DOI 10.1038/s41587-026-03082-8
- ModiFinder, JASMS (2024), DOI 10.1021/jasms.4c00061
- Pan-ReDU, Nature Communications (2025), DOI 10.1038/s41467-025-60067-y
- MassQL, Nature Methods (2025), DOI 10.1038/s41592-025-02660-z
- microbiomeMASST bioRxiv (2026), DOI 10.64898/2026.02.04.703849
- CMMC-KB bioRxiv (2026), DOI 10.64898/2026.01.24.701521

### SIRIUS
- Current SIRIUS 6 documentation, methods, CLI, licensing, and changelog pages
- CSI:FingerID, PNAS (2015), DOI 10.1073/pnas.1509788112
- CANOPUS, Nature Biotechnology (2021), DOI 10.1038/s41587-020-0740-8
- MSNovelist, Nature Methods (2022), DOI 10.1038/s41592-022-01486-3
- Archived standalone MSNovelist GitHub repository and current SIRIUS integration notes

### MZmine
- Current MZmine website and documentation for molecular networking, lipid annotation, processing wizard, and integrations
- Schmid et al., Nature Biotechnology (2023), DOI 10.1038/s41587-023-01690-2
- Heuckeroth et al., Nature Protocols (2024), DOI 10.1038/s41596-024-00996-y
- Current MZmine lipid-annotation literature and MSnLib publication

## Validation

The batch was validated against the frozen v5.3.1 schema and built successfully with 25 Tool records and the existing 13 Protocol records.
