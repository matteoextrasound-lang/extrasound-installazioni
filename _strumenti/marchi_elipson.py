"""Schede Elipson (Architect IN e Infinite). Dati dalle schede tecniche Elipson (distributore UK) e dai manuali Elipson,
confrontati con le schede Extrasound. Eseguire dalla radice: python3 _strumenti/marchi_elipson.py"""
import sys; sys.path.insert(0, '_strumenti')
from schede_util import *

X = 'https://www.extrasound.it/'
CDN = 'https://cdn.shopify.com/s/files/1/0055/9906/8206/files/'
def F(l, u): return {"label": l, "url": u}
SRC = {"IC6": F("scheda tecnica Elipson IC6", CDN + "elipson-ic6-spec-sheet.pdf"), "IC8": F("scheda tecnica Elipson IC8", CDN + "elipson-ic8-spec-sheet.pdf"),
       "IW8": F("scheda tecnica Elipson IW8", CDN + "elipson-iw8-spec-sheet.pdf"), "IC6ST": F("scheda tecnica Elipson IC6ST", CDN + "elipson-ic6st-spec-sheet.pdf"),
       "US": F("scheda tecnica Elipson IC8 Ultra Slim", CDN + "elipson-ic8-ultra-slim-spec-sheet.pdf"), "IW14C": F("scheda tecnica Elipson IW14C", CDN + "elipson-iw14c-spec-sheet.pdf"),
       "MAN": F("manuale Elipson Architect IN (dimensioni)", "https://www.manualslib.fr/manual/167653/Elipson-Iw6.html?page=13"),
       "INF": F("manuale Elipson Infinite (specifiche)", "https://www.manualslib.fr/manual/364337/Elipson-Infinite-8.html?page=21"),
       "INFI": F("manuale Elipson Infinite (installazione)", "https://www.manualslib.fr/manual/364337/Elipson-Infinite-8.html?page=18")}

# id, modello, cat, tipo, driver, potenza, risposta, xo, sens, imp, foro, est, prof, peso, fonti, url, extra
AIN = [
 (2360, "IC4", "S", "2 vie coassiale", ["woofer 100 mm in carta, sospensione in gomma", "tweeter 19 mm a cupola in seta, orientabile 35–40°"], "80 W", "85 Hz – 20 kHz (±3 dB)", "2.400 Hz", "84 dB (1 W / 1 m)", "8 Ω", "Ø 138 mm", "Ø 181 mm", "92 mm", "1,1 kg", ["MAN"], "elipson-ic4-diffusore-2-vie-coassiale-da-incasso-a-soffitto-80-w", {"nota": "Dati acustici dalla scheda Extrasound (scheda Elipson IC4 non trovata); dimensioni confermate dal manuale Elipson."}),
 (2361, "IC6", "S", "2 vie coassiale", ["woofer 165 mm in carta, sospensione in gomma", "tweeter 19 mm a cupola in seta, orientabile 35–40°"], "100 W", "70 Hz – 20 kHz (±3 dB)", "1.950 Hz", "87 dB (1 W / 1 m)", "8 Ω", "Ø 200 mm", "Ø 230 mm", "102 mm", "1,9 kg", ["IC6", "MAN"], "elipson-ic6-diffusore-2-vie-coassiale-da-incasso-a-soffitto-100-w", {"diff": "La scheda Extrasound indica tweeter da 25 mm, incrocio a 2.950 Hz e 1,45 kg; la scheda Elipson indica 19 mm, 1.950 Hz e 1,9 kg. Il manuale Elipson indica un diametro esterno di 246 mm, la scheda 230 mm."}),
 (2362, "IC8", "S", "2 vie coassiale", ["woofer 210 mm in carta, sospensione in gomma", "tweeter 25 mm a cupola in seta, orientabile 35–40°"], "125 W", "55 Hz – 20 kHz (±3 dB)", "2.550 Hz", "87 dB (1 W / 1 m)", "8 Ω", "Ø 242 mm", "Ø 290 mm", "122 mm", "2,4 kg", ["IC8"], "elipson-ic8-diffusore-2-vie-coassiale-da-incasso-a-soffitto-125-w", {}),
 (2579, "IC6ST", "2", "2 vie coassiale stereo", ["woofer 165 mm in carta, sospensione in gomma", "2 tweeter 19 mm a cupola in seta, orientabili 35–40°"], "100 W", "65 Hz – 20 kHz (±3 dB)", "2.200 Hz", "83 dB (1 W / 1 m)", "8 Ω", "Ø 200 mm", "Ø 230 mm", "105 mm", "1,7 kg", ["IC6ST"], "elipson-ic6st-diffusore-stereo-da-incasso-a-soffitto-2-vie-coassiale", {"ds": True, "diff": "La scheda Extrasound indica 102 mm di profondità; Elipson 105 mm."}),
 (31580, "IC8 Ultra Slim", "S", "3 vie", ["3 woofer 75 mm in carta trattata, sospensione in gomma", "medio 75 mm in carta trattata, sospensione in tessuto", "tweeter 25 mm a cupola in seta"], "70 W", "95 Hz – 20 kHz (±3 dB)", "", "88 dB (1 W / 1 m)", "8 Ω", "Ø 242 mm", "Ø 272 mm", "50 mm", "1,6 kg", ["US"], "elipson-ic8-ultra-slim-diffusore-3-vie-ultra-sottile-da-incasso-a-soffitto", {"diff": "La scheda Extrasound indica un tweeter da 20 mm; Elipson 1″ (25 mm)."}),
 (2363, "IW6", "P", "2 vie", ["woofer 165 mm in carta, sospensione in gomma", "tweeter 19 mm a cupola in seta con magnete al neodimio, orientabile 35–40°"], "100 W", "68 Hz – 20 kHz (±3 dB)", "2.950 Hz", "87 dB (1 W / 1 m)", "8 Ω", ["205 mm", "290 mm"], ["235 mm", "320 mm"], "75 mm", "1,5 kg", ["MAN"], "elipson-iw6-diffusore-da-incasso-a-parete-2-vie-100-w", {"nota": "Dati acustici dalla scheda Extrasound (scheda Elipson IW6 non trovata).", "diff": "La scheda Extrasound indica un foro di 190 × 277 mm; il manuale Elipson 205 × 290 mm. Verifica con la dima fornita."}),
 (2364, "IW8", "P", "2 vie", ["woofer 210 mm in carta, sospensione in gomma", "tweeter 25 mm a cupola in seta, orientabile 35–40°"], "125 W", "55 Hz – 20 kHz (±3 dB)", "2.100 Hz", "87 dB (1 W / 1 m)", "8 Ω", ["225 mm", "328 mm"], ["270 mm", "370 mm"], "88 mm", "1,55 kg", ["IW8", "MAN"], "elipson-iw8-diffusore-da-incasso-a-parete-2-vie-130-w", {"diff": "Le fonti Elipson non coincidono sul foro: 225 × 328 mm nella scheda tecnica (come Extrasound), 240 × 340 mm nel manuale. Verifica con la dima fornita."}),
 (2822, "IW14C", "L", "2 vie", ["2 woofer 130 mm in carta, sospensione in gomma", "tweeter 25 mm a cupola in seta"], "100 W", "75 Hz – 20 kHz (±3 dB)", "2.200 Hz", "87 dB (1 W / 1 m)", "8 Ω", ["370 mm", "196 mm"], ["400 mm", "225 mm"], "100 mm", "3 kg", ["IW14C"], "elipson-iw14c-diffusore-da-incasso-2-vie-doppio-140-mm-100-w", {"diff": "La scheda Extrasound indica 2 woofer da 165 mm; la scheda Elipson 2 × 130 mm."}),
]
IMG = {
 2360: "virtuemart/product/elipson-ic4.jpg » Elipson IC4 da incasso a soffitto visto di lato con griglia bianca e retro ;; virtuemart/product/elipson-ic4-griglia.jpg » Elipson IC4 senza griglia accanto alla griglia rotonda bianca",
 2361: "virtuemart/product/elipson-ic6.jpg » Elipson IC6 da incasso a soffitto visto di lato con griglia bianca e retro ;; virtuemart/product/elipson-ic6-griglia.jpg » Elipson IC6 senza griglia accanto alla griglia rotonda bianca",
 2362: "virtuemart/product/elipson-ic8.jpg » Elipson IC8 da incasso a soffitto visto di lato con griglia bianca e retro ;; virtuemart/product/elipson-ic8-griglia.jpg » Elipson IC8 senza griglia con woofer coassiale accanto alla griglia bianca",
 2363: "virtuemart/product/elipson-iw6.jpg » Elipson IW6 da incasso a parete visto di lato con griglia bianca ;; virtuemart/product/elipson-iw6-griglia.jpg » Elipson IW6 senza griglia accanto alla griglia rettangolare bianca",
 2364: "virtuemart/product/elipson-iw8.jpg » Elipson IW8 da incasso a parete visto di lato con griglia bianca ;; virtuemart/product/elipson-iw8-griglia.jpg » Elipson IW8 senza griglia accanto alla griglia rettangolare bianca",
 2579: "virtuemart/product/elipson-ic6st.jpg » Elipson IC6ST da incasso a soffitto visto di lato con griglia bianca ;; virtuemart/product/elipson-ic6st-griglia.jpg » Elipson IC6ST senza griglia accanto alla griglia rotonda bianca",
 2822: "virtuemart/product/Elipson-IW-14C-centrale-da-incasso.jpg » Elipson IW14C senza griglia con due woofer e tweeter centrale ;; virtuemart/product/Elipson-IW-14C-centrale-con-griglia.jpg » Elipson IW14C visto di lato con griglia bianca ;; virtuemart/product/Elipson-IW-14C-griglia.jpg » Elipson IW14C con griglia bianca di lato",
 31580: "elipson-IC8-ultraslim.jpg » Elipson IC8 Ultra Slim senza griglia con tre woofer, midrange e tweeter ;; elipson-IC8-ultraslim-griglia.jpg » Elipson IC8 Ultra Slim con la griglia bianca rotonda ;; elipson-IC8-retro.jpg » Retro dell'Elipson IC8 Ultra Slim con i morsetti e i fissaggi",
 31589: "Elipson-Infinite-8.jpg » Elipson Infinite 8 senza griglia visto di tre quarti ;; Elipson-Infinite-8-frontale.jpg » Elipson Infinite 8 senza griglia visto di fronte con woofer e tweeter ;; Elipson-Infinite-8-griglia.jpg » Elipson Infinite 8 con griglia nera visto di lato",
 31598: "Elipson-infinite-12.jpg » Elipson Infinite S12 senza copertura con woofer da 30 cm e due reflex ;; Elipson-infinite-12-griglia.jpg » Elipson Infinite S12 con la copertura nera visto di lato",
 31611: "elipson-infinite-14.jpg » Elipson Infinite 14 senza griglia con due woofer e tweeter centrale ;; elipson-infinite-14-griglia.jpg » Elipson Infinite 14 con la griglia nera",
}
TIPO = {"P": "Diffusore da incasso a parete", "S": "Diffusore da incasso a soffitto", "2": "Diffusore stereo da incasso a soffitto", "L": "Diffusore LCR da incasso a parete", "W": "Subwoofer passivo da incasso"}


def cap(alt):
    a = alt.lower()
    for k, v in (("retro", "Retro"), ("senza griglia", "Senza griglia"), ("griglia", "Con griglia"), ("lato", "Lato")):
        if k in a:
            return v
    return "Vista"


def ain(t):
    (id, mod, cat, tp, drv, pw, risp, xo, sens, imp, foro, est, prof, peso, fk, url, ex) = t
    tipo = TIPO[cat]
    I = imgs(IMG[id])
    fstr = foro if isinstance(foro, str) else f"{foro[0]} × {foro[1]}"
    car = [f"{tipo}, serie Architect IN.", f"Sistema: {tp}."] + [d[0].upper() + d[1:] + "." for d in drv] + ["Griglia magnetica bianca, verniciabile."]
    if ex.get("ds"):
        car.append("Stereo in un solo diffusore: due tweeter, doppi morsetti L e R.")
    acu = [f"Potenza: {pw}.", f"Risposta: {risp}.", f"Sensibilità: {sens}.", f"Impedenza: {imp}."] + ([f"Incrocio: {xo}."] if xo else [])
    dim = [f"Foro: {fstr}.", f"Ingombro: {est if isinstance(est, str) else est[0] + ' × ' + est[1]} × {prof}.", f"Peso: {peso}."]
    if forma_tonda := foro if isinstance(foro, str) else None:
        mis = {"forma": "tondo", "foro": foro.replace("Ø ", ""), "est": est.replace("Ø ", ""), "prof": prof}
    elif cat == "L":
        mis = {"forma": "rett", "orizzontale": True, "foro": foro, "est": est, "prof": prof}
    else:
        mis = {"forma": "rett", "foro": foro, "est": est, "prof": prof}
    mis["nota"] = "Foro tratteggiato in rosso; profondità = ingombro Elipson. Disegno non in scala."
    if ex.get("ds"):
        v = ["Due ingressi: canale sinistro e destro dello stesso amplificatore, 8 Ω per canale.", "Per stanze piccole dove c'è posto per un solo diffusore."]
    else:
        v = ["8 Ω: un diffusore per canale su qualsiasi amplificatore da installazione."]
    v.append(f"Potenza dichiarata da Elipson: {pw}.")
    col = [{"titolo": "Amplificazione", "link": "amplificatori.html", "icona": "sorgente", "voci": v}]
    dove = ["Orienta il tweeter (35–40°) verso la zona d'ascolto.", "Verifica travi, tubi e impianti prima di tagliare."]
    if cat == "L":
        dove.insert(0, "Centrale sopra o sotto lo schermo, oppure frontali sinistro e destro.")
    sist = [{"titolo": "Dove montarlo", "voci": dove}]
    if cat in ("S", "2"):
        sist[0]["posa"] = {"tipo": "soffitto", "distanza": "lontano dalle pareti", "nota": "zona d'ascolto"}
    if ex.get("ds"):
        sist.append({"titolo": "Schema", "voci": ["Un solo diffusore riceve i due canali."], "zone": [{"label": f"{mod} · L + R", "tipo": "2"}], "apparecchio": "Amplificatore"})
    sist.append({"titolo": "Montaggio", "passi": [["Traccia e taglia", f"Usa la dima fornita e taglia il foro: {fstr}."], ["Collega", "Rispetta la polarità: + sul morsetto rosso, − sul nero."],
        ["Fissa", "Inserisci il diffusore e stringi le viti dei fermi fino a bloccarlo sul pannello, senza forzare."], ["Orienta e chiudi", "Orienta il tweeter, poi applica la griglia magnetica. Per verniciare la griglia toglila dal diffusore."]]})
    nota = "Dati da " + ", ".join(SRC[k]["label"] for k in fk) + ", confrontati con la scheda Extrasound. Procedura di montaggio generale: le istruzioni di dettaglio sono nel manuale Elipson fornito."
    for k in ("nota", "diff"):
        if ex.get(k):
            nota += " " + ex[k]
    if ex.get("diff"):
        nota += " Fa fede il dato Elipson."
    tp0 = tp.split(",")[0]
    d = {"id": id, "tipo": "diffusore", "cat": cat, "brand": "Elipson", "model": mod, "crop": False,
         "meta": f"Elipson {mod}: {tp0}, {tipo[0].lower() + tipo[1:]}. Foro, profondità e collegamenti per l'installatore.",
         "img": I[0], "chiave": [f"{tp0} · {imp}", f"Foro {fstr}", f"Profondità {prof}"], "righe": [f"{tp0} · {drv[0].split(' in ')[0]}", tipo, "Architect IN"],
         "intro": [f"L'<strong>Elipson {mod}</strong> è un {tipo[0].lower() + tipo[1:]} della serie Architect IN: {', '.join(drv)}. {pw}, {imp}.", f"Foro <strong>{fstr}</strong>, profondità <strong>{prof}</strong>."],
         "colonne": [{"titolo": "Caratteristiche", "voci": car}, {"titolo": "Acustica", "voci": acu}, {"titolo": "Dimensioni", "voci": dim}],
         "viste": [vista(i, cap(i["alt"])) for i in I[1:4]], "misure": mis, "collega": col, "sistemi": sist, "nota": nota, "extrasound": X + url, "fonti": [SRC[k] for k in fk]}
    return salva(d)


INF_PASSI = lambda n: [["Dima", "Usa la dima fornita: ogni modello ha foro e profondità propri."], ["Traccia", "Appoggia la dima a parete o soffitto e controlla con la livella: i diffusori devono essere paralleli tra loro e perpendicolari al pavimento. Togli il centro della dima, traccia l'interno e segna gli 8 fori."],
    ["Fissa", "Con pannelli in legno rigido usa le viti fornite. Con il cartongesso Elipson consiglia di raddoppiare la lastra e usare tasselli per pareti cave, oppure un telaio interno con listelli."], ["Ancora", f"Usa tutti i {n} punti di ancoraggio."], ["Collega", "Ingressi Speakon o morsetti; cavi in rame OFC di sezione adeguata alla lunghezza."], ["Chiudi", "Monta la griglia. Rodaggio: da 20 a 50 ore a volume moderato."]]


def infinite():
    out = []
    base = {"tipo": "diffusore", "brand": "Elipson", "crop": False, "fonti": [SRC["INF"], SRC["INFI"]]}
    I = imgs(IMG[31611])
    out.append(salva(base | {"id": 31611, "cat": "L", "model": "Infinite 14", "img": I[0],
        "meta": "Elipson Infinite 14: 2 vie in cassa chiusa da incasso per home cinema, 2 woofer 6,5″. Foro, profondità e montaggio per l'installatore.",
        "chiave": ["2 vie · 2 × 6,5″ · 8 Ω", "Foro 310 × 900 mm", "Profondità 112 mm"], "righe": ["2 vie · 2 woofer 6,5″", "Diffusore LCR da incasso", "Infinite"],
        "intro": ["L'<strong>Elipson Infinite 14</strong> è un diffusore da incasso a 2 vie in cassa chiusa per frontali, centrale e surround: 2 woofer da 6,5″ (17 cm) a sandwich Rohacell e fibra di carbonio e tweeter ad anello da 29 mm. 150 W RMS, 91 dB, 8 Ω.", "Foro <strong>310 × 900 mm</strong>, profondità di incasso <strong>112 mm</strong> (100 mm senza staffe)."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["2 vie in cassa chiusa, da incasso.", "2 woofer 6,5″ a sandwich Rohacell e fibra di carbonio.", "Tweeter ad anello da 1,15″ (29 mm).", "Frontale in alluminio satinato, griglia nera.", "Ingressi Speakon e morsetti per banane."]},
                    {"titolo": "Acustica", "voci": ["Potenza: 150 W RMS, 300 W di picco.", "Risposta: 60 Hz – 30 kHz.", "Sensibilità: 91 dB (1 W / 1 m).", "Impedenza: 8 Ω, minima 4 Ω."]},
                    {"titolo": "Dimensioni", "voci": ["Foro: 310 × 900 mm.", "Ingombro: 360 × 950 × 138 mm con griglia (125 mm senza).", "Profondità di incasso: 112 mm con le staffe, 100 mm senza.", "8 punti di ancoraggio.", "Peso: 18 kg."]}],
        "viste": [vista(i, cap(i["alt"])) for i in I[1:]], "misure": {"forma": "rett", "foro": ["310 mm", "900 mm"], "est": ["360 mm", "950 mm"], "prof": "112 mm", "prof_tot": "138 mm", "nota": "Foro tratteggiato in rosso. Misure Elipson; disegno non in scala."},
        "collega": [{"titolo": "Amplificazione", "link": "amplificatori.html", "icona": "sorgente", "voci": ["8 Ω nominali, minimo 4 Ω: amplificatore stabile su carichi bassi.", "Elipson consiglia un amplificatore con potenza RMS superiore a quella nominale del diffusore."]}],
        "sistemi": [{"titolo": "Dove montarlo", "voci": ["Frontali, centrale o surround di un home cinema.", "Parete o soffitto robusti: 18 kg da ancorare su 8 punti."]}, {"titolo": "Montaggio", "passi": INF_PASSI(8)}],
        "nota": "Dati e procedura dal manuale Elipson Infinite, confrontati con la scheda Extrasound.", "extrasound": X + "elipson-infinite-14-diffusore-home-cinema-da-incasso-2-vie-150-w"}))
    I = imgs(IMG[31589])
    out.append(salva(base | {"id": 31589, "cat": "P", "model": "Infinite 8", "img": I[0],
        "meta": "Elipson Infinite 8: 2 vie in cassa chiusa da incasso per home cinema, woofer 6,5″. Foro, profondità e montaggio per l'installatore.",
        "chiave": ["2 vie · 6,5″ · 8 Ω", "Foro 280 × 420 mm", "Profondità 112 mm"], "righe": ["2 vie · woofer 6,5″", "Diffusore da incasso a parete", "Infinite"],
        "intro": ["L'<strong>Elipson Infinite 8</strong> è un diffusore da incasso a 2 vie in cassa chiusa per frontali, centrale, surround e Atmos: woofer 6,5″ a sandwich Rohacell e fibra di carbonio, tweeter ad anello da 29 mm. 100 W RMS, 88 dB, 8 Ω.", "Foro <strong>280 × 420 mm</strong>, profondità di incasso <strong>112 mm</strong> (100 mm senza staffe)."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["2 vie in cassa chiusa, da incasso a parete o soffitto.", "Woofer 6,5″ a sandwich Rohacell e fibra di carbonio.", "Tweeter ad anello da 1,15″ (29 mm).", "Frontale in alluminio satinato, griglia nera.", "Ingressi Speakon e morsetti per banane."]},
                    {"titolo": "Acustica", "voci": ["Potenza: 100 W RMS, 200 W di picco.", "Risposta: 75 Hz – 30 kHz.", "Sensibilità: 88 dB (1 W / 1 m).", "Impedenza: 8 Ω, minima 4 Ω."]},
                    {"titolo": "Dimensioni", "voci": ["Foro: 280 × 420 mm.", "Ingombro: 330 × 440 × 138 mm con griglia (125 mm senza).", "Profondità di incasso: 112 mm con le staffe, 100 mm senza.", "4 punti di ancoraggio.", "Peso: 10 kg."]}],
        "viste": [vista(i, cap(i["alt"])) for i in I[1:]], "misure": {"forma": "rett", "foro": ["280 mm", "420 mm"], "est": ["330 mm", "440 mm"], "prof": "112 mm", "prof_tot": "138 mm", "nota": "Foro tratteggiato in rosso. Misure Elipson; disegno non in scala."},
        "collega": [{"titolo": "Amplificazione", "link": "amplificatori.html", "icona": "sorgente", "voci": ["8 Ω nominali, minimo 4 Ω: amplificatore stabile su carichi bassi."]}],
        "sistemi": [{"titolo": "Dove montarlo", "voci": ["Frontali, centrale, surround o canali Atmos a soffitto."]}, {"titolo": "Montaggio", "passi": INF_PASSI(4)}],
        "nota": "Dati e procedura dal manuale Elipson Infinite, confrontati con la scheda Extrasound. La scheda Extrasound indica 9 kg; il manuale Elipson 10 kg. Fa fede il dato Elipson.", "extrasound": X + "elipson-infinite-8-diffusore-home-cinema-2-vie-in-cassa-chiusa-100-w"}))
    I = imgs(IMG[31598])
    out.append(salva(base | {"id": 31598, "cat": "W", "model": "Infinite S12", "img": I[0],
        "meta": "Elipson Infinite S12: subwoofer passivo da incasso bass-reflex 30 cm. Foro, profondità, amplificazione e montaggio per l'installatore.",
        "chiave": ["Subwoofer passivo · 12″", "Foro 400 × 900 mm", "Profondità 222 mm"], "righe": ["Subwoofer passivo · 12″", "Subwoofer da incasso", "Infinite"],
        "intro": ["L'<strong>Elipson Infinite S12</strong> è un subwoofer passivo da incasso bass-reflex con woofer da 12″ (30 cm), bobina da 3″ e magnete al neodimio: 500 W RMS, 92 dB, 8 Ω, 28 Hz a −3 dB.", "Foro <strong>400 × 900 mm</strong>, profondità di incasso <strong>222 mm</strong> (210 mm senza staffe)."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["Subwoofer passivo da incasso, bass-reflex con due condotti frontali.", "Woofer 12″ a lunga escursione, bobina 3″, magnete al neodimio.", "Frontale in alluminio satinato, copertura acustica nera.", "Ingressi Speakon e morsetti per banane."]},
                    {"titolo": "Acustica", "voci": ["Potenza: 500 W RMS, 1000 W di picco.", "Frequenza minima: 28 Hz (−3 dB).", "Sensibilità: 92 dB (1 W / 1 m).", "Impedenza: 8 Ω, minima 6,5 Ω."]},
                    {"titolo": "Dimensioni", "voci": ["Foro: 400 × 900 mm.", "Ingombro: 450 × 950 × 273 mm con copertura (260 mm senza).", "Profondità di incasso: 222 mm con le staffe, 210 mm senza.", "10 punti di ancoraggio.", "Peso: 33,5 kg."]}],
        "viste": [vista(i, cap(i["alt"])) for i in I[1:]], "misure": {"forma": "rett", "foro": ["400 mm", "900 mm"], "est": ["450 mm", "950 mm"], "prof": "222 mm", "prof_tot": "273 mm", "nota": "Foro tratteggiato in rosso. Misure Elipson; disegno non in scala."},
        "collega": [{"titolo": "Amplificazione", "icona": "subwoofer", "voci": ["Passivo: serve un amplificatore per subwoofer con filtro passa-basso; Elipson indica l'Infinite A1000.", "8 Ω nominali, minimo 6,5 Ω."]}],
        "sistemi": [{"titolo": "Schema", "voci": ["Uscita LFE del processore all'amplificatore, poi al subwoofer."], "zone": [{"label": "LFE dal processore → amplificatore", "tipo": "linea"}, {"label": "Infinite S12 · 8 Ω", "tipo": "sub"}], "apparecchio": "Processore AV"},
                    {"titolo": "Montaggio", "passi": INF_PASSI(10)}],
        "nota": "Dati e procedura dal manuale Elipson Infinite, confrontati con la scheda Extrasound.", "extrasound": X + "elipson-infinite-s12-subwoofer-passivo-da-incasso-30-cm-1000-w"}))
    return out


if __name__ == "__main__":
    for t in AIN:
        print(ain(t))
    for s in infinite():
        print(s)
