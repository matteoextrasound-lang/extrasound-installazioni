"""Porta ogni scheda alla struttura delle due schede modello (ELAC IS-AMP8100 e ELAC Vertex II IW-V62).

Si applica in genera_schede.py a ogni prodotto prima di generare l'HTML, quindi vale anche per le schede nuove.

Diffusori: 3 colonne (Caratteristiche / Acustica / Dimensioni), foto, misure di montaggio, sezione dei cavi,
amplificatore consigliato con foto e link, «Dove montarlo» con la grafica, «Montaggio in 6 passi».
Amplificatori: 3 colonne (Caratteristiche / Ingressi / Uscite), pannello posteriore, due configurazioni con le
grafiche delle zone (zone, bridge, subwoofer), «Cosa si collega» con un diffusore vero e l'immagine dell'interfaccia.
"""
import re

U = "https://www.extrasound.it/wp-content/uploads/"
MODELLI = {"elac-is-amp8100", "elac-vertex-ii-iw-v62"}


# ---------------- utilità ----------------
def testo(d):
    return " ".join(v for c in d.get("colonne", []) for v in c["voci"]) + " " + " ".join(d.get("chiave", []))


def impedenza(d):
    """Impedenza nominale più bassa dichiarata (Ω), oppure 'v100' per i diffusori solo a 100 V."""
    t = testo(d)
    if re.search(r"solo linea 100 V", t):
        return "v100"
    for v in [v for c in d.get("colonne", []) for v in c["voci"]] + d.get("chiave", []):
        if "mpedenz" in v or "Ω" in v:
            m = re.findall(r"(\d+(?:,\d+)?)\s*(?:[–-]\s*\d+\s*)?Ω", v.replace("minima", ""))
            if m and "mpedenz" in v:
                return min(float(x.replace(",", ".")) for x in m)
    m = re.findall(r"(\d+)\s*Ω", " ".join(d.get("chiave", [])))
    return min(float(x) for x in m) if m else None


def num(x):
    return f"{x:.0f}".replace(".", ",")


def cavi_calcolati(z):
    """Lunghezza massima per una perdita sotto il 5 % dell'impedenza nominale (rame, andata e ritorno)."""
    righe = []
    for sez, awg in ((0.75, "18 AWG"), (1.5, "16 AWG"), (2.5, "14 AWG")):
        l = 0.05 * z * sez / (2 * 0.0172)
        righe.append([f"Fino a {int(l)} m", f"{str(sez).replace('.', ',')} mm² ({awg})"])
    return {"intestazione": f"Distanza dall'amplificatore ({num(z)} Ω)", "righe": righe}


def cavi_100v():
    righe = []
    for sez, awg in ((0.75, "18 AWG"), (1.5, "16 AWG"), (2.5, "14 AWG")):
        l = 0.05 * (100 ** 2 / 120) * sez / (2 * 0.0172)
        righe.append([f"Fino a {int(l // 10 * 10)} m", f"{str(sez).replace('.', ',')} mm² ({awg})"])
    return {"intestazione": "Linea 100 V con 120 W di carico", "righe": righe}


NOTA_CAVI = "Sezione dei cavi: calcolo Extrasound per una perdita inferiore al 5 % dell'impedenza nominale (cavo in rame, andata e ritorno)."


# ---------------- diffusori ----------------
def amp_per(d):
    """Amplificatore del catalogo da proporre con il diffusore (slug), oppure None."""
    b, cat, s, t = d["brand"], d["cat"], d["slug"], testo(d)
    z = impedenza(d)
    if cat == "A":
        return None
    if s == "elac-iw-s10eq":
        return None
    if d.get("chiave", [""])[0].startswith("Linea 100 V") or z == "v100":
        return "artsound-mx-120m"
    if b == "Polk Audio":
        return "yamaha-xda-qs5400rk"
    if b == "ELAC":
        return "elac-is-amp8100"
    if b == "Garvan":
        return "elac-is-amp8100"
    if b == "JBL":
        return "jbl-da850"
    if b == "ArtSound":
        return "artsound-prl-1504" if s in ("artsound-ro2060", "artsound-re2060", "artsound-sq2060", "artsound-re2080") else "artsound-amp850"
    if b == "Focal":
        return "focal-100-iwsub8-amplifier" if "iwsub8" in s else "yamaha-xda-qs5400rk"
    if b == "KEF":
        if s in ("kef-ci250rrb-thx", "kef-ci3160rlb-thx"):
            return None
        return "rotel-c8-plus" if (z and z < 6) or "THX" in d["model"] or s in ("kef-ci200qsb-thx", "kef-ci200trb") else "marantz-model-m4"
    if b == "Elipson":
        if "infinite-s12" in s:
            return "elipson-infinite-a1000" if d.get("_tutti", {}).get("elipson-infinite-a1000") else None
        return "rotel-c8-plus" if "infinite" in s else "marantz-model-m4"
    return "rotel-c8-plus"


SLOT = [  # (titolo standard, parole chiave nel titolo dei passi esistenti)
    ("Traccia il foro", ("traccia", "dima", "verifica", "prevedi", "posiziona")),
    ("Taglia", ("taglia",)),
    ("Porta i cavi", ("cavi", "porta")),
    ("Collega", ("collega", "presa")),
    ("Inserisci e fissa", ("fissa", "inserisci", "mura", "telaio", "easyfit", "ancora", "rasa", "monta")),
    ("Chiudi", ("chiudi", "orienta", "griglia")),
]


def foro_txt(d):
    for c in d.get("chiave", []):
        if c.startswith("Foro"):
            return c[5:]
    return None


def sei_passi(d, vecchi):
    slots = [[] for _ in SLOT]
    titoli = [None] * 6
    for t, x in vecchi:
        tl = t.lower()
        i = next((k for k, (_, kw) in enumerate(SLOT) if any(w in tl for w in kw)), 4)
        if i == 0 and "taglia" in tl:      # «Traccia e taglia»
            slots[0].append(x); titoli[0] = titoli[0] or "Traccia il foro"; continue
        slots[i].append(x)
        titoli[i] = titoli[i] or t
    foro = foro_txt(d)
    soff = d["cat"] == "S"
    gen = [
        f"Usa la dima fornita e traccia il foro nel punto scelto{': ' + foro if foro else ''}.",
        "Prima di tagliare controlla che dietro non passino travi, tubi o cavi elettrici. Nel cartongesso basta un cutter o un seghetto a punta; un seghetto alternativo per i pannelli più duri.",
        "Porta il cavo al foro lasciandone 50–60 cm in più. Tienilo lontano dai cavi elettrici e non fissarlo con chiodi o graffette metalliche.",
        "Rispetta la polarità: + sul morsetto rosso, − sul nero, uguale su tutti i diffusori. Nessun trefolo deve restare scoperto.",
        "Inserisci il diffusore e stringi le viti dei fermi: si aprono dietro il pannello e lo bloccano. Non stringere troppo.",
        "Monta la griglia." + (" Se va verniciata, verniciala staccata dal diffusore." if "vernici" in testo(d).lower() else ""),
    ]
    if soff:
        gen[0] = f"Usa la dima fornita e traccia il foro nel soffitto{': ' + foro if foro else ''}."
    passi = []
    for i, (std, _) in enumerate(SLOT):
        x = " ".join(slots[i]) if slots[i] else gen[i]
        if i == 0 and slots[0] and foro and foro not in x and "dima" not in x:
            x += f" Foro: {foro}."
        passi.append([std if i in (0, 1, 3) else (titoli[i] if titoli[i] and len(titoli[i]) < 24 else std), x])
    return passi


def diffusore(d, tutti):
    # colonne
    d.pop("lato_titolo", None)
    tit = ["Caratteristiche", "Acustica", "Dimensioni"]
    for c, t in zip(d["colonne"], tit):
        c["titolo"] = t
    # misure di montaggio anche senza foro dichiarato
    if not d.get("misure"):
        prof = next((c[11:] for c in d.get("chiave", []) if c.startswith("Profondità")), None)
        if prof:
            d["misure"] = {"forma": "rett", "foro": ["da dima", "da dima"], "prof": prof,
                           "nota": "Foro: il produttore non lo indica, si traccia con la dima o la cassaforma fornita. Disegno non in scala."}
    # cavi
    if not d.get("cavi") and d["cat"] != "A":
        z = impedenza(d)
        if z == "v100" or d.get("chiave", [""])[0].startswith("Linea 100 V"):
            d["cavi"] = cavi_100v()
        elif z:
            d["cavi"] = cavi_calcolati(z)
        if d.get("cavi") and NOTA_CAVI not in d.get("nota", ""):
            d["nota"] = (d.get("nota", "") + " " + NOTA_CAVI).strip()
    # amplificatore consigliato con foto e link
    a = d.pop("amp", None) or amp_per(d)
    if a and a in tutti and not any(c.get("img") for c in d["collega"]):
        A = tutti[a]
        gen = next((c for c in d["collega"] if c.get("icona") in ("sorgente", "linea100v", "subwoofer") or c["titolo"] in ("Amplificazione", "Linea 100 V")), None)
        voci = list(gen["voci"]) if gen else []
        voci = [v for v in voci if not v.startswith("Ad esempio con")]
        voci.append(f"{A['brand']} {A['model']}: {A['chiave'][1]}.")
        card = {"titolo": f"Con il {A['brand']} {A['model']}", "link": f"scheda-{a}.html", "img": A["img"]["src"], "alt": A["img"]["alt"], "voci": voci}
        d["collega"] = [card] + [c for c in d["collega"] if c is not gen]
    # sistemi: Dove montarlo + Montaggio in 6 passi
    sis = d["sistemi"]
    dove = next((s for s in sis if s["titolo"].lower().startswith("dove")), None)
    if not dove:
        dove = {"titolo": "Dove montarlo", "voci": ["Verifica travi, tubi e impianti prima di tagliare."]}
        sis.insert(0, dove)
    if not dove.get("posa"):
        tondo = (d.get("misure") or {}).get("forma") == "tondo"
        if d["cat"] in ("S", "2") and (tondo or d["cat"] == "S"):
            dove["posa"] = {"tipo": "soffitto", "distanza": "lontano dalle pareti", "nota": "zona d'ascolto"}
        else:
            dove["posa"] = {"tipo": "parete", "distanza": "spazio libero", "nota": "altezza orecchie" if d["cat"] != "W" else "posizione libera"}
    mont = [s for s in sis if s.get("passi")]
    vecchi = [p for s in mont for p in s["passi"]]
    pronto = next((x for x in sis if x["titolo"] == "Montaggio in 6 passi" and len(x.get("passi", [])) == 6), None)
    if pronto:
        d["sistemi"] = [dove, pronto] + [x for x in sis if x is not dove and x is not pronto]
    elif d["slug"] not in MODELLI:
        nuovo = {"titolo": "Montaggio in 6 passi", "passi": sei_passi(d, vecchi)}
        altri = [s for s in sis if s is not dove and not s.get("passi")]
        d["sistemi"] = [dove, nuovo] + altri
    return d


# ---------------- amplificatori ----------------
def z(label, tipo=None):
    return {"label": label, "tipo": tipo} if tipo else {"label": label}


AMP = {
 "artsound-amp850": {"spk": "artsound-fl501", "gui": ("artsound-amp850-frontale.jpg", "Frontale dell'AMP850. Non ha un'interfaccia software: livelli e accensione si regolano sull'apparecchio e dallo streamer collegato."),
   "conf": {"titolo": "3 zone · bridge", "voci": ["Soggiorno con due coppie di canali in bridge: 150 W per lato su 8 Ω.", "Altre due zone stereo con i canali restanti."],
            "zone": [z("Zona 1 · Soggiorno · 2 × 150 W bridge · 8 Ω"), z("Zona 2 · Cucina · 2 × 50 W"), z("Zona 3 · Camera · 2 × 50 W")]}},
 "artsound-smart-zone-4-amp": {"spk": "artsound-fl501", "gui": ("artsound-smart-zone-4amp.jpg", "Si configura e si comanda dall'app 4STREAM (iOS e Android); RS232 per la domotica."),
   "conf": {"titolo": "4 zone · subwoofer", "voci": ["Soggiorno con un subwoofer attivo sulla Line Out della zona.", "Le altre zone stereo sui morsetti."],
            "zone": [z("Zona 1 · Soggiorno"), z("Zona 1 · Subwoofer attivo · Line Out", "sub"), z("Zona 2 · Cucina"), z("Zona 3 · Camera"), z("Zona 4 · Bagno")]}},
 "artsound-prl-1502": {"spk": "artsound-ro2060", "gui": ("artsound-prl1502-frontale.jpg", "Frontale del PRL-1502: indicatori di segnale e clip. Non ha un'interfaccia software."),
   "conf0": {"titolo": "1 zona stereo", "voci": ["Una coppia di diffusori, 2 × 150 W su 4 Ω."], "zone": [z("Sala · 2 × 150 W / 4 Ω")]},
   "conf": {"titolo": "Bridge · 300 W", "voci": ["I due canali in bridge per un solo diffusore o subwoofer passivo."], "zone": [z("Bridge · 1 × 300 W", "1")]}},
 "artsound-prl-1504": {"spk": "artsound-ro2060", "gui": ("artsound-prl1504-frontale.jpg", "Frontale del PRL-1504: indicatori dei quattro canali. Non ha un'interfaccia software."),
   "conf": {"titolo": "1 zona · bridge", "voci": ["Quattro canali in bridge: 2 × 300 W per una zona stereo."], "zone": [z("Zona 1 · 2 × 300 W bridge")]}},
 "artsound-smart-hyde": {"spk": "artsound-ro2040", "gui": ("artsound-smrt-hyde-uop.jpg", "Si configura e si comanda dall'app 4STREAM; più Smart Hyde sulla stessa rete formano l'impianto multiroom."),
   "conf0": {"titolo": "1 stanza · subwoofer", "voci": ["Una coppia di diffusori e un subwoofer attivo sul SUB OUT."], "zone": [z("Stanza · 2 × 50 W / 4 Ω"), z("Subwoofer attivo · SUB OUT", "sub")]},
   "conf": {"titolo": "Multiroom con più Smart Hyde", "voci": ["Uno Smart Hyde per stanza, tutti sulla stessa rete e comandati dall'app."], "zone": [z("Smart Hyde 1 · Soggiorno"), z("Smart Hyde 2 · Cucina"), z("Smart Hyde 3 · Camera")], "apparecchio": "Rete e app 4STREAM"}},
 "artsound-art1-1": {"spk": "artsound-mdc401", "gui": ("Artsound-1.1-sopra.jpg", "Nessuna interfaccia: si abbina in Bluetooth dallo smartphone."),
   "conf0": {"titolo": "1 zona stereo", "voci": ["Una coppia di diffusori da incasso, sorgente in Bluetooth."], "zone": [z("Stanza · 2 × 10 W / 8 Ω")]},
   "conf": {"titolo": "Su 4 Ω", "voci": ["Con diffusori da 4 Ω la potenza sale a 2 × 15 W."], "zone": [z("Stanza · 2 × 15 W / 4 Ω")]}},
 "artsound-mx-120m": {"spk": "artsound-mdt600-p", "gui": ("artsound-mx-120m-frontale.jpg", "Frontale: volume per ingresso, toni, lettore USB/SD, Bluetooth e FM."),
   "conf0": {"titolo": "Linea 100 V", "voci": ["Un solo cavo per tutti i diffusori; somma delle prese entro 120 W.", "Esempio: 8 × MDT600-P sulla presa da 9 W = 72 W."], "zone": [z("Sala · 4 × MDT600-P · 9 W", "4"), z("Dehors · 4 × MDT600-P · 9 W", "4")]},
   "conf": {"titolo": "Bassa impedenza · 4–16 Ω", "voci": ["Selettore su 4–16 Ω: diffusori normali, senza trasformatore."], "zone": [z("Sala · diffusori 8 Ω")]}},
 "artsound-mx60mkii": {"spk": "artsound-mdt600-p", "gui": ("Artsound-MX60MKII-frontale.jpg", "Frontale: volume per ingresso, toni, Bluetooth, USB e microSD; telecomando incluso."), "retro": ("Artsound-MX60MKII-posteriore.jpg", "Pannello posteriore dell'ArtSound MX60MKII", "Ingressi microfono e AUX, uscita di linea, morsetti 4–8 Ω, 70 V e 100 V, alimentazione."),
   "conf0": {"titolo": "Linea 100 V", "voci": ["Somma delle prese entro 60 W.", "Esempio: 6 × MDT600-P sulla presa da 9 W = 54 W."], "zone": [z("Negozio · 6 × MDT600-P · 9 W", "4")]},
   "conf": {"titolo": "Bassa impedenza · 4–8 Ω", "voci": ["Uscita 4–8 Ω per diffusori normali: mai insieme all'uscita 100 V."], "zone": [z("Negozio · diffusori 8 Ω")]}},
 "focal-100-iwsub8-amplifier": {"spk": "focal-100-iwsub8", "gui": ("focal-100-iwsub8-amplifier-frontale.jpg", "Frontale: accensione e indicatori. Le regolazioni sono sul pannello posteriore."),
   "conf": {"titolo": "Home cinema con un subwoofer", "voci": ["Un solo 100 IWSUB8 da 8 Ω."], "zone": [z("Ingresso LFE dal processore", "linea"), z("100 IWSUB8 · 8 Ω", "sub")]}},
 "jbl-da850": {"spk": "jbl-stage-260c", "gui": ("jbl-da850-frontale-1000.jpg", "Non ha un'interfaccia software: livelli e modalità si regolano con trimmer e interruttori sul retro."),
   "conf": {"titolo": "3 zone · bridge", "voci": ["Soggiorno con due zone in bridge: 185 W per lato.", "Altre due zone stereo."], "zone": [z("Zona 1 · Soggiorno · 2 × 185 W bridge"), z("Zona 2 · Camera · 2 × 50 W"), z("Zona 3 · Bagno · 2 × 50 W")]}},
 "jbl-da1650": {"spk": "jbl-stage-260c", "gui": ("jbl-da1650-frontale-1000.jpg", "Non ha un'interfaccia software: livelli e modalità si regolano con trimmer e interruttori sul retro."),
   "conf": {"titolo": "7 zone · bridge", "voci": ["Soggiorno con due zone in bridge: 185 W per lato.", "Altre sei zone stereo."], "zone": [z("Zona 1 · Soggiorno · 2 × 185 W bridge"), z("Zona 2 · Cucina · 2 × 50 W"), z("Zona 3 · Camera · 2 × 50 W"), z("Zona 4 · Bagno · 2 × 50 W"), z("Zona 5 · Studio · 2 × 50 W"), z("Zona 6 · Terrazzo · 2 × 50 W"), z("Zona 7 · Taverna · 2 × 50 W")]}},
 "marantz-model-m4": {"spk": "kef-ci160-2cr", "gui": ("jydfj-5.jpg", "Si configura dall'app HEOS; controllo IP per Crestron, Control4 e AMX."), "retro": ("gdf-129.jpg", "Pannello posteriore del Marantz Model M4 con morsetti, ingressi, uscite pre e sub, Ethernet", "Morsetti per 8 canali, ingressi RCA e ottici, uscite pre/sub per zona, USB, Ethernet e trigger."),
   "conf": {"titolo": "4 zone · subwoofer", "voci": ["Soggiorno con un subwoofer attivo sull'uscita della zona impostata come SUB, passa-alto sui diffusori."], "zone": [z("Zona 1 · Soggiorno · 2 × 100 W"), z("Zona 1 · Subwoofer attivo · SUB OUT", "sub"), z("Zona 2 · Cucina · 2 × 100 W"), z("Zona 3 · Camera · 2 × 100 W"), z("Zona 4 · Bagno · 2 × 100 W")]}},
 "rotel-c8-plus": {"spk": "kef-ci200rr-thx", "gui": ("rotel-c8-plus-1000.jpg", "Frontale del C8+; si comanda via IP e RS232 dal sistema di controllo."),
   "conf": {"titolo": "3 zone · bridge", "voci": ["Soggiorno con due coppie di canali in bridge: 300 W per lato su 4 Ω.", "Altre due zone stereo."], "zone": [z("Zona 1 · Soggiorno · 2 × 300 W bridge"), z("Zona 2 · Cucina · 2 × 100 W"), z("Zona 3 · Camera · 2 × 100 W")]}},
 "rotel-c8": {"spk": "focal-300-icw6", "gui": ("rotel-c8-1000.jpg", "Frontale del C8; si comanda via IP e RS232 dal sistema di controllo."),
   "conf": {"titolo": "3 zone · bridge", "voci": ["Soggiorno con due coppie di canali in bridge: 140 W per lato su 4 Ω.", "Altre due zone stereo."], "zone": [z("Zona 1 · Soggiorno · 2 × 140 W bridge"), z("Zona 2 · Cucina · 2 × 50 W"), z("Zona 3 · Camera · 2 × 50 W")]}},
 "yamaha-xda-amp5400rk": {"spk": "kef-ci160qr", "gui": ("XDA-AMP5400RK-frontale-2.jpg", "Non ha un'interfaccia software: accensione da trigger o Audio Sense, volume dalla sorgente."), "retro": ("XDA-AMP5400RK-retro.jpg", "Pannello posteriore dello Yamaha XDA-AMP5400RK", "Ingressi RCA con passanti, Euroblock dei diffusori, interruttori NORMAL/BRIDGE e AUDIO SENSE, trigger e IR."),
   "conf": {"titolo": "3 zone · bridge", "voci": ["Soggiorno con due zone in bridge: 100 W per lato su 8 Ω (diffusori da 8 Ω o più)."], "zone": [z("Zona 1 · Soggiorno · 2 × 100 W bridge · 8 Ω"), z("Zona 2 · Cucina · 2 × 50 W"), z("Zona 3 · Camera · 2 × 50 W")]}},
 "yamaha-xda-qs5400rk": {"spk": "kef-ci130-2cr", "gui": ("XDA-QS5400rk-zone.jpg", "Si configura dall'app MusicCast CONTROLLER e dal browser (indirizzo IP + /Setup)."),
   "conf": {"titolo": "3 zone · bridge e subwoofer", "voci": ["Soggiorno con due zone in bridge (100 W per lato su 8 Ω) e subwoofer attivo sulla PRE OUT.", "Altre due zone stereo."], "zone": [z("Zona 1 · Soggiorno · 2 × 100 W bridge · 8 Ω"), z("Zona 1 · Subwoofer attivo · PRE OUT", "sub"), z("Zona 2 · Cucina · 2 × 50 W"), z("Zona 3 · Camera · 2 × 50 W")]}},
}


def amplificatore(d, tutti):
    for c, t in zip(d["colonne"], ["Caratteristiche", "Ingressi", "Uscite"]):
        c["titolo"] = t
    cfg = AMP.get(d["slug"]) or d.pop("_cfg", None)
    if not cfg:
        return d
    s = cfg.get("spk")
    if s in tutti and not any(c.get("img") for c in d["collega"]):
        S = tutti[s]
        gen = next((c for c in d["collega"] if c.get("icona") in ("soffitto", "linea100v", "subwoofer", "diffusore") or c["titolo"].startswith("Diffusori")), None)
        voci = [v for v in (gen["voci"] if gen else []) if not v.startswith(("Esempi", "Ad esempio"))]
        voci.append(f"Esempio: {S['brand']} {S['model']}, {S['chiave'][0]}.")
        card = {"titolo": f"{S['brand']} {S['model']}", "link": f"scheda-{s}.html", "img": S["img"]["src"], "alt": S["img"]["alt"], "voci": voci}
        d["collega"] = [card] + [c for c in d["collega"] if c is not gen]
    if not d.get("gui") and cfg.get("gui"):
        f, cap = cfg["gui"]
        d["gui"] = {"src": U + f, "alt": f"{d['brand']} {d['model']}, frontale e comandi", "caption": cap}
    if not d.get("retro") and cfg.get("retro"):
        f, alt, cap = cfg["retro"]
        d["retro"] = {"src": U + f, "alt": alt, "titolo": "Pannello posteriore", "caption": cap}
    conf = [x for x in d["sistemi"] if x.get("zone")]
    resto = [x for x in d["sistemi"] if not x.get("zone")]
    if not conf and cfg.get("conf0"):
        conf = [cfg["conf0"]]
    if len(conf) < 2 and cfg.get("conf"):
        conf.append(cfg["conf"])
    d["sistemi"] = conf + resto
    return d


def uniforma(d, tutti):
    if d["slug"] in MODELLI:
        return d
    d["_tutti"] = tutti
    d = diffusore(d, tutti) if d["tipo"] == "diffusore" else amplificatore(d, tutti)
    d.pop("_tutti", None)
    return d
