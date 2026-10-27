# Enveda expansion — 27 October 2026, batch 2

24 new tool records prepared independently of PR #81, which remains ready for deployment. This branch starts from main `db62d32b14db4bc2933040d8bb72d21b31578b2e`, does not include or modify the 27 entries in PR #81, and does not deploy anything. Together the batches propose 51 unique additions (245 tools after both merge, relative to the 194-tool baseline).

Official READMEs, package/vignette interfaces, license information and primary DOI/title/year metadata were inspected. This is editorial source review; no third-party tool/model was executed and no comparative benchmark or developer verification is claimed. Repository activity is distinct from operational compatibility.

## Decisions that differ from intake

- Aerith and IsoPairFinder are not assigned isotopologue_correction: their documented simulation/visualization and candidate-pair prioritization are distinct from natural-abundance correction or flux estimation.
- RALPS uses its actual Bioinformatics paper (10.1093/bioinformatics/btad096), replacing the intake's unresolved ACS DOI; within-batch correction is a prerequisite, not a claimed RALPS function.
- SMART (Statistical Metabolomics Analysis) is distinct from the spatial formula-ranking SMART. The 2016 and published 2025 update belong on this single R/GUI resource entry. Current GPL-3.0 repository and differing legacy manual terms are kept separate.
- LipiDetective cites its 2026 journal article rather than the stale preprint link. MS2Lipid cites its 2024 journal article and remains subclass-level; IsoPairFinder uses its published 2026 DOI.
- RHermes represents the HERMES formula-targeted workflow and acquisition inclusion lists, not generic calibrated quantification. SIMILE's primary function is spectral comparison, not automatic molecular-network construction.
- MetDNA3's public core algorithm and complete registered hosted workflow are distinct. Prepared MRN3 structures are documented, not universal raw-file support.
- MAW's README flags no maintenance and its license badge does not establish a complete repository grant; MeRgeION's generic GNU declaration does not establish a versioned license. RASSP has public code without an identified repository-wide license. SIMILE says Modified BSD but links a missing license.txt; no precise grant is inferred. Access labels are qualified accordingly.
- MolNotator's cited method remains labelled as a preprint. Its neutral molecule nodes and network dereplication are not confirmed structures. RASSP predicts EI spectra, not ESI tandem spectra; MSGO's PFAS/lipid models are not universal chemical-domain coverage.

## Source trail

| Entry | Official documentation | Primary DOI(s) |
| --- | --- | --- |
| Aerith (`aerith`) | https://github.com/thepanlab/Aerith#readme | https://doi.org/10.1021/acs.analchem.5c03207 |
| Amanida (`amanida`) | https://github.com/mariallr/amanida#readme | https://doi.org/10.1093/bioinformatics/btab591 |
| CordBat (`cordbat`) | https://github.com/BorchLab/CordBat/blob/main/vignettes/CordBat.Rmd | https://doi.org/10.1021/acs.analchem.2c05748 |
| GetFeatistics (`getfeatistics`) | https://frigeriogianfranco.github.io/GetFeatistics/articles/GF_vignette.html | https://doi.org/10.1515/jib-2025-0047 |
| hRUV (`hruv`) | https://sydneybiox.github.io/hRUV/ | https://doi.org/10.1038/s41467-021-25210-5 |
| imputomics (`imputomics`) | https://biogenies.info/imputomics/ | https://doi.org/10.1093/bioinformatics/btae098 |
| IsoPairFinder (`isopairfinder`) | https://doddlab.github.io/IsoPairFinder_Tutorials/ | https://doi.org/10.1021/jasms.6c00253 |
| MetaboAnnotatoR (`metaboannotator`) | https://github.com/gggraca/MetaboAnnotatoR/tree/devel/vignettes | https://doi.org/10.1021/acs.analchem.1c03032 |
| Mol2CCS (`mol2ccs`) | https://github.com/enveda/ccs-prediction#readme | https://doi.org/10.1186/s13321-024-00899-w |
| MultiBaC (`multibac`) | https://bioconductor.org/packages/release/bioc/html/MultiBaC.html | https://doi.org/10.1093/bioinformatics/btac132; https://doi.org/10.1177/0962280220907365 |
| RALPS (`ralps`) | https://github.com/zamboni-lab/RALPS#readme | https://doi.org/10.1093/bioinformatics/btad096 |
| Retention Time GNN (Kwon et al.) (`retention-time-gnn`) | https://github.com/seokhokang/retention_time_gnn#readme | https://doi.org/10.1021/acs.analchem.3c03177 |
| RHermes (`rhermes`) | https://rogerginber.github.io/RHermes/articles/RHermes_UserGuide.html | https://doi.org/10.1038/s41592-021-01307-z |
| SIMILE (`simile`) | https://github.com/biorack/simile#readme | https://doi.org/10.1038/s41467-022-30118-9 |
| SMART (Statistical Metabolomics Analysis) (`smart-metabolomics`) | https://github.com/YuJenL/SMART#readme | https://doi.org/10.1021/acs.analchem.6b00603; https://doi.org/10.1021/acs.analchem.5c03225 |
| LipiDetective (`lipidetective`) | https://lipitum.github.io/lipidetective/ | https://doi.org/10.1093/bib/bbag378 |
| MAW (`maw`) | https://github.com/zmahnoor14/MAW#readme | https://doi.org/10.1186/s13321-023-00695-y |
| MergeION (`mergeion`) | https://daniellyz.github.io/mergeion.github.io/Library_Generation_Tutorial.html | https://doi.org/10.1021/acs.analchem.2c04343 |
| MetDNA3 (`metdna3`) | https://github.com/ZhuMetLab/MrnAnnoAlgo3#readme | https://doi.org/10.1038/s41467-025-63536-6 |
| MolNotator (`molnotator`) | https://github.com/ZzakB/MolNotator#readme | https://doi.org/10.1101/2021.12.21.473622 |
| MS2Lipid (`ms2lipid`) | https://github.com/systemsomicslab/ms2lipid#readme | https://doi.org/10.3390/metabo14110602 |
| MSGO (`msgo`) | https://github.com/aaronma2020/MSGO#readme | https://doi.org/10.1038/s42256-025-01140-5 |
| RASSP (`rassp`) | https://github.com/thejonaslab/rassp-public#readme | https://doi.org/10.1021/acs.analchem.2c02093 |
| TARDIS (`tardis`) | https://pablovgd.github.io/TARDIS/ | https://doi.org/10.1021/acs.analchem.5c00567 |

The ledger reconciles 24 matching intake rows for this batch. No Education, Strategies or Ask Navigator changes. Validation results are recorded in the PR after running the resulting catalogue checks.

Validation: schema covers 218 tools, 40 Strategies and 83 education resources. Editorial coverage, form sync, submission/contributor regressions, Strategy terminology/implementation tests, branding, catalogue JavaScript tests, strict production build, 10,562 local links/fragments across 280 pages, 318 relationships, five SEO tests and 279 canonical pages passed. Generated HTML is inspected directly; no browser visual inspection or third-party software benchmark is claimed.
