# Enveda validation batch 02

Validation date: 2026-10-06

## Include now
- PCPFМ / Python-Centric Pipeline for Metabolomics — workflow_reproducibility
- Nextflow4MS-DIAL — workflow_reproducibility
- DNMS2Purifier — spectral_analysis
- QC4Metabolomics — quality_control
- InjectionDesign — quality_control
- RapidMass — annotation_identification
- ShinyMetID — annotation_identification
- LipiDex 2 — annotation_identification

## Hold for another pass
- EVA — official repository points to a newer pyEVA implementation; resolve whether Navigator should use EVA, pyEVA, or alias both.
- AVIR — repository exists but current user-facing documentation is too weak for a confident editorial entry.
- MatrixQCvis — validate against current Bioconductor package rather than rely on the Enveda GitHub-style mapping.
- AnnoSM — repository metadata exists but user-facing documentation could not be confidently retrieved in this pass.
- Paramounter — valid method/code, but documentation is sparse and parameter optimization behavior needs closer editorial review before publication.

## Notes
- Workflow wrappers are not categorized as preprocessing just because they execute preprocessing software.
- Tool dependencies and downstream integrations should be represented explicitly rather than merged into a single tool identity.
- Missing SPDX metadata is left unspecified rather than inferred from repository files.
