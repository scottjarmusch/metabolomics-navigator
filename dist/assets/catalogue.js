(() => {
  const root=document.querySelector('[data-catalogue]'); if(!root)return;
  const cards=[...root.querySelectorAll('[data-record-card]')];
  const search=root.querySelector('[data-search]'); const filters=[...root.querySelectorAll('[data-filter]')]; const sort=root.querySelector('[data-sort]');
  const grid=root.querySelector('[data-record-grid]'); const counts=[...root.querySelectorAll('[data-result-count]')]; const empty=root.querySelector('[data-empty]'); const active=root.querySelector('[data-active-filters]');
  const params=new URLSearchParams(location.search); if(search&&params.get('q'))search.value=params.get('q'); filters.forEach(s=>{if(params.get(s.dataset.filter))s.value=params.get(s.dataset.filter)}); if(sort&&params.get('sort'))sort.value=params.get('sort');
  const includesToken=(value,token)=>!token||(` ${value||''} `).includes(` ${token} `);
  function data(card,key){return card.getAttribute(`data-${key}`)||''}
  function apply(){const query=(search?.value||'').trim().toLowerCase(); const values=Object.fromEntries(filters.map(s=>[s.dataset.filter,s.value]));
    let visible=cards.filter(card=>{if(query&&!data(card,'search-text').includes(query))return false; for(const [key,val] of Object.entries(values)){if(val&&!includesToken(data(card,key),val))return false} return true});
    const mode=sort?.value||'az'; visible.sort((a,b)=>{if(mode==='newest')return data(b,'created').localeCompare(data(a,'created'))||data(a,'name').localeCompare(data(b,'name')); if(mode==='updated')return data(b,'updated').localeCompare(data(a,'updated'))||data(a,'name').localeCompare(data(b,'name')); return data(a,'name').localeCompare(data(b,'name'))});
    cards.forEach(c=>c.hidden=true); visible.forEach(c=>{c.hidden=false;grid.appendChild(c)}); counts.forEach(e=>e.textContent=String(visible.length)); empty.hidden=visible.length!==0;
    const chips=[]; if(query)chips.push(`Search: ${search.value}`); filters.forEach(s=>{if(s.value)chips.push(s.options[s.selectedIndex].text.replace(/ \(\d+\)$/,''))}); active.innerHTML=chips.map(x=>`<span>${escapeHtml(x)}</span>`).join(''); active.hidden=chips.length===0;
    const next=new URLSearchParams(); if(query)next.set('q',search.value.trim()); filters.forEach(s=>{if(s.value)next.set(s.dataset.filter,s.value)}); if(mode!=='az')next.set('sort',mode); history.replaceState(null,'',`${location.pathname}${next.toString()?'?'+next:''}`)
  }
  function escapeHtml(v){return v.replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}
  let timer; search?.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(apply,100)}); filters.forEach(s=>s.addEventListener('change',apply)); sort?.addEventListener('change',apply); root.querySelectorAll('[data-reset]').forEach(b=>b.addEventListener('click',()=>{if(search)search.value='';filters.forEach(s=>s.value='');if(sort)sort.value='az';apply();search?.focus()})); apply();
})();
