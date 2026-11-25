"""Schede SORGENTI (streamer di rete da impianto): WiiM Pro, Pro Plus, Ultra, NAD CS1.
Criterio (25/11/2026): streamer senza amplificazione, con uscita trigger 12 V e rete cablata,
da collegare agli ingressi di zona degli amplificatori multizona. Dati dalle pagine e dai manuali dei produttori.
Esclusi dopo la verifica: Arcam ST5/ST25 e JBL MP350 Classic (nessun trigger, IR o RS232 dichiarato),
ELAC Discovery DS-S101-G e DS-C101W (fuori produzione per ELAC), ArtSound Smart Stream (nessuna fonte del produttore).
Eseguire dalla radice: python3 _strumenti/marchi_sorgenti.py"""
import json, sys
sys.path.insert(0, '_strumenti')
from schede_util import *

X = 'https://www.extrasound.it/'
def F(l, u): return {"label": l, "url": u}
WIIM_TRIG = F("WiiM: uso del trigger 12 V", "https://faq.wiimhome.com/en/support/solutions/articles/72000602073-how-to-use-the-12v-trigger-on-wiim-pro-wiim-pro-plus-or-wiim-ultra-")


def card(slug, voci):
    d = json.loads((DATI / f"{slug}.json").read_text(encoding="utf-8"))
    return {"titolo": f"{d['brand']} {d['model']}", "link": f"scheda-{slug}.html", "img": d["img"]["src"], "alt": d["img"]["alt"], "voci": voci}


def base(d, main, fronte, retro, retro_cap, gui_cap, schema=None):
    d |= {"tipo": "sorgente", "cat": "N", "crop": True, "tab": "Sorgenti<br>di rete", "tipo_label": "Streamer di rete",
          "lato_titolo": "Cosa si collega",
          "img": {"src": U + main[0], "alt": main[1]},
          "gui": {"src": U + fronte[0], "alt": fronte[1], "caption": gui_cap},
          "retro": {"src": U + retro[0], "alt": retro[1], "titolo": "Pannello posteriore", "caption": retro_cap}}
    if schema:
        d["viste"] = [{"src": U + schema[0], "alt": schema[1], "caption": "Schema dei collegamenti"}]
    return salva(d)


def collega_comune(nome, trig):
    return [card("elac-is-amp8100", [f"Uscita RCA del {nome} sull'ingresso analogico della zona.",
                                     f"Il trigger 12 V ({trig}) accende l'amplificatore quando parte la musica."]),
            card("rotel-c8-plus", ["4 ingressi analogici in matrice sulle 4 zone.", "Ingresso trigger 12 V."]),
            {"titolo": "Rete", "icona": "rete",
             "voci": ["Cavo Ethernet consigliato per l'impianto fisso.", "Configurazione e gruppi multiroom dall'app del produttore."]}]


def zone4(nome):
    return {"titolo": "Multizona · un apparecchio per zona",
            "voci": [f"Un {nome} per stanza, ciascuno sull'ingresso analogico della sua zona.",
                     "Le zone si uniscono dall'app quando serve la stessa musica in più stanze."],
            "apparecchio": "Amplificatore 4 zone",
            "zone": [{"label": f"Zona {i} · ingresso dal {nome}"} for i in range(1, 5)]}


def main():
    out = []
    # ---------------- WiiM Pro ----------------
    p = "WiiM Pro"
    out.append(base({"id": 46464, "slug": "wiim-pro", "brand": "WiiM", "model": "Pro",
        "meta": "WiiM Pro: streamer di rete con uscita RCA, ottica e coassiale, Ethernet e trigger 12 V. Collegamenti e schemi per l'installatore.",
        "chiave": ["Streamer · Ethernet e Wi-Fi", "Uscite RCA, ottica, coassiale", "Trigger 12 V · USB-C 5 V"],
        "righe": ["Streamer di rete", "Una zona per apparecchio", "140 × 140 × 42 mm"],
        "intro": ["Il <strong>WiiM Pro</strong> è uno streamer di rete con uscita analogica RCA e uscite digitali ottica e coassiale fino a 24 bit / 192 kHz, Ethernet 10/100 e Wi-Fi dual band.",
                  "L'uscita trigger 12 V accende l'amplificatore; più WiiM lavorano in multiroom, uno per zona sull'ingresso della zona."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["AirPlay 2, Google Cast, Spotify Connect, TIDAL Connect, DLNA, Roon Ready.", "Fino a 24 bit / 192 kHz; DAC Texas Instruments Burr-Brown PCM5121.", "Correzione ambientale RoomFit, equalizzatore grafico e parametrico a 10 bande.", "Bluetooth 5.0 in ricezione e in trasmissione.", "140 × 140 × 42 mm, 330 g; da 0 a 40 °C."]},
                    {"titolo": "Ingressi", "voci": ["Line In RCA, 1 Vrms (convertito a 48 kHz / 24 bit).", "Ottico S/PDIF fino a 192 kHz / 24 bit, solo PCM stereo (Dolby Digital e DTS non supportati).", "Ethernet RJ-45 10/100 Mbps: con il cavo collegato il Wi-Fi si spegne.", "Wi-Fi 802.11 a/b/g/n/ac, 2,4 e 5 GHz.", "Alimentazione USB-C 5 V ≥ 1,5 A (alimentatore 5 V / 2 A incluso)."]},
                    {"titolo": "Uscite", "voci": ["Line Out RCA stereo.", "Ottica e coassiale, fino a 192 kHz / 24 bit.", "Trigger 12 V, jack 2,5 mm, 220 mA.", "Bluetooth A2DP verso cuffie o diffusori."]}],
        "collega": collega_comune(p, "jack 2,5 mm"),
        "sistemi": [zone4(p), {"titolo": "Messa in servizio", "passi": [
            ["Rete", "Cavo Ethernet nella presa LAN, oppure Wi-Fi configurato dall'app WiiM Home."],
            ["Uscita", "Line Out RCA verso l'ingresso dell'amplificatore; ottica o coassiale verso un DAC o un AV receiver."],
            ["Trigger", "Cavo jack 2,5 mm (mono TS o stereo TRS) verso l'ingresso trigger dell'amplificatore."],
            ["Alimentazione", "Alimentatore USB-C 5 V / 2 A incluso."],
            ["App", "Nome della zona, ingressi, EQ e ritardo di standby del trigger."],
            ["Multiroom", "Gruppi di zone dall'app WiiM Home."]]}],
        "extrasound": X + "wiim-pro-streamer-hi-res-roon-ready-airplay-google-cast",
        "fonti": [F("specifiche WiiM Pro", "https://www.wiimhome.com/wiimpro/specs"), F("manuale WiiM Pro", "https://www.wiimhome.com/pdf/WiiM Pro User Manual.pdf"), WIIM_TRIG]},
        ("WiiM-Pro.jpg", "WiiM Pro nero visto di tre quarti"), ("WiiM-Pro-frontale.jpg", "WiiM Pro visto di fronte con i LED di stato"),
        ("WiiM-Pro-posteriore.jpg", "WiiM Pro, pannello posteriore con ingressi e uscite"),
        "Line In e Line Out RCA, trigger 12 V, USB-C, ottico in e out, coassiale out, LAN.",
        "Si configura dall'app WiiM Home: ingressi, EQ, RoomFit, gruppi multiroom e ritardo del trigger.",
        ("WiiM-Pro-aperto-a-tutto.jpg", "Schema dei collegamenti del WiiM Pro")))

    # ---------------- WiiM Pro Plus ----------------
    p = "WiiM Pro Plus"
    out.append(base({"id": 46480, "slug": "wiim-pro-plus", "brand": "WiiM", "model": "Pro Plus",
        "meta": "WiiM Pro Plus: streamer di rete con DAC AKM, uscite RCA, ottica e coassiale, Ethernet e trigger 12 V. Collegamenti e schemi per l'installatore.",
        "chiave": ["Streamer · DAC AKM AK4493SEQ", "Uscite RCA, ottica, coassiale", "Trigger 12 V · USB-C 5 V"],
        "righe": ["Streamer di rete", "Una zona per apparecchio", "140 × 140 × 42 mm"],
        "intro": ["Il <strong>WiiM Pro Plus</strong> è uno streamer di rete con DAC AKM AK4493SEQ, uscita analogica RCA e uscite digitali ottica e coassiale fino a 24 bit / 192 kHz.",
                  "Ethernet 10/100, Wi-Fi dual band e trigger 12 V con adattatore incluso; più apparecchi lavorano in multiroom, uno per zona."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["AirPlay 2, Google Cast, Spotify Connect, TIDAL Connect, Amazon Music Casting, DLNA, Roon Ready.", "DAC AKM AK4493SEQ: S/N 121 dB, THD+N −113 dB.", "Risposta 20 Hz – 20 kHz ±0,1 dB.", "Correzione ambientale RoomFit, equalizzatore grafico e parametrico a 10 bande.", "Bluetooth 5.0.", "140 × 140 × 42 mm, 400 g."]},
                    {"titolo": "Ingressi", "voci": ["Line In RCA, 2 Vrms (convertito a 192 kHz / 24 bit).", "Ottico S/PDIF fino a 192 kHz / 24 bit, solo PCM stereo.", "Ethernet 10/100 Mbps.", "Wi-Fi 802.11 b/g/n/ac, 2,4 e 5 GHz.", "Alimentazione USB-C 5 V ≥ 1,5 A (alimentatore 5 V / 2 A incluso)."]},
                    {"titolo": "Uscite", "voci": ["Line Out RCA stereo.", "Ottica e coassiale, fino a 192 kHz / 24 bit.", "Trigger 12 V, jack 2,5 mm; adattatore per trigger incluso."]}],
        "collega": collega_comune(p, "jack 2,5 mm"),
        "sistemi": [zone4(p), {"titolo": "Messa in servizio", "passi": [
            ["Rete", "Cavo Ethernet nella presa LAN, oppure Wi-Fi configurato dall'app WiiM Home."],
            ["Uscita", "Line Out RCA verso l'ingresso dell'amplificatore; ottica o coassiale verso un DAC o un AV receiver."],
            ["Trigger", "Cavo jack 2,5 mm verso l'ingresso trigger dell'amplificatore, con l'adattatore incluso se serve un jack diverso."],
            ["Alimentazione", "Alimentatore USB-C 5 V / 2 A incluso."],
            ["App", "Nome della zona, ingressi, EQ e ritardo di standby del trigger."],
            ["Multiroom", "Gruppi di zone dall'app WiiM Home."]]}],
        "extrasound": X + "wiim-pro-plus-streamer-hi-res-dac-akm-roon-ready",
        "fonti": [F("pagina WiiM Pro Plus", "https://wiimhome.com/products/wiim-pro-plus/"), WIIM_TRIG]},
        ("WiiM-Pro-Plus.jpg", "WiiM Pro Plus nero visto di tre quarti"), ("WiiM-Pro-Plus-frontale.jpg", "WiiM Pro Plus visto di fronte con i LED di stato"),
        ("WiiM-Pro-Plus-posteriore.jpg", "WiiM Pro Plus, pannello posteriore con ingressi e uscite"),
        "Line In e Line Out RCA, trigger 12 V, USB-C, ottico in e out, coassiale out, LAN.",
        "Si configura dall'app WiiM Home: ingressi, EQ, RoomFit, gruppi multiroom e ritardo del trigger.",
        ("WiiM-Pro-Plus-connessioni.jpg", "Schema dei collegamenti del WiiM Pro Plus")))

    # ---------------- WiiM Ultra ----------------
    p = "WiiM Ultra"
    out.append(base({"id": 46521, "slug": "wiim-ultra", "brand": "WiiM", "model": "Ultra",
        "meta": "WiiM Ultra: streamer di rete con DAC ESS, ingressi HDMI ARC e phono, uscita subwoofer e trigger 12 V. Collegamenti e schemi per l'installatore.",
        "chiave": ["Streamer · DAC ESS ES9038Q2M", "HDMI ARC · phono · uscita sub", "Trigger 12 V · Wi-Fi 6"],
        "righe": ["Streamer di rete", "Sala o zona principale", "211 × 200 × 72 mm"],
        "intro": ["Il <strong>WiiM Ultra</strong> è uno streamer di rete con DAC ESS ES9038Q2M, ingresso HDMI ARC per il televisore, ingresso phono MM/MC e uscita subwoofer.",
                  "Ethernet 10/100, Wi-Fi 6 e trigger 12 V su jack 3,5 mm; alimentazione di rete 100–240 V."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["Google Cast, Spotify Connect, TIDAL Connect, Amazon Music Casting, DLNA, Squeezelite, Roon Ready.", "DAC ESS ES9038Q2M: S/N 121 dB, THD+N −116 dB all'uscita analogica.", "Bluetooth 5.3.", "Alimentazione 100–240 V AC, 50/60 Hz, 0,5 A massimi.", "211 × 200 × 72 mm, 1,42 kg."]},
                    {"titolo": "Ingressi", "voci": ["HDMI ARC fino a 192 kHz / 24 bit: PCM stereo e Dolby Digital (DTS non supportato).", "Phono MM/MC.", "Line In RCA, 2 Vrms.", "Ottico fino a 192 kHz / 24 bit, PCM stereo e Dolby Digital.", "USB per memorie esterne (FAT32, NTFS, EXT4).", "Ethernet 10/100 Mbps; Wi-Fi 6."]},
                    {"titolo": "Uscite", "voci": ["Line Out RCA stereo.", "Uscita subwoofer.", "Coassiale e ottica fino a 192 kHz / 24 bit.", "Cuffie jack 3,5 mm.", "USB audio fino a 192 kHz / 24 bit (UAC 2.0).", "Trigger 12 V, jack 3,5 mm."]}],
        "collega": collega_comune(p, "jack 3,5 mm") + [{"titolo": "Televisore", "icona": "sorgente", "voci": ["Cavo HDMI sulla presa ARC del televisore: l'audio della TV va all'impianto."]}],
        "sistemi": [{"titolo": "Zona con televisore e subwoofer", "voci": ["Il televisore entra in HDMI ARC; Line Out verso l'amplificatore della zona, uscita sub verso un subwoofer attivo."],
                     "apparecchio": "Amplificatore",
                     "zone": [{"label": "Frontali · da Line Out del WiiM Ultra"}, {"label": "Subwoofer attivo · da uscita sub", "tipo": "sub"}]},
                    {"titolo": "Messa in servizio", "passi": [
            ["Rete", "Cavo Ethernet nella presa LAN, oppure Wi-Fi configurato dall'app WiiM Home."],
            ["Televisore", "HDMI sulla presa ARC del televisore."],
            ["Uscite", "Line Out RCA verso l'amplificatore; uscita sub verso il subwoofer attivo."],
            ["Trigger", "Cavo jack 3,5 mm (mono TS o stereo TRS) verso l'ingresso trigger dell'amplificatore."],
            ["Alimentazione", "Cavo di rete 100–240 V."],
            ["App", "Ingressi, uscita sub, EQ e ritardo di standby del trigger dall'app WiiM Home."]]}],
        "extrasound": X + "wiim-ultra-streamer-hi-res-dac-ess-hdmi-phono-roon",
        "fonti": [F("specifiche WiiM Ultra", "https://www.wiimhome.com/wiimultra/specs"), F("manuale WiiM Ultra", "https://www.wiimhome.com/pdf/WiiM+Ultra+User+Manual.pdf"), WIIM_TRIG]},
        ("WiiM-Ultra-alto.jpg", "WiiM Ultra grigio visto di tre quarti"), ("WiiM-Ultra.jpg", "Due WiiM Ultra nelle finiture grigia e silver"),
        ("WiiM-Ultra-posteriore.jpg", "WiiM Ultra, pannello posteriore con ingressi e uscite"),
        "HDMI ARC, phono, Line In, ottico in, USB; Line Out, sub out, coassiale e ottico out, trigger 12 V, LAN.",
        "Si configura dall'app WiiM Home: ingressi, uscita sub, EQ, RoomFit e ritardo del trigger.",
        ("WiiM-Ultra-connessioni.jpg", "Schema dei collegamenti del WiiM Ultra")))

    # ---------------- NAD CS1 ----------------
    p = "NAD CS1"
    out.append(base({"id": 46140, "slug": "nad-cs1", "brand": "NAD", "model": "CS1",
        "meta": "NAD CS1: streamer di rete endpoint con uscite RCA, coassiale e ottica, Ethernet e trigger 12 V. Collegamenti e schemi per l'installatore.",
        "chiave": ["Streamer endpoint · Ethernet e Wi-Fi 5", "Uscite RCA, coassiale, ottica", "Trigger 12 V · 140 × 140 mm"],
        "righe": ["Streamer di rete", "Una zona per apparecchio", "140 × 140 × 55 mm"],
        "intro": ["Il <strong>NAD CS1</strong> è uno streamer di rete senza ingressi audio, con uscita analogica RCA e uscite digitali coassiale e ottica, fino a 24 bit / 192 kHz.",
                  "Ethernet, Wi-Fi 5 e Bluetooth 5.2; l'uscita trigger 12 V accende l'amplificatore della zona."],
        "colonne": [{"titolo": "Caratteristiche", "voci": ["Spotify Connect, TIDAL Connect, AirPlay 2, Chromecast, Roon, DLNA.", "Fino a 192 kHz, 16–24 bit.", "DAC Texas Instruments; processore ARM Cortex-A53 quad core.", "Bluetooth 5.2 con NFC.", "140 × 140 × 55 mm (con piedini e connettori), 1,5 kg."]},
                    {"titolo": "Ingressi", "voci": ["Nessun ingresso audio.", "Ethernet RJ-45 100 Mbps.", "Wi-Fi 5 (802.11ac, 2,4 e 5 GHz).", "USB-C per l'alimentatore."]},
                    {"titolo": "Uscite", "voci": ["Analogica RCA stereo.", "Coassiale RCA 75 Ω.", "Ottica Toslink.", "Trigger 12 V, jack 3,5 mm."]}],
        "collega": collega_comune(p, "jack 3,5 mm"),
        "sistemi": [zone4(p), {"titolo": "Messa in servizio", "passi": [
            ["Rete", "Cavo Ethernet nella presa RJ-45, oppure Wi-Fi."],
            ["Uscita", "RCA verso l'ingresso dell'amplificatore; coassiale o ottica verso un DAC o un AV receiver."],
            ["Trigger", "Cavo jack 3,5 mm verso l'ingresso trigger dell'amplificatore."],
            ["Alimentazione", "Alimentatore 100–240 V incluso, uscita 5 V DC 1 A su USB-C; 0,5 W in standby di rete."],
            ["Posa", "Formato da 140 × 140 mm: trova posto nel rack o accanto all'amplificatore."],
            ["App", "Configurazione e zone dall'app del produttore."]]}],
        "extrasound": X + "nad-cs1-streamer-di-rete-hi-res-24-192-con-airplay-2-chromecast-e-roon",
        "fonti": [F("pagina NAD CS1", "https://nadelectronics.com/products/cs1-endpoint-network-streamer"), F("scheda tecnica NAD CS1", "https://nadelectronics.com/wp1.nadelectronics.com/wp-content/uploads/2022/07/CS1-Data-Sheet.pdf")]},
        ("NAD-CS1.jpg", "NAD CS1, streamer di rete: vista di tre quarti"), ("NAD-CS1-frontale.jpg", "NAD CS1 visto di fronte"),
        ("NAD-CS1-rear.jpg", "NAD CS1, pannello posteriore con le uscite"),
        "Uscita analogica RCA, coassiale, ottica, trigger 12 V, Ethernet, USB-C di alimentazione.",
        "Pulsante funzione e LED di stato sul frontale; configurazione dall'app."))
    print("\n".join(out))


if __name__ == "__main__":
    main()
