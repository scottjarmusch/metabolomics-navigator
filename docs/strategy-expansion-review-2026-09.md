# Strategy expansion review queue — September 2026

This note reviews the current Strategy collection as the evidence layer for Ask Navigator and identifies candidate additions for editorial review. It is intentionally a review queue, not an automatic population list.

## Current collection

The current repository contains 16 published Strategies:

- Bioactivity-Based Molecular Networking
- Chemoselective Reactivity-Resolved Metabolomics
- Credentialing Untargeted Features
- Feature-Based Molecular Networking (FBMN)
- Ion Identity Molecular Networking
- IDBac colony MALDI-MS/MS dereplication
- IDBac microbial library dereplication
- Metabologenomics
- MS2DECIDE
- MSI-guided molecular networking
- Native-MS metal-binding metabolomics
- OzID structural lipidomics
- Reverse metabolomics
- Stable-isotope-labeling molecular networking
- Taxonomically informed annotation
- Three-dimensional molecular cartography

(Directory contents should be treated as the source of truth if this list and the repository diverge.)

## What Ask Navigator needs from Strategies

For Ask Navigator, a useful Strategy should provide:

1. a scientific question/objective;
2. a transferable sequence of experimental/computational steps;
3. an originating publication;
4. tools/resources used in the original implementation;
5. scope/requirements/considerations;
6. later published implementations or adaptations where available.

The new optional `implementations` field is specifically intended for point 6.

## Strong candidate: SpaceM single-cell metabolomics

**Candidate name:** Spatially registered single-cell metabolomics (SpaceM)

**Primary paper:** Rappez L, Stadler M, Triana S, et al. *SpaceM reveals metabolic states of single cells*. Nature Methods 18, 799–805 (2021). DOI: 10.1038/s41592-021-01198-0.

**Why it may qualify as a Strategy:** The method integrates light microscopy, cell segmentation, spatial registration and MALDI imaging mass spectrometry to assign metabolic profiles to individual cells. The transferable idea is broader than a software package alone: spatially register imaging-MS ablation with segmented cells to construct a per-cell spatio-molecular matrix.

**Evidence of continuation:** HT SpaceM was subsequently reported as a high-throughput framework for small-molecule single-cell metabolomics in 2025 (DOI: 10.1016/j.cell.2025.08.015).

**Navigator gaps/blockers:** add `single_cell_metabolomics` to tool analysis types; ensure SpaceM/HT SpaceM tool representation is present before publishing the Strategy.

**Editorial question:** Is SpaceM best represented as both a Tool and an Analytical Strategy? The strategy should describe the transferable multimodal workflow; the Tool card should describe the implementation.

## Strong candidate: exposomics suspect screening

**Candidate name:** Suspect and non-target screening of exposome-related xenobiotics

**Example implementation:** *Development and evaluation of a comprehensive workflow for suspect screening of exposome-related xenobiotics and phase II metabolites in diverse human biofluids*. Chemosphere 351, 141221 (2024). DOI: 10.1016/j.chemosphere.2024.141221.

**Why it may qualify:** It defines a transferable UHPLC-HRMS/MS workflow for suspect screening across multiple human biofluids, including peak quality assessment, endogenous-interference handling, suspect lists, and explicit false-positive/false-negative evaluation.

**Related methodological context:** Suspect screening analysis using tandem-MS evidence is a recognized exposomics methodology, including spectral database-, substructure-, experimental-spectrum-, and derivatization-guided variants.

**Editorial question:** Define the Strategy broadly enough to be transferable without turning it into a generic "use suspect lists" card.

## Candidate requiring scoping: stable isotope-resolved metabolomics (SIRM)

**Candidate name:** Stable isotope-resolved metabolomics for pathway/flux tracing

**Evidence base:** MS-based SIRM is an established workflow family in which stable isotope-enriched precursors are followed through metabolites to infer pathway activity and flux. A 2019 Scientific Reports paper, *Integration of flux measurements and pharmacological controls to optimize stable isotope-resolved metabolomics workflows and interpretation*, explicitly describes stages and controls for a SIRM workflow.

**Why it may qualify:** Experimental design, tracer choice, labeling regime, extraction/acquisition, isotopologue correction and interpretation together form a transferable analytical strategy.

**Potential overlap:** Navigator already has *Stable-isotope-labeling molecular networking*, which is narrower and uses isotope labeling specifically with molecular networking. A SIRM Strategy would instead focus on metabolic tracing/flux.

**Editorial question:** Choose an originating/defining paper rather than using a review as the Strategy source.

## Candidate: multimodal MSI + immunophenotyping for single-cell metabolic profiling

**Example paper:** *Integration of mass cytometry and mass spectrometry imaging for spatially resolved single-cell metabolic profiling*. Nature Methods (2024), DOI: 10.1038/s41592-024-02392-6.

**Why it may qualify:** The study integrates MALDI-MSI and imaging mass cytometry on the same tissue section, co-registers both modalities, segments/phenotypes cells, and assigns MSI-derived metabolite abundances to individual cells.

**Editorial question:** This may deserve its own multimodal Strategy rather than being folded into SpaceM because the cellular phenotype layer comes from imaging mass cytometry rather than conventional microscopy.

## Candidate that may be better as an implementation, not a new Strategy

**Statistical analysis of FBMN outputs.** The Nature Protocols article *Statistical analysis of feature-based molecular networking results from non-targeted metabolomics data* (published online 2024; journal volume 2025) describes a substantial downstream workflow. It should first be evaluated as a documented extension implementation attached to the existing FBMN Strategy. Only create a separate Strategy if the methodological contribution remains independently transferable beyond "downstream analysis of FBMN."

## Population priority

Recommended next review order:

1. SpaceM / single-cell metabolomics
2. exposomics suspect screening
3. SIRM / metabolic tracing and flux
4. multimodal MSI + immunophenotyping
5. additional implementations for existing Strategies before inventing new Strategy categories

The objective is not maximum Strategy count. The best Ask Navigator coverage comes from a smaller set of clearly transferable Strategies with multiple well-curated implementations.


## Alpha batch 1 — 19 September 2026

The working collection now contains 23 Strategies; the historical list above describes the earlier snapshot.

| Candidate | Decision | Defining evidence / distinction |
|---|---|---|
| Feature-level pathway inference | Add | Li et al., 2013, DOI 10.1371/journal.pcbi.1003123. Joint network enrichment and ambiguous feature mapping is the transferable relationship; the immune-cell demonstration is not a second Strategy. |
| Paterno-Buchi lipid double-bond localization | Add | Ma and Xia, 2014, DOI 10.1002/anie.201310699. Photochemical derivatization followed by diagnostic fragmentation differs from OzID chemistry. |
| Shotgun PB identification and quantitation | Implementation/extension | Ma et al., 2016, DOI 10.1073/pnas.1523356113. Attached to the PB Strategy; tissue comparisons do not create cards. |
| Stable-isotope-assisted credentialing | Already represented | Existing `credentialing-untargeted-features`, DOI 10.1021/ac503092d. |
| Taxonomy-guided dereplication | Consolidate pending distinct evidence | Existing taxonomically informed annotation provides the candidate-ranking relationship. |
| Isotope-coded derivatization (two queue rows) | Consolidate review | One candidate family; primary-paper review remains outstanding. |

Sources inspected: [Li et al. primary article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003123), [Ma and Xia primary article](https://onlinelibrary.wiley.com/doi/10.1002/anie.201310699), [2016 extension](https://pmc.ncbi.nlm.nih.gov/articles/PMC4791002/).

No new tool entries, citation/popularity ranking, model inference, or production deployment. PB lists no catalogue tool because none was established as part of the original method; an unrelated lipid package must not be substituted. The mummichog Tool is the original computational implementation, not a competing Strategy card.

Remaining review: acquisition/QC and isotope/flux defining papers, multimodal spatial methods, then exposomics and chemical reactivity. The other STRONG candidates are still unreviewed; this batch is not approval of the queue. Existing alpha cards and their originating-publication choices still require a complete scientific audit before merge.


## Alpha batch 2 — 19 September 2026

25 Strategies in the working collection. Two reviewed additions:

- **Target-decoy-controlled DIA metabolomics:** [2022 defining paper](https://doi.org/10.1038/s41467-022-29006-z). Distinct from DaDIA because the added analytical relationship is assay/decoy evidence to statistically controlled chromatographic extraction. Existing OpenMS and SIRIUS records resolve. Biological comparisons in the paper do not become separate cards.
- **Same-section MSI and imaging mass cytometry integration:** [2024 defining paper](https://doi.org/10.1038/s41592-024-02392-6). Antibody-defined cell identity is integrated with metabolite images; this is not a renamed SpaceM card. Published integration scripts remain an external resource, with no invented catalogue slug. Mixed-pixel limitations are explicit. The colorectal-cancer demonstration does not define a cancer-specific Strategy.

Both titles and publication years were checked against publisher-deposited Crossref metadata. Software execution is not claimed. Earlier multimodal imaging methods exist; the new card is specifically scoped to the same-section MSI/IMC relationship, not a claim to the invention of all multimodal imaging.


### Ask improvements accompanying batch 2

Workflow steps now link to alternative searches by recorded tool function, without presenting them as validated substitutions. Matching uses whole terms weighted by their frequency across Strategy metadata and boosts curated keywords. No citation counts or tool popularity are used. NMR-only requests, missing flux-method coverage and the tested broad newcomer prompt no longer return misleading substitutes. See `ask-query-check-2026-09-19.md` for ten actual before/after query outputs and remaining retrieval limitations.


### Next isotope/flux review anchor

Kinetic flux profiling has a verified originating paper: Yuan et al., *Kinetic flux profiling of nitrogen assimilation in Escherichia coli*, Nature Chemical Biology 2, 529–530 (2006), DOI [10.1038/nchembio816](https://doi.org/10.1038/nchembio816). Its abstract explicitly introduces the method; the organism does not define a separate Strategy. The publisher provides supplementary methods. An expanded 2008 procedure, *Kinetic flux profiling for quantitation of cellular metabolic fluxes* (PMC2710581), should be inspected alongside those methods to establish assumptions, pool-size requirements and original implementation resources. No card was added from the abstract alone, and the retrieval coverage gap remains explicit.


## Alpha batch 3 — isotope kinetics and chemical isotope tags

The working collection now contains 27 Strategies. The earlier flux review anchor is superseded by this scoped review:

- KFP retains the 2006 originating publication. The 2008 expanded procedure is an implementation. Timed incorporation, pool measurement and model assumptions are explicit. Publisher abstracts, method figures and indexed primary-method text support this synopsis; full publisher methods access was unavailable during this pass. No instrument settings or unverified software dependencies are invented. This does not establish general coverage of 13C-MFA or every tracer design.
- Differential isotope dansylation retains the 2009 introducing method. The 2011 CSF study is an application, not a new Strategy. This card covers amine/phenol chemistry and deliberately does not imply biological flux measurement or universal metabolome coverage.

DOI/title/year checked against primary publication records and Crossref for all four publications. Crossref XML superscript/whitespace artifacts were normalized for readable isotope notation. The 25-Strategy query report remains a historical baseline: the flux prompt can now match KFP because its curated objective is flux_analysis; it must still require inspection of model and experimental fit.


### QC-RLSC addition completing batch 3

28 Strategies in this batch. The QC-RLSC card is anchored to Dunn et al. (2011), DOI 10.1038/nprot.2011.335, whose primary methods describe QC-based LOESS fitting, cross-validation and interpolation across injection order. This is a correction strategy, not a disease-specific application. XCMS is linked only for the documented LC-MS preprocessing step. Added analytical_quality_control consistently to the controlled vocabulary, schema and submission form so this purpose is not mislabeled as phenotype association.

Generated alpha query smoke check (28 Strategies): isotope-labeling time-course flux returned KFP alone; amine/phenol isotope-coded dansylation ranked the dansylation Strategy first; pooled-QC LOESS drift correction ranked QC-RLSC first. The latter two also returned weaker keyword matches, so relevance-tail filtering remains an alpha refinement rather than a completed capability.

## Batch 5: substructure discovery and chemical-set interpretation (2026-09-20)

- **Mass2Motifs / MS2LDA**: the 2016 primary paper (https://pmc.ncbi.nlm.nih.gov/articles/PMC5137707/) introduces shared fragment/loss topic inference. This is distinct from whole-spectrum molecular-network edges. The original XCMS, MzMatch, RMassBank and MS2LDA roles are recorded without substituting modern tools. The 2017 MS2LDA+ paper (https://doi.org/10.1021/acs.analchem.7b01391) stays as an extension, not an extra card.
- **ChemRICH**: the 2017 primary method (https://doi.org/10.1038/s41598-017-15231-w) links chemical structures/ontology to metabolite-set statistics. Unlike mummichog it requires identified structures and does not map ambiguous masses to pathways. ChemRICH is an external published resource because no corresponding Tool record exists; no placeholder Tool was invented.
- DOI/title/year checked against Crossref for all three papers. MS2LDA primary full text and indexed extension methods were inspected. ChemRICH full text was read through Europe PMC XML after publisher/PMC HTML access failed. Neither package was executed.
- This brings the alpha to 30 Strategies. Schema, strict build, link and SEO checks passed for these entries. The multisample extension adds no card to the count. Remaining STRONG candidates are unreviewed, not approved by association.

## Retention-order annotation review (2026-09-20)

The candidate initially pointed to LC-MS2Struct (2022). Primary-paper review instead anchors the shared analytical relationship to Bach et al. 2018, DOI 10.1093/bioinformatics/bty590 (https://academic.oup.com/bioinformatics/article/34/17/i875/5093227). The 2022 structured model, DOI 10.1038/s42256-022-00577-2, is retained as an extension. DOI/title/year verified against Crossref. This avoids treating a later software model as the origin of the broader Strategy. The intervening probabilistic framework (10.1093/bioinformatics/btaa998, online 2020 / issue 2021) remains for fuller implementation review; no unverified dependency from it was added. Original code availability is reported from the paper, not execution-tested. Alpha now contains 31 Strategies.

## Acquisition review and correction (2026-09-20)

- MS2Planner (10.1093/bioinformatics/btab279): Crossref and PubMed identify Zuo and Cao as the first authors, contradicting the imported citation. Primary full text (Europe PMC XML, PMC8336448) starts IODA with MS1 full-scan and computes successive paths by excluding already scheduled features. Corrected the earlier measured-coverage feedback description, added targeted-MS2 modes and the published IODA_MS export scripts. No instrument performance claim or execution validation added.
- Iterative measured-run exclusion: Koelmel et al. 2017, PMID 28265968 / PMC5408749, is a relevant lipidomics methodology anchor. Full-text retrieval through Europe PMC failed; keep in review rather than fold it into optimized scheduling without checking details.
- Differential/preidentified-ion acquisition: Zhang et al. 2023, DOI 10.1021/acs.analchem.3c02888. DOI/title/year/authors and primary abstract verified. The proposed distinct relationship is study-wide full-scan statistics/preidentification feeding targeted DDA of QC samples. The clinical demonstration is not a separate Strategy. Publisher full text was unavailable; detailed methods/resources remain to be reviewed before creating a complete entry.
- No new Strategy cards in this batch: the alpha remains at 31.


## Measured-run exclusion review (2026-09-21)

Added one Strategy, bringing the alpha to 32: iterative exclusion-list MS/MS acquisition. Its 2017 reference method (10.1007/s13361-017-1608-0) formalizes automated mass/retention-time grouping and background handling for metabolomics. It does not originate all iterative exclusion: the introduction acknowledges earlier proteomics work, including Bendall et al. (PMID 18936058). No sample-specific cards were created.

The [indexed primary methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC5408749/), [author documentation](https://secim.ufl.edu/secim-tools/ie-omics/) and [code repository](https://github.com/GarrettLab-UF/IE-Omics) establish the conversion and acquisition loop. Instrument compatibility and repeat-injection costs remain explicit. This differs from MS2Planner's survey-derived computational paths. Existing msconvert and MZmine slugs resolve; other resources remain external rather than inventing Tool records. DOI/title/year checked against Crossref on 2026-09-21. The 31-record DOI audit remains a historical snapshot; this entry was checked separately.

A generated-page regression distinguishes the exclusion-list query from the existing topological-scheduling query. Neither instrument execution nor scientific benchmarking is claimed. dpDDA remains in review pending fuller methods/resources checks; compare earlier targeted/untargeted DDA methods before calling it a new relationship. All changes remain in draft PR #47, with no merge or deployment.

### Next acquisition comparison

Before adding dpDDA, compare [2020 targeted versus untargeted DDA](https://pmc.ncbi.nlm.nih.gov/articles/PMC7241085/), DOI 10.3390/metabo10040126. It already tests inclusion lists from cleaned feature tables and preannotated features in QC runs. The unresolved editorial question is whether 2023 differential-feature prioritization adds a distinct relationship or belongs as an adaptation within a broader feature-prioritized acquisition Strategy. The 2023 publisher supporting-information listing identifies Progenesis QI, statTarget and MetaboAnalyst 5.0; these are review leads, not yet verified workflow bindings. Do not create a separate disease-specific card.

Validation for this batch: schema and form synchronization; strict build; editorial, submission, contributor, terminology, implementation and brand checks; catalogue and Ask controller tests; 26 generated Ask queries across 32 Strategies; 6,648 local links across 185 pages; 290 relationship links; SEO tests and 184 canonical-page checks. All passed. Three pre-existing accepted Tool stubs still await editorial enrichment.


## Reference-pool extraction and DIA networking implementation (2026-09-21)

- Added **reference-pool discovery with cohort-wide signal extraction**, anchored to Stancliffe et al. 2022 (10.1021/acs.analchem.2c01270). Primary methods and author notebooks distinguish pooled feature discovery from subsequent Skyline extraction. Pool dilution, integration curation and batch correction are explicit limitations. Two candidate rows pointing to this paper are consolidated; library generation is a component, not a second Strategy. No longevity-specific card and no claim that unknown features are identified.
- Added DIA-IntOpenStream (10.1093/bib/bbae013, 2024) as an **adaptation under FBMN**. The analytical relationship remains feature-linked spectral networking. MS-DIAL provides fragment assignment; MZmine 3's published role is MS1 processing, not DIA deconvolution. Historical GNPS, Waters2mzML and KNIME resources are retained. Acquisition metadata now includes DIA with the implementation-specific requirement for precursor-fragment assignment. No duplicate networking card.
- Both publications' DOI/title/year verified against Crossref. Primary full text was read through PMC HTML / Europe PMC XML; software was not executed. No raw-data availability claim was inferred from a paper's future release promise.
- dpDDA stays in review. The full 2020 comparison (10.3390/metabo10040126) already uses blank-filtered and preannotated feature inclusion lists. It cites Mullard et al. (10.1007/s11306-014-0763-6) and time-staggered lists (10.1016/j.jpba.2018.05.020); these origin questions must be resolved before assigning a new Strategy or adaptation.

Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC11018270/ ; https://github.com/pattilab/metabolomics_workflow ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10849173/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7241085/ . Alpha contains 33 Strategies.

Batch validation passed: schema/forms, strict build, editorial/submission/contributor checks, terminology/implementation/brand checks, catalogue/controller tests, 28 generated Ask queries, 6,695 local links across 186 pages, 290 relationship links and SEO checks.


## Predictive spatial image fusion (2026-09-23)

Added one Strategy (34 total): microscopy-MSI predictive image fusion, anchored to Van de Plas et al. 2015, DOI 10.1038/nmeth.3296. Crossref title/year and primary full text (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4382398/fullTextXML) establish ion-specific PLS modeling, reconstruction scores, residual maps and bootstrap uncertainty. Predicted finer pixels are not new MS measurements; unsupported ions must not be extrapolated. This relationship differs from SpaceM cell assignment and existing phenotype integration.

The published prototype is linked externally at https://fusion.vueinnovations.com/ rather than inventing a Tool slug or claiming open-source code. No software execution is claimed. The 2024 pharmaceutical fusion paper remains an implementation-review lead, not a separate Strategy; its final methods must be reviewed before adding an implementation. No alpha deployment.

Validation passed: schema and form synchronization, strict build, editorial/submission/contributor checks, terminology/implementation/brand checks, catalogue/controller tests, 29 generated Ask questions, 6,724 local links across 187 pages, 290 relationships and 186 canonical-page SEO checks. An initial link check overlapped the build and was discarded; the completed-build checks passed.
