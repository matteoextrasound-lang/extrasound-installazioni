"""Schede Garvan Acoustic (collezione Luna). Garvan non pubblica online le schede tecniche dei singoli modelli:
i dati vengono dalle schede Extrasound (ricavate dalle schede Garvan) e sono confrontati con la Quick reference guide
Garvan V2.3 dove il modello compare. Eseguire dalla radice: python3 _strumenti/marchi_garvan.py"""
import sys; sys.path.insert(0, '_strumenti')
from schede_util import *

X = 'https://www.extrasound.it/'
QRG = {"label": "Garvan Acoustic, Quick reference guide V2.3", "url": "https://konferencje.ptwp.pl/download/catalogue/25/9707"}

# id, modello, cat, tipo, driver, aes, sens, spl, r3, r10, imp, disp, hpf, montaggi, foro, ingombro, cover, telai, url, extra
M = [
 (2401, "KR112", "P", "coassiale 2 vie", "woofer 130 mm + tweeter 14 mm", "50 W AES (100 W continui)", "88,5 dB (89 dB a muro)", "117,5 dB", "95 Hz – 20 kHz", "56 Hz – 20 kHz (60 Hz – 20 kHz a muro)", "8 Ω", "110° (1–4 kHz), 90° (1–10 kHz)", "80 Hz (65 Hz a muro)", "CEM", "19,5 × 19,5 cm", "25,0 × 25,0 × 6,4 cm", "quadrata 19 × 19 cm", "telaio CC1919 (cartongesso), telaio frontale CF191S / CF191F (EasyFit)", "garvan-kr112-cassa-da-incasso-filo-muro-o-cartongesso", {"qrg": "La Quick reference guide Garvan indica per il KR112 con telaio EasyFit CF191S 20,6 × 20,6 × 6,7 cm; Extrasound indica una profondità di 6,4 cm."}),
 (2399, "KR111", "S", "coassiale 2 vie", "woofer 130 mm + tweeter 14 mm", "50 W AES (100 W continui)", "88 dB (89 dB a muro)", "117 dB", "95 Hz – 20 kHz (100 Hz – 20 kHz a muro)", "54 Hz – 20 kHz (85 Hz – 20 kHz a muro)", "8 Ω", "90° (1–10 kHz)", "70 Hz", "CEM", "Ø 20,5 cm", "26,0 × 20,0 × 6,8 cm", "tonda Ø 19,3 cm", "telaio CC2020 (cartongesso), telaio frontale CF202S / CF202F (EasyFit)", "garvan-kr111-cassa-da-incasso-filo-muro-o-cartongesso", {}),
 (2385, "KR117", "P", "coassiale 2 vie", "woofer 160 mm + tweeter 14 mm", "50 W AES (100 W continui)", "89,5 dB", "118,5 dB", "80 Hz – 20 kHz", "60 Hz – 20 kHz", "8 Ω", "90° (1–10 kHz)", "60 Hz", "CE", "19,5 × 19,5 cm", "25,0 × 25,0 × 7,85 cm", "quadrata 19 × 19 cm", "telaio CC1919 (cartongesso), telaio frontale CF191S / CF191F (EasyFit)", "garvan-kr117-cassa-da-incasso-filo-muro-per-cartongesso", {}),
 (2381, "KR118", "S", "coassiale 2 vie", "woofer 160 mm + tweeter 14 mm", "50 W AES (100 W continui)", "89,5 dB", "118,5 dB", "80 Hz – 20 kHz", "60 Hz – 20 kHz", "8 Ω", "90° (1–10 kHz)", "60 Hz", "CE", "Ø 20,5 cm", "26,0 × 20,0 × 7,8 cm", "tonda Ø 19,3 cm", "telaio CC2020 (cartongesso), telaio frontale CF202S / CF202F (EasyFit)", "garvan-kr118-cassa-da-incasso-filo-muro-per-cartongesso", {}),
 (2391, "KR117N30", "P", "coassiale 2 vie inclinato di 30°", "woofer 160 mm + tweeter 14 mm", "50 W AES (100 W continui)", "91 dB", "120 dB", "80 Hz – 20 kHz (84 Hz – 20 kHz a muro)", "60 Hz – 20 kHz (56 Hz – 20 kHz a muro)", "8 Ω", "90°", "60 Hz", "CEM", "28,5 × 28,5 cm (cartongesso)", "34,0 × 34,0 × 16,0 cm", "quadrata 28 × 28 cm", "telaio CR2828 (cartongesso)", "garvan-kr117n30-cassa-da-incasso-inclinata-30-filo-muro", {"incl": True}),
 (2400, "KR207", "2", "stereo, 2 larga banda", "2 altoparlanti a larga banda da 76 mm", "40 + 40 W AES (80 + 80 W continui)", "83,5 dB per canale", "111,5 dB per canale, 117,5 dB in totale", "115 Hz – 16 kHz", "85 Hz – 20 kHz (87 Hz – 20 kHz a muro)", "8 + 8 Ω", "90° (1–10 kHz)", "80 Hz", "CEM", "Ø 20,5 cm", "26,0 × 20,0 × 6,8 cm", "tonda Ø 19,3 cm", "telaio CC2020 (cartongesso), telaio frontale CF202S / CF202F (EasyFit)", "garvan-kr207-cassa-da-incasso-stereo-filo-muro-o-cartongesso", {"ds": True}),
 (2402, "KR208", "2", "stereo, 2 larga banda", "2 altoparlanti a larga banda da 76 mm", "40 + 40 W AES (80 + 80 W continui)", "83,5 dB per canale", "111,5 dB per canale, 117,5 dB in totale", "115 Hz – 16 kHz", "85 Hz – 20 kHz (87 Hz – 20 kHz a muro)", "8 + 8 Ω", "oltre 120° (1–4 kHz), 90° (1–10 kHz)", "80 Hz", "CEM", "19,5 × 19,5 cm", "25,0 × 25,0 × 6,8 cm", "quadrata 19 × 19 cm", "telaio CC1919 (cartongesso), telaio frontale CF191S / CF191F (EasyFit)", "garvan-kr208-cassa-stereo-da-incasso-filo-muro-19x19-cm", {"ds": True}),
 (2403, "KR213", "P", "2 vie", "woofer 130 mm + tweeter 25 mm", "80 W AES (160 W continui)", "88 dB", "119 dB", "80 Hz – 20 kHz", "58 Hz – 20 kHz", "8 Ω", "oltre 120° (1–4 kHz), 120° (1–10 kHz)", "55 Hz", "M", None, "34,0 × 25,0 × 7,6 cm", "28 × 19 cm", "cassaforma CM1928 (muratura)", "garvan-kr213-cassa-da-incasso-hi-fi-filo-muro-44x19-cm", {}),
 (2405, "KR316", "P", "2 vie con radiatore passivo", "woofer 130 mm + tweeter 25 mm + radiatore passivo 160 mm", "80 W AES (160 W continui)", "87,5 dB", "118,5 dB", "60 Hz – 20 kHz", "48 Hz – 20 kHz", "8 Ω", "120° (1–10 kHz)", "40 Hz", "M", None, "50,0 × 25,0 × 7,6 cm", "44 × 19 cm", "cassaforma CM1944 (muratura)", "garvan-kr316-cassa-da-incasso-hi-fi-filo-muro-44x19", {}),
 (2406, "KR313", "L", "2 vie D'Appolito", "2 woofer 130 mm + tweeter 25 mm", "160 W AES (320 W continui)", "93 dB", "124 dB", "65 Hz – 20 kHz", "57 Hz – 20 kHz", "4 Ω", "oltre 120° (1–4 kHz), 120° (1–10 kHz)", "55 Hz", "M", None, "50,0 × 25,0 × 7,6 cm", "44 × 19 cm", "cassaforma CM1944 (muratura)", "garvan-kr313-cassa-da-incasso-left-center-right-filo-muro", {}),
 (2390, "KR513", "L", "2 vie", "4 woofer 130 mm + tweeter 32 mm", "300 W AES (600 W continui)", "92,5 dB", "129 dB", "70 Hz – 20 kHz", "58 Hz – 20 kHz", "8 Ω", "oltre 120° (1–4 kHz), 80° (1–10 kHz)", "60 Hz", "MC", None, "86,0 × 25,0 × 9,95 cm", "80 × 19 cm", "cassaforma CR1981 (muratura); telaio dedicato per cartongesso", "garvan-kr513-cassa-da-incasso-left-center-right-filo-muro", {"qrg": "La Quick reference guide Garvan indica per il KR513 82,0 × 21,0 × 9,9 cm con cover 72CXS3 e cassaforma CR1981; Extrasound indica un ingombro di 86,0 × 25,0 × 9,95 cm."}),
 (2389, "KC316", "L", "2 vie D'Appolito", "2 woofer 160 mm + tweeter 25 mm", "150 W AES (300 W continui)", "93 dB", "124 dB", "58 Hz – 20 kHz", "41 Hz – 20 kHz", "4 Ω", "90° (1–10 kHz)", "40 Hz", "C", "44,5 × 19,5 cm", "50,0 × 25,0 × 8,3 cm", "44 × 19 cm", "telaio CC1944 (cartongesso)", "garvan-kc316-diffusore-lcr-da-incasso-filo-muro-44x19-cm-2", {}),
 (2398, "KR16M", "E", "2 vie, marino", "woofer 160 mm + tweeter 20 mm", "150 W AES (300 W continui)", "86,5 dB", "120,5 dB", "60 Hz – 20 kHz", "50 Hz – 20 kHz", "8 Ω", "120° (1–10 kHz)", "45 Hz", "MC", None, "50,5 × 25,5 × 10,5 cm", "44 × 19 cm", "cassaforma da murare (muratura); telaio dedicato per cartongesso", "garvan-kr16m-diffusore-marino-da-incasso-filo-muro-44x19-cm", {"marino": True}),
 (2387, "KC216", "P", "2 vie", "woofer 160 mm + tweeter 25 mm", "75 W AES (150 W continui)", "87,5 dB", "118 dB", "60 Hz – 20 kHz", "53 Hz – 20 kHz", "8 Ω", "90° (1–10 kHz)", "55 Hz", "C", "28,5 × 19,5 cm", "34,0 × 25,0 × 8,3 cm", "28 × 19 cm", "telaio CC1928 (cartongesso)", "garvan-kc216-cassa-da-incasso-hi-fi-filo-muro-28x19", {}),
]

IMG = {
 2401: "Garvan-KR112.jpg » Garvan KR112 da incasso con telaio e cover quadrata, due esemplari ;; Garvan-KR112-lifestyle-1.jpg » Cover nera quadrata della serie Luna su parete grigia ;; Garvan-KR112-lifestyle-3.jpg » Cover nera quadrata della serie Luna su parete metallizzata",
 2399: "Garvan-Luna-kr111.jpg » Garvan KR111 da incasso con telaio e cover tonda, due esemplari ;; Garvan-Luna-kr111-griglia-easy-fit.jpg » Cover tonda microforata della serie Luna a filo soffitto ;; Garvan-Luna-kr111-griglia-inox.jpg » Cover tonda in acciaio spazzolato della serie Luna",
 2385: "Garvan-KR117.jpg » Garvan KR117 da incasso con telaio e cover quadrata, due esemplari ;; Garvan-KR112-lifestyle-4.jpg » Cover rossa quadrata della serie Luna su carta da parati ;; Garvan-KR112-lifestyle-3.jpg » Cover nera quadrata della serie Luna su parete metallizzata",
 2381: "Garvan-Luna-kr118.jpg » Garvan KR118 da incasso con telaio e cover tonda, due esemplari ;; Garvan-Luna-kr111-griglia-inox.jpg » Cover tonda in acciaio spazzolato della serie Luna ;; Garvan-Luna-kr111-griglia-easy-fit.jpg » Cover tonda microforata della serie Luna a filo soffitto",
 2391: "garvan-sir16n-1.jpg » Garvan KR117N30 con altoparlante inclinato e telaio da incasso ;; virtuemart/product/garvan-sir16n-lifestyle.jpg » Diffusori da incasso Garvan a filo parete in un soggiorno",
 2400: "Garvan-Luna-kr207.jpg » Garvan KR207 stereo da incasso con telaio e cover tonda, due esemplari ;; Garvan-Luna-kr111-griglia-easy-fit.jpg » Cover tonda microforata della serie Luna a filo soffitto ;; Garvan-Luna-kr111-griglia-inox.jpg » Cover tonda in acciaio spazzolato della serie Luna",
 2402: "Garvan-kr208.jpg » Garvan KR208 stereo da incasso con telaio e cover quadrata, due esemplari ;; Garvan-KR112-lifestyle-4.jpg » Cover rossa quadrata della serie Luna su carta da parati ;; Garvan-KR112-lifestyle-3.jpg » Cover nera quadrata della serie Luna su parete metallizzata",
 2403: "virtuemart/product/garvan-sim213.jpg » Garvan KR213 da incasso con cassaforma e cover ;; virtuemart/product/garvan-sim213-lifestyle.jpg » Cover Garvan KR213 a filo su parete scura ;; Garvan-KR213-griglia-magnetica-bianca.jpg » Cover bianca Garvan KR213 a filo parete",
 2405: "virtuemart/category/extrasound-garvan-sim316.jpg » Garvan KR316 da incasso con cassaforma e cover ;; virtuemart/product/garvan-sim316-lifestyle.jpg » Cover Garvan KR316 a filo parete accanto a un quadro",
 2406: "Garvan-KR313.jpg » Garvan KR313 da incasso con due woofer, tweeter, cassaforma e cover ;; Garvan-KR313-crossover.jpg » Componenti interni del crossover Garvan",
 2390: "garvan-sir513.jpg » Garvan KR513 da incasso con quattro woofer e cover ;; virtuemart/product/garvan-sir513-lifestyle.jpg » Cover Garvan KR513 a filo su parete in pietra scura",
 2389: "garvan-sic316.jpg » Garvan KC316 da incasso con due woofer, tweeter e telaio ;; virtuemart/product/garvan-sic316-lifestyle.jpg » Garvan KC316 a filo parete sotto il televisore",
 2387: "Garvan-KC216-diffusore-incasso.jpg » Garvan KC216 da incasso con telaio e cover ;; Garvan-KC216-griglia-cornice.jpg » Cover rossa Garvan KC216 a filo parete ;; Garvan-KC216-griglia-verde.jpg » Cover verde Garvan KC216 su parete decorata",
 2398: "sir16M.jpg » Diffusore marino Garvan KR16M da incasso con telaio e cover",
 2393: "garvan-wic125.jpg » Subwoofer da incasso Garvan WIC125 con telaio e cover",
}
TIPO = {"E": "Diffusore marino da incasso", "P": "Diffusore da incasso a parete o soffitto", "S": "Diffusore da incasso a soffitto o parete", "L": "Diffusore LCR da incasso",
        "2": "Diffusore stereo da incasso", "W": "Subwoofer passivo da incasso"}
MONT = {"C": "FlushMount™ su cartongesso", "E": "EasyFit™", "M": "FlushMount™ a muro"}


def caption(alt):
    a = alt.lower()
    for k, v in (("lifestyle", "Installato"), ("soggiorno", "Installato"), ("parete", "Installato"), ("crossover", "Crossover"), ("cover", "Cover"), ("telaio", "Con telaio")):
        if k in a:
            return v
    return "Vista"


def montaggio_testo(m, telai):
    v = []
    if "C" in m:
        v.append("FlushMount™ su cartongesso: telaio da rasare nella lastra (da 12,5 a 25 mm); la cover resta perfettamente a filo.")
    if "E" in m:
        v.append("EasyFit™: telaio frontale in acciaio spazzolato o primer bianco, da montare a lavori finiti su cartongesso, legno, metallo o gres (da 4 a 40 mm), senza stuccare né tinteggiare.")
    if "M" in m:
        v.append("FlushMount™ a muro: cassaforma da murare, per pareti in muratura di almeno 90 mm.")
    v.append(f"Accessori: {telai}.")
    return v


def scheda(t):
    (id, mod, cat, tipo_s, drv, aes, sens, spl, r3, r10, imp, disp, hpf, m, foro, ing, cover, telai, url, ex) = t
    tipo = TIPO[cat]
    I = imgs(IMG[id])
    car = [f"{tipo}, collezione Luna™, progettato e costruito in Italia.", f"Tipo: {tipo_s}.", f"Altoparlanti: {drv}.", "Nessuna parte in plastica; cover magnetica intercambiabile, a filo della superficie.",
           f"Cover: {cover}.", "Venduto singolarmente; tipo di montaggio e cover si scelgono nella scheda Extrasound."]
    if ex.get("marino"):
        car.insert(2, "Per esterni, barche, saune e bagni turchi: da −25 a +70 °C.")
    if ex.get("incl"):
        car.insert(2, "Altoparlante inclinato di 30° per orientare il suono verso la zona d'ascolto.")
    acu = [f"Potenza: {aes}.", f"Sensibilità (2,83 V / 1 m): {sens}.", f"SPL massimo calcolato: {spl}.", f"Risposta (−3 dB): {r3}.", f"Gamma (−10 dB): {r10}.",
           f"Impedenza: {imp}.", f"Dispersione: {disp}.", f"Passa-alto consigliato: {hpf}, 48 dB/ottava."]
    dim = ([f"Foro: {foro}."] if foro else ["Foro: si mura la cassaforma (misure del vano da confermare con Garvan)."]) + \
          [f"Ingombro installato: {ing}.", "Collegamenti a pressione, cavi da 18 a 15 AWG (circa 0,8 – 1,6 mm²)."] + montaggio_testo(m, telai)
    mis = None
    if foro:
        p = ing.split(" × ")[-1]
        if foro.startswith("Ø"):
            mis = {"forma": "tondo", "foro": foro.replace("Ø ", ""), "prof": p}
        else:
            a, b = foro.replace(" (cartongesso)", "").replace(" cm", "").split(" × ")
            e = ing.replace(" cm", "").split(" × ")
            if float(a.replace(",", ".")) >= float(b.replace(",", ".")):
                mis = {"forma": "rett", "orizzontale": a != b and cat == "L", "foro": [f"{a} cm", f"{b} cm"], "est": [f"{e[0]} cm", f"{e[1]} cm"], "prof": p}
            if a != b and cat != "L":
                mis = {"forma": "rett", "foro": [f"{b} cm", f"{a} cm"], "est": [f"{e[1]} cm", f"{e[0]} cm"], "prof": p}
        if mis:
            mis["nota"] = "Foro tratteggiato in rosso; profondità = ingombro installato. Disegno non in scala."

    if ex.get("ds"):
        v = ["Due ingressi, uno per canale: sinistro e destro dello stesso amplificatore, 8 Ω per canale.", "Per stanze piccole e corridoi dove c'è posto per un solo diffusore."]
    else:
        v = [f"{imp}: un diffusore per canale su qualsiasi amplificatore da installazione."]
        if imp.startswith("4"):
            v.append("Carico da 4 Ω: amplificatore stabile a 4 Ω, niente parallelo sullo stesso canale.")
    v.append(f"Garvan consiglia un passa-alto a {hpf}, 48 dB/ottava: serve un amplificatore o un processore con DSP. Garvan fornisce preset EQ, filtri e protezioni.")
    col = [{"titolo": "Amplificazione", "link": "amplificatori.html", "icona": "sorgente", "voci": v}]
    if cat in ("P", "S", "2"):
        col.append({"titolo": "Linee 70 / 100 V", "icona": "linea100v", "voci": ["Con i trasformatori opzionali Garvan TRT052 e TRT054 (dato Extrasound)."]})

    dove = ["Progetta la posizione prima di chiudere pareti e controsoffitti: telai e casseforme vanno posati in corso d'opera (EasyFit escluso)."]
    if cat == "L":
        dove.insert(0, "Canali frontali e centrale dell'home theater, sopra o sotto lo schermo.")
    if ex.get("ds"):
        dove.insert(0, "Al centro della stanza: un solo punto per i due canali.")
    sist = [{"titolo": "Dove montarlo", "voci": dove}]
    if ex.get("ds"):
        sist.append({"titolo": "Schema", "voci": ["Un solo diffusore riceve i due canali."], "zone": [{"label": f"{mod} · L + R", "tipo": "2"}], "apparecchio": "Amplificatore"})
    passi = []
    if "M" in m:
        passi.append(["Mura la cassaforma", "In fase di muratura posa la cassaforma a filo del finito, in parete di almeno 90 mm, e porta il cavo all'interno."])
    if "C" in m:
        passi.append(["Telaio nel cartongesso", f"Taglia il foro ({foro or 'secondo il telaio'}) nella lastra da 12,5 – 25 mm, fissa il telaio e rasalo insieme alla parete."])
    if "E" in m:
        passi.append(["Oppure EasyFit", "A lavori finiti: foro, telaio frontale EasyFit sulla superficie (4 – 40 mm), senza stucco né tinta."])
    passi += [["Collega", "Cavo da 18 a 15 AWG nei morsetti a pressione, rispettando la polarità."],
              ["Inserisci e chiudi", "Monta l'altoparlante nel telaio e applica la cover magnetica a filo. Procedura di dettaglio sul foglio di istruzioni Garvan fornito con il telaio."]]
    sist.append({"titolo": "Montaggio", "passi": passi})

    righe0 = f"{tipo_s.split(',')[0]} · {drv.split(' + ')[0]}"
    chiave = [f"{tipo_s.split(',')[0]} · {imp}", f"Foro {foro}" if foro else "Cassaforma da murare", f"Profondità {ing.split(' × ')[-1]}"]
    nota = "Garvan non pubblica online la scheda tecnica di questo modello: dati dalla scheda Extrasound, ricavata dalla documentazione Garvan. Da verificare sul foglio di istruzioni fornito con il prodotto."
    if ex.get("qrg"):
        nota += " " + ex["qrg"]
    intro = [f"Il <strong>Garvan {mod}</strong> è un {tipo[0].lower() + tipo[1:]} della collezione Luna™: {drv}, {aes}, {sens}, {imp}.",
             f"Montaggio: {', '.join(MONT[c] for c in m)}. " + (f"Foro <strong>{foro}</strong>, ingombro <strong>{ing}</strong>." if foro else f"Ingombro installato <strong>{ing}</strong>.")]
    d = {"id": id, "tipo": "diffusore", "cat": cat, "brand": "Garvan", "model": mod, "crop": False,
         "meta": f"Garvan {mod}: {righe0}, {tipo[0].lower() + tipo[1:]} a filo. Foro, telai, montaggio e collegamenti per l'installatore.",
         "img": I[0], "chiave": chiave, "righe": [righe0, tipo, "Collezione Luna™"], "intro": intro,
         "colonne": [{"titolo": "Caratteristiche", "voci": car}, {"titolo": "Acustica", "voci": acu}, {"titolo": "Installazione", "voci": dim}],
         "viste": [vista(i, caption(i["alt"])) for i in I[1:4]], "misure": mis, "collega": col, "sistemi": sist,
         "nota": nota, "extrasound": X + url, "fonti": [QRG] if ex.get("qrg") else []}
    if cat == "E":
        d.update(lista="esterno.html", lista_label="Da esterno", tab="Diffusori<br>da esterno")
    return salva(d)


def wic125():
    I = imgs(IMG[2393])
    d = {"id": 2393, "tipo": "diffusore", "cat": "W", "brand": "Garvan", "model": "WIC125", "crop": False,
         "meta": "Garvan WIC125: subwoofer passivo da incasso 25 cm a doppia bobina, per cartongesso a filo. Foro, telaio e collegamenti per l'installatore.",
         "img": I[0], "chiave": ["Subwoofer passivo · 25 cm", "Foro 28,5 × 28,5 cm", "Profondità 12,1 cm"],
         "righe": ["Subwoofer passivo · 25 cm", "Subwoofer da incasso", "Collezione Luna™"],
         "intro": ["Il <strong>Garvan WIC125</strong> è un subwoofer passivo da incasso a filo per cartongesso, collezione Luna™: woofer da 25 cm a doppia bobina, 80 + 80 W RMS, 94 dB, 4 + 4 Ω.",
                   "Foro <strong>28,5 × 28,5 cm</strong>, ingombro installato <strong>34,0 × 34,0 × 12,1 cm</strong>, telaio CC2828."],
         "colonne": [{"titolo": "Caratteristiche", "voci": ["Subwoofer passivo da incasso a filo, collezione Luna™.", "Woofer 25 cm, cono in carta trattata, sospensione in tessuto, doppia bobina.", "Cover 28 × 28 cm a filo.", "Peso dell'altoparlante: 3,1 kg."]},
                     {"titolo": "Acustica", "voci": ["Potenza: 80 + 80 W RMS, 160 + 160 W massimi.", "Risposta: 34 – 200 Hz.", "Sensibilità (2,83 V / 1 m): 94 dB.", "Impedenza: 4 + 4 Ω (doppia bobina)."]},
                     {"titolo": "Installazione", "voci": ["Foro nel cartongesso: 28,5 × 28,5 cm.", "Ingombro installato: 34,0 × 34,0 × 12,1 cm.", "Telaio CC2828; nella scheda Extrasound si sceglie lo spessore del cartongesso e il tipo di griglia."]}],
         "viste": [], "misure": {"forma": "rett", "foro": ["28,5 cm", "28,5 cm"], "est": ["34,0 cm", "34,0 cm"], "prof": "12,1 cm", "nota": "Foro tratteggiato in rosso; profondità = ingombro installato. Disegno non in scala."},
         "collega": [{"titolo": "Amplificazione", "icona": "subwoofer", "voci": ["Passivo: serve un amplificatore con filtro passa-basso; Garvan propone il suo amplificatore dedicato.", "Doppia bobina 4 + 4 Ω: due canali (uno per bobina) oppure le bobine collegate secondo lo schema Garvan."]}],
         "sistemi": [{"titolo": "Schema 2.1", "voci": ["Coppia di diffusori Luna (es. KR112 o KR111) e WIC125 sullo stesso impianto, con passa-alto sui satelliti e passa-basso sul subwoofer."],
                      "zone": [{"label": "Diffusori Luna · L + R", "tipo": "2"}, {"label": "WIC125 · passa-basso", "tipo": "sub"}], "apparecchio": "Amplificatore con DSP"},
                     {"titolo": "Montaggio", "passi": [["Prevedi il vano", "Prima di chiudere pareti e controsoffitti: almeno 12,1 cm di profondità libera."], ["Telaio", "Taglia il foro 28,5 × 28,5 cm, fissa il telaio CC2828 e rasalo con la lastra."], ["Collega", "Cavi di potenza sulle due bobine rispettando la polarità."], ["Chiudi", "Monta il woofer e la cover a filo."]]}],
         "nota": "Garvan non pubblica online la scheda tecnica di questo modello: dati dalla scheda Extrasound. Collegamento delle due bobine da verificare sulle istruzioni Garvan.",
         "extrasound": X + "garvan-wic125-subwoofer-da-incasso-a-filo-muro", "fonti": []}
    return salva(d)


if __name__ == "__main__":
    for t in M:
        print(scheda(t))
    print(wic125())
