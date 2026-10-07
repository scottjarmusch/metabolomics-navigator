# Ask Navigator proxy test plan — 7 October 2026

Fixed 48-query editorial test set, created before running the baseline. These are proxy questions representing research contexts, not interviews with actual users. No scientific claim is validated merely by a retrieval pass.

Coverage: 12 general comparisons, six planning questions, six missing-input/scope cases, 18 published-method searches and six software/local-analysis requests. Sample contexts include soil, sediment, river water, seawater, leaves, root exudates, human plasma and urine, cultures, biofilms, fermented food, feces, cell extracts, tissue and single-cell imaging.

A method passes if the expected curated Strategy is among the first three hits; first-place accuracy is also reported separately. Comparison/planning questions should receive meaningful next-step guidance rather than specialist method cards. Missing inputs must not be treated as available. Named-software checks only verify the catalogue link, not tool compatibility. Three equivalent FBMN queries vary soil/plasma/culture context to test sample-context stability.

Runner: `scripts/evaluate_ask_proxy.cjs`. Requires Playwright and a browser, an existing strict alpha build, and the `PLAYWRIGHT_MODULE` environment override if Playwright is not installed locally. Optional first argument selects a result file. Baseline and follow-up files preserve exact responses and returned ranks; do not overwrite the baseline to conceal failures.

## Declared questions and expectations

| ID | Context / sample | Experience | Query | Expected route / Strategy |
|---|---|---|---|---|
| Q01 | terrestrial / bulk soil | newcomer | find metabolite differences in bulk soil samples | comparison_guidance |
| Q02 | freshwater / river water | newcomer | Which metabolites differ between upstream and downstream river water samples? | comparison_guidance |
| Q03 | marine / seawater | newcomer | Compare metabolite levels between coastal and offshore seawater samples | comparison_guidance |
| Q04 | terrestrial / sediment | newcomer | Find differences in metabolite abundance between contaminated and clean sediments | comparison_guidance |
| Q05 | plant / leaf extracts | newcomer | Which metabolites distinguish drought-stressed leaves from watered controls? | comparison_guidance |
| Q06 | plant / root exudates | newcomer | Compare metabolite abundances in root exudates from two plant genotypes | comparison_guidance |
| Q07 | human / plasma | newcomer | Find metabolite differences between patient and control plasma samples | comparison_guidance |
| Q08 | human / urine | newcomer | I want to discover which urine metabolites change after treatment | comparison_guidance |
| Q09 | microbial / culture supernatants | newcomer | Find metabolites that change between bacterial culture conditions | comparison_guidance |
| Q10 | food / fermented food | newcomer | How do metabolite profiles differ between fermented and unfermented food samples? | comparison_guidance |
| Q11 | animal / feces | newcomer | Compare metabolite levels in fecal samples from two diet groups | comparison_guidance |
| Q12 | cell culture / bulk cell extracts | newcomer | What chemicals are more abundant in treated cells than untreated cells? | comparison_guidance |
| Q13 | human / plasma | newcomer | I am new to metabolomics. How should I plan a patient cohort study? | clarification |
| Q14 | marine / coral | newcomer | I have never used metabolomics to study coral bleaching. Where should I start? | clarification |
| Q15 | plant / root exudates | newcomer | Before we collect samples, how can metabolomics help study root exudates? | clarification |
| Q16 | microbial / biofilm | newcomer | This is my first metabolomics study of biofilms | clarification |
| Q17 | terrestrial / soil | newcomer | I am not sure which measurements I need for soil metabolomics | clarification |
| Q18 | animal / tissue | newcomer | I am a beginner studying liver metabolism. What should I measure? | clarification |
| Q19 | terrestrial / soil | mixed | I have a soil feature table but no MS/MS. Can I build molecular networks? | constraint |
| Q20 | human / plasma | mixed | Correct instrument drift without pooled QC samples | constraint |
| Q21 | plant / leaf extracts | mixed | Infer metabolic flux from unlabeled plant metabolite abundances | constraint |
| Q22 | spatial / tissue | mixed | Can I run SpaceM without microscopy images? | constraint |
| Q23 | human / plasma | mixed | I need NMR peak assignment, not mass spectrometry | scope |
| Q24 | microbial / culture | mixed | Use mmvec without paired microbiome samples | constraint |
| Q25 | terrestrial / bulk soil | experienced | Organize bulk soil LC-MS/MS features into molecular families with feature based molecular networking | gnps-feature-based-molecular-networking |
| Q26 | human / plasma | experienced | Organize plasma LC-MS/MS features into molecular families with feature based molecular networking | gnps-feature-based-molecular-networking |
| Q27 | microbial / culture extracts | experienced | Organize bacterial LC-MS/MS features into molecular families with feature based molecular networking | gnps-feature-based-molecular-networking |
| Q28 | microbial / culture extracts | experienced | Connect measured antimicrobial bioactivity to molecular networks from fractions | bioactivity-based-molecular-networking |
| Q29 | marine / sponge extracts | experienced | Find known natural products through molecular networking dereplication | molecular-networking-dereplication |
| Q30 | plant / leaf extracts | experienced | Use taxonomic information from the plant to prioritize metabolite annotations | taxonomically-informed-annotation |
| Q31 | human / plasma | experienced | Suspect screening of xenobiotics with a candidate chemical list for exposomics | exposomics-suspect-screening |
| Q32 | environmental / water extracts | experienced | Discover recurring fragments and neutral losses as shared substructures | mass2motif-substructure-discovery |
| Q33 | human / plasma | experienced | Use retention order to rank molecular structure candidates jointly | retention-order-joint-annotation |
| Q34 | human / plasma | experienced | Infer pathways from significant unidentified features using mummichog | feature-level-pathway-inference |
| Q35 | human / plasma | experienced | Chemical class enrichment for identified metabolites using ChemRICH | chemical-similarity-set-enrichment |
| Q36 | microbial / culture extracts | experienced | Estimate metabolic flux from isotope labeling time courses | kinetic-flux-profiling |
| Q37 | spatial / tissue images | experienced | Correlate metabolite images and microbial identities using MALDI FISH | maldi-fish |
| Q38 | cell culture / single cells | experienced | Spatially registered single cell metabolomics with SpaceM | spacem-single-cell-metabolomics |
| Q39 | spatial / tissue images | experienced | Integrate mass spectrometry imaging and imaging mass cytometry on the same tissue section | msi-imc-single-cell-immunometabolism |
| Q40 | lipidomics / plasma lipids | experienced | Localize lipid double bond positions using epoxidation diagnostic fragments | epoxidation-lipid-double-bond-localization |
| Q41 | acquisition / reference mixtures | experienced | Improve precursor coverage by iterative exclusion list MS/MS acquisition | iterative-exclusion-list-acquisition |
| Q42 | human / plasma cohort | experienced | Correct signal drift with repeated pooled QC injections and LOESS | qc-rlsc-signal-drift-correction |
| Q43 | terrestrial / soil | intermediate | Use dbnorm to adjust batch effects in my soil feature table | dbnorm |
| Q44 | human / plasma | intermediate | Use MatrixQCvis to inspect my processed plasma matrix | matrixqcvis |
| Q45 | plant / extracts | intermediate | Use ROASMI to combine retention scores and MS/MS | roasmi |
| Q46 | microbial / extracts | intermediate | Use MS2DECIDE for natural product prioritization | ms2decide |
| Q47 | spatial / tissue | intermediate | Use 13C-SpaceM for spatial isotope measurements | 13c-spacem |
| Q48 | human / plasma | intermediate | Can I perform metabolomics statistics locally in R? | statistics |

## Next validation layer

Keep these questions as fixed regression coverage. Add independently written holdout paraphrases before further matching changes, ask novice researchers to use their own words, and have domain specialists assess misleading extra hits and the suitability of evidence/input requirements. Include spelling variants, abbreviated measurements, mixed intentions and contradictory descriptions. Add feedback cases without changing their expectations to fit the implementation.
