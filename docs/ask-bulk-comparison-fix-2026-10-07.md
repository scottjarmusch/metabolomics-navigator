# Bulk comparison query correction

Reported input: `find metabolite differences in bulk soil samples`.

Reproduced before the fix: 24 lexical matches, with MALDI-FISH first. Shared sample terms were sufficient to match an imaging Strategy despite a bulk-comparison aim. The catalogue currently has no curated general differential-abundance Strategy that should be substituted automatically.

The alpha now recognizes general abundance/group-comparison requests across sample types, offers study-stage clarification and processing/QC/statistics links, and adds an explicit comparison aim to the guided entry. Named software and explicit analytical approaches retain their existing routes. Missing-input constraints and novice clarification retain priority. Explicit bulk queries exclude imaging-only Strategy records unless spatial/imaging measurements are requested.

Expected final response: Start with a bulk or group comparison: clarify your study stage, measurements and groups before selecting an analysis workflow.

Guidance explains the need for a processed abundance table, group/replicate/batch metadata and QC before selecting statistical analysis. It does not select a test, sample size, normalization method or a tool solely from the soil sample context.

Regression coverage includes the exact soil query, treated/control plasma, bacterial cultures, missing MS/MS and a positive bulk-soil FBMN request. Existing explicit spatial, structural, tracer and transformation queries remain covered. Browser validation checks both the exact question and the processed-data comparison selection, statistics links and 320–1440px layouts.
