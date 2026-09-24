# GNPS2 downstream coverage audit — 2026-09-23

Scope: the official Tool Index, Workflow Index, MetaboApps overview, actual FBMN and classical-networking result linkouts, GNPS2 homepage announcement and Next Gen Web Apps listing. This is a dated public-resource audit, not a claim to enumerate private or dynamically deployed workflows. No analysis jobs were run.

## Requested resources

- ChemWalker: new reviewed Tool record in this batch. Core random-walk software and GNPS2 wrapper linked; primary 2023 paper verified.
- Everything Bagel: new reviewed Tool record in this batch. Upstream feature detection/alignment/gap filling connected to FBMN; 2026 preprint explicitly labelled. Standalone source/license and detailed execution remain unverified.
- FBMN Stats: already present. Added Hitchhiker aliases and local R/Python visibility; original 2025 issue/2024 online publication retained. No duplicate entry.

## Official Tool Index reconciliation

Exact official resource links are matched against catalogue links. A missing direct match is a review candidate, not proof of a distinct missing resource. Metadata support services and notebooks may belong under existing parent entries.

| Indexed resource | Catalogue / action |
|---|---|
| [Pubmed Co-Authors List](https://coauthor.wanglab.science/) | Exclude: author administration or NMR-only |
| [Nature Journals Author Quick Entry](https://natureauthors.wanglab.science/) | Exclude: author administration or NMR-only |
| [GNPS2 Spectral Similarity Hub](https://similarity.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [GNPS2 Structure Server](https://structure.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [GNPS2 Cytoscape](https://cytoscape.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [Metabolomics Spectrum Resolver](https://metabolomics-usi.gnps2.org) | Review for dedicated entry or existing-parent coverage |
| [GNPS2 Networking URL Formatter](https://urlformatter.gnps2.org) | Review for dedicated entry or existing-parent coverage |
| [GNPS2 Classical Networking Upset Plot Dashboard](http://classicalupset.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [GNPS2 FBMN Upset Plot Dashboard](https://fbmnupset.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [NP Classifier](https://npclassifier.gnps2.org/) | `npclassifier` |
| [GNPS2 Dashboard](https://dashboard.gnps2.org/) | `gnps-dashboard` |
| [GNPS2 Plotter Dashboard (Beta)](https://plotter.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [GNPS2 Dataset File Explorer (Beta)](https://explorer.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [GNPS2 Public Libraries Download List](https://external.gnps2.org/gnpslibrary) | Review for dedicated entry or existing-parent coverage |
| [GNPS2 Tiny Mass Sharer](https://tinymass.gnps2.org/) | `tinymass` |
| [GNPS2 MassQL Visualizer](https://massql.gnps2.org/) | `massql` |
| [GNPS2 MassQL Analysis/Chatbot](https://massql-analysis.gnps2.org/) | `gnps-massql-analysis` |
| [GNPS2 USI Playground](https://usi-playground.gnps2.org/) | `gnps-usi-playground` |
| [GNPS2 Network Customization Playground](https://networkcustomization.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [FBmnStatsGUIde](https://fbmn-statsguide.gnps2.org/) | `fbmn-stats` |
| [Chemical Proportionality](https://chemprop.gnps2.org/) | `chemprop` |
| [CorrOmics](https://corromics.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [CMMC Batch validation](https://cmmc-validation.gnps2.org/) | Review for dedicated entry or existing-parent coverage |
| [MetaboApp - DrugReadouts](https://drugreadouts.gnps2.org/) | `drug-readout` |
| [MetaboApp - CMMC Dashboard](https://cmmc-dashboard.gnps2.org/) | `cmmc-dashboard` |
| [MetaboApp - MassQL Post-MN](https://massqlpostmn.gnps2.org/) | `postmn-massql` |
| [MetaboApp - Reverse Metabolomics](https://reverse-metabolomics.gnps2.org/) | `gnps-reverse-metabolomics` |
| [MetaboApp - Conjugated Metabolome Explorer](https://conjugated-metabolome.gnps2.org/) | `conjugated-metabolome-explorer` |
| [MetaboApp - Multi‑step MassQL](https://multistep-massql.gnps2.org/) | `multistep-massql` |
| [MetaboApp - FoodReadouts](https://foodreadouts.gnps2.org/) | `food-readout` |
| [MS2LDA.org](http://ms2lda.org/) | Review for dedicated entry or existing-parent coverage |
| [Natural Products Atlas](https://www.npatlas.org/joomla/) | `natural-products-atlas` (legacy URL in index) |
| [MIBiG](https://mibig.secondarymetabolites.org/) | `mibig` |
| [ClassyFire](http://classyfire.wishartlab.com/) | Review for dedicated entry or existing-parent coverage |
| [SMART NMR](http://smart.ucsd.edu) | Exclude: author administration or NMR-only |
| [SNAP-MS](https://www.npatlas.org/discover/snapms/) | Review for dedicated entry or existing-parent coverage |

## Actual network result linkouts

| Workflow | Downstream action | Destination | Catalogue / action |
|---|---|---|---|
| FBMN | Run Chemwalker Analysis | https://gnps2.org/workflowinput?workflowname=chemwalker_nextflow_workflow | chemwalker (added here) |
| FBMN | Hitchhiker Statistics Guide | https://fbmn-statsguide.gnps2.org/Data_Preparation | fbmn-stats |
| FBMN | FBMN Simple Plotter | https://plotter.gnps2.org/ | Missing / detailed review needed |
| FBMN | Run Transitive Alignments | https://gnps2.org/workflowinput?workflowname=Transitive_alignment_workflow | Missing; verify method and wrapper |
| FBMN | Overlay Custom Network | https://gnps2.org/workflowinput?workflowname=gnps2_network_overlay_workflow | Missing; verify overlay inputs |
| FBMN | CMMC Enrichment Analysis | https://gnps2.org/workflowinput?workflowname=cmmc_gnps_network_enrichment_workflow | Review distinct wrapper vs cmmc-dashboard/cmmc-kb |
| FBMN | MassQL Interactive Analysis | https://massqlpostmn.gnps2.org | postmn-massql |
| FBMN | Multistep MassQL Interactive Analysis | https://multistep-massql.gnps2.org/ | multistep-massql |
| FBMN | Drug Readout Interactive Analysis | https://drugreadouts.gnps2.org/ | drug-readout |
| Classical | Run Transitive Alignments | https://gnps2.org/workflowinput?workflowname=Transitive_alignment_workflow | Missing; verify method and wrapper |
| Classical | Overlay Custom Network | https://gnps2.org/workflowinput?workflowname=gnps2_network_overlay_workflow | Missing; verify overlay inputs |
| Classical | CMMC Enrichment Analysis | https://gnps2.org/workflowinput?workflowname=cmmc_gnps_network_enrichment_workflow | Review distinct wrapper vs cmmc-dashboard/cmmc-kb |
| Classical | Feature Augment Network | https://gnps2.org/workflowinput?workflowname=feature_augmentation_workflow | Missing / detailed review needed |
| Classical | MassQL Interactive Analysis | https://massqlpostmn.gnps2.org | postmn-massql |
| Classical | MassQL Interactive Analysis | https://massqlpostmn.gnps2.org | postmn-massql |

## Notebook follow-up

The index also links five notebook examples: MASST post-processing, MassQL/network integration, family-consistent fragmentation, MassQL post-processing and CMMC integration. These need review as implementations or supporting resources under their existing tools, rather than automatic separate entries.

## Additional boundaries and priorities

The Workflow Index already points to catalogue entries for MSMS-Chooser, FBMN, NPClassifier, MS2LDA, MS2Query and MSHub-GC; ChemWalker fills its named gap. MetaboApps food/drug readouts, CMMC Dashboard, conjugated-metabolome explorer, reverse metabolomics, PostMN/Multi-step MassQL and ChemProp already have records. CorrOmics remains missing as an individual entry.

Prioritize FBMN Plotter, transitive alignments, network overlay, CorrOmics and the classical/FBMN UpSet comparison apps next. Review separate workflow wrappers before duplicating a tool. Spectrum Resolver, similarity/structure services, dataset explorer, network reformatting and notebook utilities also need explicit coverage decisions.

Next Gen Web Apps separates maintained apps from in-development tools and an unreviewed sandbox. Its networking packager and browser Cytoscape session generator need review as distinct utilities; browser MassQL may be an interface extension. Do not silently replace existing production entries with in-development reimplementations (including FBMN-STATS, ModiFinder and IsoPairFinder). NMR-only resources, author-administration utilities, generic genomics tools and proteomics-only TPP are outside this MS-metabolomics downstream batch.

## Sources

- https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/toolindex/
- https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/workflowindex/
- https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/metaboapps_overview/
- https://github.com/Wang-Bioinformatics-Lab/Feature_Based_Molecular_Networking_Workflow/blob/master/workflowdisplay.yaml
- https://github.com/Wang-Bioinformatics-Lab/Classical_Networking_Workflow/blob/master/workflowdisplay.yaml
- https://gnps2.org/homepage
- https://apps.gnps2.org/

Ask Navigator and the large handoff remain held back. This tool batch is separate.


## Follow-up 2026-09-24

Added CorrOmics and GNPS2 Network Overlay after reviewing official app source and the working Progenesis overlay tutorial. Earlier missing labels above remain the initial audit snapshot. CorrOmics links paired tables through explicit sample metadata; no dedicated publication or explicit license was established. The overlay source repository and general documentation link were unavailable, so the entry uses the working official tutorial and limits its claims accordingly. FBMN Plotter endpoint retrieval timed out; do not infer retirement from that. Transitive-alignment documentation is available but still labels its citation “In Press”; primary-paper identity remains to be resolved.
