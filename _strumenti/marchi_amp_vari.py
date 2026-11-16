"""Schede amplificatori Rotel C8 / C8+, Yamaha XDA-AMP5400RK / XDA-QS5400RK, Marantz Model M4.
Eseguire dalla radice: python3 _strumenti/marchi_amp_vari.py"""
import sys; sys.path.insert(0, '_strumenti')
from schede_util import *

X = 'https://www.extrasound.it/'
def F(l, u): return {"label": l, "url": u}
ROT_SPEC = F("scheda tecnica Rotel C8+", "https://iear.be/docs/spec-sheet/198266.pdf")
ROT_HEN = F("scheda Rotel C8+ (Henley Audio, distributore UK)", "https://www.henleyaudio.co.uk/brands/rotel/products/c8plus-amplifiers/")
ROT_MAN = F("manuale Rotel C8 / C8+", "https://manuals.plus/rotel/c8-and-c8plus-eight-channel-power-amplifiers-manual")
YAMP = F("manuale Yamaha XDA-AMP5400RK", "https://au.yamaha.com/files/download/other_assets/7/1229907/web_VCM9320_XDA-AMP5400RK_om_UAGLF_EnFrEs_C0.pdf")
YQS = F("manuale Yamaha XDA-QS5400RK", "https://se.yamaha.com/files/download/other_assets/2/1229902/web_VCM9300_XDA-QS5400RK_om_UAGLF_EnFrEs_C0.pdf")
MAR = F("Infosheet Marantz Model M4", "https://www.stassen.nl/images/Marantz_Infosheet_Model M4_EU.pdf")
DIFF = {"titolo": "Diffusori da incasso", "link": "diffusori.html", "icona": "soffitto"}
Z4 = lambda w: [{"label": f"Zona {i} · {w}"} for i in range(1, 5)]


def amp(d, imgspec, retro_cap):
    I = imgs(imgspec)
    r = next((i for i in I if "retro" in i["alt"].lower() or "posteriore" in i["alt"].lower()), None)
    d |= {"tipo": "amplificatore", "cat": "M", "crop": True, "img": I[0], "lato_titolo": "Cosa si collega"}
    if r:
        d["retro"] = {"src": r["src"], "alt": r["alt"], "titolo": "Pannello posteriore", "caption": retro_cap}
    return salva(d)


def main():
    out = []
    rot_passi = [["Spegni", "Spegni tutti gli apparecchi prima di collegare, diffusori compresi; volume dell'amplificatore al minimo prima di accendere o spegnere."],
                 ["Ingressi", "Sorgenti sugli ingressi analogici (e digitali sul C8+); la matrice le assegna alle zone."],
                 ["Diffusori", "Morsetti Phoenix estraibili a vite: cabla il connettore a banco, poi inseriscilo."],
                 ["Bridge (opzionale)", "Una coppia di canali a ponte per zona: schema di collegamento nella figura 3 del manuale Rotel."],
                 ["Zone", "Per ogni zona imposta sorgente, volume, bassi, alti e bilanciamento."], ["Controllo", "Trigger 12 V, RS232 o IP verso il sistema di controllo."]]
    out.append(amp({"id": 63199, "slug": "rotel-c8-plus", "brand": "Rotel", "model": "C8+",
        "meta": "Rotel C8+: amplificatore da installazione 8 canali, 4 zone, classe AB, DAC e matrice. Potenze, ingressi, controllo e schemi d'impianto.",
        "chiave": ["8 canali · 4 zone", "8 × 100 W / 8 Ω · 8 × 150 W / 4 Ω", "Bridge 300 W · rack 2U"], "righe": ["8 canali · 4 zone", "Amplificatore multizona", "Rack 2U"],
        "intro": ["Il <strong>Rotel C8+</strong> è un amplificatore da installazione in classe AB a 8 canali e 4 zone: 8 × 100 W su 8 Ω, 8 × 150 W su 4 Ω, 300 W a ponte su 4 Ω.",
                  "4 ingressi analogici e 4 digitali in matrice su tutte le zone, DAC 24 bit / 192 kHz, controllo IP e RS232, rack 2U."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["Classe AB, trasformatore toroidale, 32 dispositivi di uscita.", "Per zona: volume, bassi e alti (±10 dB a 100 Hz e 10 kHz) indipendenti.", "Priority Zone PA Override: annunci su tutte le zone.", "Risposta 10 Hz – 100 kHz (+0, −0,5 dB); S/N 100 dB; THD < 0,1%; fattore di smorzamento 80.", "Rack 2U senza spazio sopra e sotto; 430 × 97 × 414 mm, 18,35 kg.", "Consumo massimo 980 W; standby < 0,5 W (< 2 W in network standby)."]},
                    {"titolo": "Ingressi", "voci": ["4 analogici RCA stereo (430 mV).", "2 coassiali e 2 ottici, 24 bit / 192 kHz, 4 DAC Texas Instruments.", "Ingressi in matrice su tutte le zone.", "Trigger 12 V, RS232, Ethernet (IP)."]},
                    {"titolo": "Uscite", "voci": ["Potenza: 8 × 100 W su 8 Ω, 8 × 150 W su 4 Ω (tutti i canali).", "Bridge: 300 W per canale su 4 Ω (4 canali).", "Morsetti Phoenix estraibili con viti di blocco.", "Uscita fissa RCA e uscite link bufferizzate per altri amplificatori."]}],
        "collega": [DIFF | {"voci": ["Una coppia di diffusori per zona, 4 – 8 Ω; oppure un diffusore a ponte."]}, {"titolo": "Sorgenti", "icona": "sorgente", "voci": ["Fino a 8 sorgenti (4 analogiche, 4 digitali) distribuite alle zone dalla matrice."]},
                    {"titolo": "Controllo", "icona": "domotica", "voci": ["IP e RS232 verso i sistemi di controllo; trigger 12 V."]}],
        "sistemi": [{"titolo": "4 zone stereo", "voci": ["Ogni zona sceglie una delle 8 sorgenti."], "zone": Z4("2 × 100 W / 8 Ω")}, {"titolo": "Messa in servizio", "passi": rot_passi}],
        "nota": "Dati dalla scheda tecnica Rotel C8+ e dal distributore Henley Audio, procedura dal manuale Rotel, confrontati con la scheda Extrasound.", "extrasound": X + "rotel-c8-plus-amplificatore-multizona-8-canali", "fonti": [ROT_SPEC, ROT_HEN, ROT_MAN]},
        "rotel-c8-plus-1000.jpg » Rotel C8+ nero, vista frontale ;; rotel-c8-plus-retro-1000.jpg » Pannello posteriore del Rotel C8+ con ingressi e uscite ;; rotel-c8-plus-interno-1000.jpg » Vista interna del Rotel C8+ con trasformatore toroidale",
        "Ingressi analogici e digitali, morsetti Phoenix, trigger, RS232 ed Ethernet."))
    out.append(amp({"id": 63195, "brand": "Rotel", "model": "C8",
        "meta": "Rotel C8: amplificatore da installazione 8 canali, 4 zone, classe AB. Potenze, ingressi, controllo e schemi d'impianto.",
        "chiave": ["8 canali · 4 zone", "8 × 50 W / 8 Ω · 8 × 70 W / 4 Ω", "Bridge 140 W / 4 Ω"], "righe": ["8 canali · 4 zone", "Amplificatore multizona", "Classe AB"],
        "intro": ["Il <strong>Rotel C8</strong> è un amplificatore da installazione in classe AB a 8 canali e 4 zone: 8 × 50 W su 8 Ω, 8 × 70 W su 4 Ω, 140 W a ponte su 4 Ω.",
                  "4 ingressi analogici, toni per zona, controllo IP e RS232. Rispetto al C8+ non ha ingressi digitali."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["Classe AB, trasformatore toroidale; THD < 0,1%.", "Per zona: volume, bassi e alti (±10 dB a 100 Hz e 10 kHz).", "Risposta 10 Hz – 100 kHz (±0,5 dB); S/N 100 dB; fattore di smorzamento 80.", "Consumo 570 W; standby < 0,5 W."]},
                    {"titolo": "Ingressi", "voci": ["4 RCA stereo (0,3 V / 31 kΩ).", "Trigger 12 V, RS232, IP."]},
                    {"titolo": "Uscite", "voci": ["Potenza: 8 × 50 W su 8 Ω, 8 × 70 W su 4 Ω (tutti i canali).", "Bridge: 140 W su 4 Ω.", "Morsetti Phoenix."]}],
        "collega": [DIFF | {"voci": ["Una coppia di diffusori per zona, 4 – 8 Ω; oppure un diffusore a ponte."]}, {"titolo": "Sorgenti", "icona": "sorgente", "voci": ["4 sorgenti analogiche assegnabili alle zone."]},
                    {"titolo": "Controllo", "icona": "domotica", "voci": ["IP e RS232 verso i sistemi di controllo; trigger 12 V."]}],
        "sistemi": [{"titolo": "4 zone stereo", "voci": ["Ogni zona con sorgente e toni propri."], "zone": Z4("2 × 50 W / 8 Ω")}, {"titolo": "Messa in servizio", "passi": rot_passi}],
        "nota": "Rotel non pubblica una scheda tecnica separata del C8: potenze, consumo e ingressi sono dati Extrasound; procedura dal manuale Rotel C8 / C8+. Da confermare con Rotel.", "extrasound": X + "rotel-c8-amplificatore-multizona-8-canali", "fonti": [ROT_MAN]},
        "rotel-c8-1000.jpg » Rotel C8 nero, vista frontale ;; rotel-c8-retro-1000.jpg » Pannello posteriore del Rotel C8 con ingressi e uscite ;; rotel-c8-interno-1000.jpg » Vista interna del Rotel C8 con trasformatore toroidale",
        "Ingressi RCA, morsetti Phoenix, trigger, RS232 ed Ethernet."))
    rack_y = ["Rack EIA con le staffe e le viti incluse; con altri apparecchi che scaldano lascia più di 1U sopra e sotto, retro del rack aperto, almeno 10 cm dalle pareti.", "Senza rack: piedini antiscivolo e 10 cm liberi sopra, ai lati e dietro."]
    out.append(amp({"id": 29683, "brand": "Yamaha", "model": "XDA-AMP5400RK",
        "meta": "Yamaha XDA-AMP5400RK: amplificatore multizona 8 canali, 4 zone, classe D, rack 1U. Potenze, bridge, trigger, Audio Sense e collegamenti.",
        "chiave": ["8 canali · 4 zone", "50 W / 8 Ω · 90 W / 4 Ω", "Bridge 100 W / 8 Ω · 1U"], "righe": ["8 canali · 4 zone", "Amplificatore multizona", "Rack 1U"],
        "intro": ["Lo <strong>Yamaha XDA-AMP5400RK</strong> è un amplificatore multizona a 8 canali per 4 zone stereo, in formato 1U: 50 W su 8 Ω e 90 W su 4 Ω per canale, ponte da 100 W su 8 Ω.",
                  "Non ha controlli di volume: va pilotato da una sorgente con volume, ad esempio lo streamer XDA-QS5400RK o un preamplificatore."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["Potenza nominale: 90 / 50 W su 4 / 8 Ω (2 canali); dinamica tutti i canali 80 / 50 W.", "Massima effettiva (JEITA): 130 / 65 W; 260 W a ponte.", "THD 0,04% (25 W, 8 Ω); S/N 108 dB; risposta 5 Hz – 40 kHz.", "Audio Sense: accende la zona quando arriva il segnale (modalità STANDBY ~7 s, ACTIVE ~1 s). Auto standby dopo 8 ore.", "437 × 46 × 443 mm, 6 kg; consumo massimo 130 W, standby 0,3 – 0,5 W."]},
                    {"titolo": "Ingressi", "voci": ["4 ingressi RCA stereo (AMP 1–4 IN), massimo 1 V; uscite passanti THRU OUT, attive anche in standby.", "Trigger IN 1–4 (mini-jack mono, 12 V).", "IR IN / OUT (mini-jack mono)."]},
                    {"titolo": "Uscite", "voci": ["4 uscite diffusori su Euroblock (L/R), cavo da AWG26 a AWG16, non stagnato.", "Bridge: 100 W su 8 Ω per zona; diffusori da 8 Ω o più.", "Carico minimo 4 Ω in modalità normale.", "Trigger OUT 1–4, 12 V."]}],
        "collega": [DIFF | {"voci": ["Una coppia di diffusori per zona, 4 Ω o più; a ponte 8 Ω o più."]}, {"titolo": "Sorgenti con volume", "icona": "sorgente", "voci": ["Streamer o preamplificatore con regolazione di volume: l'amplificatore non ne ha.", "Per configurazioni mono o con una sorgente su più zone usa i ponticelli e i cavi RCA mono (esempi 1–7 del manuale)."]},
                    {"titolo": "Trigger e IR", "icona": "domotica", "voci": ["Trigger IN per accendere ogni zona, trigger OUT per accendere altri apparecchi; IR passante."]}],
        "sistemi": [{"titolo": "4 zone stereo", "voci": ["Una sorgente per zona, accensione da trigger o Audio Sense."], "zone": Z4("2 × 50 W / 8 Ω")},
                    {"titolo": "Messa in servizio", "passi": [["Stacca la corrente", "Scollega il cavo di alimentazione prima di collegare o di cambiare gli interruttori NORMAL/BRIDGE e AUDIO SENSE."], ["Sorgente", "Collega una sorgente con volume."], ["Diffusori", "Allenta le viti degli Euroblock, inserisci i cavi, stringi e inserisci il connettore in SPEAKERS."], ["Ingressi", "Cavi RCA stereo, o ponticelli e RCA mono per gli schemi del manuale."], ["Trigger e IR", "Cavi mini-jack mono."], ["Installazione", rack_y[0]]]}],
        "nota": "Dati e procedura dal manuale Yamaha XDA-AMP5400RK, confrontati con la scheda Extrasound.", "extrasound": X + "yamaha-xda-amp5400rk-amplificatore-multi-room-8-canali-4-zone-classe-d", "fonti": [YAMP]},
        "XDA-AMP5400RK-frontale.jpg » Yamaha XDA-AMP5400RK visto di fronte ;; XDA-AMP5400RK-frontale-2.jpg » Yamaha XDA-AMP5400RK, frontale con indicatori di stato ;; XDA-AMP5400RK-lato.jpg » Yamaha XDA-AMP5400RK visto di lato", ""))
    out.append(amp({"id": 29693, "brand": "Yamaha", "model": "XDA-QS5400RK",
        "meta": "Yamaha XDA-QS5400RK: streamer MusicCast a 4 zone con amplificatore 8 canali, rack 1U. Potenze, ingressi, CUT IN, zone e messa in servizio.",
        "chiave": ["4 zone · MusicCast", "50 W / 8 Ω · 90 W / 4 Ω", "CUT IN · rack 1U"], "righe": ["8 canali · 4 zone", "Streamer amplificato MusicCast", "Rack 1U"],
        "intro": ["Lo <strong>Yamaha XDA-QS5400RK</strong> è uno streamer MusicCast a 4 zone con amplificatore a 8 canali integrato, in formato 1U: 50 W su 8 Ω e 90 W su 4 Ω per canale, ponte da 100 W su 8 Ω.",
                  "Ogni zona ha sorgente, volume e limite massimo propri; ingresso CUT IN per annunci e due porte Ethernet."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["Potenza nominale: 90 / 50 W su 4 / 8 Ω (2 canali); a ponte 100 W su 8 Ω.", "MusicCast, AirPlay, radio Internet, servizi di streaming, server di rete.", "Formati: WAV, MP3, WMA, AAC, FLAC, ALAC, AIFF.", "Per zona: accensione, volume (−80 a 0 dB), mute, sorgente, volume massimo e iniziale.", "437 × 46 × 443 mm, 6,3 kg; consumo massimo 130 W; standby 0,2 W (6 W con 4 zone in network standby)."]},
                    {"titolo": "Ingressi", "voci": ["CUT IN e AUX RCA stereo (AUX massimo 2,4 V).", "4 USB 2.0 per memorie.", "2 Ethernet: mai entrambe sullo stesso router.", "IR IN."]},
                    {"titolo": "Uscite", "voci": ["4 uscite diffusori su Euroblock; carico minimo 4 Ω (8 Ω a ponte).", "4 PRE OUT RCA stereo (2 V nominali).", "4 trigger OUT 12 V, IR OUT, 4 chime."]}],
        "collega": [DIFF | {"voci": ["Una coppia di diffusori per zona; a ponte un diffusore da 8 Ω o più."]}, {"titolo": "Annunci (CUT IN)", "icona": "microfono", "voci": ["Fade: abbassa la musica e mixa l'annuncio; Cut: sostituisce la musica. Sensibilità, trim e accensione da CUT IN regolabili."]},
                    {"titolo": "Rete", "icona": "rete", "voci": ["App MusicCast CONTROLLER; configurazione avanzata dal browser all'indirizzo IP seguito da /Setup."]}],
        "sistemi": [{"titolo": "4 zone", "voci": ["Output Select assegna ogni coppia di canali a una zona (predefinito AMP1 → zona 1 … AMP4 → zona 4)."], "zone": Z4("2 × 50 W / 8 Ω")},
                    {"titolo": "Messa in servizio", "passi": [["Installa", rack_y[0]], ["Collega", "Diffusori agli Euroblock, eventuali PRE OUT, CUT IN e trigger; un solo cavo Ethernet verso il router."], ["MusicCast", "Apri l'app MusicCast CONTROLLER, tocca Setup, tieni premuto CONNECT per 5 secondi e segui le istruzioni."], ["Altre zone", "Aggiungi ogni zona con «Add New Device» nelle impostazioni dell'app."], ["Web setup", "Indirizzo IP + /Setup nel browser per Output Select, CUT IN, volumi e standby."], ["Bridge (opzionale)", "Cavo di alimentazione staccato, interruttore su BRIDGE, diffusori da 8 Ω o più."]]}],
        "nota": "Dati e procedura dal manuale Yamaha XDA-QS5400RK, confrontati con la scheda Extrasound.", "extrasound": X + "yamaha-xda-qs5400rk-streamer-musiccast-multi-room-4-zone-con-amplificatore-8-canali", "fonti": [YQS]},
        "XDA-QS5400rk-frontale.jpg » Yamaha XDA-QS5400RK visto di fronte ;; XDA-QS5400rk-zone.jpg » Yamaha XDA-QS5400RK, indicatori delle 4 zone ;; XDA-QS5400rk-retro.jpg » Pannello posteriore dello Yamaha XDA-QS5400RK",
        "Euroblock dei diffusori, PRE OUT, CUT IN, AUX, USB, Ethernet, trigger e IR."))
    out.append(amp({"id": 35865, "brand": "Marantz", "model": "Model M4",
        "meta": "Marantz Model M4: amplificatore streaming HEOS 8 canali, 4 zone. Potenze, ingressi, uscite sub, controllo IP e collegamenti.",
        "chiave": ["8 canali · 4 zone HEOS", "8 × 100 W / 8 Ω", "Controllo IP · rack"], "righe": ["8 canali · 4 zone", "Amplificatore streaming HEOS", "Rack"],
        "intro": ["Il <strong>Marantz Model M4</strong> è un amplificatore di distribuzione a 8 canali e 4 zone con HEOS integrato: 8 × 100 W su 8 Ω, 125 W su 4 Ω, modalità a ponte.",
                  "Ogni zona ha streaming indipendente, uscita pre o subwoofer con filtri, trigger 12 V; controllo IP per Crestron, Control4 e AMX."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["8 × 100 W su 8 Ω (20 Hz – 20 kHz, 0,05% THD); 125 W su 4 Ω (1 kHz, 0,1%).", "Diffusori da 4 a 16 Ω; modalità a ponte (4 × 200 W secondo Extrasound).", "HEOS, AirPlay 2, Spotify Connect, TIDAL, Amazon Music, Deezer, TuneIn; DLNA.", "Decodifica Dolby Digital, LPCM, DSD 2,8 / 5,6 MHz; FLAC, ALAC, WAV fino a 192 kHz / 24 bit.", "Niente Wi-Fi né Bluetooth: solo rete cablata.", "442 × 415 × 106 mm, 8 kg; raffreddamento attivo, kit rack incluso."]},
                    {"titolo": "Ingressi", "voci": ["4 RCA stereo, 2 ottici.", "4 USB-A (FAT32 e NTFS).", "2 Ethernet."]},
                    {"titolo": "Uscite", "voci": ["Morsetti per 8 canali (4 zone).", "4 pre out RCA stereo, oppure 4 uscite subwoofer mono (selezionabili).", "Filtri: passa-alto 40 – 250 Hz, passa-basso 40 – 120 Hz.", "4 trigger 12 V, uno per zona."]}],
        "collega": [DIFF | {"voci": ["Una coppia di diffusori per zona, 4 – 16 Ω."]}, {"titolo": "Subwoofer", "icona": "subwoofer", "voci": ["Subwoofer attivo sull'uscita della zona impostata come SUB, con passa-alto sui diffusori."]},
                    {"titolo": "Controllo e rete", "icona": "rete", "voci": ["App HEOS; controllo TCP/IP per Crestron, Control4, AMX."]}],
        "sistemi": [{"titolo": "4 zone", "voci": ["Ogni zona ha il suo modulo HEOS e può riprodurre una sorgente diversa."], "zone": Z4("2 × 100 W / 8 Ω")},
                    {"titolo": "Messa in servizio", "passi": [["Monta", "Nel rack con il kit incluso, rispettando la ventilazione."], ["Collega", "Diffusori ai morsetti, eventuali subwoofer o pre out, sorgenti locali."], ["Rete", "Cavo Ethernet (il Wi-Fi non c'è)."], ["Configura", "App HEOS per zone e servizi; integrazione IP con il sistema di controllo."]]}],
        "nota": "Dati dall'Infosheet Marantz Model M4, confrontati con la scheda Extrasound. Potenza a ponte e procedura di dettaglio da confermare sul manuale Marantz.", "extrasound": X + "amplificatore-multi-zona-100w-marantz-model-m4", "fonti": [MAR]},
        "dfhdg-149.jpg » Marantz Model M4, amplificatore multizona ;; gdf-129.jpg » Marantz Model M4, altra vista", "Morsetti, pre out e sub out, ingressi, USB, Ethernet e trigger."))
    return out


if __name__ == "__main__":
    for s in main():
        print(s)
