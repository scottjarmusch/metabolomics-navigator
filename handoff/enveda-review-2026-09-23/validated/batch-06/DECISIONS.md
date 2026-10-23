# Enveda validation batch 06

Validation date: 2026-10-06

## Include now
- LipidFinder — quality_control
- AirdPro — data_conversion
- pyOpenMS-viz — visualization_reporting
- MobiLipid — quality_control
- MetaPro — preprocessing
- MAFFIN — normalization
- IDSL_MINT — machine_learning
- Mass2SMILES — annotation_identification
- MS-BART — annotation_identification
- LipidA-IDER — annotation_identification
- SpecTUS — annotation_identification
- spectral-denoising — spectral_analysis
- ViMMS — data_acquisition
- MESSES — data_management_sharing
- ISFrag — quality_control
- DaDIA — preprocessing
- JPA — preprocessing
- BreathXplorer — preprocessing

## Hold
- AVIR remains on hold because the repository is sparse and current user-facing documentation was not sufficient for a defensible entry.

## Notes
- ViMMS is an acquisition-strategy simulator, not instrument-control software.
- MobiLipid corrects and evaluates CCS bias in IM-MS lipidomics; it is QC rather than generic CCS prediction.
- LipidFinder consumes already-preprocessed feature tables and is primarily cleanup/filtering plus lipid-oriented putative annotation.
- SpecTUS and MS-BART are research de novo structure models, so their research/benchmarking context should remain visible.
