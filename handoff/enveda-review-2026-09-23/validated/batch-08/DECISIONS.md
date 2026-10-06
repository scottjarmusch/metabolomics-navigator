# Enveda validation batch 08

Validation date: 2026-10-06

## Include now
- Norm-ISWSVR — normalization
- isoSCAN — isotope_tracing_flux
- FAMetA — isotope_tracing_flux
- rIDIMS — preprocessing
- SERDA — normalization
- ConCISE — molecular_networking
- BAM — molecular_networking
- SGMNS — molecular_networking
- GNN-RT — machine_learning
- SigmaCCS — machine_learning
- PACCS — machine_learning
- FSA — annotation_identification
- DeepION — machine_learning
- FIDDLE — annotation_identification
- DiffSpectra — annotation_identification
- mssearchr — spectral_analysis
- MASSISTANT — annotation_identification
- CRISP — preprocessing
- DiffMS — annotation_identification
- mass2adduct — annotation_identification
- OrbiFragsNets — annotation_identification
- TeFT — annotation_identification
- MOCCal — preprocessing
- CCSfind — preprocessing
- DeepGCN-RT — machine_learning

## Hold
- MCN/molecular_communities is too sparsely documented for promotion in this pass.
- 3D-MPEA source repository no longer resolves.
- SagMSI repository metadata is too sparse for a defensible draft.
- MRMPro documentation repository is too sparse; locate the primary software/documentation home first.
- AsRTNet is highly application-specific and needs a separate scope review.

## Taxonomy corrections
- SERDA is a normalization method despite its Enveda placement under isotope tracing.
- rIDIMS is direct-infusion MS processing/preprocessing, not stable-isotope analysis.
- MOCCal and CCSfind calculate/calibrate or curate experimental CCS; they are not structure-based CCS prediction tools.
