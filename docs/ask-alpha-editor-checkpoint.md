# Ask Navigator alpha: editor review checkpoint

Review branch: `ask-navigator-strategy-alpha`, draft PR #47. Do not merge or deploy this checkpoint without the maintainer's decision.

## What to review

The alpha retrieves published Strategies from curated metadata, then exposes their actual workflow resources and step-specific catalogue alternatives. It does not generate a new workflow or infer experimental compatibility. The beginner entry offers preparation guidance before downstream search.

## Short reviewer exercise

| Input/action | Expected behavior |
|---|---|
| New to metabolomics, comparing treated and untreated cells | Opens study-first guidance; does not invent a complete workflow. |
| Planning + unknown measurements + unsure aim | Preparation guidance and guide/catalogue links. |
| Processed data + feature table + related molecules | Explains that spectral families require MS/MS. |
| Correct signal drift then explore pathways | Offers QC and pathway choices only. |
| Molecular networking and pathway enrichment | Offers molecular-family and pathway choices only. |
| Estimate flux through metabolic pathways | Returns kinetic flux profiling, without treating the wording as two aims. |
| Choose analytical QC from a mixed question | Returns QC-RLSC and clears the mixed-question panel. |
| Pathway analysis, not flux | Requests clarification; does not treat flux as a positive request. |
| Correct drift without pooled QCs | Explains that constraints need clarification rather than recommending QC-RLSC. |
| First metabolomics study / Where do I begin? | Opens beginner guidance. |
| Ask for NMR-only workflows | Explains the MS-only scope. |

Try your own paraphrases after these scripted cases. Record the exact input, available data, expected next step and actual response. Distinguish a missing Strategy from a poor match or a confusing interface.

## Scientific checks

- Does each Strategy represent a transferable analytical method rather than a tool listing or biological application?
- Are the originating paper, workflow resources and assumptions accurate?
- Are later applications/extensions clearly separate from the originating method?
- Could a novice mistake related results for an executable, complete study plan?

## Known limitations and next decisions

The catalogue currently contains 31 Strategies; the strong-candidate queue is not fully reviewed. Lexical relevance and the relative score cutoff are heuristics, not confidence estimates. Mixed-aim detection covers four explicit aim families, not arbitrary language; exclusion requests now defer to clarification rather than being interpreted; more varied novice phrasing remains an important test area. The beginner route covers only selected aims and sends uncertain measurements to clarification. Study design, statistics, sample-size decisions and acquisition compatibility are not automatically resolved.

Before public rollout: review varied novice phrasing and multi-aim/negated requests, resolve misleading results, and check a representative set of originating papers. Passing the automated regression suite alone is not scientific or usability sign-off.
