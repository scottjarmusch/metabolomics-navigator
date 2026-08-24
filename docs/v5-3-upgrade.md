# v5.3 information-model freeze

v5.3 is the final pre-population information-model refinement before building the benchmark corpus.

## Changes

- adds **Disease-state comparison** as a protocol objective
- replaces the narrower **Host–microbiome metabolomics** objective with **Host–microbe interaction**
- retires the legacy `sample_contexts` protocol field
- keeps sample matrix, biological context, and organism information in separate fields
- automatically renders safe inverse tool relationships
- rejects self-referential and duplicate tool relationships
- migrates the two seed Protocol records to the frozen context model

## Upgrade order

1. Upload the v5.3 GitHub helper inside `.github` first. This updates the protocol submission form.
2. Commit it to `main` and allow validation/deployment to finish.
3. Upload the v5.3 root update at repository root.
4. Commit it to `main`. Validation and deployment should run automatically.

The schema, vocabulary, parser, and generated pages are synchronized in this release.
