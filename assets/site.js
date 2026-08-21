const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('#main-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('open', !open);
  });
}

const atlasSearch = document.querySelector('[data-atlas-search]');
if (atlasSearch) {
  const input = atlasSearch.querySelector('input[name="q"]');
  const scopeButtons = atlasSearch.querySelectorAll('[data-search-scope]');
  const actions = {
    tools: atlasSearch.dataset.toolsAction,
    protocols: atlasSearch.dataset.protocolsAction,
  };
  const placeholders = {
    tools: 'Search tools, functions, platforms…',
    protocols: 'Search protocols, objectives, methods…',
  };

  scopeButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const scope = button.dataset.searchScope;
      if (!actions[scope]) return;
      atlasSearch.action = actions[scope];
      if (input) input.placeholder = placeholders[scope];
      scopeButtons.forEach((item) => {
        const active = item === button;
        item.classList.toggle('active', active);
        item.setAttribute('aria-pressed', String(active));
      });
    });
  });
}
