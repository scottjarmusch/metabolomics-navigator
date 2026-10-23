# Enveda expansion review — 22 October 2026

Ten tool records added from the intake. Primary DOI/title/year verified against Crossref and official documentation; no software execution, clinical validation or comparative benchmarking claimed.

| Tool | Evidence and boundaries |
| --- | --- |
| massNet | https://github.com/wabdelmoula/massNet ; DOI 10.1093/bioinformatics/btac032 (2022). Main.py expects prepared HDF5 spectra, m/z, labels and coordinates. 3D Slicer license text checked. Legacy Python/Keras/TensorFlow requirements and specimen-level evaluation caution retained. |
| WaveICA 2.0 | https://github.com/dengkuistat/WaveICA_2.0 ; DOI 10.1007/s11306-021-01839-7 (2021). Package manual requires sample-by-peak matrix and injection order. MIT LICENSE conflicts with DESCRIPTION License: No; disclose the inconsistency. Batch-label independence does not mean metadata-free correction. |
| SigmaCCS | https://github.com/zmzhang/SigmaCCS ; DOI 10.1038/s42004-023-00939-w (2023). MIT license. SMILES, adducts, conformer preparation and trained parameters required; documented predicted dataset covers protonated, sodiated and deprotonated ions. Not instrument calibration. |
| Rapid QC-MS | https://czbiohub-sf.github.io/Rapid-QC-MS/ ; DOI 10.1021/acs.analchem.4c00786 (2024). BSD-3-Clause terms verified in LICENSE.txt. Windows processing with MSConvert/MS-DIAL; chiefly Thermo-tested. Notification/cloud setup is optional and separate. |
| AutonoMS | https://autonoms.readthedocs.io/en/latest/ ; https://github.com/gkreder/autonoms ; DOI 10.1021/jasms.3c00396 (2024). Public source without explicit code license identified. Python 3.8 requirement in pyproject. Documented RapidFire–6560 hardware and vendor layout, tune-ion calibration and Skyline files required. Not a general AI scientist or arbitrary instrument controller. |
| MBROLE3 | https://csbg.cnb.csic.es/mbrole3/help.php ; DOI 10.1093/nar/gkad405 (2023). Free web service, identifier lists and background required. Direct and indirect annotation evidence distinguished. No raw-spectrum identification claim. |
| PaintOmics | https://github.com/ConesaLab/PaintOmics ; DOI 10.1093/nar/gkac352 (2022). GPL-3.0. Original paintomics4 source path now returns current PaintOmics AI README; canonical entry covers documented pathway core, with AI extension explicitly not validated here. Avoid a duplicate version-specific tool. |

Reconciled the 17 tools merged in PR #77 as published in the intake ledger. All ten new records retain editorial provenance, not developer verification. Schema, editorial completeness, strict build, relationship resolution, local links and SEO must pass before merge.

Deferred identity check: intake MetNet points to the KEGG-organism network comparison tool (10.1371/journal.pone.0246962), not the similarly named Bioconductor MS-network inference package. Do not silently substitute one for the other.

## Spectral expansion

- MSBERT: https://github.com/zhanghailiangcsu/MSBERT ; DOI 10.1021/acs.analchem.4c02426 (2024). MIT. MSP embedding/similarity examples and matchms integration verified; no comparative accuracy claims.
- MWFormer: https://github.com/zhanghailiangcsu/MWFormer ; DOI 10.1021/acs.analchem.4c03781. Journal issue 2025, online December 2024. MIT. stream.py shows MSP/peak-list inputs and molecular-weight estimates; not formula/structure generation.
- GCMSFormer: https://github.com/zxguocsu/GCMSFormer ; DOI 10.1021/acs.analchem.3c05772 (2024). MIT. Resolution.py reads netCDF and requires a model/reference vocabulary. Simulation-based training and experimental applicability limits stated.

Validation completed 2026-10-23: 191 tools, 40 Strategies and 83 education resources pass schema validation and all CI-equivalent checks. Strict build passed; 9,499 internal links/fragments across 253 pages, 318 relationship links, five SEO tests and 252 canonical pages passed. No duplicate primary publication DOIs found for the ten additions.
