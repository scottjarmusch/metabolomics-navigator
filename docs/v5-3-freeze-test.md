# v5.3 pre-population freeze test

## Clinical host–microbe edge case

A synthetic protocol representing paired sputum and plasma analysis in human *Pseudomonas aeruginosa* infection validated cleanly using:

- primary objective: `disease_state_comparison`
- secondary objectives: `host_microbe_interaction`, `biomarker_discovery`
- sample types: `sputum`, `plasma`
- biological contexts: `human`, `microbial`, `host_microbe`
- organisms: `Homo sapiens`, `Pseudomonas aeruginosa`

This demonstrates that infection studies no longer need to be misclassified as host–microbiome studies.

## Relationship graph

Safe inverse relationships are generated from one stored declaration. Tests confirmed, for example, that:

- `xcms → alternative → MZmine` renders `MZmine → alternative → xcms`
- `MassIVE → integrates with → GNPS` renders the reciprocal GNPS integration
- `MASST → part of → GNPS` renders `GNPS → contains → MASST`

Explicit declarations take precedence over inferred inverses, and duplicate display entries are suppressed.

## Scaling

A fresh 500-synthetic-tool test passed after the v5.3 changes:

- 512 total tool pages
- 2 protocol pages
- validation: ~2.7 seconds
- static build: ~2.9 seconds
- tools catalogue HTML: ~0.60 MB
- tool JSON export: ~0.65 MB
- complete generated site: ~5.86 MB

The current static architecture remains appropriate for the benchmark corpus and several hundred catalogue entries.
