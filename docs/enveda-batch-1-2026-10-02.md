# Enveda intake: first isotope/spatial batch

The review inventory is a discovery source, not evidence that each row deserves a separate Navigator entry. This batch selects five tools after checking official repositories, package metadata and primary publication metadata. It does not import the bulk handoff or change Ask Navigator.

| Intake candidate | Decision | Evidence / boundary |
|---|---|---|
| khipu | Add annotation tool | Official README describes ion grouping and neutral-mass inference. Not a flux solver. https://github.com/shuzhao-li-lab/khipu ; DOI 10.1021/acs.analchem.2c05810 |
| Khipu-web | Fold into khipu publication coverage | Interface extension from the same project; avoid a duplicate tool card. DOI 10.1021/jasms.4c00175 |
| SIMPEL | Add isotope post-processing tool | Separate downstream flux modelling is required. Official package DESCRIPTION and primary paper: https://github.com/SIMPELmetabolism/SIMPEL ; DOI 10.1038/s42003-024-05844-z |
| isoSCAN | Add GC-CI-MS tool | Restrict platform to documented GC chemical-ionization MS; the intake's LC-MS label is not supported by the package description. https://github.com/jcapelladesto/isoSCAN ; DOI 10.1021/acs.analchem.0c02998 |
| FAMetA | Add fatty-acid isotope modelling tool | Package DESCRIPTION declares GPL (>=2). The paper's hosted app was not availability-tested. https://github.com/maialba3/FAMetA ; DOI 10.1093/bib/bbad064 |
| 13C-SpaceM | Add research-code resource | Not a turnkey replacement for SpaceM. Public code has no verified explicit license and requires prepared registration/segmentation outputs. https://github.com/Buglakova/13C-SpaceM ; DOI 10.1038/s42255-024-01118-4 |
| gutSMASH | Hold for separate scope review | A biosynthetic/metabolic gene-cluster resource must not be imported as a flux-analysis tool from the intake mapping. |
| IsoSolve | Hold | Mixed-platform/NMR flag needs evidence for the specific MS workflow before inclusion. |
| IsoPairFinder | Hold | Verify primary publication status and distinguish maintained software from experimental web reimplementations. |
| LipidSIM | Hold | Intake has no software URL; locate an official implementation and access terms. |

Publication metadata were checked through Crossref. isoSCAN's primary paper was published online in December 2020 and assigned to a 2021 issue; the record makes the date distinction explicit. No installation, execution, benchmark or developer verification is claimed. Maintenance remains unclear rather than inferred from repository availability. Tool names/aliases were searched in the existing catalogue before adding records.

Next batch: QC/preprocessing candidates, followed by annotation candidates that fill published Strategy steps. Recheck against the current catalogue, not only the intake's older duplicate list. Keep input compatibility separate from lexical search relevance.
