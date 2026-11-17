"""Schede home cinema (categoria H): processori AV e finali multicanale.
Dati dalle schede Extrasound, verificati con le pagine e le schede dei produttori dove indicato.
Eseguire dalla radice: python3 _strumenti/marchi_homecinema.py"""
import sys, json; sys.path.insert(0, '_strumenti')
from schede_util import *

X = 'https://www.extrasound.it/'
def F(l, u): return {"label": l, "url": u}
def z(label, tipo="2"): return {"label": label, "tipo": tipo}
def spk(slug):
    f = DATI / f"{slug}.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"brand": "", "model": slug, "img": {"src": "", "alt": ""}}
def card(slug, voci, titolo=None):
    d = spk(slug)
    if not d["img"]["src"]:
        return {"titolo": titolo or slug, "link": f"scheda-{slug}.html", "icona": "sorgente", "voci": voci}
    return {"titolo": titolo or f"{d['brand']} {d['model']}", "link": f"scheda-{slug}.html", "img": d["img"]["src"], "alt": d["img"]["alt"], "voci": voci}

SUB = {"titolo": "Subwoofer", "icona": "subwoofer"}
CTRL = {"titolo": "Controllo", "icona": "domotica"}

# ---------------- dati ----------------
P = []  # schede: dict già nella forma finale (senza img, che si risolve sotto)


ESCLUSI = {"marantz-av-10", "marantz-av-20", "marantz-av7706", "nad-m17-v2i", "nad-m28", "marantz-mm7025", "marantz-mm7055", "marantz-mm8077"}  # non specifici da installazione


def scheda(id, brand, model, url, kind, chiave, righe, intro, car, ing, usc, imgs_spec, gui_cap, conf, collega, nota, fonti, slug=None):
    if (slug or globals()["slug"](f"{brand} {model}")) in ESCLUSI:
        return None
    I = imgs(imgs_spec)
    front, retro = I[0], next((i for i in I if any(k in i["alt"].lower() for k in ("posteriore", "retro"))), None)
    guiimg = next((i for i in I if "frontal" in i["alt"].lower() and i is not front), front)
    d = {"id": id, "tipo": "amplificatore", "cat": "H", "brand": brand, "model": model, "crop": True,
         "tab": "Home<br>cinema", "lista": "home-cinema.html", "lista_label": "Home cinema",
         "tipo_label": "Processore AV" if kind == "P" else "Finale multicanale",
         "meta": f"{brand} {model}: {righe[0].lower()}, {righe[1].lower()}. Ingressi, uscite, configurazioni e collegamenti per l'installatore.",
         "img": front, "chiave": chiave, "righe": righe, "intro": intro,
         "colonne": [{"titolo": "Caratteristiche", "voci": car}, {"titolo": "Ingressi", "voci": ing}, {"titolo": "Uscite", "voci": usc}],
         "collega": collega, "gui": {"src": guiimg["src"], "alt": guiimg["alt"], "caption": gui_cap},
         "sistemi": conf, "nota": nota, "extrasound": X + url, "fonti": fonti}
    if retro:
        d["retro"] = {"src": retro["src"], "alt": retro["alt"], "titolo": "Pannello posteriore", "caption": "Ingressi, uscite e collegamenti di controllo."}
    if slug:
        d["slug"] = slug
    return salva(d)


ESTR = "Dati dalla scheda Extrasound"


def run():
    out = []
    INF14 = lambda v: card("elipson-infinite-14", v)
    THX = lambda v: card("kef-ci3160rlm-thx", v)
    S66 = lambda v: card("jbl-studio-66lcr", v)
    S12 = lambda v: card("elipson-infinite-s12", v)
    atmos714 = lambda fin: {"titolo": "7.1.4 · Dolby Atmos", "voci": ["Frontali, centrale, 4 surround, 4 altezze e subwoofer.", f"Le uscite pre vanno al finale ({fin})."],
                            "zone": [z("Frontali L · C · R", "3"), z("Surround e surround back", "4"), z("Altezze Atmos", "4"), z("Subwoofer · LFE", "sub")]}

    # ---------- processori ----------
    out.append(scheda(65963, "Arcam", "AV41", "arcam-av41-processore-av-16-canali-uscite-xlr-dirac-live-hdmi-2-1", "P",
        ["Processore AV · 16 canali", "7 HDMI 2.1 · 8K/60", "Dirac Live · XLR"], ["16 canali · Dolby Atmos", "Processore AV", "Rack o libero"],
        ["L'<strong>Arcam AV41</strong> è un processore AV a 16 canali con decodifica Dolby Atmos, DTS:X e Auro-3D, 7 ingressi HDMI 2.1 e uscite XLR e RCA per tutti i canali.",
         "Si abbina ai finali Arcam PA720 e PA410; correzione ambientale Dirac Live, controllo RS232, IR e IP."],
        ["Decodifica 16 canali: Dolby Atmos, DTS:X, Auro-3D.", "Video 8K a 60 Hz e 4K a 120 Hz; Dolby Vision, HDR10+, HDR10, HLG.", "DAC: 2 × ESS 9026PRO.", "Streaming: AirPlay 2, Chromecast, Spotify Connect, Tidal Connect, Roon Ready; Bluetooth aptX HD.",
         "Consumo 50 W massimi, 40 W a riposo, < 0,5 W in standby.", "433 × 425 × 171 mm, 10,6 kg."],
        ["7 HDMI 2.1, HDCP 2.3, eARC.", "Ingressi stereo: sensibilità 1, 2 o 4 V, 47 kΩ.", "Wi-Fi, Ethernet, RS232, IR.", "Microfono di calibrazione incluso."],
        ["3 HDMI (compresa Zona 2).", "16 XLR: 2 V nominali, 10 V massimi.", "RCA: 1 V nominale, 5 V massimi, 560 Ω.", "Cuffie: 5 V su 32 Ω."],
        "arcam-av41-1-1000.jpg » Arcam AV41 processore AV, vista frontale ;; arcam-av41-3-1000.jpg » Arcam AV41, pannello posteriore con i collegamenti",
        "Si configura dal menu a schermo; Dirac Live per la correzione ambientale; controllo da RS232, IR e rete.",
        [atmos714("Arcam PA720 + PA410"), {"titolo": "9.1.6 · 16 canali", "voci": ["Tutti i 16 canali assegnati: 9 sul piano d'ascolto, 6 altezze, subwoofer."], "zone": [z("Frontali L · C · R", "3"), z("Surround, back e wide", "4"), z("Wide aggiuntivi", "2"), z("Altezze Atmos", "4"), z("Altezze aggiuntive", "2"), z("Subwoofer · LFE", "sub")]}],
        [card("arcam-pa720", ["Finale a 7 canali per frontali e surround, ingressi XLR."], "Con l'Arcam PA720"), INF14(["Frontali e centrale da incasso, 8 Ω."]), SUB | {"voci": ["Subwoofer attivi sulle uscite sub, oppure passivi con un finale dedicato."]}, CTRL | {"voci": ["RS232, IR ed Ethernet verso il sistema di controllo."]}],
        ESTR + ", confrontata con la pagina Arcam.", []))
    out.append(scheda(65971, "Arcam", "AVP45", "arcam-avp45-processore-av-16-canali-uscite-xlr-auro-3d-dirac-live", "P",
        ["Processore AV · 16 canali", "7 HDMI 2.1a · 8K", "XLR · Auro-3D · IMAX"], ["16 canali · Dolby Atmos", "Processore AV", "Rack o libero"],
        ["L'<strong>Arcam AVP45</strong> è un processore AV a 16 canali assegnabili con Dolby Atmos, DTS:X, IMAX Enhanced, Auro-3D e MPEG-H, 7 ingressi HDMI 2.1a e uscite XLR e RCA per tutti i canali.",
         "Streaming integrato, display a colori da 6,5″, Bluetooth 5.4."],
        ["16 canali assegnabili; Dolby Atmos, TrueHD, DTS:X, DTS-HD MA, IMAX Enhanced, Auro-3D, MPEG-H.", "HDMI 2.1a, HDCP 2.3, 8K a 60 Hz o 4K a 120 Hz; HDR10, HDR10+, Dolby Vision, HLG; VRR, ALLM, eARC.",
         "Streaming: Spotify, Tidal e Qobuz Connect, Roon Ready, AirPlay, Google Cast, UPnP, fino a 24 bit / 192 kHz.", "Consumo 50 W massimi.", "432 × 399 × 170 mm, 9,4 kg."],
        ["7 HDMI (Zona 1).", "3 RCA, 1 XLR, 2 coassiali, 2 ottici.", "Bluetooth 5.4 (AAC, LE Audio, Auracast)."],
        ["2 HDMI Zona 1, 1 HDMI Zona 2.", "16 XLR (5 V di picco).", "16 RCA (2 V)."],
        "arcam-avp45-1-1000.jpg » Arcam AVP45 processore AV, vista frontale ;; arcam-avp45-2-1000.jpg » Arcam AVP45, vista di tre quarti ;; arcam-avp45-3-1000.jpg » Arcam AVP45, pannello posteriore con i collegamenti",
        "Si configura dal menu a schermo e dal display frontale; correzione ambientale Dirac Live.",
        [atmos714("Arcam PA720 + PA410"), {"titolo": "Zona 2", "voci": ["Sala principale in 7.1.4 e una seconda zona con la sua uscita HDMI."], "zone": [z("Sala · 7.1.4", "4"), z("Zona 2 · HDMI e uscita stereo", "2")]}],
        [card("arcam-pa720", ["Finale a 7 canali, ingressi XLR."], "Con l'Arcam PA720"), THX(["LCR da incasso THX, 4 Ω: serve un finale robusto."]), SUB | {"voci": ["Subwoofer sulle uscite assegnate."]}, CTRL | {"voci": ["Rete, IR e RS232."]}],
        ESTR + ".", []))
    out.append(scheda(46164, "NAD", "M17 V2i", "nad-m17-v2i-pre-processore-home-cinema-11-1-con-dirac-live-e-bluos", "P",
        ["Processore AV · 11.1", "Dirac Live · BluOS", "XLR e RCA"], ["11.1 · Dolby Atmos", "Processore AV", "Masters Series"],
        ["Il <strong>NAD M17 V2i</strong> è un pre-processore home cinema 11.1 con Dolby Atmos e DTS:X, uscite XLR e RCA, Dirac Live Full Bandwidth e streaming BluOS.",
         "Si abbina al finale NAD M28 a 7 canali."],
        ["Formati: Dolby Atmos, DTS:X.", "Distorsione < 0,005%; toni ±10 dB.", "Dirac Live Full Bandwidth inclusa.", "435 × 156 × 386 mm, 10,9 kg."],
        ["HDMI 4K UHD, HDR, HDCP.", "Ethernet gigabit, BluOS con MQA.", "Trigger 12 V, RS-232."],
        ["11.1 XLR e RCA."],
        "NAD-M17-V2i.jpg » NAD M17 V2i, vista frontale ;; NAD-M17-V2i-rear.jpg » NAD M17 V2i, pannello posteriore",
        "Si configura dal menu e dall'app BluOS; Dirac Live per la correzione ambientale.",
        [atmos714("NAD M28"), {"titolo": "5.1.2 con un solo finale", "voci": ["Il NAD M28 a 7 canali basta per un 5.1.2."], "zone": [z("Frontali L · C · R", "3"), z("Surround", "2"), z("Altezze Atmos", "2"), z("Subwoofer · LFE", "sub")]}],
        [card("nad-m28", ["Finale a 7 canali da 200 W su 8 Ω."], "Con il NAD M28"), INF14(["Frontali e centrale da incasso."]), SUB | {"voci": ["Subwoofer attivo sull'uscita sub."]}, CTRL | {"voci": ["Trigger 12 V e RS-232."]}],
        ESTR + ".", []))
    for (id, mod, url, ch, hdmi, peso, conf2) in ((46111, "MP-40 2.1", "lyngdorf-mp-40-2-1-processore-home-cinema-12-canali-hdmi-2-1-roomperfect", 12, 3, "6,7 kg", ("7.1.4 · 12 canali", [z("Frontali L · C · R", "3"), z("Surround e back", "4"), z("Altezze Atmos", "4"), z("Subwoofer", "sub")])),
                                                   (46100, "MP-60 2.1", "lyngdorf-mp-60-2-1-processore-home-cinema-16-canali-hdmi-2-1-roomperfect", 16, 5, "9 kg", ("9.1.6 · 16 canali", [z("Frontali L · C · R", "3"), z("Surround, back e wide", "4"), z("Wide aggiuntivi", "2"), z("Altezze Atmos", "4"), z("Altezze aggiuntive", "2"), z("Subwoofer", "sub")]))):
        out.append(scheda(id, "Lyngdorf", mod, url, "P",
            [f"Processore · {ch} canali", f"{hdmi} HDMI 2.1 · 8K", "RoomPerfect · 16 XLR"], [f"{ch} canali · Dolby Atmos", "Processore home cinema", "Rack 4U"],
            [f"Il <strong>Lyngdorf {mod}</strong> è un processore home cinema a {ch} canali di decodifica con Dolby Atmos, DTS:X e Auro-3D, {hdmi} ingressi HDMI 2.1 e 16 uscite XLR.",
             "Correzione ambientale RoomPerfect™ con microfono incluso; rack 4U. Si abbina al finale Lyngdorf MXA-8400."],
            [f"{ch} canali di decodifica e upmixing: Dolby Atmos, DTS:X, Auro-3D; Dolby Surround, Auro-Matic, DTS Neural:X.", "Risposta ±0,5 dB 20 Hz – 20 kHz; THD 0,005%.", "RoomPerfect™, Subwoofer Level Assistant, 32 voicing.",
             "Streaming: radio Internet, AirPlay 2, Spotify Connect, TIDAL Connect, Roon Ready, DLNA.", f"Rack 4U o libero; 450 × 147 × 370 mm, {peso}; standby < 0,5 W."],
            [f"{hdmi} HDMI 2.1, HDCP 2.3; 8K60, 4K120, Dolby Vision, VRR, eARC.", "1 AES/EBU, 3 coassiali, 4 ottici, 1 USB audio.", "1 XLR per il microfono RoomPerfect™.", "RS232, 2 IR in, 1 IR out, trigger in, 4 trigger out, Ethernet."] + (["Moduli opzionali AES/EBU DCI e AES67 a 16 canali."] if ch == 16 else []),
            ["2 HDMI, HDCP 2.3.", "16 XLR analogiche (massimo 8 V RMS).", "1 coassiale digitale per le zone (96 kHz / 24 bit)."],
            f"Lyngdorf-{mod.replace(' ', '-').replace('.', '-')}.jpg » Lyngdorf {mod}, vista frontale ;; Lyngdorf-{mod.replace(' ', '-').replace('.', '-')}-posteriore.jpg » Lyngdorf {mod}, pannello posteriore",
            "Si configura dall'interfaccia del processore; misura e correzione con RoomPerfect™ e il microfono incluso.",
            [atmos714("Lyngdorf MXA-8400"), {"titolo": conf2[0], "voci": ["Più finali MXA-8400 in rack per tutti i canali."], "zone": conf2[1]}],
            [card("lyngdorf-mxa-8400", ["Finale a 8 canali, 8 × 200 W su 8 Ω, ingressi XLR."], "Con il Lyngdorf MXA-8400"), THX(["LCR da incasso THX per la sala."]), SUB | {"voci": ["Subwoofer con Subwoofer Level Assistant."]}, CTRL | {"voci": ["RS232, IR, trigger ed Ethernet."]}],
            ESTR + ", ricavata dalla scheda Lyngdorf.", []))
    for (id, mod, url, slug, chs, desc, hdmi, ana, outp, cons, dims, peso, fin, conf2, img) in (
        (30357, "AV 10", "preamplificatore-av-15-4-canali-marantz-av-10", "marantz-av-10", "15.4", "fino a 15.4 canali", "7 ingressi 8K, 3 uscite (eARC, Zone)", "5 analogici (1 XLR), phono MM, 2 ottici, 2 coassiali", "pre out 17.4 RCA e XLR, 4 subwoofer, 2 Zone", "100 W; 0,2 W in standby", "442 × 480 × 189 mm", "", "marantz-amp-10",
         ("9.4.6 · 15.4 canali", [z("Frontali L · C · R", "3"), z("Surround, back e wide", "4"), z("Wide aggiuntivi", "2"), z("Altezze Atmos", "4"), z("Altezze aggiuntive", "2"), z("4 subwoofer", "sub")]),
         "av-10.jpg » Marantz AV 10, vista frontale ;; av-10-lato.jpg » Marantz AV 10, vista laterale ;; av-10-retro.jpg » Marantz AV 10, pannello posteriore"),
        (2783, "AV 20", "marantz-av-20-preamplificatore-processore-av-13-4-di-riferimento", None, "13.4", "fino a 13.4 canali", "7 ingressi 8K, 3 uscite (eARC, Zone)", "6 analogici (1 XLR), phono MM, 2 ottici, 2 coassiali, USB", "pre out 15.4 RCA e XLR, 4 subwoofer, 2 Zone", "90 W; 0,2 W in standby", "circa 442 × 437 × 191 mm", "circa 15 kg", "marantz-amp-20",
         ("7.4.6 · 13.4 canali", [z("Frontali L · C · R", "3"), z("Surround e back", "4"), z("Altezze Atmos", "4"), z("Altezze aggiuntive", "2"), z("4 subwoofer", "sub")]),
         "Marantz-AV20.jpg » Marantz AV 20, vista di tre quarti ;; Marantz-AV20-fronte.jpg » Marantz AV 20, vista frontale ;; Marantz-AV20-posteriore.jpg » Marantz AV 20, pannello posteriore"),
        (27192, "AV7706", "pre-amplificatore-surround-av-marantz-av7706", None, "11.2", "fino a 11.2 canali", "8 ingressi (1 frontale), 3 uscite (eARC, Zone)", "7 analogici, phono MM, ingresso 7.1, 2 ottici, 2 coassiali", "pre out 11.2 RCA e XLR, 2 subwoofer, 2 Zone", "60 W; 0,2 W in standby", "440 × 392 × 185 mm", "10,4 kg", "marantz-mm8077",
         ("7.2.4 · 11.2 canali", [z("Frontali L · C · R", "3"), z("Surround e back", "4"), z("Altezze Atmos", "4"), z("2 subwoofer", "sub")]),
         "av7706.jpg » Marantz AV7706, vista frontale ;; av7706-aperto.jpg » Marantz AV7706 con lo sportello frontale aperto ;; av7706-retro.jpg » Marantz AV7706, pannello posteriore")):
        out.append(scheda(id, "Marantz", mod, url, "P",
            [f"Processore AV · {chs}", "HDMI 8K" if "8K" in hdmi else "8 HDMI · eARC", "Audyssey XT32 · XLR"], [f"{chs} canali · Dolby Atmos", "Processore AV", "Marantz"],
            [f"Il <strong>Marantz {mod}</strong> è un processore AV {desc} con Dolby Atmos, DTS:X, Auro-3D e IMAX Enhanced e uscite pre RCA e XLR.",
             "Calibrazione Audyssey MultEQ XT32" + ("; Dirac Live opzionale." if mod != "AV7706" else "; rete con HEOS e AirPlay 2.")],
            [f"Canali: {desc}.", "Formati: Dolby Atmos, DTS:X" + (" Pro" if mod != "AV7706" else "") + ", Auro-3D, IMAX Enhanced, MPEG-H" + (", 360 Reality Audio." if mod != "AV7706" else "."),
             "Calibrazione Audyssey MultEQ XT32" + ("; Dirac Live opzionale." if mod != "AV7706" else "."), f"Consumo {cons}.", f"{dims}" + (f", {peso}." if peso else ".")],
            [f"HDMI: {hdmi}.", f"Audio: {ana}."] + (["Wi-Fi, Bluetooth, Ethernet, HEOS, AirPlay 2."] if mod == "AV7706" else []),
            [f"Uscite: {outp}."],
            img, "Si configura dal menu a schermo con l'assistente di configurazione; calibrazione Audyssey con il microfono incluso.",
            [atmos714(f"Marantz {spk(fin)['model']}"), {"titolo": conf2[0], "voci": ["Tutti i canali del processore assegnati."], "zone": conf2[1]}],
            [card(fin, ["Finale multicanale Marantz con ingressi XLR."], f"Con il Marantz {spk(fin)['model']}"), INF14(["Frontali e centrale da incasso."]), SUB | {"voci": ["Subwoofer attivi sulle uscite sub."]}, CTRL | {"voci": ["Rete, IR e controllo IP."]}],
            ESTR + ".", [], slug))
    out.append(scheda(27580, "Rotel", "RSP-1576 MKII", "preamplificatore-av-multicanale-7-1-4-rotel-rsp-1576mkii", "P",
        ["Processore AV · 7.1.4", "7 HDMI 2.0b · 4K/60", "Dirac Live · rack 3U"], ["7.1.4 · Dolby Atmos", "Processore AV", "Rack 3U"],
        ["Il <strong>Rotel RSP-1576 MKII</strong> è un processore A/V 7.1.4 con Dolby Atmos e DTS:X, 7 ingressi HDMI e correzione ambientale Dirac Live Full.",
         "Ingressi analogici con Analog Bypass; si abbina ai finali Rotel RMB."],
        ["Formati: LPCM fino a 192 kHz / 24 bit, Dolby TrueHD, Dolby Atmos, DTS-HD MA, DTS:X; fino a 7.1.4.", "DSP Texas Instruments quad-core; DAC Wolfson 24 bit / 192 kHz.", "Dirac Live Full.",
         "S/N 112 dB; Analog Bypass 10 Hz – 100 kHz (±1 dB).", "230 V; consumo 60 W, standby < 0,5 W.", "431 × 144 × 348 mm (3U), 8,8 kg."],
        ["7 HDMI (HDCP 2.2, HDMI 2.0b), fino a 4K 60 Hz, HDR10.", "RCA 270 mV, XLR 500 mV (100 kΩ); phono 3,5 mV (47 kΩ)."],
        ["2 HDMI con ARC.", "Uscite pre: 1 V."],
        "RSP-1576.jpg » Rotel RSP-1576 MKII, vista frontale ;; RSP-1576-retro.jpg » Rotel RSP-1576 MKII, pannello posteriore",
        "Si configura dal menu a schermo; Dirac Live per la correzione ambientale.",
        [atmos714("Rotel RMB-1587MKII + RMB-1504"), {"titolo": "5.1.4", "voci": ["Senza surround back: basta un finale a 5 canali più uno a 4 per le altezze."], "zone": [z("Frontali L · C · R", "3"), z("Surround", "2"), z("Altezze Atmos", "4"), z("Subwoofer · LFE", "sub")]}],
        [card("rotel-rmb-1587mkii", ["Finale a 7 canali da 155 W su 8 Ω."], "Con il Rotel RMB-1587MKII"), S66(["LCR da incasso, 6 Ω."]), SUB | {"voci": ["Subwoofer attivo sull'uscita sub."]}, CTRL | {"voci": ["RS232, IR e trigger."]}],
        ESTR + ".", []))

    # ---------- finali ----------
    def fin(id, brand, model, url, chiave, righe, intro, car, ing, usc, img, gui, conf, collega, nota, fonti, slug=None):
        return scheda(id, brand, model, url, "F", chiave, righe, intro, car, ing, usc, img, gui, conf, collega, nota, fonti, slug)
    n51 = lambda w: {"titolo": "5.1", "voci": ["Frontali, centrale e surround; subwoofer attivo dal processore."], "zone": [z(f"Frontali L · R · {w}"), z(f"Centrale · {w}", "1"), z(f"Surround · {w}"), z("Subwoofer attivo · dal processore", "sub")], "apparecchio": model_holder[0]}
    model_holder = [""]
    PROC = lambda v: {"titolo": "Processore AV", "icona": "sorgente", "voci": v}
    out.append(fin(65973, "Arcam", "PA720", "arcam-pa720-finale-di-potenza-7-canali-classe-g-7x100w", ["7 canali · classe G", "7 × 100 W / 8 Ω", "XLR o RCA · RS232"], ["7 canali · classe G", "Finale multicanale", "Arcam"],
        ["L'<strong>Arcam PA720</strong> è un finale di potenza a 7 canali in classe G (primi 20 W in classe A): 100 W per canale su 8 Ω con tutti i canali in funzione.", "Ingressi RCA o XLR commutabili; controllo Ethernet e RS232."],
        ["7 canali in classe G, primi 20 W in classe A.", "7 canali 20 Hz – 20 kHz: 100 / 140 W (8 / 4 Ω); 5 canali 1 kHz: 110 / 175 W; 2 canali: 140 / 225 W.", "THD 0,002%; S/N 105 dB; risposta 20 Hz – 20 kHz ±0,05 dB.", "Consumo 1,5 kW massimi, 90 W a riposo, < 0,5 W in standby.", "433 × 425 × 177 mm, 18 kg."],
        ["7 ingressi RCA o XLR commutabili: 800 mV RCA, 1,6 V XLR (50 W / 8 Ω), 10 kΩ.", "Ethernet e RS232."], ["7 uscite diffusori."],
        "arcam-pa720-1-1000.jpg » Arcam PA720 finale di potenza 7 canali, vista frontale ;; arcam-pa720-2-1000.jpg » Arcam PA720, pannello posteriore",
        "Non ha un'interfaccia a schermo: si accende e si controlla da Ethernet e RS232 o dal processore.",
        [{"titolo": "7.1", "voci": ["Frontali, centrale, surround e surround back; subwoofer dal processore."], "zone": [z("Frontali L · R · 100 W"), z("Centrale · 100 W", "1"), z("Surround · 100 W"), z("Surround back · 100 W"), z("Subwoofer attivo · dal processore", "sub")], "apparecchio": "Arcam PA720"},
         {"titolo": "5.1.2", "voci": ["Due canali alle altezze Atmos al posto dei surround back."], "zone": [z("Frontali L · R"), z("Centrale", "1"), z("Surround"), z("Altezze Atmos"), z("Subwoofer attivo", "sub")], "apparecchio": "Arcam PA720"}],
        [INF14(["Frontali e centrale da incasso, 8 Ω."]), card("arcam-av41", ["Processore AV a 16 canali con uscite XLR."], "Con l'Arcam AV41"), CTRL | {"voci": ["Ethernet e RS232."]}],
        ESTR + ", confrontata con la pagina Arcam (7 × 100 W su 8 Ω, classe G, ingressi RCA o XLR).", [F("pagina Arcam PA720", "https://www.arcam.co.uk/product,hda,power-amplifiers,pa720.htm")]))
    out.append(fin(65975, "Arcam", "PA410", "arcam-pa410-finale-di-potenza-4-canali-classe-ab-4x50w", ["4 canali · classe AB", "4 × 50 W / 8 Ω", "RS232"], ["4 canali · classe AB", "Finale multicanale", "Arcam"],
        ["L'<strong>Arcam PA410</strong> è un finale di potenza a 4 canali in classe AB: 50 W per canale su 8 Ω con tutti i canali in funzione.", "Ideale per le altezze Atmos accanto a un PA720, o per due zone stereo."],
        ["4 canali in classe AB.", "4 canali 20 Hz – 20 kHz: 50 / 70 W (8 / 4 Ω); 2 canali: 60 / 90 W.", "THD 0,003%; S/N 105 dB.", "Consumo 700 W massimi, 90 W a riposo, < 0,5 W in standby.", "433 × 325 × 105 mm, 10 kg."],
        ["4 ingressi, sensibilità 600 mV (50 W / 8 Ω), 10 kΩ.", "RS232."], ["4 uscite diffusori."],
        "arcam-pa410-1-1000.jpg » Arcam PA410 finale di potenza 4 canali, vista frontale ;; arcam-pa410-2-1000.jpg » Arcam PA410, pannello posteriore",
        "Non ha un'interfaccia a schermo: si controlla via RS232 o dal processore.",
        [{"titolo": "4 altezze Atmos", "voci": ["Con un PA720 per i 7 canali principali completa un 7.1.4."], "zone": [z("Altezze anteriori · 50 W"), z("Altezze posteriori · 50 W")], "apparecchio": "Arcam PA410"},
         {"titolo": "2 zone stereo", "voci": ["Due coppie di diffusori, ognuna dalla sua sorgente."], "zone": [z("Zona 1 · 2 × 50 W"), z("Zona 2 · 2 × 50 W")], "apparecchio": "Arcam PA410"}],
        [card("kef-ci160-2cr", ["Diffusore da soffitto per le altezze Atmos, 8 Ω."], "KEF Ci160.2CR"), card("arcam-av41", ["Processore AV a 16 canali."], "Con l'Arcam AV41"), CTRL | {"voci": ["RS232."]}],
        ESTR + ".", []))
    for (id, mod, url, ch, w8, w6, cons, dims, peso, imgs_s, conf_a, conf_b, extra) in (
        (529, "MM7055", "marantz-mm7055", 5, "140 W", "170 W", "400 W", "440 × 183 × 384 mm", "15,2 kg",
         "Marantz-MM7055-finale-AV.jpg » Marantz MM7055, vista di tre quarti ;; Marantz-MM7055-finale-AV-frontale.jpg » Marantz MM7055, vista frontale ;; Marantz-MM7055-finale-AV-posteriore.jpg » Marantz MM7055, pannello posteriore",
         ("5.1", [z("Frontali L · R"), z("Centrale", "1"), z("Surround"), z("Subwoofer attivo · dal processore", "sub")]), ("3 frontali + 2 altezze", [z("Frontali L · C · R", "3"), z("Altezze Atmos")]), "trasformatore EI, oltre 65.000 µF"),
        (530, "MM7025", "marantz-mm7025", 2, "140 W", "170 W", "220 W", "440 × 126 × 352 mm", "10,5 kg",
         "Marantz-MM7025-finale-audio-video.jpg » Marantz MM7025, vista di tre quarti ;; Marantz-MM7025-finale-AV-frontale.jpg » Marantz MM7025, vista frontale ;; Marantz-MM7025-finale-AV-posteriore.jpg » Marantz MM7025, pannello posteriore",
         ("Frontali di un sistema AV", [z("Frontali L · R · 140 W")]), ("Zona stereo", [z("Zona 2 · 2 × 140 W")]), "trasformatore EI, 30.000 µF"),
        (1037, "MM8077", "marantz-mm8077", 7, "150 W", "180 W", "880 W", "440 × 185 × 384 mm", "18 kg",
         "Marantz-MM8077-finale-AV.jpg » Marantz MM8077, vista di tre quarti ;; Marantz-MM8077-finale-AV-frontale.jpg » Marantz MM8077, vista frontale ;; Marantz-MM8077-finale-AV-posteriore.jpg » Marantz MM8077, pannello posteriore",
         ("7.1", [z("Frontali L · R"), z("Centrale", "1"), z("Surround"), z("Surround back"), z("Subwoofer attivo · dal processore", "sub")]), ("5.1.2", [z("Frontali L · R"), z("Centrale", "1"), z("Surround"), z("Altezze Atmos"), z("Subwoofer attivo", "sub")]), "classe A/B, retroazione di corrente, toroidale 100.000 µF")):
        out.append(fin(id, "Marantz", mod, url, [f"{ch} canali · {w8} / 8 Ω", f"{w6} / 6 Ω", "XLR e RCA"], [f"{ch} canali", "Finale multicanale", "Marantz"],
            [f"Il <strong>Marantz {mod}</strong> è un finale di potenza a {ch} canali da {w8} su 8 Ω ({w6} su 6 Ω), con ingressi RCA e XLR.", "Si abbina ai processori Marantz AV."],
            [f"{ch} canali; {extra}.", f"Potenza: {w8} su 8 Ω, {w6} su 6 Ω (RMS).", "Risposta 8 – 100 kHz (±3 dB)" if mod != "MM8077" else "Risposta 10 Hz – 100 kHz (±3 dB)", "THD 0,03%; fattore di smorzamento 100; S/N 105 dB.", f"Consumo {cons}, standby 0,4 W.", f"{dims}, {peso}."],
            ["Ingressi RCA (1,2 V / 22 kΩ) e XLR (2,4 V / 30 kΩ)."], [f"{ch} uscite diffusori."],
            imgs_s, "Non ha un'interfaccia a schermo: si accende con il processore.",
            [{"titolo": conf_a[0], "voci": ["Uscite pre del processore sugli ingressi XLR o RCA."], "zone": conf_a[1], "apparecchio": f"Marantz {mod}"}, {"titolo": conf_b[0], "voci": ["Assegnazione alternativa dei canali."], "zone": conf_b[1], "apparecchio": f"Marantz {mod}"}],
            [INF14(["Frontali e centrale da incasso, 8 Ω."]), card("marantz-av7706", ["Processore AV 11.2 con uscite XLR."], "Con il Marantz AV7706"), CTRL | {"voci": ["Accensione dal processore."]}],
            ESTR + ".", []))
    for (id, mod, url, ch, w8, w4, ex, conf_a, conf_b, img) in (
        (30398, "AMP 10", "finale-di-potenza-16-canali-400-200-watt-marantz-amp-10", 16, "200 W", "400 W", "16 XLR e 16 RCA (selettore); 16 coppie di morsetti SPKT-1+; consumo 500 W (140 W senza segnale), 0,2 W in standby; circa 442 × 488 × 188 mm, 19,8 kg",
         ("9.1.6 · 15 canali", [z("Frontali L · C · R", "3"), z("Surround, back e wide", "4"), z("Wide aggiuntivi"), z("Altezze Atmos", "4"), z("Altezze aggiuntive"), z("Subwoofer attivi · dal processore", "sub")]),
         ("BTL · frontali da 400 W", [z("Frontali L · R · BTL 400 W / 8 Ω"), z("Centrale · BTL 400 W / 8 Ω", "1"), z("Altri canali · 200 W / 8 Ω", "4")]),
         "marantz-amp-10.jpg » Marantz AMP 10, vista frontale ;; marantz-amp-10-lato.jpg » Marantz AMP 10, vista laterale ;; marantz-amp-10-retro.jpg » Marantz AMP 10, pannello posteriore"),
        (39671, "AMP 20", "marantz-amp-20-finale-multicanale-12x200-w-con-ingressi-bilanciati-e-modalita-btl-bi-amp", 12, "200 W", "400 W", "12 XLR e 12 RCA (selettore); 12 coppie di morsetti SPKT-1+; consumo 400 W (110 W senza segnale), 0,2 W in standby; circa 442 × 442 × 191 mm, 18 kg",
         ("7.1.4 · 11 canali", [z("Frontali L · C · R", "3"), z("Surround e back", "4"), z("Altezze Atmos", "4"), z("Subwoofer attivi · dal processore", "sub")]),
         ("BTL · frontali da 400 W", [z("Frontali L · R · BTL 400 W / 8 Ω"), z("Altri canali · 200 W / 8 Ω", "4")]),
         "Marantz-AMP20.jpg » Marantz AMP 20, vista di tre quarti ;; Marantz-AMP20-frontale.jpg » Marantz AMP 20, vista frontale ;; Marantz-AMP20-posteriore.jpg » Marantz AMP 20, pannello posteriore")):
        out.append(fin(id, "Marantz", mod, url, [f"{ch} canali · classe D", f"{w8} / 8 Ω · {w4} / 4 Ω", "BTL 400 W / 8 Ω"], [f"{ch} canali · classe D", "Finale multicanale", "Marantz"],
            [f"Il <strong>Marantz {mod}</strong> è un finale di potenza a {ch} canali in classe D: {w8} su 8 Ω, {w4} su 4 Ω, {w4} su 8 Ω con due canali in BTL.", "Bi-amp, ingressi XLR o RCA, RS232, Remote Bus e trigger."],
            [f"{ch} canali in classe D Marantz, moduli HDAM-SA2.", f"Potenza: {w8} su 8 Ω (1 kHz, 0,05%, 2 canali), {w4} su 4 Ω.", "BTL: due canali in uno da 400 W su 8 Ω; bi-amp.", ex + "."],
            [f"{ch} ingressi XLR e {ch} RCA, selezionabili.", "RS232, Remote Bus, trigger in / out, IR."], [f"{ch} coppie di morsetti SPKT-1+."],
            img, "Non ha un'interfaccia a schermo: si accende e si controlla dal processore, via Remote Bus, trigger o RS232.",
            [conf_a and {"titolo": conf_a[0], "voci": ["Uscite pre del processore sugli ingressi XLR."], "zone": conf_a[1], "apparecchio": f"Marantz {mod}"}, {"titolo": conf_b[0], "voci": ["Due canali in BTL per ogni diffusore più impegnativo."], "zone": conf_b[1], "apparecchio": f"Marantz {mod}"}],
            [THX(["LCR da incasso THX, 4 Ω."]), card("arcam-av41", ["Processore AV a 16 canali con uscite XLR."], "Con l'Arcam AV41"), CTRL | {"voci": ["RS232, Remote Bus, trigger."]}],
            ESTR + ", confrontata con l'infosheet Marantz AMP 10." if ch == 16 else ESTR + ".", [F("infosheet Marantz AMP 10", "https://www.cepro.com/wp-content/uploads/2023/01/Marantz-Amp-10-–-Infosheet.pdf")] if ch == 16 else []))
    for (id, mod, url, ch, w8, w4, ex, conf_b, img, slug) in (
        (27592, "RMB-1555", "finale-di-potenza-multicanale-120w-x-5-rotel-rmb-1555", 5, "120 W", "170 W", "fattore di smorzamento 180; S/N 116 dB; guadagno 26,5 dB; consumo 650 W, standby 0,5 W; 431 × 188 × 454 mm (4U), 21,8 kg",
         ("3 frontali + 2 altezze", [z("Frontali L · C · R", "3"), z("Altezze Atmos")]), "rmb1555.jpg » Rotel RMB-1555, vista frontale ;; rmb1555-retro.jpg » Rotel RMB-1555, pannello posteriore", "rotel-rmb-1555"),
        (27645, "RMB-1504", "finale-di-potenza-multicanale-70w-x-4-rotel-rmb-1504", 4, "70 W", "115 W", "fattore di smorzamento > 200; S/N 115 dB; guadagno 26 dB; accensione con segnale da 4 mV; consumo 450 W; 431 × 144 × 443 mm (3U), 14,9 kg",
         ("2 zone stereo", [z("Zona 1 · 2 × 70 W"), z("Zona 2 · 2 × 70 W")]), "rmb1504.jpg » Rotel RMB-1504, vista frontale ;; rmb1504-retro.jpg » Rotel RMB-1504, pannello posteriore", "rotel-rmb-1504"),
        (27653, "RMB-1506", "rotel-rmb-1506-finale-multicanale-6x50w-in-classe-ab", 6, "50 W", "80 W", "fattore di smorzamento > 200; S/N 115 dB; trigger 12 V, rilevamento del segnale, uscita link; consumo 450 W; 431 × 144 × 424 mm (3U), 15,3 kg",
         ("3 zone stereo", [z("Zona 1 · 2 × 50 W"), z("Zona 2 · 2 × 50 W"), z("Zona 3 · 2 × 50 W")]), "RMB-1506-frontale.jpg » Rotel RMB-1506, vista frontale ;; RMB-1506-retro.jpg » Rotel RMB-1506, pannello posteriore", "rotel-rmb-1506")):
        conf_a = {"titolo": f"{ch} canali · home cinema", "voci": ["Uscite pre del processore sugli ingressi RCA."], "zone": ([z("Frontali L · R"), z("Centrale", "1"), z("Surround"), z("Subwoofer attivo · dal processore", "sub")] if ch == 5 else [z("Altezze Atmos", "4")] if ch == 4 else [z("Surround e back", "2"), z("Altezze Atmos", "4")]), "apparecchio": f"Rotel {mod}"}
        conf_b2 = {"titolo": conf_b[0], "voci": ["Assegnazione alternativa dei canali."], "zone": conf_b[1], "apparecchio": f"Rotel {mod}"}
        out.append(fin(id, "Rotel", mod, url, [f"{ch} canali · classe AB", f"{w8} / 8 Ω · {w4} / 4 Ω", "Trigger 12 V"], [f"{ch} canali · classe AB", "Finale multicanale", "Rotel"],
            [f"Il <strong>Rotel {mod}</strong> è un finale multicanale in classe AB a {ch} canali: {w8} per canale su 8 Ω e {w4} su 4 Ω con tutti i canali in funzione.", "Per home cinema e impianti multizona; carico minimo 4 Ω."],
            [f"{ch} canali in classe AB; THD e intermodulazione < 0,03%.", f"Potenza continua: {w8} su 8 Ω, {w4} su 4 Ω (tutti i canali).", "Impedenza minima 4 Ω.", ex + "."],
            ["Ingressi RCA.", "Trigger 12 V."], [f"{ch} uscite diffusori."], img, "Non ha un'interfaccia a schermo: si accende con trigger 12 V o col segnale.",
            [conf_a, conf_b2], [S66(["LCR da incasso, 6 Ω."]), card("rotel-rsp-1576-mkii", ["Processore A/V 7.1.4 con Dirac Live."], "Con il Rotel RSP-1576 MKII"), CTRL | {"voci": ["Trigger 12 V dal processore."]}],
            ESTR + ".", [], slug))
    for (id, mod, url, ch, w8, w4, w2, ex, img, slug) in (
        (63186, "RMB-1585MKII", "rotel-rmb-1585mkii-finale-multicanale-5-canali", 5, "210 W", "340 W", "2 × 440 W su 4 Ω", "Selettore 5 canali / Bi-Amp; fattore di smorzamento 223; S/N 120 dB; consumo 1.200 W", "rotel-rmb-1585mkii-nero-e-silver-1000.jpg » Rotel RMB-1585MKII nero e silver, vista frontale ;; rotel-rmb-1585mkii-retro-1000.jpg » Rotel RMB-1585MKII, pannello posteriore ;; rotel-rmb-1585mkii-interno-1000.jpg » Rotel RMB-1585MKII, interno con i trasformatori toroidali", "rotel-rmb-1585mkii"),
        (63191, "RMB-1587MKII", "rotel-rmb-1587mkii-finale-multicanale-7-canali", 7, "155 W", "250 W", "2 × 335 W su 4 Ω", "Fattore di smorzamento 330; S/N 111 dB; consumo 1.400 W", "rotel-rmb-1587mkii-nero-e-silver-1000.jpg » Rotel RMB-1587MKII nero e silver, vista frontale ;; rotel-rmb-1587mkii-retro-1000.jpg » Rotel RMB-1587MKII, pannello posteriore ;; rotel-rmb-1587mkii-interno-1000.jpg » Rotel RMB-1587MKII, interno con i trasformatori toroidali", "rotel-rmb-1587mkii")):
        conf_a = {"titolo": "5.1" if ch == 5 else "7.1", "voci": ["Uscite pre del processore sugli ingressi XLR o RCA."], "zone": [z("Frontali L · R"), z("Centrale", "1"), z("Surround")] + ([z("Surround back")] if ch == 7 else []) + [z("Subwoofer attivo · dal processore", "sub")], "apparecchio": f"Rotel {mod}"}
        conf_b = ({"titolo": "Bi-amp frontali", "voci": ["Selettore su Bi-Amp: quattro canali per i frontali (alti e bassi separati)."], "zone": [z("Frontale L · bassi + alti"), z("Frontale R · bassi + alti"), z("Centrale", "1")], "apparecchio": f"Rotel {mod}"} if ch == 5
                  else {"titolo": "5.1.2", "voci": ["Due canali alle altezze Atmos."], "zone": [z("Frontali L · R"), z("Centrale", "1"), z("Surround"), z("Altezze Atmos"), z("Subwoofer attivo", "sub")], "apparecchio": f"Rotel {mod}"})
        out.append(fin(id, "Rotel", mod, url, [f"{ch} canali · classe AB", f"{w8} / 8 Ω · {w4} / 4 Ω", "Rack 5U · XLR"], [f"{ch} canali · classe AB", "Finale multicanale", "Rotel"],
            [f"Il <strong>Rotel {mod}</strong> è un finale multicanale in classe AB a {ch} canali: {w8} su 8 Ω e {w4} su 4 Ω per canale con tutti i canali in funzione.", "Due trasformatori toroidali, ingressi XLR e RCA, rack 5U per installazione."],
            [f"{ch} canali in classe AB, 2 trasformatori toroidali.", f"Potenza: {w8} su 8 Ω, {w4} su 4 Ω (tutti i canali); {w2}.", ex + ".", "431 × 237 × 456 mm (5U), circa 37,5 kg.", "Lascia almeno 10 cm attorno al telaio; 4 ventole termostatiche; protezioni termica e da sovracorrente."],
            ["Ingressi XLR e RCA a commutazione automatica.", "Trigger 12 V in (3 – 30 V AC/DC) con uscita pass-through."], [f"{ch} uscite diffusori: cavo nudo, forcelle o banane doppie."],
            img, "Non ha un'interfaccia a schermo: si accende con il trigger 12 V del processore.",
            [conf_a, conf_b], [THX(["LCR da incasso THX, 4 Ω."]), card("rotel-rsp-1576-mkii", ["Processore A/V 7.1.4 con Dirac Live."], "Con il Rotel RSP-1576 MKII"), CTRL | {"voci": ["Trigger 12 V."]}],
            ESTR + ", confrontata con la scheda Rotel." if ch == 7 else ESTR + ".", [F("scheda tecnica Rotel RMB-1587MKII", "https://iear.be/docs/spec-sheet/199315.pdf")] if ch == 7 else [], slug))
    out.append(fin(31047, "Hegel", "C55", "hegel-c55-finale-multicanale-5x150w-home-theater", ["5 canali · 150 W / 8 Ω", "300 W / 4 Ω · 600 W / 2 Ω", "Rack 3U"], ["5 canali", "Finale multicanale da installazione", "Hegel"],
        ["L'<strong>Hegel C55</strong> è un finale di potenza a 5 canali per home theater e installazioni: 150 W su 8 Ω, 300 W su 4 Ω, 600 W su 2 Ω per canale.", "Guadagno e fase regolabili per canale; rack 3U con staffe integrate."],
        ["5 × 150 / 300 / 600 W su 8 / 4 / 2 Ω (1 kHz, 1% THD).", "Carico minimo 2 Ω; fattore di smorzamento oltre 2.000.", "THD < 0,01% a 100 W / 8 Ω; S/N oltre 100 dB.", "Guadagno 23 o 29 dB e fase 0 / 180° per canale.", "Rack 3U, staffe posteriori regolabili; Hegel consiglia 1U libera sopra e sotto.", "482 × 132 × 520 mm, 37,5 kg."],
        ["5 XLR e 5 RCA.", "Trigger: ingresso mini-jack 5 – 12 V."], ["5 uscite diffusori.", "Trigger: uscita mini-jack 11,9 V, per il collegamento in cascata."],
        "hegel-c55.jpg » Hegel C55, vista frontale ;; hegel-c55-retro.jpg » Hegel C55, pannello posteriore",
        "Non ha un'interfaccia a schermo: guadagno e fase si impostano per canale sul retro; accensione via trigger.",
        [{"titolo": "5.1", "voci": ["Frontali, centrale e surround; subwoofer dal processore."], "zone": [z("Frontali L · R · 150 W"), z("Centrale · 150 W", "1"), z("Surround · 150 W"), z("Subwoofer attivo · dal processore", "sub")], "apparecchio": "Hegel C55"},
         {"titolo": "Bi-amp frontali", "voci": ["Quattro canali per i frontali in bi-amp, il quinto per il centrale; fase e guadagno per canale."], "zone": [z("Frontale L · bassi + alti"), z("Frontale R · bassi + alti"), z("Centrale", "1")], "apparecchio": "Hegel C55"}],
        [THX(["LCR da incasso THX, 4 Ω: il C55 regge fino a 2 Ω."]), card("arcam-av41", ["Processore AV con uscite XLR."], "Con l'Arcam AV41"), CTRL | {"voci": ["Trigger in / out per l'accensione a cascata."]}],
        ESTR + ", confrontata con la pagina Hegel.", [F("pagina Hegel C55", "https://www.hegel.com/products/custom/c55")]))
    out.append(fin(46074, "Lyngdorf", "MXA-8400", "lyngdorf-mxa-8400-finale-multicanale-8-x-400-w-purifi-eigentakt", ["8 canali · Purifi", "8 × 200 W / 8 Ω · 400 W / 4 Ω", "Bridge 4 × 800 W"], ["8 canali · Purifi Eigentakt", "Finale multicanale", "Lyngdorf"],
        ["Il <strong>Lyngdorf MXA-8400</strong> è un finale a 8 canali con moduli Purifi Eigentakt: 8 × 200 W su 8 Ω, 8 × 400 W su 4 Ω, 4 × 800 W su 8 Ω in bridge.", "Ingressi XLR, uscite Neutrik speakON."],
        ["8 × 400 W su 4 Ω, 8 × 200 W su 8 Ω; bridge 4 × 800 W su 8 Ω.", "Corrente massima 25 A per canale; THD 0,001%; S/N 128 dB; fattore di smorzamento > 1.200.", "Sensibilità HIGH (2 V) o LOW (6 V).", "Consumo 29 W a riposo, < 0,5 W in standby; standby automatico dopo 15 minuti.", "450 × 145 × 349 mm, 10,3 kg."],
        ["8 XLR analogici, 10 kΩ."], ["8 Neutrik speakON."],
        "Lyngdorf-MXA-8400.jpg » Lyngdorf MXA-8400, vista di tre quarti ;; Lyngdorf-MXA-8400-frontale.jpg » Lyngdorf MXA-8400, vista frontale ;; Lyngdorf-MXA-8400-posteriore.jpg » Lyngdorf MXA-8400, pannello posteriore",
        "Non ha un'interfaccia a schermo: sensibilità e modalità si impostano sull'apparecchio; si comanda dal processore Lyngdorf.",
        [{"titolo": "7.1 · 8 canali", "voci": ["Frontali, centrale, surround, surround back e un canale libero."], "zone": [z("Frontali L · R · 200 W"), z("Centrale · 200 W", "1"), z("Surround"), z("Surround back"), z("Canale 8 · altezza o sub passivo", "1")], "apparecchio": "Lyngdorf MXA-8400"},
         {"titolo": "Bridge · 4 × 800 W", "voci": ["Coppie di canali in bridge per LCR e subwoofer passivi."], "zone": [z("Frontali L · R · 800 W bridge"), z("Centrale · 800 W bridge", "1"), z("Subwoofer passivo · 800 W bridge", "sub")], "apparecchio": "Lyngdorf MXA-8400"}],
        [THX(["LCR da incasso THX, 4 Ω."]), card("lyngdorf-mp-60-2-1", ["Processore a 16 canali con RoomPerfect™."], "Con il Lyngdorf MP-60 2.1"), CTRL | {"voci": ["Accensione e standby automatici."]}],
        ESTR + ", confrontata con la pagina Lyngdorf.", [F("pagina Lyngdorf MXA-8400", "https://www.lyngdorf.com/lyngdorf-mxa-8400")]))
    out.append(fin(46176, "NAD", "M28", "nad-m28-finale-di-potenza-7-canali-purifi-eigentakt-7-x-200-w", ["7 canali · Purifi", "7 × 200 W / 8 Ω", "XLR e RCA"], ["7 canali · Purifi Eigentakt", "Finale multicanale", "Masters Series"],
        ["Il <strong>NAD M28</strong> è un finale a 7 canali con moduli Purifi Eigentakt: 200 W per canale su 8 Ω e 340 W su 4 Ω con tutti i canali in funzione.", "Si abbina al pre-processore NAD M17 V2i."],
        ["Tutti i canali: 200 W (8 Ω), 340 W (4 Ω); due canali: 220 W (8 Ω), 400 W (4 Ω).", "Potenza dinamica IHF: 280 W (8 Ω), 560 W (4 Ω, un canale).", "S/N oltre 102 dB; risposta ±0,1 dB 20 Hz – 20 kHz.", "435 × 156 × 380 mm; standby 0,5 W o meno."],
        ["Ingressi XLR e RCA."], ["7 uscite diffusori."],
        "NAD-M28.jpg » NAD M28, vista di tre quarti ;; NAD-M28-frontale.jpg » NAD M28, vista frontale ;; NAD-M28-rear.jpg » NAD M28, pannello posteriore",
        "Non ha un'interfaccia a schermo: si accende con il processore.",
        [{"titolo": "7.1", "voci": ["Frontali, centrale, surround e surround back."], "zone": [z("Frontali L · R · 200 W"), z("Centrale · 200 W", "1"), z("Surround"), z("Surround back"), z("Subwoofer attivo · dal processore", "sub")], "apparecchio": "NAD M28"},
         {"titolo": "5.1.2", "voci": ["Due canali alle altezze Atmos."], "zone": [z("Frontali L · R"), z("Centrale", "1"), z("Surround"), z("Altezze Atmos"), z("Subwoofer attivo", "sub")], "apparecchio": "NAD M28"}],
        [INF14(["Frontali e centrale da incasso, 8 Ω."]), card("nad-m17-v2i", ["Pre-processore 11.1 con Dirac Live."], "Con il NAD M17 V2i"), CTRL | {"voci": ["Accensione dal processore."]}],
        ESTR + ".", []))
    out.append(fin(31572, "Elipson", "Infinite A1000", "elipson-infinite-a1000-amplificatore-mono-1000-w-classe-d-dsp-per-subwoofer", ["Mono · 1000 W / 4 Ω", "DSP · filtro 40 – 200 Hz", "Per Infinite S12"], ["Mono · classe D · DSP", "Amplificatore per subwoofer", "Infinite"],
        ["L'<strong>Elipson Infinite A1000</strong> è un amplificatore mono in classe D da 1000 W su 4 Ω con DSP, per subwoofer passivi come l'Elipson Infinite S12.", "Filtro, equalizzatore, fase e filtro subsonico regolabili; modalità SUB o LFE."],
        ["1000 W RMS su 4 Ω (< 1% THD), classe D.", "Filtro passa-basso 39,4 – 204 Hz, pendenza 12 – 48 dB/ottava a passi di 6 dB (scheda Elipson).", "Equalizzatore a 9 bande 19,7 – 125 Hz (−6 / +3 dB); 7 preset, 3 per l'Infinite S12.", "Fase 0 – 315° a passi di 45°; subsonico 24 dB/ottava regolabile 20,3 – 40,5 Hz.", "Spegnimento automatico regolabile 5 – 30 minuti; standby < 0,5 W; 115 / 230 V.", "425 × 89 × 368 mm senza piedini e staffe, 12,5 kg."],
        ["XLR bilanciato L/R, RCA, alto livello a morsetti (sensibilità 220 mV RCA/XLR, 2,6 V alto livello).", "Trigger 12 V; accensione automatica a 3,2 mV."], ["Morsetti per il subwoofer.", "Uscite di linea RCA L/R (200 mV)."],
        "elipson-infinite-a1000.jpg » Elipson Infinite A1000, vista frontale ;; elipson-infinite-a1000-retro.jpg » Elipson Infinite A1000, pannello posteriore ;; elipson-infinite-a1000-lato.jpg » Elipson Infinite A1000, vista laterale",
        "Regolazioni dal frontale e dal telecomando: modalità SUB / LFE, filtro, equalizzatore, fase, volume.",
        [{"titolo": "Home cinema · LFE", "voci": ["Uscita LFE del processore all'A1000 in modalità LFE: il filtro lo fa il processore."], "zone": [z("LFE dal processore", "linea"), z("Infinite S12 · 8 Ω", "sub")], "apparecchio": "Elipson A1000"},
         {"titolo": "Stereo · SUB", "voci": ["Modalità SUB: l'A1000 filtra il segnale; dalle uscite RCA il segnale va al finale dei diffusori."], "zone": [z("Ingresso alto livello o RCA", "linea"), z("Infinite S12 · filtro 40 – 200 Hz", "sub")], "apparecchio": "Elipson A1000"}],
        [S12(["Subwoofer passivo da incasso 12″, 8 Ω: 3 preset dedicati nel DSP."]), {"titolo": "Processore AV", "icona": "sorgente", "voci": ["Uscita LFE su XLR o RCA."]}, CTRL | {"voci": ["Trigger 12 V e accensione automatica col segnale."]}],
        "Dati dalla scheda prodotto Elipson, confrontati con la scheda Extrasound: la scheda Extrasound indica un filtro 40 – 200 Hz e un equalizzatore 20 – 125 Hz.", [F("scheda prodotto Elipson Infinite A1000", "https://cdn.shopify.com/s/files/1/0528/0291/2421/files/Fiche_produit_Infinite_A1000_Elipson.pdf")]))
    return out


if __name__ == "__main__":
    for s in run():
        if s:
            print(s)
