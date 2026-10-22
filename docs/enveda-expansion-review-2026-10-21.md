# Enveda tool expansion — 21 October 2026

Nine additional records, following MSI-Explorer and MobiLipid in the same tools-only review branch. No Ask Navigator code or Education release changes.

| Tool | Evidence and editorial decision |
|---|---|
| FragHub | Official manual and 2024 primary paper. Reference-library processing, not raw peak extraction. LICENSE says CC BY-NC 4.0 despite the CeCILL README badge; disclose the conflict and classify as source available. |
| MRMQuant | Official repository, releases and primary 2024 paper (PMC11339730). MRM mzML/text, target transitions and calibration prerequisites recorded. Explicit code license not located; do not equate the paper's open-source wording with verified reuse terms. |
| Eclipse | BMXP module manual and 2025 journal paper. Matches compatible-method feature tables. Custom license includes commercial redistribution restrictions despite its MIT heading. |
| LipidSigR | Official package DESCRIPTION, tutorials and 2025 journal record. Separate R package linked to the existing LipidSig web tool. Correct DOI is 10.1093/bioadv/vbaf047; use the 2025 journal issue year (Crossref's generic published field differs). |
| DeepRTAlign | Official manual and 2023 primary paper. Paper explicitly includes metabolomics; prepared feature tables, not raw spectra. |
| QuantyFey | Official tutorial and 2025 primary paper. Works on integrated signals, not peak integration. README has multiple installation routes despite a Windows-only overview; describe route-dependent requirements. |
| NP3 MS Workflow | Official manual, GPL-3.0-or-later license and 2024 primary paper. GNPS2 interface documented; full local CLI distinct. Preserve manual caution for less-tested negative-mode steps. |
| MS2Planner | Official manual, academic/noncommercial license and 2021 primary paper. Link existing Strategy to software entry; no new Strategy. Outputs schedules requiring instrument-compatible conversion. |
| LipidFinder | Official README/MIT metadata, original 2017 and version-2 journal papers. One canonical entry across versions. Version-2 journal issue is 2021 (online metadata includes 2020). High-resolution chromatographically separated lipid features; no shotgun/MS/MS claims. |

Each entry links the official documentation and DOI. Primary DOI/title/year checked using Crossref plus journal/PubMed records where date fields differ. Inclusion is editorial review, not developer verification, execution testing or independent performance validation. No comparative accuracy claims copied.

Reconciled 15 previously validated rows against main as published. MSnLib, GNPS2, ChemWalker and Met-ID were already covered by canonical records; mark covered rather than create duplicates. Their intake publications are not automatically appended. Other rows retain their existing status. MolDiscovery remains unreviewed: the current repository README mainly redirects to an academic service, so deployment/access and implementation need further examination.

Nine-entry batch validation: schema and all CI-equivalent local checks passed for 175 tools, 40 Strategies and 83 learning resources. Strict build passed; 8,886 links/fragments, 315 relationships, five SEO tests and metadata for 236 canonical pages passed. No shared tool-publication DOI duplicates found for these nine additions.

## Second expansion batch

- MAMSI: official PyPI package, GitHub README/LICENSE and 2025 primary paper (10.1021/acs.analchem.5c01327). BSD-3-Clause. Matched multiblock abundance data and modeled outcome required; annotation limited to documented NPC assays. https://github.com/kopeckylukas/py-mamsi
- SEISMiQ: official prediction documentation/LICENSE and final 2025 Digital Discovery paper (10.1039/D5DD00115C), replacing the intake preprint. Apache-2.0 code; separate model/data terms remain distinct. Formula plus spectrum required. Drug-impurity domain and CASMI checkpoint support stated without claiming broad biological-metabolite validation. https://github.com/Boehringer-Ingelheim/seismiq

Second batch validation: 177-tool strict build passed. Final link check: 8,964 links/fragments across 239 pages and 315 relationship links; SEO passed for 238 canonical pages.

## Third expansion batch — 22 October 2026

- Met4DX: https://github.com/ZhuMetLab/Met4DX and DOI 10.1021/jasms.4c00290 (2024). R/Docker processing for documented timsTOF PASEF and Agilent IM-AIF inputs. LICENCE is CC BY-NC-ND 4.0, so source available rather than unrestricted open source. Mode-specific precursor/calibration prerequisites retained.
- GNN-RT: https://github.com/Qiong-Yang/GNN-RT and DOI 10.1021/acs.analchem.0c04071 (2021). Graph-based RT prediction as orthogonal small-molecule annotation evidence; chromatographic adaptation required. AGPL-3.0 metadata verified.
- FastEI: https://github.com/Qiong-Yang/FastEI and DOI 10.1038/s41467-023-39279-7 (2023). EI matching, not LC-ESI-MS/MS or chromatogram deconvolution. Official example.py/test.py demonstrate two-column query spectra and ranked retrieval. Apache-2.0 LICENSE verified.
- SMQVP: https://github.com/mzlab-research/SMQVP and DOI 10.3390/metabo15060354 (2025). Spatial peak tables, not raw imaging import. Requires pixel coordinates and extracted intensities. No explicit code license identified; hosted service not execution-tested.

Crossref titles/years checked for all four. No shared primary DOI found against existing catalogue tool entries. All describe documented capabilities, not independently tested performance.

Final 17-tool batch validation: 181 tools, 40 Strategies and 83 education resources pass the strict build and all CI-equivalent local checks. Post-build checks passed for 9,120 local links/fragments across 243 pages, 315 relationships, five SEO tests and 242 canonical pages. A transient Windows generated-file lock interrupted the first build; the retry completed successfully.
