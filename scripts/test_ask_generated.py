"""Exercise the shipped Ask controller against metadata from the strict site build."""
import json
import subprocess
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class Cards(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.tools = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "ask-strategy-card" in values.get("class", "").split():
            self.cards.append({k[5:]: v for k, v in attrs if k.startswith("data-")})
        if 'data-ask-tool' in values:
            self.tools.append({k[5:]: v for k, v in attrs if k.startswith('data-')})

CASES = [
    ('Can SIMPEL infer flux from unlabeled features?', None, 'missing input'),
    ('Can SIMPEL infer flux from unlabelled features?', None, 'missing input'),
    ('Use khipu to group adduct and isotope peaks', None, 'Named tools found'),
    ('Can Everything Bagel replace statistical analysis?', None, 'Named tools found'),
    ('Use ChemWalker to prioritize structures from my molecular network', None, 'Named tools found'),
    ("Epoxidation lipid double bond localization with epoxide fragments", "Epoxidation-assisted lipid double-bond localization", None),
    ("Spatial isotope tracing with tissue isotopologue maps", "Tissue isotope imaging with iso-imaging", None),
    ("Find double bond positions without derivatization", None, "missing input"),
    ("Map isotope incorporation without a tracer", None, "missing input"),
    ("Prioritize biotransformations from ordered abundance changes", "Chemical proportionality for transformation prioritization", None),
    ("Model paired microbiome metabolomics conditional associations", "Conditional microbe–metabolite association modeling", None),
    ("MALDI FISH link metabolites to microbial identity", "Correlative metabolite and microbial imaging with MALDI-FISH", None),
    ("Microfluidic bioactivity fractionation luminescent bioreporter", "Microfluidic fractionation for compound-resolved bioactivity", None),
    ("Infer transformations without ordered samples", None, "missing input"),
    ("Use mmvec without paired microbiome samples", None, "missing input"),
    ("I study bacteria. Can metabolomics help me discover new antibiotics?", None, "study guide"),
    ("We have blood samples from 200 patients and controls. Where should we start?", None, "study guide"),
    ("We forgot to measure pooled QC samples. How can we fix batch effects?", None, "missing input"),
    ("Can you compare treated and untreated cells and tell me which pathways changed?", None, "study guide"),
    ("Do I need MS/MS before I collect my samples?", None, "study guide"),
    ("I am a beginner with NMR and LC-MS data. What should I do?", None, "study guide"),
    ("Can I analyze my metabolomics statistics locally in R?", None, "tool catalogue"),
    ("Predict ion images from histology with microscopy mass spectrometry image fusion", "Predictive fusion of microscopy and mass spectrometry imaging", None),
    ("Process thousands of samples using pooled reference discovery", "Reference-pool discovery with cohort-wide signal extraction", None),
    ("DIA IntOpenStream MSE molecular networking", "Feature-Based Molecular Networking (FBMN)", None),
    ("Use iterative exclusion lists for previously fragmented ions", "Iterative exclusion-list MS/MS acquisition", None),
    ("Schedule precursor ions using topological sorting", "Iterative optimized MS/MS acquisition", None),
    ("Use retention order to rank structure candidates jointly", "Retention-order-assisted joint molecular annotation", None),
    ("I want pathway analysis, not flux", None, "exclusion"),
    ("Correct drift without pooled QC samples", None, "missing input"),
    ("I don't have MS/MS spectra for molecular networking", None, "missing input"),
    ("I cannot use isotope tracers but want flux", None, "exclusion"),
    ("This is my first metabolomics study", None, "study guide"),
    ("I have raw LC-MS files. Where do I begin?", None, "study guide"),
    ("I'm not sure whether I measured flux", None, "study guide"),
    ("I don't know what to do with these measurements", None, "study guide"),

    ("Estimate flux through metabolic pathways", "Kinetic flux profiling from isotope-labeling time courses", None),
    ("Correct signal drift then explore pathways", None, "separately"),
    ("Molecular networking and pathway enrichment", None, "separately"),
    ("Estimate flux and explore molecular families", None, "separately"),
    ("Compare QC drift correction and isotope flux estimation", None, "separately"),
    ("I am new to metabolomics and want to compare treated and untreated cells", None, "scientific aim"),
    ("I have NMR spectra and need peak assignment", None, "outside scope"),
    ("Find pathways when most of my significant features are unidentified", "Feature-level pathway inference before metabolite identification", None),
    ("Discover shared substructures from recurring fragments and neutral losses", "Shared-substructure discovery with Mass2Motifs", None),
    ("Test chemical class enrichment of identified metabolites with ChemRICH", "Chemical-similarity metabolite-set enrichment", None),
    ("Estimate flux from isotope labeling time courses", "Kinetic flux profiling from isotope-labeling time courses", None),
    ("Compare amines and phenols with isotope coded dansylation", "Isotope-coded dansylation for comparative metabolomics", None),
    ("Correct signal drift with pooled QC LOESS", "QC-based robust LOESS signal-drift correction", None),
    ("Control false discoveries in DIA data using an assay library", "Target-decoy-controlled DIA metabolomics", None),
    ("Link immune cell phenotypes to spatial metabolite images", "Same-section MSI and imaging mass cytometry integration", None),
]

JS = r"""
const fs=require('fs'),vm=require('vm');
const fixture=JSON.parse(fs.readFileSync(0,'utf8'));
class E {
 constructor(dataset={}){this.dataset=dataset;this.hidden=true;this.events={};this.value='';this.children=[];}
 addEventListener(k,f){this.events[k]=f;}
 appendChild(c){this.children=this.children.filter(x=>x!==c);this.children.push(c);}
}
const cards=fixture.cards.map(x=>new E(x)),input=new E(),button=new E(),grid=new E(),count=new E(),empty=new E();
const tools=(fixture.tools||[]).map(x=>new E(x)),toolPanel=new E();
grid.children=[...cards];
const elements={'#ask-query':input,'#ask-search-button':button,'#ask-strategy-results':grid,'#ask-result-count':count,'#ask-empty':empty,'#ask-tool-matches':toolPanel};
vm.runInNewContext(fixture.controller,{document:{querySelector:s=>elements[s],querySelectorAll:s=>s==='.ask-strategy-card'?cards:s==='[data-ask-tool]'?tools:[]}});
const answers=fixture.queries.map(query=>{input.value=query;button.events.click();return {query,message:count.textContent,results:grid.children.filter(x=>!x.hidden).map(x=>x.dataset.name),tools:tools.filter(x=>!x.hidden).map(x=>x.dataset.slug)};});
process.stdout.write(JSON.stringify(answers));
"""

def run():
    parser = Cards()
    parser.feed((ROOT / "dist/ask/index.html").read_text(encoding="utf-8"))
    if not parser.cards:
        raise AssertionError("Build the site first: no rendered Strategy cards found")
    payload = {"cards": parser.cards, "tools": parser.tools, "controller": (ROOT / "assets/ask.js").read_text(encoding="utf-8"), "queries": [c[0] for c in CASES]}
    result = subprocess.run(["node", "-e", JS], input=json.dumps(payload), capture_output=True, text=True, encoding="utf-8", check=True)
    answers = json.loads(result.stdout)
    assert len(answers) == len(CASES), "Every regression question must produce an answer"
    for (query, expected, message), answer in zip(CASES, answers):
        print(json.dumps(answer, ensure_ascii=True))
        if expected:
            assert answer["results"] and answer["results"][0] == expected, query
        else:
            assert not answer["results"] and message in answer["message"], query
        if query == 'Use khipu to group adduct and isotope peaks':
            assert answer['tools'] == ['khipu'], 'Named tool must resolve to its catalogue entry'
        if 'MS/MS spectra' in query:
            assert 'spectra' not in answer['tools'], 'Generic spectra must not be read as the Spectra package'
    print(f"Generated Ask checks passed: {len(CASES)} questions against {len(parser.cards)} Strategy cards.")

if __name__ == "__main__":
    run()
