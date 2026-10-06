# Enveda validation batch 07

Validation date: 2026-10-06

## Include now
- MobilityTransformR — data_conversion
- mspack — data_conversion
- LipidSpace — statistics
- ALISTER — reference_data_search
- MassQLab — spectral_analysis
- IonToolPack — quality_control
- QComics — quality_control
- LipidQMap — quantification
- MeTEor — statistics
- PLSKO — machine_learning
- omicsMIC — statistics
- arcMS — data_conversion
- msiFlow — workflow_reproducibility
- lcmsWorld — visualization_reporting

## Hold
- DisCoPad is currently primarily a reproducibility/code repository around a paper rather than a clearly packaged researcher-facing tool.
- SpectraX has insufficient user-facing documentation for a confident entry.
- GraphBio and MODE are broad omics visualization applications; hold pending a scope decision on generic omics resources.
- OSCA-Finder remains sparse and needs a second pass.

## Notes
- ALISTER is a curated pre-analytical knowledge resource, not a data-processing QC algorithm.
- IonToolPack contains multiple omics-agnostic MS utilities; primary Navigator function is QC because PeakQC is a central workflow, with visualization as secondary.
- msiFlow is a workflow collection for MSI/microscopy and is best represented as workflow_reproducibility rather than visualization alone.
