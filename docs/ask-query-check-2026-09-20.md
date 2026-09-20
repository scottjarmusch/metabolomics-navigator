# Ask alpha query check - 2026-09-20

Ten regression questions using the generated 30-Strategy catalogue and shipped deterministic controller. These are curated checks, not an independent user study or a measure of scientific accuracy. No model inference or paid service is used.

## Filtering change

For multi-term queries with at least two terms recognized in eligible records, retain scores at or above 40% of the best lexical score. Single-recognized-term queries retain all positive matches, subject to the existing six-result display limit. This is a relevance heuristic, not a probability or suitability threshold. The leading result remains unchanged in these eight specific examples.

Before filtering: the pathway, ChemRICH and DIA queries each displayed six results, including weak matches. After filtering, each returns its specific methodological match. Spatial immunophenotyping retains SpaceM as a second match; it is related, not equivalent.

## Exact inputs and outputs

### I am new to metabolomics and want to compare treated and untreated cells

Please add your scientific aim or measurement type so we can identify a published Strategy.


### I have NMR spectra and need peak assignment

Navigator covers MS-based metabolomics; NMR-only workflows are outside scope.


### Find pathways when most of my significant features are unidentified

1 matching published Strategy.

1. Feature-level pathway inference before metabolite identification

### Discover shared substructures from recurring fragments and neutral losses

1 matching published Strategy.

1. Shared-substructure discovery with Mass2Motifs

### Test chemical class enrichment of identified metabolites with ChemRICH

1 matching published Strategy.

1. Chemical-similarity metabolite-set enrichment

### Estimate flux from isotope labeling time courses

1 matching published Strategy.

1. Kinetic flux profiling from isotope-labeling time courses

### Compare amines and phenols with isotope coded dansylation

1 matching published Strategy.

1. Isotope-coded dansylation for comparative metabolomics

### Correct signal drift with pooled QC LOESS

1 matching published Strategy.

1. QC-based robust LOESS signal-drift correction

### Control false discoveries in DIA data using an assay library

1 matching published Strategy.

1. Target-decoy-controlled DIA metabolomics

### Link immune cell phenotypes to spatial metabolite images

2 matching published Strategies.

1. Same-section MSI and imaging mass cytometry integration
2. Spatially registered single-cell metabolomics

## Remaining limitations

Keyword overlap can still mistake negation, ambiguous aims or unrecognized synonyms. A novice requesting a general study still receives clarification rather than a complete study-design conversation. The score cutoff may hide useful adjacent methods; reviewers should test paraphrases and multi-goal questions. Experimental compatibility still needs human review.

## Additional exploratory checks

All six built-in example prompts retained their intended leading family: bioactivity networking, FBMN, metabologenomics, reverse metabolomics, MSI-guided networking and isotope-labeling networking. Broad networking prompts still show several related methods.

`Compare QC drift correction and isotope flux estimation` returns only kinetic flux profiling because the existing flux guard restricts eligible objectives. This is a known mixed-intent limitation, not a successful multi-goal recommendation. `I need to identify unknown peaks in patient plasma` returns molecular-networking dereplication, Mass2Motifs, feature-level pathway inference and isotope-labeling networking; without acquisition details, this list is not an implementable recommendation. Future novice guidance should clarify acquisition and study aims before presenting such lists.
