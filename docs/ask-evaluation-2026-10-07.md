# Ask Navigator evaluation — 7 October 2026

Source branch: `codex/ask-education-alpha`, synced with production release #75. Counts: 164 tools, 40 Strategies and 83 Education resources. This is a deterministic catalogue search and study guide; no external AI service is used.

## Changes

Named-tool eligibility includes tools explicitly recorded in later published implementations. The cards label those implementation tools separately from the originating workflow. Beginner/raw-data and QC questions now expose appropriate next-step links. No-match searches offer catalogue and learning routes. New searches clear stale guided messages. Generic words such as method/workflow/approach cannot create matches by themselves.

## Actual browser journeys

These are automated interactions with the generated interface, not independent novice usability testing. Guided journeys show the selections used; free-text journeys show the exact input. Outputs are recorded without treating a matched Strategy as confirmed compatibility.

| Researcher / input | Final guidance or response | Strategies | Next-step links |
|---|---|---|---|
| New cohort researcher — Patient cohort; planning / unsure measurements / unsure aim | Start with the guide and your MS facility: define the comparison, sample handling, controls and suitable measurements before choosing an analysis workflow. | None | Find tutorials and video workshops |
| New LC-MS user — I have raw LC-MS files. Where do I begin? | Start with data processing and quality control. Ask your MS facility which file format and acquisition type you have; then use the study guide to choose a downstream aim. | None | Find tutorials and video workshops; Understand data processing · Browse preprocessing tools; Explore quality-control tools |
| Feature table only — Processed feature table; find molecular families | Spectral molecular families need fragmentation spectra linked to precursors. A feature table alone does not provide that evidence; check whether MS/MS was acquired. | None | Find tutorials and video workshops |
| Missing QC controls — Processed data; drift correction; QC/order missing | The pooled-QC drift-correction route needs repeated representative QC injections and injection order. Missing QC cannot be reconstructed by selecting this method. Review available controls and batch effects with your analyst. | None | Find tutorials and video workshops; Explore quality-control tools |
| Ordinary abundance study — Processed data; flux; no tracer experiment | Ordinary abundance measurements do not support these isotope-tracer flux methods. You can explore group differences or plan a suitable tracer experiment with a specialist. | None | Find tutorials and video workshops |
| Local statistical analysis — Can I analyze my metabolomics statistics locally in R? | Local analysis in R or Python is an option. Use the tool catalogue statistics filter to explore packages; the analysis depends on your study design, metadata and processed measurements. This request does not identify a specific published Strategy. | None | Find tutorials and video workshops; Explore statistical analysis tools, including local software |
| Retention model researcher — Use ROASMI to combine retention scores and MS/MS | 1 matching published Strategy. | Retention-order-assisted joint molecular annotation | None |
| Natural products researcher — Use MS2DECIDE for natural product prioritization | 1 matching published Strategy. | MS2DECIDE | None |
| No catalogue match — zzzz-unrepresented-method-xxxx | No matching published Strategy in the current collection. | None | Find tutorials and video workshops; Browse the curated Strategies · Explore the tool catalogue |
| QC evidence available — Processed feature table; drift correction; repeated QC and injection order available | QC drift correction requires repeated representative QC injections and recorded injection order. Check these requirements before using the published method. | QC-based robust LOESS signal-drift correction | Find tutorials and video workshops; Explore quality-control tools |

## Validation and limits

Schema, strict alpha build, controller tests, 56 metadata-driven query regressions and all ten browser journeys passed. Browser checks covered six context starters, reset behavior, missing-input gates, rendered implementation-tool links and widths 320/375/768/1440 without overflow or JavaScript errors. 8,910 local links/fragments and 313 relationships passed. Catalogue, contributor, submission, terminology and implementation tests passed.

SEO checks were evaluated against the independent alpha project canonical. The production-specific homepage assertion initially rejected the alpha URL as expected; an alpha-specific test harness checked the same metadata assertions without changing the shipped production guard. All five SEO unit assertions and canonical/sitemap checks passed under that harness. The published alpha snapshot is noindex and its robots file disallows crawling.

Remaining release gates: independent novice and domain-expert review; narrower compatibility checks for proposed step alternatives; broader reviewed guided aims. Planning guidance requires local MS-facility input and does not select sample sizes, controls or acquisition parameters. The four guided analytical aims still do not cover every experiment context. No production Ask deployment is authorized by this alpha refresh.
