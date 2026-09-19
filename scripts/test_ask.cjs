// Run the shipped Ask controller with a minimal DOM.
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
class Element {
  constructor(dataset={}) { this.dataset=dataset; this.events={}; this.children=[]; this.value=''; this.hidden=true; }
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
