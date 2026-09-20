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

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "ask-strategy-card" in values.get("class", "").split():
            self.cards.append({k[5:]: v for k, v in attrs if k.startswith("data-")})

CASES = [
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
grid.children=[...cards];
const elements={'#ask-query':input,'#ask-search-button':button,'#ask-strategy-results':grid,'#ask-result-count':count,'#ask-empty':empty};
vm.runInNewContext(fixture.controller,{document:{querySelector:s=>elements[s],querySelectorAll:s=>s==='.ask-strategy-card'?cards:[]}});
const answers=fixture.queries.map(query=>{input.value=query;button.events.click();return {query,message:count.textContent,results:grid.children.filter(x=>!x.hidden).map(x=>x.dataset.name)};});
process.stdout.write(JSON.stringify(answers));
"""

def run():
    parser = Cards()
    parser.feed((ROOT / "dist/ask/index.html").read_text(encoding="utf-8"))
    if not parser.cards:
        raise AssertionError("Build the site first: no rendered Strategy cards found")
    payload = {"cards": parser.cards, "controller": (ROOT / "assets/ask.js").read_text(encoding="utf-8"), "queries": [c[0] for c in CASES]}
    result = subprocess.run(["node", "-e", JS], input=json.dumps(payload), capture_output=True, text=True, encoding="utf-8", check=True)
    answers = json.loads(result.stdout)
    assert len(answers) == len(CASES), "Every regression question must produce an answer"
    for (query, expected, message), answer in zip(CASES, answers):
        print(json.dumps(answer, ensure_ascii=True))
        if expected:
            assert answer["results"] and answer["results"][0] == expected, query
        else:
            assert not answer["results"] and message in answer["message"], query
    print(f"Generated Ask checks passed: {len(CASES)} questions against {len(parser.cards)} Strategy cards.")

if __name__ == "__main__":
    run()
