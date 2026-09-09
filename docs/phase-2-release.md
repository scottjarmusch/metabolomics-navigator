# Phase 2 — curated Analytical Strategies

## Collection

Retained Reverse metabolomics and Native MS metabolomics for metal-binding compounds. Added all 11 supplied candidates after curation: bioactivity-based networking, chemoselective metabolomics, feature credentialing, two IDBac strategies, metabologenomics, MSI-guided networking, OzID structural lipidomics, isotope-labeling networking, taxonomically informed annotation, and 3D cartography.

The collection remains 13 Strategies, but now contains methodological layers rather than routine software procedures. ChemProp, Qemistree and RDD remain Tool concepts.

## Preserved software workflows

Moved the 11 routine records from `content/strategies/` to `content/tool-workflows/`. The mapping in `config/tool-workflows.yml` places them on GNPS, MZmine, MASST, CANOPUS, CSI:FingerID, MSNovelist and SIRIUS. Tool pages render expandable descriptions, steps, requirements, considerations and original citations. Full source records remain versioned. Removed Strategy-to-Strategy links to the retired pages; their canonical Tool links remain.

## Scientific corrections

- Corrected Kuo/Huang/Hsu and Klitgaard/Nielsen/Frandsen/Andersen/Nielsen attribution.
- Anchored OzID to the original Thomas et al. analytical-method paper, DOI 10.1021/ac7017684, rather than using a later software paper as its origin. LipidOz is explicitly a later implementation; removed the conflation with OzFAD.
- Limited credentialing's platform scope to the supported LC-MS example and removed the unsupported environmental objective.
- Distinguished the demonstrated mouse serum/liver setting for chemoselective metabolomics from possible later adaptations.
- Added bioactivity-networking software-version compatibility notes and Cytoscape; removed the generic MassIVE homepage as evidence of a dataset-specific raw-data resource.
- Explained that contemporary metabologenomics and taxonomy resources are not necessarily software from the original papers.
- Updated editorial dates without claiming author verification or independent software benchmarking.

## Relationships

Seven pending relationships use the schema's existing external-resource representation until the corresponding Tools are populated: Cytoscape, IDBac (two Strategies), NPLinker, MIBiG, LipidOz and 'ili. `config/pending-strategy-tools.yml` records them for conversion to internal links. No dangling internal slugs or relaxed validation.

## Validation

Passed catalogue/schema validation (79 Tools, 13 Strategies, 11 preserved workflows), form synchronization, editorial readiness, strict Pages build, catalogue JavaScript tests, 3,661 local links across 109 pages, terminology regression tests, and both terminology audits. Preserved workflow owner mappings and schema validation are now part of catalogue validation.

Browser checks passed for 33 existing route/viewport combinations plus all 13 Strategies at three widths (39 checks). Verified GNPS workflow disclosure. Mobile Strategy rendering was inspected. Full release QA remains in Phase 7.

Phase 3 is next: GNPS2 Tool population. Ask Navigator remains a placeholder.
