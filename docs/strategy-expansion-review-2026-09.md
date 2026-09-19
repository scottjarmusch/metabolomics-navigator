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
