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
    var state = {cat:'*', brand:'*'};
    function apply(){
      var n = 0;
      grid.querySelectorAll('.pcard').forEach(function(c){
        var ok = (state.cat === '*' || c.dataset.cat.indexOf(state.cat) > -1) && (state.brand === '*' || c.dataset.brand === state.brand);
        c.hidden = !ok; if (ok){ n++; c.classList.add('in'); }
      });
      count.textContent = n;
    }
    box.addEventListener('click', function(e){
      var b = e.target.closest('.chip'); if (!b) return;
      state[b.dataset.f] = b.dataset.v;
      box.querySelectorAll('.chip[data-f="'+b.dataset.f+'"]').forEach(function(x){ x.classList.toggle('is-on', x === b); });
      apply();
    });
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
