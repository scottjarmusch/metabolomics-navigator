# Strategy candidate staging — September 2026

This is a **high-recall methodological candidate queue**, not a list of approved Navigator Strategies.

Editorial rule: **a new biological application does not create a new Strategy; a new analytical relationship between measurements, data types, tools, or evidence layers can.** Application papers should be attached to an existing Strategy as implementations/use cases.

Status meanings:
- **ADDED / EXISTING** — already represented in the current working branch/catalogue.
- **STRONG** — concept appears methodologically distinct; verify the defining primary paper before creating a card.
- **PRIMARY PAPER NEEDED** — plausible methodological concept identified from reviews/tool landscapes; do not create a Strategy until a paper introducing or materially formalizing it is found.
- **REVIEW** — may collapse into an existing Strategy after reading the primary literature.
- **IMPLEMENTATION/EXTENSION / IMPLEMENTATION / IMPLEMENTATION/TOOL LAYER** — more likely a use case, documented procedure, or extension than a new Strategy.

## Dereplication & natural-product discovery

| Candidate | Status | Evidence / next step |
|---|---|---|
| Molecular networking as a dereplication strategy | ADDED | 10.1021/np400413s |
| Reference-standard-seeded molecular networking | REVIEW | Potential implementation/variant of molecular-networking dereplication |
| Reference-organism spectral dereplication | REVIEW | Potential implementation/variant of molecular-networking dereplication |
| GC-MS deconvolution-assisted natural-product dereplication | PRIMARY PAPER NEEDED | Review-derived candidate |
| Ion-mobility-assisted natural-product dereplication | PRIMARY PAPER NEEDED | IM-MS/natural-products review literature |
| Taxonomy-guided natural-product dereplication | REVIEW | Existing taxonomically informed annotation covers this absent a distinct analytical relationship; do not create a renamed duplicate |
| BGC-informed dereplication | STRONG | Find defining paper distinct from metabologenomics |
| Comparative-strain metabolomics for novelty prioritization | STRONG | Comparative microbial metabolomics review: PMID 27604382 |
| Mutant-versus-wild-type comparative metabolomics | STRONG | Find defining workflow paper |
| OSMAC-guided comparative metabolomics | STRONG | Find defining workflow paper |
| Co-culture-induced metabolite discovery | STRONG | Find defining workflow paper |
| Bioactivity-correlated comparative metabolomics | STRONG | Distinct from network-dependent BMN if supported by defining paper |
| Chemometrics-guided bioactive natural-product prioritization | REVIEW | 10.1021/acs.jnatprod.4c00647 |
| MS2 plus NMR orthogonal dereplication | REVIEW | 10.1021/acs.jnatprod.4c00647 |
| Building-block-based molecular networking | STRONG | Molecules 2023 review; find original BBMN paper |
| Substructure-motif-guided molecular networking | STRONG | Molecules 2023 review; find original method paper |
| Analog-series expansion from known seed compounds | REVIEW | May collapse into molecular-networking dereplication |
| Mass-defect-filter-guided natural-product discovery | PRIMARY PAPER NEEDED | Find defining method paper |
| Homologous-series/formula-family dereplication | PRIMARY PAPER NEEDED | Find defining method paper |
| Colony MALDI-MS/MS dereplication before scale-up | EXISTING | Current IDBac colony MALDI-MS/MS Strategy |
| Taxonomy-plus-metabolite microbial library prioritization | EXISTING | Current IDBac microbial library Strategy |
| Metabologenomics | EXISTING | Current Strategy |
| Natural-product class prediction-guided prioritization | PRIMARY PAPER NEEDED | Find methodology introducing class priors for NP discovery |
| Rare-feature prioritization across extract libraries | PRIMARY PAPER NEEDED | Find defining workflow |
| Cross-species comparative metabolomics for chemodiversity | PRIMARY PAPER NEEDED | Find defining workflow |

## Acquisition, coverage & quality control

| Candidate | Status | Evidence / next step |
|---|---|---|
| Iterative optimized MS/MS acquisition | ADDED | 10.1093/bioinformatics/btab279 |
| Iterative exclusion-list DDA | STRONG | Find canonical exclusion-list metabolomics method paper |
| Differential-peak targeted DDA | STRONG | PMID 37594469 |
| DDA-assisted DIA metabolomics (DaDIA) | ADDED | 10.1021/acs.analchem.0c05022 |
| Pooled-QC-guided DDA library generation | STRONG | PMID 36475608 and related methods |
| Library-assisted DIA metabolomics with FDR control | ADDED | Alpha batch 2: 10.1038/s41467-022-29006-z; target-decoy-controlled DIA extraction, distinct from acquisition-only DaDIA |
| Open-source DIA/MSE annotation and networking | STRONG | PMID 38324622 |
| Narrow-window DIA / gas-phase-fractionated metabolomics | PRIMARY PAPER NEEDED | Find metabolomics-specific method paper |
| Multi-energy collision acquisition | PRIMARY PAPER NEEDED | Find defining workflow |
| Semi-targeted toxicant inclusion-list acquisition | STRONG | PMID 39354300 |
| Pooled-QC signal-drift correction | STRONG | Find primary method; pooled-QC review PMID 38055671 |
| QC-based feature filtering | STRONG | Find defining methods paper |
| Blank subtraction and contaminant filtering | PRIMARY PAPER NEEDED | Find defining workflow |
| Reference-material-anchored batch harmonization | PRIMARY PAPER NEEDED | Find defining workflow |
| Randomized-block acquisition for large cohorts | PRIMARY PAPER NEEDED | Find metabolomics methodology paper |
| Large-cohort discovery plus targeted re-extraction | STRONG | PMID 36475608 |
| Dual-polarity coordinated acquisition | PRIMARY PAPER NEEDED | Find defining workflow |
| Orthogonal RP/HILIC coverage expansion | STRONG | Find primary paper; exposomics review DOI 10.1093/exposome/osab003 |
| Complementary LC-MS plus GC-MS metabolomics | STRONG | Find defining strategy paper |
| Adaptive/intelligent precursor selection | PRIMARY PAPER NEEDED | Find metabolomics-specific real-time acquisition strategy |
| Targeted reacquisition of unidentified features | PRIMARY PAPER NEEDED | Find defining workflow |
| Longitudinal QC/reference injection design | PRIMARY PAPER NEEDED | Find methods paper |
| Cross-batch pooled reference normalization | PRIMARY PAPER NEEDED | Find methods paper |

## Annotation & identification

| Candidate | Status | Evidence / next step |
|---|---|---|
| CCS-assisted metabolite identification | STRONG | IM-MS review PMID 33522625; find defining workflow |
| Predicted-CCS candidate filtering | STRONG | Find AllCCS or equivalent defining paper |
| Retention-time-assisted annotation | STRONG | Find canonical workflow |
| Retention-order-constrained structure annotation | STRONG | LC-MS2Struct 2022 method |
| Formula-first computational annotation | STRONG | Find defining workflow |
| In-silico fragmentation candidate ranking | STRONG | Find canonical MetFrag/CFM-ID-style method paper |
| Machine-learning spectrum-prediction candidate ranking | STRONG | Find defining workflow |
| De novo structure generation from MS/MS | STRONG | Enveda review category; select canonical primary paper |
| Chemical-class prediction before structure annotation | STRONG | Find canonical class-prediction workflow |
| Spectral-embedding nearest-neighbor annotation | STRONG | Spec2Vec/MS2DeepScore/DreaMS family; select canonical method |
| Motif/substructure-first annotation | STRONG | MS2LDA family |
| Network-propagated annotation | STRONG | Find defining method |
| Ion-identity-assisted annotation | EXISTING | Current IIMN Strategy |
| Adduct/isotope grouping before annotation | STRONG | Find CAMERA/ion-identity style defining workflow |
| Multi-library consensus spectral annotation | PRIMARY PAPER NEEDED | Find defining workflow |
| Orthogonal LC-MS/MS plus MSI annotation | STRONG | MSI annotation review DOI 10.1002/mas.21794 |
| Spatial-correlation-assisted MSI annotation | STRONG | MSI annotation review; find primary method |
| Confidence-tiered metabolite identification | REVIEW | May be reporting standard rather than Strategy |
| Unknown-first prioritization after exhaustive annotation | PRIMARY PAPER NEEDED | Find dark-metabolome workflow |
| Formula + RT + CCS + MS/MS evidence fusion | PRIMARY PAPER NEEDED | Find explicit multimodal scoring method |
| Candidate ranking using biological/taxonomic priors | STRONG | Find primary method paper |
| Annotation rescue using analogue libraries | PRIMARY PAPER NEEDED | Find defining workflow |
| Spectral entropy-based annotation workflow | PRIMARY PAPER NEEDED | Find method paper if workflow-level novelty exists |
| Cross-platform spectral matching | PRIMARY PAPER NEEDED | Find method paper that establishes transfer strategy |

## Isotope tracing & flux

| Candidate | Status | Evidence / next step |
|---|---|---|
| Stable isotope-resolved metabolomics (SIRM) | STRONG | Identify defining methodology paper |
| Pulse-chase isotope metabolomics | STRONG | Find defining workflow |
| Isotopologue spectral analysis for flux inference | STRONG | Find canonical 13C-MFA/metabolomics paper |
| Stable-isotope-assisted metabolite credentialing | EXISTING | `credentialing-untargeted-features`, 10.1021/ac503092d; no additional card |
| Isotope-assisted elemental composition inference | PRIMARY PAPER NEEDED | Find primary method |
| Stable-isotope-labeling molecular networking | EXISTING | Current Strategy |
| Isotope plus ion-mobility multidimensional metabolomics | STRONG | Verify primary paper around PMID 35089687 |
| Tracer-guided discovery of unknown pathway products | PRIMARY PAPER NEEDED | Find defining method |
| Multiple-tracer comparative flux metabolomics | PRIMARY PAPER NEEDED | Find defining strategy |
| Isotope-coded derivatization for relative quantification | STRONG | Find canonical method |
| Natural-abundance isotope tracing | REVIEW | Assess scope and methodological distinctiveness |
| Position-specific isotope tracing by MS/MS | PRIMARY PAPER NEEDED | Find defining strategy |
| Dynamic isotope labeling for turnover estimation | PRIMARY PAPER NEEDED | Find defining method |

## Spatial & single-cell metabolomics

| Candidate | Status | Evidence / next step |
|---|---|---|
| Spatially registered single-cell metabolomics (SpaceM) | ADDED | 10.1038/s41592-021-01198-0 |
| High-throughput SpaceM | IMPLEMENTATION/EXTENSION | Attach as implementation unless methodological distinction is strong |
| MSI-guided molecular networking | EXISTING | Current Strategy |
| Three-dimensional molecular cartography | EXISTING | Current Strategy |
| Multimodal MSI plus imaging mass cytometry | ADDED | Alpha batch 2: 10.1038/s41592-024-02392-6; same-section antibody-defined phenotypes plus metabolic signals |
| MSI plus spatial transcriptomics integration | STRONG | Find earliest defining method; SpaMTP 2026 is a later framework |
| MSI plus histology image fusion | STRONG | Find defining image-fusion paper |
| On-tissue derivatization MSI | STRONG | npj Imaging 2024 review; identify canonical method |
| Ion-mobility-enhanced MSI | STRONG | npj Imaging 2024 review; identify primary metabolomics/lipidomics paper |
| Spatial segmentation-driven differential metabolomics | STRONG | Find primary method |
| Co-localization-guided spatial molecular families | PRIMARY PAPER NEEDED | Find defining workflow |
| Single-cell MALDI plus microscopy phenotyping | REVIEW | Distinguish from SpaceM |
| Spatial isotope tracing by MSI | STRONG | Find defining method |
| Spatial metabolomics plus proteomics integration | PRIMARY PAPER NEEDED | Find methodology paper |
| Spatial metabolomics plus glycomics integration | PRIMARY PAPER NEEDED | Find methodology paper |
| Spatially resolved pathway enrichment | PRIMARY PAPER NEEDED | Find defining analytical method |
| Cross-section 3D MSI reconstruction | PRIMARY PAPER NEEDED | Distinguish from current 3D cartography Strategy |

## Exposomics & repository-scale analysis

| Candidate | Status | Evidence / next step |
|---|---|---|
| Suspect screening of exposome-related xenobiotics | ADDED | 10.1016/j.chemosphere.2024.141221 |
| Non-target exposomics screening | STRONG | Exposomics methodological reviews; identify defining workflow |
| Spectral-database-based suspect screening | STRONG | 10.1016/j.trac.2024.117699 review family |
| Substructure-guided suspect screening | STRONG | 10.1016/j.trac.2024.117699 review family |
| Experimental-spectrum-guided suspect screening | STRONG | 10.1016/j.trac.2024.117699 review family |
| Derivatization-assisted suspect screening | STRONG | 10.1016/j.trac.2024.117699 review family |
| Dual LC-HRMS and GC-HRMS exposomics | STRONG | 10.1093/exposome/osab003 |
| Passive-sampling-coupled exposomics | STRONG | 10.1093/exposome/osab003 |
| Semi-targeted toxicant inclusion-list exposomics | STRONG | PMID 39354300 |
| Exposure-metabolome association workflow | PRIMARY PAPER NEEDED | Find defining methodology |
| Reverse metabolomics | EXISTING | Current Strategy |
| Domain-specific repository spectrum search | IMPLEMENTATION/TOOL LAYER | Usually tool/use-case rather than new Strategy |
| Metadata-stratified repository mining | STRONG | Find method that adds cohort/phenotype metadata as evidence |
| Public-data prevalence mapping for metabolites | PRIMARY PAPER NEEDED | Find defining method |
| Repository-based organ/tissue distribution mapping | IMPLEMENTATION | Likely implementation of reverse metabolomics |
| Cross-repository harmonized spectral searching | PRIMARY PAPER NEEDED | Find defining strategy |

## Structural lipidomics

| Candidate | Status | Evidence / next step |
|---|---|---|
| OzID structural lipidomics | EXISTING | Current Strategy |
| Data-independent OzID lipidomics | STRONG | Find defining paper |
| Paternò–Büchi double-bond localization | ADDED | Alpha batch 1: 10.1002/anie.201310699; 2016 extension retained as implementation |
| Epoxidation-assisted double-bond localization | STRONG | Find defining method |
| Electron-activated dissociation structural lipidomics | STRONG | Find metabolomics/lipidomics primary paper |
| Ion-mobility-resolved lipid isomer analysis | STRONG | IM-MS review PMID 33522625; find primary method |
| LC-IMS-PASEF four-dimensional lipidomics | STRONG | Verify Lipid4DAnalyzer-associated primary paper |
| Class-specific lipid derivatization | PRIMARY PAPER NEEDED | Find defining strategy |
| Oxidized-lipid discovery / epilipidomics | STRONG | Find defining workflow |
| Shotgun plus LC orthogonal lipidomics | PRIMARY PAPER NEEDED | Find strategy paper |
| Retention-index-assisted lipid annotation | PRIMARY PAPER NEEDED | Find defining method |
| Ozone/PB orthogonal double-bond confirmation | PRIMARY PAPER NEEDED | Find paper integrating complementary chemistries |
| Sn-position-resolved lipidomics | STRONG | Find defining fragmentation/derivatization strategy |
| Stereochemistry-aware lipidomics | PRIMARY PAPER NEEDED | Find methodological paper |

## Multiomics, systems & biological context

| Candidate | Status | Evidence / next step |
|---|---|---|
| Genome-guided targeted metabolomics | STRONG | Find defining NP/metabolomics workflow |
| Metabolome-guided genome mining | STRONG | Find defining workflow |
| Metabolomics plus transcriptomics pathway integration | STRONG | Find method paper introducing integration logic |
| Metabolomics plus proteomics pathway integration | STRONG | Find defining workflow |
| Metabolomics plus microbiome association networks | STRONG | Find methodology paper, not application-only |
| Host-microbe metabolite source attribution | STRONG | Find defining strategy |
| Correlation-based metabolic network reconstruction | STRONG | Find canonical metabolomics network method |
| Biochemical-network-guided feature interpretation | STRONG | Find defining method |
| Feature-level pathway inference without full identification | ADDED | Alpha batch 1: 10.1371/journal.pcbi.1003123; `feature-level-pathway-inference` |
| Chemical-class enrichment analysis | STRONG | Find defining method |
| Molecular-family enrichment across phenotypes | PRIMARY PAPER NEEDED | Find defining workflow |
| Longitudinal metabolomics trajectory analysis | PRIMARY PAPER NEEDED | Find methodology paper |
| Time-resolved biotransformation tracking | STRONG | Find defining workflow |
| Dose-response metabolomics for mode-of-action inference | PRIMARY PAPER NEEDED | Find methodological paper |
| Perturbation-resolved metabolomics using genetic knockouts | STRONG | Find defining strategy |
| Perturbation-resolved metabolomics using inhibitors | PRIMARY PAPER NEEDED | Find defining method |
| Cross-omics latent-factor integration with metabolomics | PRIMARY PAPER NEEDED | Find method with transferable analytical architecture |
| Causal mediation of exposure–metabolite–phenotype relationships | PRIMARY PAPER NEEDED | Assess scope as metabolomics Strategy |
| Reaction-network-guided unknown annotation | STRONG | Find KGMN/related defining method |

## Chemical reactivity & derivatization

| Candidate | Status | Evidence / next step |
|---|---|---|
| Class-selective derivatization-enhanced untargeted metabolomics | STRONG | Find canonical workflow |
| Isotope-coded derivatization metabolomics | REVIEW | Consolidate with isotope-coded derivatization for relative quantification in the isotope section; defining paper still required |
| Post-column reaction metabolomics | STRONG | Find metabolomics-specific primary paper |
| Reactive-metabolite trapping metabolomics | STRONG | Find defining strategy |
| Carbonyl-selective metabolomics | STRONG | Find canonical method |
| Amine-selective metabolomics | STRONG | Find canonical method |
| Carboxyl-selective metabolomics | STRONG | Find canonical method |
| Thiol-selective metabolomics | STRONG | Find canonical method |
| Redox-reactivity-resolved metabolomics | PRIMARY PAPER NEEDED | Find distinct methodological paper |
| Enzyme-activity-probe metabolomics | PRIMARY PAPER NEEDED | Find methodology linking probe response to metabolite/enzyme activity |

## Queue size

This staging document contains **161 methodological concepts** across 9 families. It intentionally exceeds the target needed to reach 100 published Strategies because primary-paper review will merge, reject, or demote a substantial fraction to implementations.

## Source anchors used for this first staging pass

- Yang et al. 2013, *Molecular Networking as a Dereplication Strategy*, DOI 10.1021/np400413s.
- Guo et al. 2021, DaDIA, DOI 10.1021/acs.analchem.0c05022.
- MS2Planner iterative optimized acquisition, DOI 10.1093/bioinformatics/btab279.
- Rappez et al. 2021, SpaceM, DOI 10.1038/s41592-021-01198-0.
- Suspect-screening workflow, *Chemosphere* 2024, DOI 10.1016/j.chemosphere.2024.141221.
- Suspect-screening strategy review, DOI 10.1016/j.trac.2024.117699.
- Analytical strategies for chemical exposomics, DOI 10.1093/exposome/osab003.
- MS/MS molecular-networking dereplication review, DOI 10.3390/molecules28010157.
- Comparative microbial metabolomics review, PMID 27604382.
- MSI annotation/identification strategies review, DOI 10.1002/mas.21794.
- IM-MS metabolomics/lipidomics review, PMID 33522625.
- Large-cohort untargeted metabolomics workflow, PMID 36475608.
- Pooled-QC scoping review, PMID 38055671.
- DIA-IntOpenStream, PMID 38324622.

Review articles are discovery sources only. Navigator Strategy pages must cite the defining primary methodological paper, not a review, unless the review itself introduces the transferable analytical strategy.
