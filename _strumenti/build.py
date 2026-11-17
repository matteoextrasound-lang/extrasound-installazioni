#!/usr/bin/env python3
"""Inserisce header e footer comuni in tutte le pagine del sito.

Uso:  python3 _strumenti/build.py
Ogni pagina contiene i segnaposto <!-- HEADER -->…<!-- /HEADER --> e
<!-- FOOTER -->…<!-- /FOOTER -->: il contenuto tra i segnaposto viene rigenerato.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEDE = sorted(p.name for p in ROOT.glob("scheda-*.html"))   # schede prodotto generate da genera_schede.py
PAGES = ["index.html", "amplificatori.html", "diffusori.html", "esterno.html", "home-cinema.html", "impianti.html", "contatti.html"] + SCHEDE
PRODOTTI = ["amplificatori.html", "diffusori.html", "esterno.html", "home-cinema.html"] + SCHEDE

GRUNGE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <filter id="grunge" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="1.4 0.09" numOctaves="2" seed="7" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.7 1.95" result="mask"/>
    <feComposite in="SourceGraphic" in2="mask" operator="in"/>
  </filter>
</svg>'''

def cur(page, target):
    return ' aria-current="page"' if page == target else ''

def header(page):
    in_prod = page in PRODOTTI
    return f'''{GRUNGE}
<canvas class="bg-waves" aria-hidden="true"></canvas>
<header class="site-header">
  <a class="logo" href="index.html" aria-label="Extrasound Custom, home">
    <span class="logo-red">EXTRASOUND</span><span class="logo-white">CUSTOM</span>
  </a>
  <button class="menu-toggle" aria-expanded="false" aria-controls="menu" aria-label="Apri il menu"><span></span><span></span></button>
  <nav id="menu" class="main-menu" aria-label="Menu principale">
    <div class="has-sub{' is-current' if in_prod else ''}">
      <button class="sub-toggle" aria-expanded="false" aria-controls="sub-prodotti">Prodotti<svg viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1.5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>
      <div class="submenu" id="sub-prodotti">
        <a href="amplificatori.html"{cur(page, "amplificatori.html")}>Amplificatori</a>
        <a href="diffusori.html"{cur(page, "diffusori.html")}>Diffusori</a>
        <a href="esterno.html"{cur(page, "esterno.html")}>Da esterno</a>
        <a href="home-cinema.html"{cur(page, "home-cinema.html")}>Home cinema</a>
      </div>
    </div>
    <a href="impianti.html" class="menu-link"{cur(page, "impianti.html")}>Impianti tipo</a>
    <a href="contatti.html" class="menu-cta"{cur(page, "contatti.html")}>Contattaci</a>
  </nav>
</header>'''

FOOTER = '''<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-col footer-brand">
      <a class="logo logo-sm" href="index.html" aria-label="Extrasound Custom, home"><span class="logo-red">EXTRASOUND</span><span class="logo-white">CUSTOM</span></a>
      <p>Progetto, fornitura e installazione di impianti hi-fi, multiroom e home cinema su misura, a cura di Extrasound.</p>
      <a class="btn btn-sm" href="contatti.html">Richiedi un preventivo</a>
    </div>
    <div class="footer-col">
      <p class="footer-head">Contatti</p>
      <p>Via Archimede, 605<br>47521 Cesena (FC) – Italia</p>
      <p>Tel. <a href="tel:+390547645626">+39 0547 645626</a><br><a href="mailto:info@extrasound.it">info@extrasound.it</a></p>
    </div>
    <div class="footer-col">
      <p class="footer-head">Prodotti</p>
      <p><a href="amplificatori.html">Amplificatori</a><br><a href="diffusori.html">Diffusori</a><br><a href="esterno.html">Da esterno</a><br><a href="home-cinema.html">Home cinema</a><br><a href="impianti.html">Impianti tipo</a></p>
      <p class="footer-head">Negozio</p>
      <p><a href="https://www.extrasound.it" target="_blank" rel="noopener">extrasound.it</a></p>
    </div>
  </div>
  <div class="footer-legal">
    <p><strong>EXTRASOUND Srl</strong> · Via Archimede, 605 · 47521 Cesena (FC) · Partita IVA IT04436860409 · CCIAA Forlì-Cesena REA FO411761 · Capitale sociale € 3.900,00 i.v.</p>
    <p><a href="https://www.extrasound.it/privacy-policy" target="_blank" rel="noopener">Privacy policy</a> · <a href="https://www.extrasound.it/utilizzo-dei-cookies" target="_blank" rel="noopener">Utilizzo dei cookies</a> · <a href="https://www.extrasound.it/condizioni-generali" target="_blank" rel="noopener">Condizioni generali</a></p>
  </div>
</footer>'''

def replace(html, name, content):
    pat = re.compile(rf'<!-- {name} -->.*?<!-- /{name} -->', re.S)
    assert pat.search(html), f"segnaposto {name} mancante"
    return pat.sub(lambda m: f'<!-- {name} -->\n{content}\n<!-- /{name} -->', html)

for p in PAGES:
    f = ROOT / p
    html = f.read_text(encoding="utf-8")
    html = replace(html, "HEADER", header(p))
    html = replace(html, "FOOTER", FOOTER)
    f.write_text(html, encoding="utf-8")
    print("ok", p)
