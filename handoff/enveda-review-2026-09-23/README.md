# Enveda computational-metabolomics review → Navigator intake handoff

Source review: https://github.com/enveda/computational-metabolomics-review  
Source dataset: `tools_list.tsv`  
Navigator taxonomy baseline: current `main` branch as of 2026-09-23.

This directory is an **editorial intake package**, not a publication batch. It mines the review inventory, excludes NMR-category records, de-duplicates obvious existing/versioned Navigator resources, and maps new candidates into Navigator's current vocabulary where possible.

## Mining summary

- 747 source records
- 47 records excluded because the source category contains NMR
- 56 records matched to an existing Navigator slug or likely versioned existing tool
- 644 new intake candidates
- 3 candidates could not be mapped confidently to an existing primary function and are isolated for taxonomy/manual review

## Package structure

- `packages/*.tsv`: candidate manifests grouped by proposed Navigator **primary function**
- `manual-review.tsv`: taxonomy, scope, mixed-platform, and adjacent-field cases
- `existing-or-version.tsv`: likely existing Navigator tools or version updates
- `excluded-nmr.tsv`: source rows excluded under the no-NMR rule
- `source-category-mapping.yml`: first-pass mapping rules

Each candidate row includes the source-review category, publication/tool links, proposed Navigator function/platform/analysis/interface/resource-type fields, and review flags.

## Editorial boundary

Do **not** copy these rows directly into `content/tools/`.

The Enveda review is a discovery source. Before a candidate becomes a Navigator entry, verify against the tool's official site/repository/documentation and primary publication:

1. Current metabolomics relevance and scope
2. Primary/secondary Navigator functions and capabilities
3. Analytical platforms and analysis types
4. Interfaces
5. Access model/license
6. Inputs/outputs and formats
7. Maintenance/activity
8. Claims, limitations, and citations

Rows flagged `scope_review_adjacent_field` may be proteomics, ICP-MS, general cheminformatics, or other adjacent-domain resources. Include only where an MS-metabolomics use case is defensible.

Rows flagged `mixed_nmr_mentions` were not automatically removed if the source category itself was not NMR; this catches multi-platform resources that may still have valid MS functionality.

## Taxonomy suggestions surfaced

- **Single-cell metabolomics:** consider `single_cell_metabolomics` as an analysis type rather than a new primary function.
- **Ion mobility:** the current `acquisition.ion_mobility` field covers compatibility, but the number of dedicated tools suggests evaluating whether users need an explicit discovery/filter dimension.
- **FT-ICR MS:** treat as an analyzer/acquisition dimension; do not automatically equate FT-ICR with direct infusion.
- **Biosynthetic gene cluster ↔ metabolomics linking:** most tools fit `multiomics_integration` and/or `reference_data_search`, but a capability such as `genome_metabolome_linking` could improve discovery.
- **IR-assisted identification:** standalone IR tools should remain out of Navigator's MS scope; MS+IR annotation resources can be reviewed individually without adding a general IR platform.
