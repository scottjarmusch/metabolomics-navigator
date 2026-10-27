# Enveda expansion review — 27 October 2026

This batch prepares 27 genuinely new catalogue records against main `db62d32b14db4bc2933040d8bb72d21b31578b2e`. It enriches selected handoff drafts from PR #74; it does not bulk-import that branch or overwrite the 19 draft slugs already covered by live records. Entries are proposed for review; they are not deployed by this document.

## Evidence and limits

Official README/documentation and repository license information were checked on 27 October 2026. Publication DOI/title/year metadata were checked with Crossref and primary publisher/resource pages where needed. Repository activity is recorded separately from maintenance confidence. No third-party software, pretrained model or hosted analysis job was executed; no benchmark, developer verification or independent validation is claimed.

Corrections to intake:
- OpenTIMS: removed the unrelated DOI 10.1038/s41592-021-01332-y (Editing naive CD4+ T cells); replaced with the actual OpenTIMS/TimsPy/TimsR paper, 10.1021/acs.jproteome.0c00962.
- DEIMoS: CCS calibration is not molecular-structure CCS prediction; removed ccs_prediction.
- TIMSCONVERT: removed macOS support because the documented SDK route is incompatible; GUI/CLI and separate Bruker terms are explicit.
- SpectriPy: R package wrapping Python functionality, rather than a separately advertised Python package.
- InjectionDesign, specXplore and TidyMS: added missing primary publications.
- MIST-CF: distinguishes public NPLIB1 and NIST-restricted pretrained models, formula ranking versus structure identification, and first-online 2023 versus issue 2024.
- MS-RIDD: source LGPL and assembly CC-BY terms are distinguished; requires CID-derived annotations and OAD spectra.
- PCPFM: MIT text is prefaced by planned-release wording, so access is conservatively unclear. No silent unrestricted-license claim.
- specXplore: Windows guidance conflicts within the README; the macOS ARM similarity warning is retained. Current operational compatibility was not tested.
- NeatMS: archived repository recorded; stale documentation's publication-pending statement is distinguished from the later primary paper.
- The Tidy-Direct-to-MS intake row is held separately: a shared repository does not establish that the new base TidyMS entry covers its distinct 2023 publication.

## Per-entry source trail

| Entry | Official documentation | Primary publication DOI(s) |
| --- | --- | --- |
| BLINK (`blink`) | https://github.com/biorack/blink#readme | https://doi.org/10.1038/s41598-023-40496-9 |
| DEIMoS (`deimos`) | https://deimos.readthedocs.io/ | https://doi.org/10.1021/acs.analchem.1c05017 |
| DreaMS (`dreams`) | https://dreams-docs.readthedocs.io/ | https://doi.org/10.1038/s41587-025-02663-3 |
| MassCube (`masscube`) | https://huaxuyu.github.io/masscubedocs/docs/quickstart/ | https://doi.org/10.1038/s41467-025-60640-5 |
| MassFormer (`massformer`) | https://github.com/Roestlab/massformer#readme | https://doi.org/10.1038/s42256-024-00816-8 |
| Metabonaut (`metabonaut`) | https://rformassspectrometry.github.io/Metabonaut/ | https://doi.org/10.1007/s11306-026-02538-x |
| MIST-CF (`mist-cf`) | https://github.com/samgoldman97/mist-cf#readme | https://doi.org/10.1021/acs.jcim.3c01082 |
| MS-RIDD (`ms-ridd`) | https://github.com/Metabolomics-CompMS/MS-RIDD#readme | https://doi.org/10.1038/s42004-022-00778-1 |
| MSEntropy (`msentropy`) | https://msentropy.readthedocs.io/ | https://doi.org/10.1038/s41592-021-01331-z; https://doi.org/10.1038/s41592-023-02012-9 |
| mzQuality (`mzquality`) | https://hankemeierlab.github.io/mzQuality/ | https://doi.org/10.1021/jasms.5c00073 |
| NeatMS (`neatms`) | https://neatms.readthedocs.io/en/latest/ | https://doi.org/10.1021/acs.analchem.1c02220 |
| NetID (`netid`) | https://github.com/LiChenPU/NetID#readme | https://doi.org/10.1038/s41592-021-01303-3 |
| SLAW (`slaw`) | https://github.com/zamboni-lab/SLAW#readme | https://doi.org/10.1021/acs.analchem.1c02687 |
| UmetaFlow (`umetaflow`) | https://github.com/biosustain/snakemake_UmetaFlow#readme | https://doi.org/10.1186/s13321-023-00724-w |
| InjectionDesign (`injectiondesign`) | https://github.com/CSi-Studio/InjectionDesign#readme | https://doi.org/10.1186/s12859-023-05598-1 |
| LipiDex 2 (`lipidex-2`) | https://github.com/coongroup/LipiDex-2/wiki | https://doi.org/10.1021/acs.analchem.4c00359 |
| Nextflow4MS-DIAL (`nextflow4ms-dial`) | https://github.com/Nextflow4Metabolomics/nextflow4ms-dial#readme | https://doi.org/10.1021/jasms.4c00364 |
| Python-Centric Pipeline for Metabolomics (`pcpfm`) | https://github.com/shuzhao-li-lab/PythonCentricPipelineForMetabolomics#readme | https://doi.org/10.1371/journal.pcbi.1011912 |
| AutoCCS (`autoccs`) | https://github.com/PNNL-Comp-Mass-Spec/AutoCCS#readme | https://doi.org/10.1093/bioinformatics/btab429 |
| G-Aligner (`g-aligner`) | https://github.com/CSi-Studio/G-Aligner#readme | https://doi.org/10.1186/s12859-023-05525-4 |
| metaboprep (`metaboprep`) | https://mrcieu.github.io/metaboprep/ | https://doi.org/10.1093/bioinformatics/btac059 |
| pyEVA (`pyeva`) | https://github.com/HuanLab/pyEVA#readme | https://doi.org/10.1021/acs.analchem.1c01309 |
| OpenTIMS (`opentims`) | https://michalsta.github.io/opentims/ | https://doi.org/10.1021/acs.jproteome.0c00962 |
| SpectriPy (`spectripy`) | https://rformassspectrometry.github.io/SpectriPy/ | https://doi.org/10.21105/joss.08070 |
| specXplore (`specxplore`) | https://github.com/kevinmildau/specXplore#readme | https://doi.org/10.1021/acs.analchem.3c04444 |
| TidyMS (`tidyms`) | https://tidyms.readthedocs.io/en/latest/ | https://doi.org/10.3390/metabo10100416 |
| TIMSCONVERT (`timsconvert`) | https://gtluu.github.io/timsconvert/ | https://doi.org/10.1093/bioinformatics/btac419 |

## Held candidates and boundaries

DNMS2Purifier needs inspection of its separate DOCX user manual and exact input/output requirements. RapidMass needs its operational manual and data interface checked beyond the brief repository introduction. ShinyMetID distributes code/library archives and a video guide; its real-data interface and provenance need inspection before a complete published record. These source candidates were not promoted. The SMART name collision and remaining handoff drafts remain separate review work.

The source ledger reconciles the 25 matching intake rows for this batch and the three tools published in PR #79. TidyMS is documented as a distinct base-resource addition; pyEVA is documented as the Python implementation of the original EVA method rather than inventing a new paper. No Strategies, Ask Navigator or Education content is changed.

## Validation

Schema: 221 tools, 40 Strategies and 83 education resources. All new records meet the live editorial coverage checklist. Form synchronization, submission/contributor regression tests, Strategy terminology and implementation tests, branding audit, catalogue JavaScript tests and strict production-path build passed. Local-link checks covered 10,668 links/fragments across 283 pages and 319 relationships. Five SEO tests and 282 canonical-page metadata/sitemap checks passed. Generated HTML was checked directly; an attempted local browser preview timed out, so no visual browser inspection is claimed.
