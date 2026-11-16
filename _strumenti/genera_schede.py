#!/usr/bin/env python3
"""Genera le schede prodotto e gli elenchi Amplificatori / Diffusori.

Uso:  python3 _strumenti/genera_schede.py && python3 _strumenti/build.py

Ogni prodotto è un file JSON in _dati/prodotti/<slug>.json (struttura descritta
in _strumenti/MANUTENZIONE.md). Da ognuno nasce scheda-<slug>.html; gli elenchi
amplificatori.html e diffusori.html vengono aggiornati tra i segnaposto
<!-- LISTA --> e <!-- /LISTA -->.
"""
import json, pathlib, re, html
from jinja2 import Environment, FileSystemLoader

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATI = ROOT / "_dati" / "prodotti"
V = "13"  # versione di css/js

SOTTO = {  # sottocategorie: codice -> etichetta
    "M": "Amplificatori multicanale", "P": "Da incasso a parete", "S": "Da incasso a soffitto",
    "L": "LCR per home cinema", "2": "Stereo 2+2 vie", "W": "Subwoofer da incasso", "A": "Amplificati",
}

esc = lambda s: html.escape(str(s), quote=True)


# ---------- disegni SVG ----------
def disegno(m):
    """Disegno quotato: frontale (rettangolare o tondo) + vista laterale."""
    tondo = m.get("forma") == "tondo"
    q = []  # elementi SVG
    if tondo:
        q.append('<circle cx="126" cy="169" r="118" class="frame"/>')
        q.append('<circle cx="126" cy="169" r="104" class="cut"/>')
        q.append('<circle cx="126" cy="169" r="62" class="drv"/><circle cx="126" cy="169" r="20" class="drv-in"/>')
        if m.get("est"): q.append(f'<path d="M8 330H244M8 324v12M244 324v12" class="q"/><text x="126" y="350" class="qt">Ø {esc(m["est"])}</text>')
        q.append(f'<path d="M22 22H230M22 16v12M230 16v12" class="q q-red"/><text x="126" y="14" class="qt qt-red">foro Ø {esc(m["foro"])}</text>')
        top, bot = 51, 287
    else:
        l, a = m.get("est") or ["", ""], m["foro"]
        orizz = m.get("orizzontale", False)
        if orizz:  # LCR orizzontali
            q.append('<rect x="10" y="110" width="232" height="118" rx="4" class="frame"/>')
            q.append('<rect x="20" y="120" width="212" height="98" class="cut"/>')
            for cx in (60, 126, 192):
                q.append(f'<circle cx="{cx}" cy="169" r="{30 if cx != 126 else 16}" class="drv"/>')
            if l[0]: q.append(f'<path d="M10 260H242M10 254v12M242 254v12" class="q"/><text x="126" y="280" class="qt">{esc(l[0])}</text>')
            q.append(f'<path d="M20 92H232M20 86v12M232 86v12" class="q q-red"/><text x="126" y="82" class="qt qt-red">foro {esc(a[0])}</text>')
            if l[0]: q.append(f'<path d="M0 110V228" class="q"/><text x="-2" y="169" class="qt" transform="rotate(-90 -2 169)">{esc(l[1])}</text>')
            q.append(f'<path d="M252 120V218M246 120h12M246 218h12" class="q q-red"/><text x="268" y="169" class="qt qt-red" transform="rotate(-90 268 169)">foro {esc(a[1])}</text>')
            top, bot = 120, 218
        else:
            q.append('<rect x="40" y="40" width="172" height="258" rx="4" class="frame"/>')
            q.append('<rect x="51" y="51" width="150" height="236" class="cut"/>')
            q.append('<circle cx="126" cy="105" r="26" class="drv"/><circle cx="126" cy="105" r="10" class="drv-in"/>')
            q.append('<circle cx="126" cy="210" r="52" class="drv"/><circle cx="126" cy="210" r="18" class="drv-in"/>')
            if l[0]: q.append(f'<path d="M40 330H212M40 324v12M212 324v12" class="q"/><text x="126" y="350" class="qt">{esc(l[0])}</text>')
            q.append(f'<path d="M51 22H201M51 16v12M201 16v12" class="q q-red"/><text x="126" y="14" class="qt qt-red">foro {esc(a[0])}</text>')
            if l[0]: q.append(f'<path d="M20 40V298M14 40h12M14 298h12" class="q"/><text x="12" y="172" class="qt" transform="rotate(-90 12 172)">{esc(l[1])}</text>')
            q.append(f'<path d="M226 51V287M220 51h12M220 287h12" class="q q-red"/><text x="244" y="172" class="qt qt-red" transform="rotate(-90 244 172)">foro {esc(a[1])}</text>')
            top, bot = 62, 276
    # vista laterale
    q.append(f'<rect x="276" y="{top-12}" width="10" height="{bot-top+24}" class="frame"/>')
    q.append(f'<rect x="286" y="{top+10}" width="62" height="{bot-top-20}" class="box"/>')
    if m.get("prof_tot"):
        q.append(f'<path d="M276 330H348M276 324v12M348 324v12" class="q"/><text x="312" y="350" class="qt">{esc(m["prof_tot"])}</text>')
    q.append(f'<path d="M286 372H348M286 366v12M348 366v12" class="q q-red"/><text x="317" y="392" class="qt qt-red">montaggio {esc(m["prof"])}</text>')
    q.append(f'<text x="126" y="392" class="qt qt-muted">frontale</text>')
    label = f'Disegno quotato: foro {m["foro"] if tondo else " × ".join(m["foro"])}, profondità di montaggio {m["prof"]}'
    cap = m.get("nota", "Cornice in nero, foro nel muro tratteggiato in rosso. Misure del produttore; disegno non in scala.")
    return (f'<figure class="drawing reveal"><svg class="diagram dim" viewBox="-10 0 370 400" role="img" aria-label="{esc(label)}">'
            + "".join(q) + f'</svg><figcaption>{esc(cap)}</figcaption></figure>')


def schema(s, model):
    """Schema d'impianto: apparecchio a sinistra, zone a destra con i diffusori."""
    zone = s["zone"]
    n = len(zone)
    step = 84 if n <= 4 else 64
    h = 40 + step * (n - 1) + 40
    ys = [40 + step * i for i in range(n)]
    mid = (ys[0] + ys[-1]) / 2
    out = [f'<svg class="diagram" viewBox="0 0 600 {h}" role="img" aria-label="Schema: {esc(model)} con {n} uscite o zone">']
    out.append(f'<g class="amp" transform="translate(14 {mid-29:.0f})"><rect width="150" height="58" rx="3"/><rect x="8" y="10" width="34" height="8" class="amp-led"/>'
               f'<circle cx="132" cy="29" r="5" class="amp-knob"/><line x1="8" y1="40" x2="110" y2="40" class="amp-line"/><line x1="8" y1="47" x2="110" y2="47" class="amp-line"/>'
               f'<text x="75" y="80" class="lbl-amp">{esc(s.get("apparecchio", model))}</text></g>')
    out.append(f'<path class="bus" d="M164 {mid:.0f}H196M196 {ys[0]}V{ys[-1]}"/>')
    for y, z in zip(ys, zone):
        t = z.get("tipo", "2")
        cls = "wire wire-line" if t in ("sub", "linea") else "wire"
        g = [f'<g class="zone" transform="translate(196 {y})"><path class="{cls}" d="M0 0H330"/><text x="14" y="-12" class="lbl">{esc(z["label"])}</text>']
        if t in ("sub", "linea"):
            g.append('<rect x="345" y="-19" width="38" height="38" rx="4" class="spk"/><circle cx="364" cy="0" r="11" class="spk-in"/>')
        else:
            k = {"1": 1, "2": 2, "4": 4, "3": 3}.get(t, 2)
            for i in range(k):
                cx = 360 + 44 * i if k <= 2 else 340 + 32 * i
                r = 17 if k <= 2 else 13
                g.append(f'<circle cx="{cx}" cy="0" r="{r}" class="spk"/><circle cx="{cx}" cy="0" r="{r//2}" class="spk-in"/>')
        g.append("</g>")
        out.append("".join(g))
    out.append("</svg>")
    return "".join(out)


def posa(x):
    """Schema di posizionamento a parete o a soffitto."""
    d = esc(x.get("distanza", "≥ 60 cm"))
    if x.get("tipo") == "soffitto":
        return ('<svg class="diagram" viewBox="0 0 600 300" role="img" aria-label="Schema di posizionamento a soffitto">'
                '<path d="M20 40H580M20 40V280" class="wall"/><text x="300" y="30" class="lbl lbl-c">soffitto</text>'
                '<text x="14" y="160" class="lbl lbl-c" transform="rotate(-90 14 160)">parete</text>'
                '<rect x="250" y="40" width="64" height="12" rx="3" class="spk-rect"/>'
                f'<path d="M20 70H250" class="wire"/><text x="120" y="62" class="lbl">{d}</text>'
                f'<path d="M282 52L180 250M282 52L384 250" class="ear"/><text x="300" y="200" class="lbl lbl-muted lbl-c">{esc(x.get("nota","area di ascolto"))}</text>'
                '<circle cx="282" cy="262" r="10" class="head"/></svg>')
    return ('<svg class="diagram" viewBox="0 0 600 300" role="img" aria-label="Schema di posizionamento a parete">'
            '<path d="M20 30H580M20 30V280" class="wall"/><text x="300" y="22" class="lbl lbl-c">soffitto</text>'
            '<text x="14" y="160" class="lbl lbl-c" transform="rotate(-90 14 160)">angolo</text>'
            '<rect x="250" y="120" width="56" height="84" rx="3" class="spk-rect"/><circle cx="278" cy="140" r="9" class="spk-in"/><circle cx="278" cy="178" r="16" class="spk-in"/>'
            f'<path d="M278 30V120" class="wire"/><text x="288" y="80" class="lbl">{d}</text>'
            f'<path d="M20 162H250" class="wire"/><text x="120" y="152" class="lbl">{d}</text>'
            f'<path d="M330 162H560" class="ear"/><text x="430" y="152" class="lbl lbl-muted">{esc(x.get("nota","altezza orecchie"))}</text>'
            '<circle cx="570" cy="162" r="10" class="head"/></svg>')


ICONE = {
    "subwoofer": '<rect x="12" y="10" width="40" height="44" rx="4"/><circle cx="32" cy="34" r="12"/><circle cx="32" cy="34" r="4"/><circle cx="32" cy="17" r="1.6"/>',
    "sorgente": '<rect x="8" y="16" width="48" height="28" rx="3"/><path d="M24 52h16M32 44v8"/><circle cx="20" cy="30" r="3"/><circle cx="32" cy="30" r="3"/><circle cx="44" cy="30" r="3"/>',
    "domotica": '<path d="M10 30L32 12l22 18"/><path d="M16 26v26h32V26"/><path d="M27 52V38h10v14"/><path d="M44 8c4 2 7 5 8 9M48 4c6 3 10 8 11 14" class="thin"/>',
    "rete": '<rect x="10" y="20" width="44" height="26" rx="3"/><path d="M18 46v8M46 46v8M24 30h4M32 30h4M40 30h4"/>',
    "diffusore": '<rect x="18" y="8" width="28" height="48" rx="3"/><circle cx="32" cy="20" r="5"/><circle cx="32" cy="40" r="9"/>',
    "soffitto": '<path d="M6 16h52"/><circle cx="32" cy="34" r="16"/><circle cx="32" cy="34" r="6"/>',
    "linea100v": '<path d="M8 32h12l6-12 8 24 6-12h16"/><text x="32" y="58" font-size="10" text-anchor="middle" stroke="none" fill="#111">100 V</text>',
    "microfono": '<rect x="24" y="8" width="16" height="28" rx="8"/><path d="M18 30c0 8 6 14 14 14s14-6 14-14M32 44v10M24 54h16"/>',
    "bluetooth": '<path d="M24 20l16 16-8 8V12l8 8-16 16"/>',
    "app": '<rect x="20" y="6" width="24" height="52" rx="4"/><path d="M28 50h8"/>',
    "cavo": '<path d="M10 44c10 0 10-24 22-24s12 24 22 24"/><circle cx="10" cy="44" r="3"/><circle cx="54" cy="44" r="3"/>',
}


def icona(nome):
    return f'<svg class="acc-icon" viewBox="0 0 64 64" aria-hidden="true">{ICONE.get(nome, ICONE["sorgente"])}</svg>'


# ---------- elenchi ----------
def card(p):
    chiave = "".join(f"<li>{esc(k)}</li>" for k in p.get("chiave", [])[:3])
    sotto = " · ".join(SOTTO[c] for c in p["cat"] if c in SOTTO and c != "M") or SOTTO.get(p["cat"][0], "")
    return (f'<a class="pcard reveal" href="scheda-{p["slug"]}.html" data-cat="{esc(p["cat"])}" data-brand="{esc(p["brand"])}">'
            f'<span class="pcard-img"><img src="{esc(p["img"]["src"])}" alt="{esc(p["img"]["alt"])}" width="1000" height="1000" loading="lazy"></span>'
            f'<span class="pcard-brand">{esc(p["brand"])}</span><span class="pcard-name">{esc(p["model"])}</span>'
            f'<span class="pcard-sub">{esc(sotto)}</span><ul class="pcard-keys">{chiave}</ul></a>')


def lista(prodotti, filtri):
    marche = sorted({p["brand"] for p in prodotti})
    chips = ['<button class="chip is-on" data-f="cat" data-v="*">Tutti</button>']
    for c in filtri:
        n = sum(1 for p in prodotti if c in p["cat"])
        if n:
            chips.append(f'<button class="chip" data-f="cat" data-v="{c}">{SOTTO[c]} <small>{n}</small></button>')
    bchips = ['<button class="chip is-on" data-f="brand" data-v="*">Tutti i marchi</button>'] + [
        f'<button class="chip" data-f="brand" data-v="{esc(b)}">{esc(b)}</button>' for b in marche]
    cards = "\n".join(card(p) for p in prodotti)
    return (f'<div class="filters" data-target="#griglia">' + ("<div class=\"chips\">" + "".join(chips) + "</div>" if len(chips) > 2 else "")
            + "<div class=\"chips chips-brand\">" + "".join(bchips) + f'</div><p class="count"><span>{len(prodotti)}</span> prodotti</p></div>'
            f'<div class="pgrid" id="griglia">\n{cards}\n</div>')


def main():
    env = Environment(loader=FileSystemLoader(ROOT / "_strumenti" / "modelli"), autoescape=True)
    env.globals.update(disegno=disegno, schema=schema, posa=posa, icona=icona)
    tpl = env.get_template("scheda.html.j2")
    prodotti = []
    for f in sorted(DATI.glob("*.json")):
        p = json.loads(f.read_text(encoding="utf-8"))
        amp = p["tipo"] == "amplificatore"
        p.setdefault("lista", "amplificatori.html" if amp else "diffusori.html")
        p.setdefault("lista_label", "Amplificatori" if amp else "Diffusori")
        p.setdefault("tipo_label", "Amplificatore da installazione" if amp else "Diffusore da incasso")
        p.setdefault("lato_titolo", "Cosa si collega" if amp else "Misure di montaggio")
        for k in ("collega", "sistemi", "viste", "intro", "fonti"):
            p.setdefault(k, [])
        out = ROOT / f'scheda-{p["slug"]}.html'
        old = out.read_text(encoding="utf-8") if out.exists() else ""
        new = tpl.render(p=p, v=V)
        # conserva header/footer già inseriti da build.py
        for name in ("HEADER", "FOOTER"):
            m = re.search(rf"<!-- {name} -->.*?<!-- /{name} -->", old, re.S)
            if m:
                new = re.sub(rf"<!-- {name} -->.*?<!-- /{name} -->", lambda _: m.group(0), new, flags=re.S)
        out.write_text(new, encoding="utf-8")
        prodotti.append(p)
    # elenchi
    for nome, tipo, filtri in (("amplificatori.html", "amplificatore", ["M"]), ("diffusori.html", "diffusore", ["P", "S", "L", "2", "W", "A"])):
        f = ROOT / nome
        s = f.read_text(encoding="utf-8")
        sel = [p for p in prodotti if p["tipo"] == tipo]
        sel.sort(key=lambda p: (p["brand"], p["model"]))
        s = re.sub(r"<!-- LISTA -->.*?<!-- /LISTA -->", lambda _: "<!-- LISTA -->\n" + lista(sel, filtri) + "\n<!-- /LISTA -->", s, flags=re.S)
        f.write_text(s, encoding="utf-8")
    print(f"{len(prodotti)} schede generate")


if __name__ == "__main__":
    main()
