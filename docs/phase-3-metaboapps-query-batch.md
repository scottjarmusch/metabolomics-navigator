# Phase 3 — MetaboApps query and context batch

Reviewed 10 September 2026, following the successful deployment of `fa81532` (GitHub Pages run 34448208439). Phase 3 remains in progress.

Added **PostMN MassQL**, **Multi-step MassQL** and **GNPS2 Reverse Metabolomics**, bringing the catalogue to **87 Tools and 13 Strategies**. These are separate launchable apps linked to the MetaboApps parent and their relevant processing/query Tools. Task guides expose the new pages.

Corrected two material handoff assumptions: the current Multi-step MassQL app is documented specifically for bile acids, and the Reverse Metabolomics app starts from MS/MS USIs rather than structure strings. The latter remains distinct from the existing experimental Strategy. None of the three pages claims a verified standalone app paper; each supplies a direct documentation citation. Query-source application papers are not promoted into the app's core bibliography.

Source pages reviewed:

- [PostMN MassQL](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapp_PostMN_MassQL/)
- [Multi-step MassQL](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapp_Multi-Step_MassQL/)
- [Reverse Metabolomics](https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapp_Reverse_Metabolomics/)

The three public app URLs returned Streamlit HTML shells. No query jobs were launched, and end-to-end service operation was not tested. Access notes retain GNPS2's academic/industry distinction without assigning unverified code licenses.

All catalogue, form-sync, editorial, strict-build, catalogue-JS, terminology-regression and terminology-audit checks pass. Link validation checks **3,981 local links/fragments over 117 pages** and **203 declared/parent-child relationship links**. All nine new-Tool route/viewport checks (1280, 640, 390 px) pass, including citation rendering, parent links, keyboard skip link and no horizontal overflow or browser JavaScript errors.

Next: reconcile and finish the remaining GNPS2 inventory, including remaining MetaboApps and launchable scientific web apps; update the existing MS2LDA page after the child apps. Then follow the master phase order. No Ask Navigator implementation yet.
