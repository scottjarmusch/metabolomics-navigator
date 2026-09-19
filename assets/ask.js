(() => {
  const input = document.querySelector('#ask-query');
  const searchButton = document.querySelector('#ask-search-button');
  const cards = [...document.querySelectorAll('.ask-strategy-card')];
  const count = document.querySelector('#ask-result-count');
  const empty = document.querySelector('#ask-empty');
  const examples = [...document.querySelectorAll('[data-ask-example]')];
  if (!input || !cards.length) return;

  const stop = new Set(['a','an','and','are','for','from','i','in','into','my','of','on','the','to','with']);
  const tokenize = value => value.toLowerCase()
    .replace(/[^a-z0-9+/-]+/g,' ')
    .split(/\s+/).filter(x => x.length > 1 && !stop.has(x));

  function scoreCard(card, tokens) {
    const hay = (card.dataset.search || '').toLowerCase();
    const name = (card.dataset.name || '').toLowerCase();
    if (!tokens.length) return 0;
    let score = 0;
    for (const token of tokens) {
      if (name.includes(token)) score += 4;
      if (hay.includes(token)) score += 1;
    }
    return score;
  }

  function runSearch(value) {
    const tokens = tokenize(value);
    const ranked = cards.map(card => ({card, score: scoreCard(card,tokens)}))
      .filter(x => x.score > 0)
      .sort((a,b) => b.score - a.score || Number(b.card.dataset.year||0) - Number(a.card.dataset.year||0));

    cards.forEach(card => card.hidden = true);
    ranked.slice(0,6).forEach(x => x.card.hidden = false);

    const shown = Math.min(ranked.length,6);
    if (!tokens.length) {
      count.textContent = 'Choose an example or describe your question.';
      empty.hidden = true;
    } else if (shown) {
      count.textContent = shown + (ranked.length > shown ? ` of ${ranked.length}` : '') + ' matching published Strateg' + (shown === 1 ? 'y' : 'ies') + '.';
      empty.hidden = true;
    } else {
      count.textContent = 'No matching published Strategy in the current collection.';
      empty.hidden = false;
    }
  }

  searchButton?.addEventListener('click', () => runSearch(input.value));
  input.addEventListener('keydown', event => {
    if (event.key === 'Enter') { event.preventDefault(); runSearch(input.value); }
  });
  examples.forEach(button => button.addEventListener('click', () => {
    input.value = button.dataset.askExample || button.textContent.trim();
    runSearch(input.value);
    input.focus();
  }));
})();
