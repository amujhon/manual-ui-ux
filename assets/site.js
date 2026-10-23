(() => {
  'use strict';
  const root = document.documentElement;
  try { if (localStorage.getItem('manual-uiux-theme') === 'dark') root.dataset.theme = 'dark'; } catch (_) {}
  document.querySelectorAll('.theme-toggle').forEach(button => {
    button.addEventListener('click', () => {
      const dark = root.dataset.theme !== 'dark';
      root.dataset.theme = dark ? 'dark' : 'light';
      try { localStorage.setItem('manual-uiux-theme', dark ? 'dark' : 'light'); } catch (_) {}
    });
  });

  const sidebar = document.getElementById('reader-sidebar');
  const overlay = document.getElementById('nav-overlay');
  const menu = document.querySelector('.mobile-menu');
  const closeMenu = () => {
    sidebar?.classList.remove('open');
    overlay?.classList.remove('visible');
    menu?.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  };
  menu?.addEventListener('click', () => {
    const open = !sidebar?.classList.contains('open');
    sidebar?.classList.toggle('open', open);
    overlay?.classList.toggle('visible', open);
    menu.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
    if(open) sidebar?.querySelector('a')?.focus();
  });
  overlay?.addEventListener('click', closeMenu);
  sidebar?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeMenu(); });

  document.querySelectorAll('button.copy-code').forEach(button => {
    button.addEventListener('click', async () => {
      const code = button.parentElement.querySelector('pre code')?.textContent || '';
      try {
        await navigator.clipboard.writeText(code);
        const previous = button.textContent;
        button.textContent = 'Copiado ✓';
        setTimeout(() => button.textContent = previous, 1600);
      } catch (_) {
        // Clipboard may be denied on file://; fallback with selection.
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(button.parentElement.querySelector('code'));
        selection.removeAllRanges(); selection.addRange(range);
        button.textContent = 'Seleccionado';
      }
    });
  });

  const progressBar = document.getElementById('reading-progress');
  const article = document.querySelector('[data-article]');
  if (progressBar && article) {
    const update = () => {
      const start = article.getBoundingClientRect().top + window.scrollY;
      const end = article.getBoundingClientRect().bottom + window.scrollY - window.innerHeight * .6;
      const p = end > start ? Math.min(1, Math.max(0, (window.scrollY-start)/(end-start))) : 1;
      progressBar.style.width = (p*100).toFixed(2)+'%';
    };
    window.addEventListener('scroll', update, { passive:true });
    window.addEventListener('resize', update);
    update();
    const sections = [...article.querySelectorAll('h2[id],h3[id]')];
    const outline = document.querySelectorAll('.outline-item');
    if ('IntersectionObserver' in window && sections.length) {
      const observer = new IntersectionObserver(entries => {
        for(const entry of entries) if(entry.isIntersecting) {
          outline.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#'+entry.target.id));
        }
      }, {rootMargin:'-110px 0px -68% 0px'});
      sections.forEach(h => observer.observe(h));
    }
  }

  const searchInput = document.getElementById('chapter-search');
  const resultsPanel = document.getElementById('search-results');
  const normalize = text => String(text).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  function runSearch(raw) {
    const query = normalize(raw.trim());
    const cards = [...document.querySelectorAll('.chapter-card')];
    if(!query) {
      cards.forEach(card => card.hidden = false);
      document.querySelectorAll('[data-group]').forEach(group => group.hidden = false);
      if(resultsPanel) { resultsPanel.hidden=true; resultsPanel.replaceChildren(); }
      return;
    }
    cards.forEach(card => {
      card.hidden = !normalize(card.getAttribute('data-title')).includes(query);
    });
    document.querySelectorAll('[data-group]').forEach(group => {
      group.hidden = ![...group.querySelectorAll('.chapter-card')].some(c => !c.hidden);
    });
    if(!resultsPanel) return;
    const hits = (window.MANUAL_SEARCH_INDEX || []).filter(item => normalize(item.title+' '+item.text).includes(query)).slice(0,8);
    resultsPanel.replaceChildren();
    const title = document.createElement('h3');
    title.textContent = hits.length ? `${hits.length} coincidencia(s) en los capítulos publicados` : 'Sin coincidencias en el contenido publicado';
    resultsPanel.appendChild(title);
    hits.forEach(item => {
      const link = document.createElement('a'); link.className = 'search-result'; link.href=item.url;
      const subtitle=document.createElement('span');subtitle.textContent='CAPÍTULO '+String(item.chapter).padStart(2,'0');
      const bold=document.createElement('strong');bold.textContent=item.title;
      const p=document.createElement('p');p.textContent=item.text;
      link.append(subtitle,bold,p);resultsPanel.appendChild(link);
    });
    resultsPanel.hidden = false;
  }
  searchInput?.addEventListener('input',e => runSearch(e.target.value));
  document.addEventListener('keydown', e => {
    if (e.key === '/' && searchInput && !['INPUT','TEXTAREA'].includes(document.activeElement.tagName) && !e.ctrlKey && !e.metaKey) {
      e.preventDefault();searchInput.focus();
    }
  });
})();
