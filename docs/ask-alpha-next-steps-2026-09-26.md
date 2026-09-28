# Ask Navigator alpha checkpoint — 26 September 2026

## This preview

Source branch: codex/ask-education-alpha. Combines the strategy-first controller from PR #47 with the published 34 Strategies, main catalogue (143 tools), and Education alpha (57 resources). Does not merge PR #47 or the large handoff into production. GNPS downstream draft #62 remains separate.

Adds expandable recorded Strategy requirements and links from published workflow tools to the Education tool filter. A tutorial link is a catalogue lookup, not evidence that the tutorial implements every step of a Strategy. Education resources keep their individual review and date labels.

## Priorities before production

1. Independent novice testing: record exact question, study stage, data available, expected next action, actual response and whether the researcher can proceed. Include cohorts, natural products, exposomics, lipids and spatial studies. The current four guided aims are intentionally limited.
2. Replace broad keyword overlaps with better curated aim/measurement constraints. Distinguish unknown from absent data. Do not equate a matched Strategy with compatibility or a complete experimental design.
3. Expand beginner paths only with reviewed scientific requirements. Sample handling, study controls, acquisition, QC and statistical design require explicit coverage; do not invent cohort sample sizes or universal recipes.
4. Audit step-level alternatives for compatible inputs/outputs and capabilities. Existing links use general catalogue function filters and do not establish interchangeability.
5. Review primary citations and requirements with domain specialists. Pending requests include MALDI-FISH, compound-resolved microfluidic bioactivity fractionation, microbiome drug-metabolism framework, and the questioned PMID 38224745. These are not silently added to the 34 published Strategies.
6. Verify Education content end to end, identify version-specific tutorials, and replace unhelpful or stale resources. Dates indicate publication, not scientific endorsement or interface currency.
7. Agree on workflow export behavior for this strategy-first interface. Prior preview exports should not be assumed to exist or be scientifically validated here.

## Reviewer prompts

- We have blood from 200 patients and controls. Where should we start?
- We forgot pooled QC samples. Can we correct instrument drift?
- I have a feature table but no MS/MS. Can I build molecular networks?
- Can I run statistics locally in R?
- How do I group related molecules in LC-MS/MS data?
- How do I identify unknown pollutants in plasma?
- Can metabolomics help discover antibiotics from bacteria?
- I want lipid double-bond positions.
- I have tissue MALDI images and histology.
- Can I estimate flux without an isotope-tracer experiment?

Passing deterministic regression checks is not scientific or usability sign-off. Reviewers should also try their own wording.

## Validation before alpha refresh

Strict build: 143 tools, 34 Strategies, 57 learning resources. 7,638 local links/fragments and 290 relationship links passed. Ask controller tests and all 36 generated query cases passed. Browser checks confirmed novice clarification, FBMN retrieval, expandable requirements, filtered Education handoff, date sorting and widths 320/375/768/1440 without horizontal overflow. Mobile screenshot inspected. An initial browser run failed a response assertion; the instrumented repeat produced the expected response and no JavaScript errors.

## 27 September: study-context starters

Six experiment contexts now open tailored clarification: cohort comparison, comparative metabolomics, natural products/drug discovery, exposomics, lipidomics and spatial metabolomics. These are prompts, not complete workflow templates. Each clears old results and leaves stage, measurements and analytical aim unanswered. Start over clears the selected context too. Dedicated regression tests exercise all six selections and prevent stale recommendations or assumed data. The four analytical aims remain limited pending scientific review.

## 27 September: actionable guidance

Beginner responses now expose appropriate catalogue/learning links: raw data to processing and QC; planning or uncertain measurements to Education; local R/Python statistics queries to the statistics catalogue. These remain exploration links rather than validated recommendations. New searches and reset clear stale actions. Regression tests cover each route and clearing behavior.

## 28 September: explicit QC and tracer evidence

Local alpha now asks whether repeated representative QC injections and injection order exist before offering pooled-QC drift correction, and whether tracer labeling measurements and times exist before offering isotope-flux methods. Unknown and absent answers give distinct guidance and no method cards. Questions appear only for the relevant aim and reset on aim/study changes. These checks are prerequisites, not proof of full compatibility. Unit tests cover all three answer states and reset. Free-text search remains an exploration route, not a validated compatibility engine.
