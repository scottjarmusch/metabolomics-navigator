# Study-first Ask alpha review (2026-09-20)

## Changes

- A separate expandable entry asks for study stage, measurement type and scientific aim. Unknown answers are valid and lead to clarification rather than a fabricated workflow.
- Planning and raw-file requests receive preparation guidance and links to the existing guide/catalogue. Processed-data requests use curated search phrases to retrieve existing Strategies; no capabilities or tool dependencies are generated.
- A feature table alone does not enable fragmentation-based molecular-family recommendations. Flux and QC results state the experiment-specific requirements.
- Questions containing both QC/drift correction and flux now ask users to explore each aim separately. Buttons search the existing QC and flux metadata. No combined workflow is inferred.

## Verification and limits

- Controller regression tests cover missing answers, planning, raw files, unknown measurements, an incompatible feature table, QC search, stale-result clearing and mixed QC/flux intent.
- Generated-catalogue coverage increases from ten to eleven queries, retaining the earlier leading results and adding the mixed-intent clarification case.
- Browser interaction confirmed the feature-table safeguard. Responsive and link checks caught an overflowing select layout and nonexistent guide-root route; both were corrected before final validation.
- This is a limited deterministic guide, not a general conversational assistant. Mixed-intent detection currently recognizes QC plus flux only. Other combinations, negation, study-design details and acquisition-specific compatibility still require further review. No new Strategy cards or catalogue entries were added in this batch.
- Supersedes the QC-plus-flux limitation reported in `ask-query-check-2026-09-20.md`; that document remains a historical snapshot of the earlier controller.

Final browser check: the expanded form fits a 390 x 844 viewport; the feature-table warning and QC/flux clarification render correctly. Selecting Explore analytical QC returns QC-RLSC and clears the clarification panel. The viewport override was reset after testing.
