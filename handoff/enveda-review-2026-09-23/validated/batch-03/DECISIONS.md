# Enveda validation batch 03

Validation date: 2026-10-06

## Include now
- G-Aligner — preprocessing
- metaboprep — quality_control
- LPPtiger 2 — annotation_identification
- AutoCCS — preprocessing
- MS2DECIDE — annotation_identification
- pyEVA — quality_control

## Taxonomy notes
- AutoCCS calculates/calibrates experimental collision cross sections; it should not be labeled with the existing `ccs_prediction` capability.
- pyEVA is treated as the current implementation lineage of EVA; retain EVA as an alias/history note rather than publish two near-duplicate entries.
- metaboprep is primarily study-level QC/filtering of processed metabolomics tables, not raw-data preprocessing.
- LPPtiger 2 is specialized epilipid/oxidized-lipid annotation and in-silico fragmentation, not a general lipidomics suite.
