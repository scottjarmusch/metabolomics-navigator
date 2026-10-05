# Enveda batch 2: QC and preprocessing

Seven new tool records passed catalogue validation and the strict site build. Source checks used the official repositories/documentation, package DESCRIPTION/license declarations, and the primary publications' DOI/title/year metadata. No software was installed or execution-tested; maintenance is not inferred from an accessible repository.

| Tool | Decision and requirements |
|---|---|
| RawHummus | Raw-data/log QC and reporting. Local R/Shiny use and hosted memory limitations are distinguished. No automatic repair claim. |
| dbnorm | Statistical batch adjustment of processed matrices. Batch labels and the documented input transformation are required; biological confounding remains a concern. |
| MAFFIN | Sample normalization using feature selection and signal correction. Serial-QC loading information is explicit. The package declares MIT plus its LICENSE file. |
| Paramounter | Reclassify from QC to preprocessing. The available implementation is R scripts, with a checked mzXML import and XCMS/MSnbase dependencies; do not advertise an installable R package without evidence. Preserve the repository warning about false-positive features. |
| QC4Metabolomics | A containerized locally deployed QC system, not a public upload portal. Record MetabolomiQCsR as a component/alias, with mzML, metadata parsing, database and worker requirements. |
| MsQuality | Standardized low-level QC metrics from Spectra/MsExperiment objects. Not a drift-correction method. Official Bioconductor page and repository explicitly support MS-metabolomics use. |
| MatrixQCvis | Interactive matrix-level QC. Require a SummarizedExperiment object; replace the intake's preprint with the journal article (online 2021; issue 2022). |

## QComics: held because publication-to-software identity is unresolved

Intake row 475 pairs `ricoderks/QComics` with DOI `10.1021/acs.analchem.3c03660`. The repository identifies a Shiny application by Rico Derks, operating on pooled-QC MultiQuant exports. The paper by González-Domínguez and colleagues describes a QC procedure implemented using common tools such as Excel and MetaboAnalyst. The primary full text does not establish a connection to that repository. Do not attach the paper as the Shiny application's primary publication merely because the names match.

Sources:
- https://github.com/ricoderks/QComics
- https://research.chalmers.se/publication/539394/file/539394_Fulltext.pdf
- https://doi.org/10.1021/acs.analchem.3c03660

This is an unresolved identity mapping, not evidence that either resource lacks value. Future review may yield separately described software and methodological resources.

## Full intake ledger

`docs/enveda-validation-ledger.tsv` preserves all 644 distinct candidate source rows from PR60's `packages/*.tsv` at commit `72687d1a0ebd7617e0c6c0eadf5544b6344063a5`. It is not an import into the public catalogue. Twelve rows have source-validated records across PR71 and this batch; Khipu-web is covered by khipu; five rows are explicitly held; all remaining rows are unreviewed. An intake flag alone never becomes validation or automatic exclusion.

Update ledger decisions in place in later batches. Check candidates against current main plus pending tool PRs to avoid duplicate work. Before publication, verify scope, software identity, primary paper, license/access, input/output requirements, relationships and the full site checks. Do not promote application papers to tool-origin publications or substitute a review for primary evidence.

## Validation completed 2026-10-05

Schema validation: 152 tools and 40 Strategies. Strict production-path build passed. All CI-equivalent checks passed, including submission/contributor tests, form synchronization, terminology, implementation rendering, catalogue behavior and SEO. Link checking resolved 7,402 local links/fragments and 294 relationship links across 213 pages.

The brand audit now exempts only the quoted third-party name column in this intake ledger; review notes remain checked. A targeted regression check confirmed that an external name containing the retired word is accepted while stale Navigator branding in review notes is rejected. Education and Ask Navigator are unchanged; this batch does not deploy or merge them.
