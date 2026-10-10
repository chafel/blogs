(() => {
  'use strict';
  const search = document.querySelector('#knowledge-search');
  const articlesOnly = document.querySelector('#articles-only');
  const buttons = [...document.querySelectorAll('.type-filter')];
  const sections = [...document.querySelectorAll('.knowledge-section')];
  const links = [...document.querySelectorAll('.category-link')];
  const cards = [...document.querySelectorAll('.entry-card')];
  const resultCount = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  if (!search) return;
  let selectedType = '';
  const normalize = value => value.normalize('NFKC').toLocaleLowerCase().trim();
  const searchable = new Map(cards.map(card => [card, normalize(card.dataset.search)]));
  const total = cards.length;

  function setActive(id) {
    links.forEach(link => {
      const active = link.hash === `#${id}`;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
  }

  function filter() {
    const terms = normalize(search.value).split(/\s+/).filter(Boolean);
    let matches = 0;
    cards.forEach(card => {
      const show = (!selectedType || card.dataset.type === selectedType)
        && (!articlesOnly.checked || card.dataset.published === 'true')
        && terms.every(term => searchable.get(card).includes(term));
      card.hidden = !show;
      if (show) matches += 1;
    });
    sections.forEach(section => {
      const count = section.querySelectorAll('.entry-card:not([hidden])').length;
      section.hidden = count === 0;
      section.querySelector('.section-count').textContent = count;
      const link = links.find(item => item.dataset.category === section.id);
      if (link) link.querySelector('.category-count').textContent = count;
    });
    buttons.forEach(button => {
      const selected = button.dataset.type === selectedType;
      button.classList.toggle('selected', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    const filtering = terms.length || selectedType || articlesOnly.checked;
    resultCount.textContent = filtering ? `找到 ${matches} 个条目 / 共 ${total} 个` : `共 ${total} 个条目`;
    empty.hidden = matches !== 0;
    setActive('directory');
  }

  function reset() {
    search.value = '';
    selectedType = '';
    articlesOnly.checked = false;
    filter();
  }

  search.addEventListener('input', filter);
  articlesOnly.addEventListener('change', filter);
  buttons.forEach(button => button.addEventListener('click', () => {
    selectedType = button.dataset.type;
    filter();
  }));
  document.querySelector('#reset-filters').addEventListener('click', () => {
    reset();
    search.focus();
  });
  links.forEach(link => link.addEventListener('click', () => {
    const id = link.hash.slice(1);
    // A category with no current matches still remains reachable from the index.
    if (id === 'directory' || document.getElementById(id)?.hidden) reset();
    setActive(id);
  }));
  document.addEventListener('keydown', event => {
    const typing = /INPUT|TEXTAREA|SELECT/.test(event.target.tagName) || event.target.isContentEditable;
    if (event.key === '/' && !typing && !event.metaKey && !event.ctrlKey && !event.altKey) {
      event.preventDefault();
      search.focus();
    }
    if (event.key === 'Escape' && document.activeElement === search) {
      reset();
      search.focus();
    }
  });

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting && !entry.target.hidden);
      if (visible.length) setActive(visible[0].target.id);
    }, {rootMargin: '-90px 0px -65% 0px', threshold: 0});
    sections.forEach(section => observer.observe(section));
  }
  // Browser history and item deep links should never point into a hidden result.
  window.addEventListener('hashchange', () => {
    const target = document.getElementById(location.hash.slice(1));
    if (target && (target.hidden || target.closest('[hidden]'))) {
      reset();
      target.scrollIntoView();
    }
  });
  document.querySelector('.search-tools').hidden = false;
})();
