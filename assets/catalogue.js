(() => {
  const root = document.querySelector('[data-catalogue]');
  if (!root) return;
  const cards = [...root.querySelectorAll('[data-tool-card]')];
  const search = root.querySelector('[data-search]');
  const filters = [...root.querySelectorAll('[data-filter]')];
  const sort = root.querySelector('[data-sort]');
  const grid = root.querySelector('[data-tool-grid]');
  const counts = [...root.querySelectorAll('[data-result-count]')];
  const empty = root.querySelector('[data-empty]');
  const active = root.querySelector('[data-active-filters]');

  const params = new URLSearchParams(location.search);
  if (search && params.get('q')) search.value = params.get('q');
  filters.forEach(select => { if (params.get(select.dataset.filter)) select.value = params.get(select.dataset.filter); });
  if (sort && params.get('sort')) sort.value = params.get('sort');

  function includesToken(value, token) {
    return !token || (` ${value} `).includes(` ${token} `);
  }

  function apply() {
    const query = (search?.value || '').trim().toLowerCase();
    const values = Object.fromEntries(filters.map(s => [s.dataset.filter, s.value]));
    let visible = cards.filter(card => {
      if (query && !card.dataset.searchText.includes(query)) return false;
      if (values.function && card.dataset.function !== values.function) return false;
      if (values.platforms && !includesToken(card.dataset.platforms, values.platforms)) return false;
      if (values.interfaces && !includesToken(card.dataset.interfaces, values.interfaces)) return false;
      if (values.access && card.dataset.access !== values.access) return false;
      if (values.resourceTypes && !includesToken(card.dataset.resourceTypes, values.resourceTypes)) return false;
      return true;
    });

    const mode = sort?.value || 'az';
    visible.sort((a, b) => {
      if (mode === 'newest') return b.dataset.created.localeCompare(a.dataset.created) || a.dataset.name.localeCompare(b.dataset.name);
      if (mode === 'updated') return b.dataset.updated.localeCompare(a.dataset.updated) || a.dataset.name.localeCompare(b.dataset.name);
      return a.dataset.name.localeCompare(b.dataset.name);
    });

    cards.forEach(card => card.hidden = true);
    visible.forEach(card => { card.hidden = false; grid.appendChild(card); });
    counts.forEach(el => el.textContent = String(visible.length));
    empty.hidden = visible.length !== 0;

    const chips = [];
    if (query) chips.push(`Search: ${search.value}`);
    filters.forEach(select => { if (select.value) chips.push(select.options[select.selectedIndex].text.replace(/ \(\d+\)$/, '')); });
    active.innerHTML = chips.map(x => `<span>${escapeHtml(x)}</span>`).join('');
    active.hidden = chips.length === 0;

    const next = new URLSearchParams();
    if (query) next.set('q', search.value.trim());
    filters.forEach(select => { if (select.value) next.set(select.dataset.filter, select.value); });
    if (mode !== 'az') next.set('sort', mode);
    history.replaceState(null, '', `${location.pathname}${next.toString() ? '?' + next : ''}`);
  }

  function escapeHtml(value) {
    return value.replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
  }

  let timer;
  search?.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(apply, 100); });
  filters.forEach(select => select.addEventListener('change', apply));
  sort?.addEventListener('change', apply);
  root.querySelectorAll('[data-reset]').forEach(button => button.addEventListener('click', () => {
    if (search) search.value = '';
    filters.forEach(select => select.value = '');
    if (sort) sort.value = 'az';
    apply();
    search?.focus();
  }));
  apply();
})();
