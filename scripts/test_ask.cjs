// Run the shipped Ask controller with a minimal DOM.
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
class Element {
  constructor(dataset={}) { this.dataset=dataset; this.events={}; this.children=[]; this.value=''; this.hidden=true; }
  focus() { this.focused=true; }
  addEventListener(name, callback) { this.events[name]=callback; }
  appendChild(card) { this.children=this.children.filter(x=>x!==card); this.children.push(card); }
}
const input=new Element(), button=new Element(), results=new Element(), count=new Element(), empty=new Element();
const cards=Array.from({length:8},(_,i)=>new Element({name:i===7?'isotope tracing':'other '+i,search:'isotope tracing',year:'2020'}));
results.children=[...cards];
const elements={'#ask-query':input,'#ask-search-button':button,'#ask-strategy-results':results,'#ask-result-count':count,'#ask-empty':empty};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../assets/ask.js'),'utf8'),{document:{querySelector:s=>elements[s],querySelectorAll:s=>s==='.ask-strategy-card'?cards:[]}});
input.value='isotope';button.events.click();
assert.equal(results.children.filter(x=>!x.hidden)[0],cards[7],'Best match must appear first, not in original catalogue order');
assert.equal(cards.filter(x=>!x.hidden).length,6);
input.value='unrepresentedquery';button.events.click();assert.equal(empty.hidden,false);assert(cards.every(x=>x.hidden));
input.value='';button.events.click();assert.equal(empty.hidden,true);assert(cards.every(x=>x.hidden));
input.value='isotope';input.events.keydown({key:'Enter',preventDefault(){}});assert.equal(cards[7].hidden,false);
console.log('Ask tests passed: relevance order, six-result limit, no match, empty query and Enter.');

input.value='NMR spectra';button.events.click();assert(cards.every(x=>x.hidden));assert.match(count.textContent,/outside scope/);
input.value='carbon flux';button.events.click();assert(cards.every(x=>x.hidden));assert.match(count.textContent,/not a substitute/);
input.value='I am new to metabolomics and want to compare treated and untreated cells';button.events.click();assert(cards.every(x=>x.hidden));assert.match(count.textContent,/scientific aim/);

// Flux routing is driven by curated objectives when a qualifying record exists.
cards[7].dataset.objectives='flux_analysis';input.value='isotope flux';button.events.click();assert.equal(cards.filter(x=>!x.hidden).length,1);assert.equal(cards[7].hidden,false);

// A single incidental word should not accompany a much stronger workflow match.
const focused=[new Element({name:'pooled QC LOESS signal drift',search:'pooled QC LOESS signal drift',keywords:'pooled QC LOESS signal drift'}),new Element({name:'other acquisition',search:'signal acquisition'})];
const focusedGrid=new Element(); focusedGrid.children=[...focused];
const focusedInput=new Element(), focusedButton=new Element(), focusedCount=new Element(), focusedEmpty=new Element();
const focusedElements={'#ask-query':focusedInput,'#ask-search-button':focusedButton,'#ask-strategy-results':focusedGrid,'#ask-result-count':focusedCount,'#ask-empty':focusedEmpty};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../assets/ask.js'),'utf8'),{document:{querySelector:s=>focusedElements[s],querySelectorAll:s=>s==='.ask-strategy-card'?focused:[]}});
focusedInput.value='pooled QC LOESS signal drift';focusedButton.events.click();
assert.equal(focused[0].hidden,false);assert.equal(focused[1].hidden,true);
assert.match(focusedCount.textContent,/^1 matching/);
focusedInput.value='signal';focusedButton.events.click();
assert.equal(focused[1].hidden,false,'Broad searches retain weaker but comparable results');
focusedInput.value='notincatalogue';focusedButton.events.click();
assert(focused.every(x=>x.hidden),'No-match search must remain safe after score filtering');

// Guided entry and mixed-intent behavior use the same shipped controller.
const guideButton=new Element(), stage=new Element(), data=new Element(), aim=new Element(), message=new Element(), guidance=new Element(), mixed=new Element();
const guidedElements={...focusedElements,'#ask-guide-button':guideButton,'#ask-stage':stage,'#ask-data':data,'#ask-aim':aim,'#ask-guide-message':message,'#ask-guidance':guidance,'#ask-mixed':mixed};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../assets/ask.js'),'utf8'),{document:{querySelector:s=>guidedElements[s],querySelectorAll:s=>s==='.ask-strategy-card'?focused:[]}});
focusedInput.value='Compare QC drift correction and isotope flux estimation';focusedButton.events.click();
assert(focused.every(x=>x.hidden));assert.equal(mixed.hidden,false);assert.match(focusedCount.textContent,/separately/);
focusedInput.value='new to metabolomics';focusedButton.events.click();assert.equal(guidance.open,true);assert.equal(mixed.hidden,true);
guideButton.events.click();assert.match(message.textContent,/Choose a study stage/);
stage.value='planning';data.value='msms';aim.value='families';guideButton.events.click();assert.match(message.textContent,/before choosing/);assert(focused.every(x=>x.hidden));
stage.value='raw';guideButton.events.click();assert.match(message.textContent,/raw files/);
stage.value='analysis';data.value='features';guideButton.events.click();assert.match(message.textContent,/table alone/);assert(focused.every(x=>x.hidden));
data.value='unknown';guideButton.events.click();assert.match(message.textContent,/clarify/);
data.value='msms';aim.value='qc';guideButton.events.click();assert.equal(focused[0].hidden,false);assert.match(message.textContent,/repeated representative QC/);
stage.value='planning';guideButton.events.click();assert(focused.every(x=>x.hidden),'Planning guidance must clear previous results');
console.log('Guided-entry checks passed: missing answers, planning, raw files, unknown measurements, incompatible table, QC and mixed intent.');

// Show only the aims mentioned, and let the chosen aim execute its existing search.
const choices=[new Element({askIntent:'qc',askExample:'pooled QC LOESS signal drift'}),new Element({askIntent:'flux',askExample:'isotope labeling time course flux'}),new Element({askIntent:'pathways',askExample:'pathway enrichment unidentified features'}),new Element({askIntent:'families',askExample:'feature based molecular networking'})];
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../assets/ask.js'),'utf8'),{document:{querySelector:s=>guidedElements[s],querySelectorAll:s=>s==='.ask-strategy-card'?focused:s==='[data-ask-intent]'||s==='[data-ask-example]'?choices:[]}});
focusedInput.value='QC correction then pathway interpretation';focusedButton.events.click();
assert.deepEqual(choices.filter(x=>!x.hidden).map(x=>x.dataset.askIntent),['qc','pathways']);
choices[0].events.click();assert.equal(mixed.hidden,true);assert.equal(focused[0].hidden,false);assert.equal(focusedInput.focused,true);
focusedInput.value='molecular networking and pathways';focusedButton.events.click();
assert.deepEqual(choices.filter(x=>!x.hidden).map(x=>x.dataset.askIntent),['pathways','families']);
focusedInput.value='flux through pathways';focusedButton.events.click();assert.equal(mixed.hidden,true,'Related concepts without separate aims should not trigger a split');
focusedInput.value='NMR QC and flux';focusedButton.events.click();assert.equal(mixed.hidden,true);assert.match(focusedCount.textContent,/outside scope/);
