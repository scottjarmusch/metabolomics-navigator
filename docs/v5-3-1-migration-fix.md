# v5.3.1 migration compatibility fix

v5.3 intentionally retired the broad `sample_contexts` Strategy field and renamed the objective `host_microbiome` to `host_microbe_interaction`. The first v5.3 package migrated the curated Strategy records, but it did not account for community or test Strategies that had already been created in a live repository under v5.2.

v5.3.1 fixes that upgrade path without weakening the frozen v5.3 schema.

When Strategy records are loaded, legacy v5.2 fields are normalized in memory before validation and rendering:

- `sample_contexts: human` → `biological_contexts: human`
- `sample_contexts: microbial` → `biological_contexts: microbial`
- `sample_contexts: marine` → `biological_contexts: marine`
- `sample_contexts: environmental` → `biological_contexts: environmental`
- `sample_contexts: food` → `biological_contexts: food_fermentation`
- `sample_contexts: synthetic_standards` → `biological_contexts: synthetic_reference` and `sample_types: synthetic_standards`
- `sample_contexts: other` → `biological_contexts: broadly_applicable`
- `host_microbiome` → `host_microbe_interaction`

New submissions continue to use only the v5.3 model. This compatibility layer exists solely to prevent previously valid v5.2 records from breaking the site during an upgrade.
