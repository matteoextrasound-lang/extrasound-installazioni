/* Extrasound B2B — invio della lista con i dati aziendali (richiesta.html)
   Invia a un endpoint REST su extrasound.it. Se l'invio non riesce, propone
   un'email precompilata a info@extrasound.it con lo stesso contenuto. */
(function(){
  var ENDPOINT = 'https://www.extrasound.it/wp-json/extrasound-b2b/v1/richiesta';
  var EMAIL = 'info@extrasound.it';
  var L = window.ESLista; if (!L) return;
  var form = document.getElementById('req-form'), ul = document.getElementById('riepilogo');
  var vuota = document.getElementById('vuota'), tot = document.getElementById('req-tot');
  var msg = document.getElementById('req-msg'), altro = document.getElementById('req-altro');
  var btn = form.querySelector('button[type=submit]');

  function render(l){
    ul.innerHTML = l.map(L.riga).join('');
    vuota.hidden = !!l.length;
    var n = l.reduce(function(a, x){ return a + x.qty; }, 0);
    tot.textContent = l.length ? l.length + (l.length === 1 ? ' prodotto' : ' prodotti') + ' · ' + n + (n === 1 ? ' pezzo' : ' pezzi') : '';
    btn.disabled = !l.length;
  }
  L.collega(ul); L.onchange.push(render); render(L.get());

  form.addEventListener('change', function(e){
    if (e.target.name === 'consegna'){
      altro.hidden = e.target.value.indexOf('altro') < 0;
      altro.querySelector('textarea').required = !altro.hidden;
    }
  });

  function dati(){
    var d = {}; new FormData(form).forEach(function(v, k){ d[k] = typeof v === 'string' ? v.trim() : v; });
    return d;
  }
  function testo(d, l){
    var r = ['RICHIESTA PREVENTIVO B2B', '',
      'Ragione sociale: ' + d.ragione_sociale, 'P. IVA: ' + d.piva + (d.cf ? '  ·  C.F.: ' + d.cf : ''),
      'SDI: ' + (d.sdi || '-') + '  ·  PEC: ' + (d.pec || '-'),
      'Sede legale: ' + d.indirizzo + ', ' + d.cap + ' ' + d.citta + ' (' + d.provincia + ')', '',
      'Referente: ' + d.referente, 'Email: ' + d.email, 'Telefono: ' + d.telefono, '',
      'Consegna: ' + d.consegna + (d.indirizzo_consegna ? ' — ' + d.indirizzo_consegna : '')];
    if (d.riferimento) r.push('Riferimento: ' + d.riferimento);
    if (d.note) r.push('Note: ' + d.note);
    r.push('', 'PRODOTTI');
    l.forEach(function(x){ r.push(x.qty + ' x ' + x.brand + ' ' + x.model); });
    return r.join('\n');
  }
  function errore(t){ msg.hidden = false; msg.className = 'req-msg err'; msg.textContent = t; msg.scrollIntoView({block:'nearest', behavior:'smooth'}); }

  form.addEventListener('submit', function(e){
    e.preventDefault();
    var l = L.get();
    if (!l.length) return errore('La lista è vuota: aggiungi almeno un prodotto.');
    if (!form.checkValidity()){ form.reportValidity(); return; }
    var d = dati();
    if (!d.sdi && !d.pec){ errore('Inserisci il codice destinatario SDI oppure la PEC.'); form.elements.sdi.focus(); return; }
    if (!/^(IT)?\s?\d{11}$/i.test(d.piva.replace(/\s/g, ''))){ errore('Controlla la partita IVA: 11 cifre, con o senza "IT".'); form.elements.piva.focus(); return; }

    btn.disabled = true; btn.textContent = 'Invio in corso…'; msg.hidden = true;
    var body = new URLSearchParams();
    Object.keys(d).forEach(function(k){ body.append(k, d[k]); });
    body.append('prodotti', JSON.stringify(l.map(function(x){ return {slug: x.slug, brand: x.brand, model: x.model, qty: x.qty}; })));
    body.append('pagina', location.href);

    fetch(ENDPOINT, {method: 'POST', body: body})
      .then(function(r){ return r.json().then(function(j){ if (!r.ok || !j.ok) throw new Error(j.message || 'errore'); return j; }); })
      .then(function(j){
        L.clear(); form.reset(); altro.hidden = true;
        msg.hidden = false; msg.className = 'req-msg ok';
        msg.innerHTML = '<strong>Richiesta inviata' + (j.numero ? ' (n. ' + j.numero + ')' : '') + '.</strong> Ti abbiamo mandato una copia a ' +
          d.email.replace(/[<>&]/g, '') + '. Ti rispondiamo con il preventivo.';
        msg.scrollIntoView({block:'nearest', behavior:'smooth'});
        btn.textContent = 'Inviata';
      })
      .catch(function(){
        var t = testo(d, l);
        var mail = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Richiesta preventivo B2B · ' + d.ragione_sociale) + '&body=' + encodeURIComponent(t);
        msg.hidden = false; msg.className = 'req-msg err';
        msg.innerHTML = '<strong>Invio non riuscito.</strong> Puoi mandarci la stessa richiesta via email: ' +
          '<a href="' + mail + '">apri l’email già compilata</a> oppure copia il testo qui sotto e invialo a ' +
          '<a href="mailto:' + EMAIL + '">' + EMAIL + '</a>.<pre></pre>';
        msg.querySelector('pre').textContent = t;
        btn.disabled = false; btn.textContent = 'Riprova l’invio';
      });
  });
})();
