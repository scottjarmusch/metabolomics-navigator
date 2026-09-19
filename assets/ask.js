(() => {
  const input = document.querySelector('#ask-query');
  const searchButton = document.querySelector('#ask-search-button');
  const results = document.querySelector('#ask-strategy-results');
  const cards = [...document.querySelectorAll('.ask-strategy-card')];
  const count = document.querySelector('#ask-result-count');
  const empty = document.querySelector('#ask-empty');
  const examples = [...document.querySelectorAll('[data-ask-example]')];
  if (!input || !cards.length) return;

  const stop = new Set(['a','an','and','are','for','from','i','in','into','my','of','on','the','to','with','have','has','want','need','find','using','use','can','how','what','when','most','is','am','do','me','data','metabolomics']);
  const tokenize = value => [...new Set(value.toLowerCase()
    .replace(/[^a-z0-9]+/g,' ').split(/\s+/)
    .filter(x => x.length > 1 && !stop.has(x))
    .map(x => x.length > 4 && x.endsWith('s') ? x.slice(0,-1) : x))];
  const metadata = new Map(cards.map(card => [card, {
    words: new Set(tokenize(card.dataset.search || '')),
    name: new Set(tokenize(card.dataset.name || '')),
    keywords: new Set(tokenize(card.dataset.keywords || '')),
  }]));
  const weight = token => 1 + Math.log((cards.length+1)/(1+cards.filter(c=>metadata.get(c).words.has(token)).length));
  function scoreCard(card, tokens) {
    const data=metadata.get(card);
    return tokens.reduce((score,token)=>score + (data.words.has(token) ? weight(token)*(1 + (data.name.has(token)?1:0) + (data.keywords.has(token)?1:0)) : 0),0);
  }

  function runSearch(value) {
    const tokens = tokenize(value);
    let eligible=cards;
    const nmrOnly=/\bnmr\b/i.test(value) && !/\b(?:ms|lc-ms|mass spectrometry)\b/i.test(value);
    if(nmrOnly) eligible=[];
    const flux=/\bflux(?:es)?\b/i.test(value);
    if(flux) eligible=eligible.filter(card=>(card.dataset.objectives || '').split(' ').includes('flux_analysis'));
    const generalOnly=tokens.length && tokens.every(t=>['new','compare','treated','untreated','cell','study','experiment','start','begin','research'].includes(t));
    if(generalOnly) eligible=[];
    const ranked = eligible.map(card => ({card, score: scoreCard(card,tokens)}))
      .filter(x => x.score > 0)
      .sort((a,b) => b.score - a.score || Number(b.card.dataset.year||0) - Number(a.card.dataset.year||0));

    cards.forEach(card => card.hidden = true);
    ranked.slice(0,6).forEach(x => {
      results.appendChild(x.card);
      x.card.hidden = false;
    });

    const shown = Math.min(ranked.length,6);
    if (!tokens.length) {
      count.textContent = 'Choose an example or describe your question.';
      empty.hidden = true;
    } else if (shown) {
      count.textContent = shown + (ranked.length > shown ? ` of ${ranked.length}` : '') + ' matching published Strateg' + (shown === 1 ? 'y' : 'ies') + '.';
      empty.hidden = true;
    } else {
      count.textContent = nmrOnly ? 'Navigator covers MS-based metabolomics; NMR-only workflows are outside scope.' : flux && !eligible.length ? 'No curated flux-analysis Strategy is available yet. Isotope networking is not a substitute for flux inference.' : generalOnly ? 'Please add your scientific aim or measurement type so we can identify a published Strategy.' : 'No matching published Strategy in the current collection.';
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
