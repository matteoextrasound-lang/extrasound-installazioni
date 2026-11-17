"""Funzioni di supporto per scrivere i file di dati delle schede (_dati/prodotti/*.json).

Le istruzioni di montaggio vanno prese dal manuale del produttore di ogni serie:
qui ci sono solo i blocchi già verificati, riusabili tra modelli della stessa serie.
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATI = ROOT / "_dati" / "prodotti"
U = "https://www.extrasound.it/wp-content/uploads/"
TAB = {"M": "Amplificatori<br>multicanale", "P": "Diffusori<br>da incasso", "S": "Diffusori<br>da soffitto",
       "L": "Diffusori<br>LCR", "2": "Diffusori<br>stereo", "W": "Subwoofer<br>da incasso", "A": "Diffusori<br>amplificati"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def imgs(spec):
    """'file » alt ;; file » alt' -> lista di dict (le immagini di extrasound.it)."""
    out = []
    for part in spec.split(";;"):
        part = part.strip()
        if not part:
            continue
        f, _, alt = part.partition("»")
        out.append({"src": U + f.strip(), "alt": alt.strip()})
    return out


def vista(i, caption):
    return {"src": i["src"], "alt": i["alt"], "caption": caption}


# Prodotti la cui scheda su extrasound.it è stata allineata ai dati del produttore (17/11/2026):
# dalla nota si tolgono le frasi sulle differenze con Extrasound.
CORRETTI = {28281, 28178, 28046, 2918, 28246, 28234, 1757, 39961, 40834, 31975, 32050, 32085, 32068, 2909, 31048, 29870,
            2361, 2822, 31580, 31589, 62254, 62268, 62280, 62294, 62308, 62322, 62336, 62350, 62439, 62453, 62467}
FINE = r"\.(?=\s|$)"


def pulisci_nota(n):
    n = re.sub(r"\s*La scheda Extrasound (indica|riporta).*?" + FINE, "", n)
    n = re.sub(r"\s*La profondità di montaggio \w+ differisce da quella indicata nella scheda Extrasound.*?" + FINE, "", n)
    n = re.sub(r"\s*Fa fede il dato \w+" + FINE, "", n)
    return n.strip()


def salva(d):
    if d.get("id") in CORRETTI and d.get("nota"):
        d["nota"] = pulisci_nota(d["nota"])
    d.setdefault("slug", slug(f'{d["brand"]} {d["model"]}'))
    d.setdefault("tab", TAB.get(d["cat"][0], "Prodotti"))
    DATI.mkdir(parents=True, exist_ok=True)
    (DATI / f'{d["slug"]}.json').write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    return d["slug"]


# ---------- ELAC Vertex II (manuale "Vertex II operating instructions 1.0.0") ----------
ELAC_V2_FONTI = [{"label": "manuale d'uso ELAC Vertex II", "url": "https://elac.com/download/iw-v62/vertex-ii-operating-instructions_1.0.0.pdf"}]
ELAC_V2_CAVI = {"righe": [["Fino a 7,5 m", "18 AWG (circa 0,8 mm²)"], ["Oltre 7,5 m", "16 AWG (circa 1,3 mm²)"], ["Massimo ai morsetti", "14 AWG (circa 2,1 mm²)"]]}


def elac_v2_passi(foro, soffitto):
    dove = "nel soffitto" if soffitto else "nel punto scelto"
    return [
        ["Traccia il foro", f"Ritaglia la dima di carta, appoggiala {dove} e traccia il bordo interno: {foro}."],
        ["Taglia", "Nel cartongesso basta un cutter; vanno bene anche un seghetto a punta o un seghetto alternativo. Taglia pulito: la cornice copre comunque i bordi."],
        ["Porta i cavi", "Fai arrivare il cavo all'apertura lasciandone circa 60 cm in più e spella le estremità di 6 mm. Non fissarlo con chiodi o graffette metalliche e tienilo lontano dai cavi elettrici."],
        ["Collega", "Rispetta la polarità (+ rosso sul + dell'amplificatore). I morsetti sono a molla: premi il cappuccio, infila il filo, rilascia. Nessun trefolo deve restare scoperto."],
        ["Inserisci e fissa", "Togli la griglia magnetica, ruota le staffe verso l'interno e inserisci il diffusore. Con un cacciavite a croce gira ogni vite in senso orario: la staffa ruota in posizione e stringe contro il cartongesso. Non stringere troppo, per non rompere la staffa."],
        ["Chiudi", "Rimetti la griglia magnetica. Se vuoi verniciare la cornice, la parte interna della dima protegge il woofer; anche la griglia si può verniciare."],
    ]


def elac_v2_con_amp():
    return {"titolo": "Con gli amplificatori ELAC Integrator", "link": "amplificatori.html", "icona": "sorgente",
            "voci": ["6 Ω: va sulle uscite normali (4–8 Ω), un diffusore per canale.",
                     "Non in bridge, che sugli ELAC Integrator richiede diffusori da 8 Ω.",
                     "Amplificazione consigliata dal produttore: da 30 a 120 W per canale."]}
