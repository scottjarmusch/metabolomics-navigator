// Exercise the shipped catalogue controller without a browser or extra packages.
const {readFileSync} = require('node:fs');
const {join} = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const code = readFileSync(join(__dirname, '../assets/catalogue.js'), 'utf8');
class Element {
  constructor(attrs={}) { this.attrs=attrs; this.dataset={}; this.events={}; this.children=[]; this.value=''; this.hidden=false; }
  getAttribute(k) { return this.attrs[k]; }
  setAttribute(k,v) { this.attrs[k]=v; }
  addEventListener(k,fn) { this.events[k]=fn; }
  appendChild(e) { this.children=this.children.filter(x=>x!==e); this.children.push(e); }
  replaceChildren() { this.children=[]; }
  focus() { this.focused=true; }
  get selectedIndex() { return this.options.findIndex(o=>o.value===this.value); }
}
function setup(query='') {
  const cards = [
    new Element({'data-name':'alpha','data-search-text':'Alpha LC-MS spectral search Dührkop','data-function':'reference_data_search spectral_analysis','data-platforms':'lc_ms','data-created':'2024-01-01','data-updated':'2026-09-01'}),
    new Element({'data-name':'beta','data-search-text':'Beta LC-MS peak detection','data-function':'preprocessing','data-platforms':'lc_ms','data-created':'2025-01-01','data-updated':'2026-08-01'}),
  ];
  const search=new Element(), sort=new Element(), filter=new Element();
  filter.dataset.filter='function'; filter.options=[{value:'',text:'All functions'},{value:'preprocessing',text:'Preprocessing (1)'},{value:'reference_data_search',text:'Reference data search (1)'},{value:'spectral_analysis',text:'Spectral analysis (1)'}];
  sort.value='az'; sort.options=['az','newest','updated'].map(value=>({value,text:value}));
  const grid=new Element(), count=new Element(), empty=new Element(), active=new Element(), reset=new Element();
  const singles={'[data-search]':search,'[data-sort]':sort,'[data-record-grid]':grid,'[data-result-count]':count,'[data-empty]':empty,'[data-active-filters]':active};
  const root={querySelector:s=>singles[s],querySelectorAll:s=>({'[data-record-card]':cards,'[data-filter]':[filter],'[data-reset]':[reset]})[s]};
  let url='';
  vm.runInNewContext(code,{
    document:{querySelector:()=>root,createElement:()=>new Element()},
    location:{search:query,pathname:'/metabolomics-navigator/tools/',hash:''},
    history:{replaceState:(_a,_b,value)=>{url=value;}},URLSearchParams,
    setTimeout:fn=>{fn();return 1;},clearTimeout:()=>{},
  });
  return {cards,search,sort,filter,grid,count,empty,active,reset,url:()=>url};
}
let s=setup('?q=search+LC-MS');
assert.equal(s.count.textContent,'1'); // Noncontiguous query terms.
assert.equal(s.cards[0].hidden,false);
assert.equal(s.cards[1].hidden,true);
s=setup('?function=spectral_analysis'); assert.equal(s.count.textContent,'1');
s=setup('?q=duhrkop'); assert.equal(s.count.textContent,'1'); // Diacritics.
s=setup('?q=LC-MS&function=preprocessing');
assert.equal(s.count.textContent,'1'); assert.equal(s.active.children.length,2);
s.active.children[1].events.click();
assert.equal(s.count.textContent,'2'); assert.equal(s.active.children.length,1);
assert.ok(!s.url().includes('function=')); assert.ok(s.search.focused);
s=setup('?q=%3Cimg%20src=x%20onerror=alert(1)%3E');
assert.equal(s.count.textContent,'0'); assert.equal(s.empty.hidden,false);
assert.ok(s.active.children[0].textContent.includes('<img')); // Treated as text, never HTML.
s.reset.events.click(); assert.equal(s.count.textContent,'2'); assert.equal(s.empty.hidden,true);
assert.equal(s.active.hidden,true); assert.equal(s.url(),'/metabolomics-navigator/tools/');
s=setup('?sort=newest'); assert.equal(s.grid.children[0].attrs['data-name'],'beta');
s.sort.value='updated'; s.sort.events.change(); assert.equal(s.grid.children[0].attrs['data-name'],'alpha');
s=setup('?sort=invalid&function=invalid'); assert.equal(s.count.textContent,'2'); assert.equal(s.sort.value,'az');
vm.runInNewContext(code,{document:{querySelector:()=>null}});
console.log('Catalogue tests passed: multiword search, diacritics, combined filters, removable chips, safe text, empty/reset, sorting, invalid URL values and non-catalogue pages.');
