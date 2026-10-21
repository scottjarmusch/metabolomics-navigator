# Enveda specialist tool batch — 21 October 2026

Based on current main (1928131). Adds two tool entries, with no Ask Navigator changes.

- MSI-Explorer (row 3): napari imaging-MS software. Verified imzML input, ROI/spectrum exploration, preprocessing and mass-based database annotation in the official manual. BSD-3-Clause verified in LICENSE. Record is explicitly not a bulk LC-MS processing recommendation.
- MobiLipid (row 19): R Markdown CCS quality-control workflow, not a generic lipid-identification or flux tool. Requires labeled standards and ion-mobility measurements. Repository code availability is recorded separately from licensing: no explicit software license identified. No correction capability is inferred for unsupported class/adduct combinations.

Primary titles, DOI and publication years checked against Crossref and PubMed; no application-only publications added. Neither tool was present in current main by name/DOI, or among the first 100 changed paths in intake PRs 60/74. The broader intake PRs remain separate. No installation, execution or performance validation performed; maintenance status remains unclear.

## Sources

- https://github.com/MMV-Lab/MSI-Explorer — official manual and LICENSE
- https://pubmed.ncbi.nlm.nih.gov/40476501/ — MSI-Explorer, Analytical Chemistry (2025), DOI 10.1021/acs.analchem.5c01513
- https://github.com/FelinaHildebrand/MobiLipid — official workflow and input requirements
- https://pubmed.ncbi.nlm.nih.gov/38693701/ — MobiLipid, Analytical Chemistry (2024), DOI 10.1021/acs.analchem.4c01253

Status: validated entries pending merge. Review is editorial, not developer verification. Existing intake ledger statuses outside this batch are unchanged.

## Validation

Catalogue schema passes for 166 tools, 40 Strategies and 83 Education resources. Form synchronization, editorial coverage, submission/contributor checks, Strategy terminology and implementations, branding and catalogue JavaScript checks pass. Final strict production-path build passes; 8,539 local links/fragments and 313 relationships pass. All five SEO tests and metadata checks across 227 canonical pages pass. Both rendered entries contain their publication and scope details.
