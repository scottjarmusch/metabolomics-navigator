# Enveda expansion — 27 October 2026, batch 3

45 new records prepared from the remaining review drafts. This branch starts from main `db62d32b14db4bc2933040d8bb72d21b31578b2e` independently of PRs #81 and #82. It neither deploys nor merges those changes. The three batches propose 96 unique additions, for 290 tools relative to the 194-tool baseline.

Official repository documentation, package metadata, license texts and primary publication identities were reviewed on 2026-10-27. This is editorial review: no third-party tool, model or benchmark was executed, and no developer verification is claimed. Repository recency is not proof of operational compatibility. Existing catalogue checks validate the website, not the scientific accuracy of external software.

## Material corrections and limits

- LPPtiger 2 cites its actual oxidized-lipid workflow paper, replacing the unrelated MSRIDD DOI. LipidA-IDER retains the verified original paper; the intake update DOI returned 404 and is omitted.
- LipidSpace is a distinct resource from LORA. Its actual paper is used and the mismatched LORA intake row remains unresolved.
- Spectral Denoising uses the published 2025 Denoising Search paper, replacing its README's mismatched Flash Entropy DOI. Norm-ISWSVR uses the original 2022 method paper rather than treating the later application evaluation as its introduction.
- MS-BART and DiffMS cite verified arXiv manuscripts, with author-reported conference association distinguished from an independently verified proceedings citation. Mass2SMILES and LipidQMap remain explicitly labelled preprints.
- SpecTUS and MASSISTANT use EI spectra, not ESI tandem spectra. Their final NIST-trained models are not distributed; MASSISTANT remains a training-oriented release with inference instructions pending. DiffMS requires a molecular formula.
- CCSfind and MOCCal calculate experimental/calibrated CCS; they are not assigned structure-to-CCS prediction. MobilityTransformR performs CE effective-mobility scaling, not ion-mobility CCS prediction. SERDA is normalization, not isotope tracing.
- rIDIMS scan subdivisions do not create independent biological replicates. Its online tutorial records a package-loading error; no current operational success is inferred. lcmsWorld macOS compatibility and ConCISE's deprecated macOS GUI are qualified.
- Restricted LPPtiger 2, LipidA-IDER, LipidQMap, MetaPro and Norm-ISWSVR terms are explicit. MESSES has a modified Clear BSD text with a citation condition; an unmodified standard license is not claimed. Public code without an established reuse grant is labelled source-available.
- IonToolPack cites the PeakQC component paper; no claim is made that this paper introduces every later module. IDSL_MINT's original fingerprint paper is distinguished from additional documented modules.

## Candidates held back

The remaining nine drafts are not promoted: dnMS2Purifier, RapidMass, ShinyMetID, DADIA, FSA, TEFT and qComics need stronger interface/publication evidence; mssearchr is distinct from the intake's mspepsearchr citation; DiffSpectra documents IR/Raman/UV-Vis inputs, not a demonstrated MS workflow. These require separate follow-up rather than inferred claims.

## Source trail

| Entry | Official documentation | Primary DOI(s) |
| --- | --- | --- |
| LPPtiger 2 (`lpptiger2`) | https://github.com/LMAI-TUD/lpptiger2#readme | https://doi.org/10.1038/s41467-022-33225-9 |
| AirdPro (`airdpro`) | https://github.com/CSi-Studio/AirdPro#readme | https://doi.org/10.1186/s12859-021-04490-0 |
| BreathXplorer (`breathxplorer`) | https://github.com/HuanLab/breathXplorer#readme | https://doi.org/10.1021/jasms.4c00152 |
| IDSL_MINT (`idsl-mint`) | https://github.com/idslme/IDSL_MINT#readme | https://doi.org/10.1186/s13321-024-00804-5 |
| ISFrag (`isfrag`) | https://github.com/HuanLab/ISFrag#readme | https://doi.org/10.1021/acs.analchem.1c01644 |
| JPA (`jpa`) | https://github.com/HuanLab/JPA#readme | https://doi.org/10.3390/metabo12030212 |
| LipidA-IDER (`lipida-ider`) | https://github.com/Systems-Biology-Of-Lipid-Metabolism-Lab/LipidA-IDER#readme | https://doi.org/10.1021/acs.analchem.1c03566 |
| Mass2SMILES (`mass2smiles`) | https://github.com/volvox292/mass2smiles#readme | https://doi.org/10.1101/2023.07.06.547963 |
| MESSES (`messes`) | https://moseleybioinformaticslab.github.io/MESSES/ | https://doi.org/10.3390/metabo13070842 |
| MetaPro (`metapro`) | https://csi-studio.github.io/MetaPro/guide/user-manual.html | https://doi.org/10.1007/s11306-023-02018-6 |
| MS-BART (`ms-bart`) | https://github.com/OpenDFM/MS-BART#readme | https://doi.org/10.48550/arXiv.2510.20615 |
| pyOpenMS-viz (`pyopenms-viz`) | https://pyopenms-viz.readthedocs.io/en/latest/index.html | https://doi.org/10.1021/acs.jproteome.4c00873 |
| spectral-denoising (`spectral-denoising`) | https://spectral-denoising.readthedocs.io/en/latest/index.html | https://doi.org/10.1038/s41592-025-02646-x |
| SpecTUS (`spectus`) | https://github.com/hejjack/SpecTUS#readme | https://doi.org/10.1021/acs.analchem.6c02423 |
| ViMMS (`vimms`) | https://glasgowcompbio.github.io/vimms/ | https://doi.org/10.3390/metabo9100219; https://doi.org/10.21105/joss.03990 |
| ALISTER (`alister`) | https://github.com/Fraunhofer-ITMP/alister#readme | https://doi.org/10.1016/j.cca.2024.117858 |
| arcMS (`arcms`) | https://leesulab.github.io/arcMS/ | https://doi.org/10.1093/bioadv/vbae160 |
| IonToolPack (`iontoolpack`) | https://github.com/pnnl/IonToolPack#readme | https://doi.org/10.1021/jasms.4c00146 |
| lcmsWorld (`lcmsworld`) | https://github.com/PGB-LIV/lcmsWorld#readme | https://doi.org/10.1021/acs.jproteome.0c00618 |
| LipidQMap (`lipidqmap`) | https://github.com/swinnenteam/LipidQMap#readme | https://doi.org/10.1101/2025.10.15.682422 |
| LipidSpace (`lipidspace`) | https://lifs-tools.org/tools/lipidspace.html | https://doi.org/10.1021/acs.analchem.3c02449 |
| MassQLab (`massqlab`) | https://github.com/JohnsonDylan/MassQLab#readme | https://doi.org/10.1002/rcm.10132 |
| MeTEor (`meteor`) | https://github.com/scibiome/meteor#readme | https://doi.org/10.1093/bioadv/vbae178 |
| MobilityTransformR (`mobilitytransformr`) | https://github.com/LiesaSalzer/MobilityTransformR/blob/main/vignettes/MobilityTransformR.Rmd | https://doi.org/10.1093/bioinformatics/btac441 |
| msiFlow (`msiflow`) | https://github.com/Immunodynamics-Engel-Lab/msiflow#readme | https://doi.org/10.1038/s41467-024-55306-7 |
| mspack (`mspack`) | https://github.com/fhanau/mspack#readme | https://doi.org/10.1093/bioinformatics/btab636 |
| omicsMIC (`omicsmic`) | https://github.com/WQLin8/omicsMIC#readme | https://doi.org/10.1093/nargab/lqae071 |
| PLSKO (`plsko`) | https://guannan-yang.github.io/PLSKO/PLSKO.html | https://doi.org/10.1093/bioinformatics/btaf475 |
| BAM (`bam`) | https://github.com/HassounLab/BAM#readme | https://doi.org/10.1021/acs.analchem.4c01565 |
| CCSfind (`ccsfind`) | https://github.com/sangeeta97/ccs_find#readme | https://doi.org/10.1002/jms.5040 |
| ConCISE (`concise`) | https://zquinlan.github.io/conCISE/ | https://doi.org/10.3390/metabo12121275 |
| CRISP (`crisp`) | https://github.com/vivekmathema/GCxGC-CRISP#readme | https://doi.org/10.1093/bib/bbab550 |
| DeepGCN-RT (`deepgcn-rt`) | https://github.com/kangqiyue/DeepGCN-RT#readme | https://doi.org/10.1016/j.chroma.2023.464439 |
| DeepION (`deepion`) | https://github.com/BioNet-XMU/DeepION#readme | https://doi.org/10.1021/acs.analchem.3c05002 |
| DiffMS (`diffms`) | https://github.com/coleygroup/DiffMS#readme | https://doi.org/10.48550/arXiv.2502.09571 |
| FIDDLE (`fiddle`) | https://msfiddle.readthedocs.io | https://doi.org/10.1038/s41467-025-66060-9 |
| mass2adduct (`mass2adduct`) | https://github.com/kbseah/mass2adduct#readme | https://doi.org/10.1021/acs.analchem.0c04720 |
| MASSISTANT (`massistant`) | https://github.com/BartaLazar/MASSISTANT#readme | https://doi.org/10.1016/j.chroma.2025.466216 |
| MOCCal (`moccal`) | https://github.com/HinesLab/MOCCal#readme | https://doi.org/10.1021/acs.analchem.3c04290 |
| Norm-ISWSVR (`norm-iswsvr`) | https://github.com/Dingxian666/Norm-ISWSVR#readme | https://doi.org/10.1021/acs.analchem.1c05502 |
| OrbiFragsNets (`orbifragsnets`) | https://github.com/EdwinChingate/OrbiFragsNets#readme | https://doi.org/10.1016/j.mex.2023.102257 |
| PACCS (`paccs`) | https://github.com/yuxuanliao/PACCS#readme | https://doi.org/10.1002/cem.70040 |
| rIDIMS (`ridims`) | https://bioinovarlab.github.io/rIDIMS/articles/rIDIMS.html | https://doi.org/10.1016/j.talanta.2024.127273 |
| SERDA (`serda`) | https://github.com/slfan2013/SERDA#readme | https://doi.org/10.3390/metabo13080944 |
| SGMNS (`sgmns`) | https://github.com/DLUT-datas/SGMNS#readme | https://doi.org/10.1021/acs.analchem.3c00849 |

The ledger reconciles 45 matching intake rows. No Education, Strategies or Ask Navigator changes. Local checks and CI results are reported in the PR.
