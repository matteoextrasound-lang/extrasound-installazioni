/* Extrasound Custom — animazioni comuni */
(function(){
  var doc = document.documentElement;
  doc.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Header compatto dopo lo scorrimento */
  var header = document.querySelector('.site-header');
  function onScroll(){ header.classList.toggle('scrolled', window.scrollY > 30); }
  window.addEventListener('scroll', onScroll, {passive:true}); onScroll();

  /* Menu su telefono */
  var toggle = document.querySelector('.menu-toggle');
  var menu = document.getElementById('menu');
  if (toggle && menu){
    toggle.addEventListener('click', function(){
      var open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', open);
      toggle.setAttribute('aria-label', open ? 'Chiudi il menu' : 'Apri il menu');
      menu.classList.toggle('open', open);
    });
    menu.addEventListener('click', function(e){
      if (e.target.tagName === 'A'){ toggle.setAttribute('aria-expanded','false'); menu.classList.remove('open'); }
    });
  }

  /* Menu a tendina Prodotti: si apre al passaggio del mouse (CSS) o con un clic/tocco */
  document.querySelectorAll('.has-sub').forEach(function(item){
    var btn = item.querySelector('.sub-toggle');
    function set(open){ item.classList.toggle('open', open); btn.setAttribute('aria-expanded', open); }
    btn.addEventListener('click', function(e){ e.stopPropagation(); set(!item.classList.contains('open')); });
    document.addEventListener('click', function(e){ if (!item.contains(e.target)) set(false); });
    item.addEventListener('keydown', function(e){ if (e.key === 'Escape'){ set(false); btn.focus(); } });
  });


  /* Sezioni: il prodotto scivola dentro quando la sezione entra nello schermo */
  var features = document.querySelectorAll('.feature');
  features.forEach(function(f){
    var media = f.querySelector('.feature-media');
    media.addEventListener('transitionend', function(e){
      if (e.propertyName === 'transform' && f.classList.contains('in')) f.classList.add('landed');
    });
  });
  if (reduce || !('IntersectionObserver' in window)){
    features.forEach(function(f){ f.classList.add('in','landed'); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, {threshold:0.25});
    features.forEach(function(f){ io.observe(f); });
  }

  /* Filtri degli elenchi prodotti */
  document.querySelectorAll('.filters').forEach(function(box){
    var grid = document.querySelector(box.dataset.target), count = box.querySelector('.count span');
    var state = {cat:'*', brand:'*', linea:'*'};
    function apply(){
      var n = 0;
      grid.querySelectorAll('.pcard').forEach(function(c){
        var ok = (state.cat === '*' || c.dataset.cat.indexOf(state.cat) > -1) &&
                 (state.brand === '*' || c.dataset.brand === state.brand) &&
                 (state.linea === '*' || (c.dataset.linea || '').indexOf(state.linea) > -1);
        c.hidden = !ok; if (ok){ n++; c.classList.add('in'); }
      });
      count.textContent = n;
    }
    function pick(f, v){
      var b = box.querySelector('.chip[data-f="'+f+'"][data-v="'+v+'"]'); if (!b) return;
      state[f] = v;
      box.querySelectorAll('.chip[data-f="'+f+'"]').forEach(function(x){ x.classList.toggle('is-on', x === b); });
    }
    box.addEventListener('click', function(e){
      var b = e.target.closest('.chip'); if (!b) return;
      pick(b.dataset.f, b.dataset.v); apply();
    });
    /* preselezione da indirizzo: pagina.html#linea=V oppure #cat=E */
    function fromHash(){
      var h = decodeURIComponent(location.hash.slice(1)); if (h.indexOf('=') < 0) return;
      Object.keys(state).forEach(function(k){ pick(k, '*'); });
      h.split('&').forEach(function(kv){ var p = kv.split('='); if (p.length === 2 && p[0] in state) pick(p[0], p[1]); });
      apply();
    }
    fromHash(); window.addEventListener('hashchange', fromHash);
  });

  /* Comparsa degli elementi .reveal (schede prodotto) */
  var reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)){
    reveals.forEach(function(el){ el.classList.add('in'); });
  } else {
    var ro = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if (en.isIntersecting){ en.target.classList.add('in'); ro.unobserve(en.target); } });
    }, {threshold:0.15});
    reveals.forEach(function(el){ ro.observe(el); });
  }

  /* Leggero effetto profondità sul prodotto con il mouse */
  if (!reduce && window.matchMedia('(pointer:fine)').matches){
    features.forEach(function(f){
      var img = f.querySelector('.product');
      f.addEventListener('mousemove', function(e){
        if (!f.classList.contains('landed')) return;
        var r = f.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        img.style.translate = (x * 18).toFixed(1) + 'px ' + (y * 18).toFixed(1) + 'px';
      });
      f.addEventListener('mouseleave', function(){ img.style.translate = ''; });
    });
  }

  /* Sfondo: onde sonore che scorrono */
  var c = document.querySelector('.bg-waves');
  if (!c || reduce) return;
  var ctx = c.getContext('2d'), w, h, dpr = Math.min(window.devicePixelRatio || 1, 2), t = 0, scrollY = 0;
  function size(){ w = c.clientWidth; h = c.clientHeight; c.width = w * dpr; c.height = h * dpr; ctx.setTransform(dpr,0,0,dpr,0,0); }
  size(); window.addEventListener('resize', size);
  window.addEventListener('scroll', function(){ scrollY = window.scrollY; }, {passive:true});
  var lines = [
    {amp:38, freq:.0062, speed:.010, y:.30, color:'rgba(227,23,31,.55)', width:1.4},
    {amp:26, freq:.0090, speed:.016, y:.34, color:'rgba(227,23,31,.25)', width:1},
    {amp:52, freq:.0042, speed:.007, y:.72, color:'rgba(255,255,255,.10)', width:1},
    {amp:30, freq:.0075, speed:.012, y:.76, color:'rgba(227,23,31,.22)', width:1}
  ];
  function draw(){
    ctx.clearRect(0,0,w,h);
    var shift = scrollY * .15;
    lines.forEach(function(l, i){
      ctx.beginPath();
      for (var x = 0; x <= w; x += 6){
        var env = Math.sin((x / w) * Math.PI);
        var y = h * l.y - shift * (i % 2 ? .6 : 1) % h
          + Math.sin(x * l.freq + t * l.speed * 60) * l.amp * env
          + Math.sin(x * l.freq * 2.3 - t * l.speed * 40) * l.amp * .35 * env;
        x ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
      }
      ctx.strokeStyle = l.color; ctx.lineWidth = l.width; ctx.stroke();
    });
    t += 1 / 60;
    requestAnimationFrame(draw);
  }
  document.addEventListener('visibilitychange', function(){ if (!document.hidden) size(); });
  requestAnimationFrame(draw);
})();

/* ===== Lista prodotti (B2B) =====
   La lista resta nel browser di chi la compila (localStorage, se disponibile).
   "Richiedi preventivo" porta a richiesta.html, dove si inviano lista e dati aziendali. */
(function(){
  var KEY = 'esb2b-lista', mem = [];
  function load(){ try { var v = JSON.parse(localStorage.getItem(KEY) || '[]'); return Array.isArray(v) ? v : []; } catch(e){ return mem; } }
  function save(l){ mem = l; try { localStorage.setItem(KEY, JSON.stringify(l)); } catch(e){} render(); }
  function esc(s){ return String(s).replace(/[&<>"']/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
  function totale(l){ return l.reduce(function(n, x){ return n + x.qty; }, 0); }
  window.ESLista = {
    get: load,
    set: function(slug, qty){ var l = load(); l.forEach(function(x){ if (x.slug === slug) x.qty = Math.max(1, Math.min(999, qty | 0 || 1)); }); save(l); },
    remove: function(slug){ save(load().filter(function(x){ return x.slug !== slug; })); },
    clear: function(){ save([]); },
    onchange: []
  };

  /* finestrella in basso a destra (non su richiesta.html, dove la lista è nella pagina) */
  var inPagina = !!document.getElementById('richiesta');
  var dock = null, panel, items, nEl, toast;
  if (!inPagina){
    dock = document.createElement('aside');
    dock.className = 'lista-dock';
    dock.setAttribute('aria-label', 'Lista prodotti');
    dock.innerHTML =
      '<div class="lista-panel" id="lista-panel" hidden>' +
        '<div class="lista-head"><b>La tua lista</b><button type="button" class="lista-x" aria-label="Chiudi la lista">&times;</button></div>' +
        '<ul class="lista-items"></ul>' +
        '<p class="lista-empty">Nessun prodotto. Apri una scheda o un elenco e premi <em>Aggiungi alla lista</em>.</p>' +
        '<div class="lista-foot"><a class="btn lista-go" href="richiesta.html">Richiedi preventivo</a><button type="button" class="lista-clear">Svuota</button></div>' +
      '</div>' +
      '<p class="lista-toast" role="status" aria-live="polite"></p>' +
      '<button type="button" class="lista-toggle" aria-expanded="false" aria-controls="lista-panel">' +
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/></svg>' +
        '<span>Lista</span><span class="lista-n">0</span></button>';
    document.body.appendChild(dock);
    panel = dock.querySelector('.lista-panel'); items = dock.querySelector('.lista-items');
    nEl = dock.querySelector('.lista-n'); toast = dock.querySelector('.lista-toast');
    var tg = dock.querySelector('.lista-toggle');
    function apri(on){ panel.hidden = !on; tg.setAttribute('aria-expanded', on); dock.classList.toggle('is-open', on);
      try { sessionStorage.setItem(KEY + '-open', on ? '1' : ''); } catch(e){} }
    tg.addEventListener('click', function(){ apri(panel.hidden); });
    dock.querySelector('.lista-x').addEventListener('click', function(){ apri(false); });
    dock.querySelector('.lista-clear').addEventListener('click', function(){ window.ESLista.clear(); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && !panel.hidden) apri(false); });
    try { if (sessionStorage.getItem(KEY + '-open') && load().length) apri(true); } catch(e){}
  }

  /* riga modificabile: usata sia nella finestrella sia in richiesta.html */
  function riga(x){
    return '<li data-slug="' + esc(x.slug) + '">' +
      '<a class="li-img" href="scheda-' + esc(x.slug) + '.html"><img src="' + esc(x.img || '') + '" alt="" loading="lazy"></a>' +
      '<a class="li-t" href="scheda-' + esc(x.slug) + '.html"><small>' + esc(x.brand) + '</small>' + esc(x.model) + '</a>' +
      '<span class="li-q"><button type="button" data-q="-1" aria-label="Diminuisci">&minus;</button>' +
      '<input type="number" min="1" max="999" value="' + x.qty + '" aria-label="Quantità ' + esc(x.brand + ' ' + x.model) + '">' +
      '<button type="button" data-q="1" aria-label="Aumenta">+</button></span>' +
      '<button type="button" class="li-rm" aria-label="Togli ' + esc(x.brand + ' ' + x.model) + ' dalla lista">&times;</button></li>';
  }
  function collega(ul){
    ul.addEventListener('click', function(e){
      var li = e.target.closest('li'); if (!li) return;
      var s = li.dataset.slug, b = e.target.closest('button'); if (!b) return;
      if (b.classList.contains('li-rm')) return window.ESLista.remove(s);
      if (b.dataset.q){ var inp = li.querySelector('input'); window.ESLista.set(s, (+inp.value || 1) + (+b.dataset.q)); }
    });
    ul.addEventListener('change', function(e){
      var li = e.target.closest('li'); if (li && e.target.tagName === 'INPUT') window.ESLista.set(li.dataset.slug, +e.target.value);
    });
  }
  window.ESLista.riga = riga; window.ESLista.collega = collega;
  if (items) collega(items);

  function render(){
    var l = load();
    if (dock){
      items.innerHTML = l.map(riga).join('');
      nEl.textContent = totale(l);
      dock.classList.toggle('is-empty', !l.length);
      dock.querySelector('.lista-go').classList.toggle('is-off', !l.length);
    }
    document.querySelectorAll('[data-add]').forEach(function(b){
      var x = l.filter(function(y){ return y.slug === b.dataset.slug; })[0];
      b.classList.toggle('is-in', !!x);
      b.textContent = x ? 'In lista (' + x.qty + ') · aggiungi' : 'Aggiungi alla lista';
    });
    window.ESLista.onchange.forEach(function(f){ f(l); });
  }

  var tt;
  function avvisa(t){
    if (!dock) return;
    toast.textContent = t;
    dock.classList.remove('bump'); void dock.offsetWidth; dock.classList.add('bump', 'has-toast');
    clearTimeout(tt); tt = setTimeout(function(){ dock.classList.remove('has-toast'); }, 2400);
  }
  /* impianti tipo: aggiunge tutti i prodotti con le quantità indicate */
  document.addEventListener('click', function(e){
    var b = e.target.closest('[data-add-set]'); if (!b) return;
    var set; try { set = JSON.parse(b.dataset.addSet); } catch(err){ return; }
    var l = load();
    set.forEach(function(s){
      var x = l.filter(function(y){ return y.slug === s.slug; })[0];
      if (x) x.qty = Math.min(999, x.qty + s.qty); else l.push(s);
    });
    save(l);
    avvisa('Aggiunti ' + set.length + ' prodotti dell\u2019impianto');
  });
  document.addEventListener('click', function(e){
    var b = e.target.closest('[data-add]'); if (!b) return;
    e.preventDefault();
    var l = load(), x = l.filter(function(y){ return y.slug === b.dataset.slug; })[0];
    if (x) x.qty = Math.min(999, x.qty + 1);
    else l.push({slug: b.dataset.slug, brand: b.dataset.brand, model: b.dataset.model, img: b.dataset.img, qty: 1});
    save(l);
    avvisa('Aggiunto: ' + b.dataset.brand + ' ' + b.dataset.model);
  });
  window.addEventListener('storage', function(e){ if (e.key === KEY) render(); });
  render();
})();

/* ===== Immagini delle schede apribili a schermo intero ===== */
(function(){
  var SEL = '.sheet-visual img, .views img, .rear img, .gui img, .acc > img, .sheet-page figure img';
  var imgs = Array.prototype.slice.call(document.querySelectorAll(SEL)).filter(function(i){ return !i.closest('a'); });
  if (!imgs.length) return;
  var lb = document.createElement('div');
  lb.className = 'lb'; lb.hidden = true;
  lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Immagine ingrandita');
  lb.innerHTML = '<span class="lb-n"></span><img class="lb-img" alt=""><p class="lb-cap"></p>' +
    '<button type="button" class="lb-prev" aria-label="Immagine precedente">&#8249;</button>' +
    '<button type="button" class="lb-next" aria-label="Immagine successiva">&#8250;</button>' +
    '<button type="button" class="lb-x" aria-label="Chiudi">&times;</button>';
  document.body.appendChild(lb);
  var big = lb.querySelector('.lb-img'), cap = lb.querySelector('.lb-cap'), num = lb.querySelector('.lb-n'), cur = 0, last = null;
  function didascalia(i){
    var f = i.closest('figure'), c = f && f.querySelector('figcaption');
    return c ? c.textContent.trim() : (i.alt || '');
  }
  function mostra(n){
    cur = (n + imgs.length) % imgs.length;
    var i = imgs[cur];
    big.src = i.currentSrc || i.src; big.alt = i.alt || '';
    cap.textContent = didascalia(i);
    num.textContent = imgs.length > 1 ? (cur + 1) + ' / ' + imgs.length : '';
    lb.querySelector('.lb-prev').hidden = lb.querySelector('.lb-next').hidden = imgs.length < 2;
  }
  function apri(n){ last = document.activeElement; mostra(n); lb.hidden = false; document.documentElement.style.overflow = 'hidden'; lb.querySelector('.lb-x').focus(); }
  function chiudi(){ lb.hidden = true; document.documentElement.style.overflow = ''; if (last) last.focus(); }
  imgs.forEach(function(i, n){
    i.classList.add('zoomable'); i.setAttribute('tabindex', '0'); i.setAttribute('role', 'button');
    i.setAttribute('aria-label', 'Ingrandisci: ' + (i.alt || 'immagine'));
    var p = i.parentElement;
    if (p && (p.tagName === 'FIGURE' || p.classList.contains('sheet-visual'))) p.classList.add('zoom-hint');
    i.addEventListener('click', function(){ apri(n); });
    i.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); apri(n); } });
  });
  lb.querySelector('.lb-x').addEventListener('click', chiudi);
  lb.querySelector('.lb-prev').addEventListener('click', function(){ mostra(cur - 1); });
  lb.querySelector('.lb-next').addEventListener('click', function(){ mostra(cur + 1); });
  big.addEventListener('click', chiudi);
  lb.addEventListener('click', function(e){ if (e.target === lb) chiudi(); });
  document.addEventListener('keydown', function(e){
    if (lb.hidden) return;
    if (e.key === 'Escape') chiudi();
    else if (e.key === 'ArrowLeft') mostra(cur - 1);
    else if (e.key === 'ArrowRight') mostra(cur + 1);
  });
  /* scorrimento col dito sul telefono */
  var x0 = null;
  lb.addEventListener('touchstart', function(e){ x0 = e.touches[0].clientX; }, {passive: true});
  lb.addEventListener('touchend', function(e){
    if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
    if (Math.abs(dx) > 50) mostra(cur + (dx < 0 ? 1 : -1));
  });
})();
