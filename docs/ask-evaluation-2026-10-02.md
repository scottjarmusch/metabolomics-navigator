# Ask alpha evaluation — 2 October 2026

Twelve additional questions were run against the actual rendered Strategy/tool metadata and shipped deterministic controller. These are automated search-path checks, not independent novice usability testing.

Initial failures: named tools could retrieve unrelated Strategies through shared words; an unlabeled feature table could retrieve a flux Strategy. The alpha now recognizes catalogue tool names, limits named-tool Strategy matches to recorded workflow tools, and treats unlabeled/unlabelled measurements as a constraint. Ambiguous generic words such as spectra require explicit software context and canonical case before becoming tool matches.

| Input | Final response | Catalogue links |
|---|---|---|
| I have never used metabolomics. How should I plan a patient cohort study? | Please use the study guide to clarify your scientific aim and available measurements. | None |
| We have raw LC-MS files from treated and control cells. Where do I begin? | Please use the study guide to clarify your scientific aim and available measurements. | None |
| I have a feature table but no tandem spectra. Can I use molecular networking? | Your question includes an exclusion or missing input. This search cannot reliably apply those constraints; use the study guide to specify your available measurements before selecting a method. | None |
| I want to estimate metabolic flux but did not use labeled substrates. | Your question includes an exclusion or missing input. This search cannot reliably apply those constraints; use the study guide to specify your available measurements before selecting a method. | None |
| Use khipu to group adduct and isotope peaks in my LC-MS feature table. | Named tools found in the catalogue, but no matching curated Strategy records these tools in its workflow. Review the tool scope and requirements above; capabilities are not inferred from other Strategies. | khipu |
| Can SIMPEL alone infer fluxes from an ordinary unlabeled feature table? | Your question includes an exclusion or missing input. This search cannot reliably apply those constraints; use the study guide to specify your available measurements before selecting a method. | simpel |
| I have GC chemical ionization isotope labeling data for isoSCAN. | Named tools found in the catalogue, but no matching curated Strategy records these tools in its workflow. Review the tool scope and requirements above; capabilities are not inferred from other Strategies. | isoscan |
| I have carbon-13 fatty acid labeling profiles and want FAMetA. | Named tools found in the catalogue, but no matching curated Strategy records these tools in its workflow. Review the tool scope and requirements above; capabilities are not inferred from other Strategies. | fameta |
| Can 13C-SpaceM process my microscopy images without MALDI measurements? | Your question includes an exclusion or missing input. This search cannot reliably apply those constraints; use the study guide to specify your available measurements before selecting a method. | 13c-spacem |
| Use ChemWalker to prioritize structures from my molecular network. | Named tools found in the catalogue, but no matching curated Strategy records these tools in its workflow. Review the tool scope and requirements above; capabilities are not inferred from other Strategies. | chemwalker |
| I want to find relationships between metabolites and microbes with CorrOmics. | Named tools found in the catalogue, but no matching curated Strategy records these tools in its workflow. Review the tool scope and requirements above; capabilities are not inferred from other Strategies. | corromics |
| Can Everything Bagel replace statistical analysis of patient groups? | Named tools found in the catalogue, but no matching curated Strategy records these tools in its workflow. Review the tool scope and requirements above; capabilities are not inferred from other Strategies. | everything-bagel |

No Strategy was returned for these twelve cases after the fixes. This is appropriate for their missing-input, introductory, and tool-specific wording; it does not mean that no useful scientific method exists. Existing positive Strategy-retrieval regressions remain in the 51-case suite.

Still needed before production: independent novice testing; more helpful experiment-specific clarification; rigorous input/output compatibility for tool substitutions; reviewed coverage for gaps revealed by named-tool searches. Tool links do not answer whether one package can replace another. No LLM inference or external AI service is used.

Validation passed: schema (154 tools, 40 Strategies, 83 Education resources), strict alpha build, controller unit checks and 51 generated Strategy-search cases. Browser checks confirmed named-tool links, missing-input handling, Spectra disambiguation, preserved MS2LDA retrieval, cleared stale links, Everything Bagel tutorial filtering and 320–1440px layouts without JavaScript errors.
