"""Schede ArtSound. Dati dalle schede tecniche ArtSound (House of Music) pubblicate dai distributori,
confrontati con le schede Extrasound. Eseguire dalla radice: python3 _strumenti/marchi_artsound.py"""
import sys; sys.path.insert(0, '_strumenti')
from schede_util import *

X = 'https://www.extrasound.it/'
def F(label, url): return {"label": label, "url": url}
TELE = 'https://www.telecontrol.ro/domains/telecontrol.ro/files/download_files/'
SRC = {
 "RO2060": F("scheda tecnica ArtSound RO2060", "https://test11.avcomfort.ru/uploads/instructions/accoustics/92855/RO2060_uk.pdf"),
 "RE2060": F("scheda tecnica ArtSound RE2060", "https://avcomfort.ru/uploads/instructions/accoustics/125525/RE2060_uk.pdf"),
 "RE2080": F("scheda tecnica ArtSound RE2080", TELE + "re2080-0-pdf7469.pdf"),
 "RE2040": F("scheda tecnica ArtSound RE2040", TELE + "re2040-0-pdf9842.pdf"),
 "SQ2060": F("scheda tecnica ArtSound SQ2060", TELE + "sq2060-0-pdf1174.pdf"),
 "SQ2040": F("scheda tecnica ArtSound SQ2040 (FR)", "https://res.cloudinary.com/sonepar-fr/raw/upload/s--Smxny5DO--/v1/documents/1110/00001659_SQ2040_fr.pdf"),
 "RO2040": F("scheda tecnica ArtSound RO2040 (NL)", "https://www.iear.be/docs/spec-sheet/182813.pdf"),
 "HPRO650": F("scheda tecnica ArtSound HPRO650", "https://avcomfort.ru/uploads/instructions/accoustics/125524/HPRO650_uk.pdf"),
 "HPRE650": F("scheda tecnica ArtSound HPRE650", TELE + "hpre650-0-pdf8097.pdf"),
 "HPRO525": F("scheda tecnica ArtSound HPRO525", TELE + "hpro525-0-pdf3269.pdf"),
 "HPSQ525": F("scheda tecnica ArtSound HPSQ525", "https://noortehnik.ee/wp-content/uploads/2025/09/HPSQ525-uk.pdf"),
 "HPRO550": F("scheda tecnica ArtSound HPRO550 (FR)", "https://res.cloudinary.com/sonepar-fr/raw/upload/s--c8WmX5qK--/v1/documents/1110/00012823_HPRO550_fr.pdf"),
 "MDC64": F("scheda tecnica ArtSound MDC64", TELE + "mdc64-0-pdf5481.pdf"),
 "MDC6": F("manuale ArtSound MDC6", "https://easylounge.com/pdf/Produits/2f74505f-d093-4dc1-b089-7199a01dfdb6/MDC6_man.pdf"),
 "MDC": F("manuale ArtSound MDC401 / MDC501 / MDC620", "https://stylesound.com/wp-content/uploads/2024/01/MDC401-501-620_manual.pdf"),
 "MD30": F("scheda tecnica ArtSound MD30", TELE + "md30-0-pdf8642.pdf"),
 "FL501": F("scheda tecnica ArtSound FL501", "https://avcomfort.ru/uploads/instructions/accoustics/92851/FL501_uk.pdf"),
 "FL401": F("scheda tecnica ArtSound FL401", TELE + "fl401-0-pdf9639.pdf"),
 "FL101": F("scheda tecnica ArtSound FL101", "https://avcomfort.ru/uploads/instructions/accoustics/86718/FL101_uk.pdf"),
 "FL30": F("scheda tecnica ArtSound FL30", TELE + "fl30-09044.pdf"),
 "FL301": F("scheda tecnica ArtSound FL301 (FR)", "https://easylounge.com/pdf/Produits/bd6ab5c5-79e7-4fce-9a2a-d480b3164e0d/FL301_fr.pdf"),
 "FL550": F("scheda tecnica ArtSound FL550", "https://homemovie.hu/wp-content/uploads/2018/10/FL550_uk.pdf"),
 "FL620": F("scheda tecnica ArtSound FL620", "https://www.mstronics.com/images/products/old/285_spec_enfl620.pdf"),
 "FL502BT": F("scheda tecnica ArtSound FL502BT Single", "https://easylounge.com/pdf/Produits/92ac5879-cf0d-4013-8059-4c1cce3c16bc/fl502-bt-single_657872f27223d.pdf"),
 "FL101BT": F("manuale ArtSound FL101BT / FL501BT", "https://manuals.online/artplussound/speakers/fl101bt/user-manual/1c7x1"),
 "DC84": F("scheda tecnica ArtSound DC84", TELE + "dc84-0-pdf7604.pdf"),
 "MDT500": F("scheda tecnica ArtSound MDT500-P", TELE + "mdt500-p-0-pdf5732.pdf"),
 "MDT600": F("scheda tecnica ArtSound MDT600-P (FR)", "https://res.cloudinary.com/sonepar-fr/raw/upload/s--ot5e3d_v--/v1/documents/1110/00007404_MDT600-P_fr.pdf"),
}
SERIE = {"I": "Intiimi", "H": "Happi", "F": "Flat", "B": "Basic", "W": "Waterproof", "T": "Basic 100 V"}

# id, modello, cat, serie, forma, vie, driver, risposta, sens, imp, amp, foro, est (diametro o [h, l]), prof, peso, kit, fonte, url, extra
M = [
 (29843, "RO2060", "S", "I", "tondo", "2 vie coassiale", ["woofer 6″ al neodimio", "tweeter 1″ a cupola in titanio, orientabile"], "58 Hz – 20 kHz", "87 dB", "4 – 8 Ω", "40 – 140 W (consigliata)", "Ø 210 mm", "Ø 235 mm", "100 mm", "1,8 kg", "KITRO3", "RO2060", "coppia-diffusori-incasso-2-vie-artsound-intiimi-ro2060", {"alti": True}),
 (29834, "RO2040", "S", "I", "tondo", "2 vie coassiale", ["woofer 4″ al neodimio", "tweeter 1″ a cupola in titanio, orientabile"], "60 Hz – 20 kHz", "84 dB", "4 – 8 Ω", "20 – 120 W (consigliata)", "Ø 150 mm", "Ø 175 mm", "80 mm", "1,2 kg", "KITRO1", "RO2040", "coppia-diffusori-incasso-2-vie-artsound-intiimi-ro2040", {"alti": True}),
 (29861, "RE2060", "P", "I", "rett", "2 vie", ["woofer 6″ al neodimio", "tweeter 1″ a cupola in titanio, orientabile"], "58 Hz – 20 kHz", "87 dB", "4 – 8 Ω", "40 – 140 W (consigliata)", ["270 mm", "180 mm"], ["295 mm", "205 mm"], "85 mm", "1,8 kg", "KITRE3", "RE2060", "coppia-diffusori-incasso-2-vie-artsound-intiimi-re2060", {"alti": True}),
 (29870, "RE2080", "P", "I", "rett", "3 vie", ["woofer 8″ al neodimio", "medio 2″ in titanio", "tweeter 1″ a cupola in titanio"], "48 Hz – 20 kHz", "90 dB", "4 – 8 Ω", "160 W massimi", ["335 mm", "230 mm"], ["360 mm", "255 mm"], "100 mm", "2,2 kg", "KITRE4", "RE2080", "artsound-re2080-diffusori-in-wall-3-vie-serie-superiore", {"diff": "La scheda Extrasound indica un'amplificazione di 40 – 160 W; ArtSound dichiara solo la potenza massima, 160 W."}),
 (2909, "RE2040", "P", "I", "rett", "2 vie", ["woofer 4″ al neodimio", "tweeter 1″ a cupola in titanio, orientabile"], "60 Hz – 20 kHz", "84 dB", "4 – 8 Ω", "100 W massimi", ["195 mm", "125 mm"], ["220 mm", "150 mm"], "70 mm", "1,2 kg", "KITRE1", "RE2040", "artsound-re2040-intiimi-diffusori-in-wall-2-vie-con-tweeter-orientabile", {"diff": "La scheda Extrasound indica un'amplificazione di 20 – 120 W; ArtSound dichiara 100 W massimi."}),
 (31048, "SQ2060", "S", "I", "rett", "2 vie coassiale", ["woofer 6″ al neodimio", "tweeter 1″ a cupola in titanio, orientabile"], "58 Hz – 20 kHz", "87 dB", "4 – 8 Ω", "120 W massimi", ["210 mm", "210 mm"], ["235 mm", "235 mm"], "100 mm", "1,8 kg", "KITSQ3", "SQ2060", "coppia-diffusori-incasso-2-vie-artsound-intiimi-sq2060", {"diff": "La scheda Extrasound indica un'amplificazione di 40 – 140 W; ArtSound dichiara 120 W massimi."}),
 (29882, "SQ2040", "S", "I", "rett", "2 vie coassiale", ["woofer 4″ al neodimio", "tweeter 1″ a cupola in titanio"], "60 Hz – 20 kHz", "84 dB", "4 – 8 Ω", "20 – 120 W (consigliata)", ["140 mm", "140 mm"], ["165 mm", "165 mm"], "80 mm", "1,2 kg", "KITSQ1", "SQ2040", "coppia-diffusori-incasso-2-vie-artsound-intiimi-sq2040", {}),
 (32059, "HPRO650", "S", "H", "tondo", "2 vie coassiale", ["woofer 6,5″ in alluminio, sospensione in gomma", "tweeter 0,75″ in alluminio, orientabile"], "50 Hz – 20 kHz", "88 dB", "8 Ω", "20 – 120 W (consigliata)", "Ø 205 mm", "Ø 230 mm", "85 mm", "1,25 kg", "KITRO3", "HPRO650", "artsound-hpro650-coppia-diffusori-da-incasso-rotondi-2-vie-waterproof", {"umido": True}),
 (32050, "HPRE650", "P", "H", "rett", "2 vie", ["woofer 5,25″ in alluminio, sospensione in gomma", "tweeter 0,75″ in alluminio, orientabile"], "50 Hz – 20 kHz", "88 dB", "8 Ω", "60 W massimi", ["245 mm", "160 mm"], ["280 mm", "190 mm"], "70 mm", "1,5 kg", "KITRE2", "HPRE650", "artsound-hpre650-diffusori-da-incasso-rettangolari-2-vie-serie-happi", {"umido": True, "diff": "La scheda Extrasound indica un'amplificazione di 20 – 120 W; ArtSound dichiara 60 W massimi e un woofer da 5,25″."}),
 (31975, "HPRO525", "S", "H", "tondo", "2 vie coassiale", ["woofer 5,25″ in alluminio, sospensione in gomma", "tweeter 0,75″ in alluminio, orientabile"], "50 Hz – 20 kHz", "88 dB", "8 Ω", "60 W massimi", "Ø 180 mm", "Ø 200 mm", "70 mm", "1,1 kg", "KITRO2", "HPRO525", "artsound-hpro525-coppia-diffusori-da-incasso-rotondi-2-vie-per-ambienti-umidi", {"umido": True, "diff": "La scheda Extrasound indica 60 Hz – 20 kHz e 10 – 100 W; ArtSound dichiara 50 Hz – 20 kHz e 60 W massimi."}),
 (31963, "HPSQ525", "S", "H", "rett", "2 vie coassiale", ["woofer 5,25″ in alluminio, sospensione in gomma", "tweeter 0,75″ in alluminio, orientabile"], "60 Hz – 20 kHz", "88 dB", "8 Ω", "10 – 100 W (consigliata)", ["148 mm", "148 mm"], ["170 mm", "170 mm"], "80 mm", "1 kg", "KITSQ4", "HPSQ525", "artsound-hpsq525-coppia-diffusori-da-incasso-quadrati-2-vie-per-ambienti-umidi", {"umido": True}),
 (31957, "HPRO550", "2", "H", "tondo", "2 vie coassiale stereo", ["woofer 5,25″ in alluminio, sospensione in gomma", "2 tweeter 0,75″ in alluminio"], "60 Hz – 20 kHz", "88 dB", "8 Ω", "10 – 100 W (consigliata)", "Ø 180 mm", "Ø 200 mm", "80 mm", "1,1 kg", "KITRO2", "HPRO550", "artsound-hpro550-diffusore-da-incasso-rotondo-stereo-a-singolo-diffusore-lr", {"umido": True, "ds": True}),
 (32142, "MDC64", "S", "W", "tondo", "bobina singola, doppio cono", ["woofer 6,5″ in polipropilene e carbonio a doppio cono"], "95 Hz – 20 kHz", "86 dB", "8 Ω", "100 W massimi", "Ø 133 mm", "Ø 180 mm", "83 mm", "1 kg", "", "MDC64", "artsound-mdc64-diffusori-da-incasso-waterproof-compatti-per-ambienti-umidi-coppia", {"stagno": True}),
 (32085, "MDC6", "S", "W", "tondo", "bobina singola, doppio cono", ["woofer 5″ in polipropilene a doppio cono"], "102 Hz – 20 kHz", "86 dB", "8 Ω", "65 W massimi", "Ø 130 mm", "Ø 155 mm", "50 mm", "0,5 kg", "", "MDC6", "diffusori-da-incasso-waterproof-2-vie-artsound-mdc6", {"stagno": True, "viti": True, "diff": "La scheda Extrasound indica un foro di 125 mm e 10 – 50 W; il manuale ArtSound indica 130 mm e 65 W massimi."}),
 (32077, "MDC620", "S", "B", "tondo", "2 vie coassiale", ["woofer 6,5″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "70 Hz – 20 kHz", "90 dB", "8 Ω", "20 – 120 W (consigliata)", "Ø 205 mm", "Ø 240 mm", "70 mm", "1,2 kg", "", "MDC", "artsound-mdc620-diffusori-da-incasso-soffitto-6-5-multiroom-coppia", {}),
 (30404, "MDC501", "S", "B", "tondo", "2 vie coassiale", ["woofer 5,25″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "85 Hz – 20 kHz", "88 dB", "8 Ω", "10 – 100 W (consigliata)", "Ø 175 mm", "Ø 212 mm", "70 mm", "0,89 kg", "", "MDC", "artsound-mdc501-diffusori-da-incasso-soffitto-compatti-per-multiroom-coppia", {}),
 (30341, "MDC401", "S", "B", "tondo", "2 vie coassiale", ["woofer 4″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "90 Hz – 20 kHz", "86 dB", "8 Ω", "10 – 85 W (consigliata)", "Ø 135 mm", "Ø 165 mm", "70 mm", "0,75 kg", "", "MDC", "artsound-mdc401-diffusori-da-incasso-soffitto-ultra-compatti-multiroom-coppia", {}),
 (32068, "MD30", "S", "B", "tondo", "gamma intera", ["altoparlante 3″ in polipropilene"], "50 Hz – 15 kHz", "91 dB", "8 Ω", "20 W massimi", "Ø 80 mm", "Ø 105 mm", "44 mm", "0,375 kg", "KIT RO105", "MD30", "artsound-md30-diffusori-da-incasso-soffitto-compatti-multiroom-coppia", {"diff": "La scheda Extrasound indica un'amplificazione di 10 – 50 W e corpo in metallo; ArtSound dichiara 20 W massimi e corpo in ABS."}),
 (40043, "FL501", "S", "F", "tondo", "2 vie coassiale", ["woofer 5,25″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "85 Hz – 20 kHz", "88 dB", "8 Ω", "10 – 100 W (consigliata)", "Ø 180 mm", "Ø 200 mm", "70 mm", "1 kg", "KITRO2 · MOKIT RO212", "FL501", "artsound-fl501-diffusore-da-incasso-rotondo-2-vie-con-griglia-magnetica-verniciabile", {"flat": True}),
 (39961, "FL401", "S", "F", "tondo", "2 vie coassiale", ["woofer 4″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "70 Hz – 20 kHz", "84 dB", "8 Ω", "60 W massimi", "Ø 160 mm", "Ø 180 mm", "70 mm", "1 kg", "", "FL401", "artsound-fl401-diffusore-da-incasso-rotondo-2-vie-con-griglia-magnetica-verniciabile", {"flat": True, "diff": "La scheda Extrasound indica 90 Hz – 20 kHz e 10 – 100 W; ArtSound dichiara 70 Hz – 20 kHz e 60 W massimi."}),
 (40409, "FL101", "S", "F", "rett", "2 vie coassiale", ["woofer 5,25″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "85 Hz – 20 kHz", "88 dB", "8 Ω", "10 – 100 W (consigliata)", ["148 mm", "148 mm"], ["170 mm", "170 mm"], "70 mm", "0,95 kg", "KITSQ1", "FL101", "artsound-fl101-coppia-diffusori-da-incasso-quadrati-ultra-piatti-2-vie", {"flat": True}),
 (40687, "FL301", "P", "F", "rett", "2 vie", ["woofer 5,25″ in polipropilene e carbonio", "tweeter 1″ in policarbonato"], "75 Hz – 20 kHz", "87 dB", "8 Ω", "20 – 120 W (consigliata)", ["245 mm", "160 mm"], ["280 mm", "190 mm"], "70 mm", "2,125 kg", "KITRE2", "FL301", "artsound-fl301-coppia-di-diffusori-da-incasso-ultrapiatti", {"flat": True}),
 (40834, "FL620", "S", "F", "tondo", "2 vie coassiale", ["woofer 6,5″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "63 Hz – 20 kHz", "92 dB", "8 Ω", "40 W RMS, 80 W massimi", "Ø 205 mm (da confermare)", "Ø 245 mm", "75 mm", "1,75 kg", "MOKIT RO238", "FL620", "artsound-fl620-coppia-diffusori-da-incasso-ultra-sottili", {"flat": True, "diff": "La scheda Extrasound indica 70 Hz – 20 kHz e 20 – 120 W; la scheda ArtSound indica 63 Hz – 20 kHz e 40 W RMS (80 W massimi). La scheda ArtSound non etichetta chiaramente il foro: 205 mm è il valore Extrasound."}),
 (39813, "FL550", "2", "F", "tondo", "2 vie coassiale stereo", ["woofer 5,25″ in polipropilene e carbonio", "2 tweeter 0,5″ in policarbonato"], "95 Hz – 20 kHz", "87 dB", "8 Ω", "10 – 100 W (consigliata)", "Ø 180 mm", "Ø 200 mm", "80 mm", "1,1 kg", "KITRO2", "FL550", "artsound-fl550-diffusore-da-incasso-stereo-in-un-unico-punto-con-griglia-ultrapiatta", {"flat": True, "ds": True}),
 (39776, "FL30", "S", "F", "tondo", "gamma intera", ["altoparlante 3″ in polipropilene e carbonio"], "150 Hz – 20 kHz", "90 dB", "8 Ω", "10 – 50 W (consigliata)", "Ø 85 mm", "Ø 100 mm", "52 mm", "0,35 kg", "", "FL30", "artsound-fl30-coppia-diffusori-da-incasso-extra-small-con-griglia-ultrapiatta", {"flat": True}),
 (42875, "DC84", "S", "W", "rett", "2 vie", ["woofer 6,5″ in polipropilene e carbonio", "tweeter 0,5″ a cupola"], "63 Hz – 20 kHz", "86 dB", "8 Ω", "100 W massimi", ["146 mm", "146 mm"], ["146 mm", "146 mm"], "75 mm", "0,75 kg", "KIT SQ180/180", "DC84", "artsound-dc84-diffusori-da-incasso-waterproof-per-ambienti-umidi-coppia", {"stagno": True, "diff": "La scheda ArtSound riporta come ingombro le stesse misure del foro (146 × 146 mm): da verificare sul prodotto."}),
 (42885, "MDT500-P", "S", "T", "tondo", "gamma intera", ["altoparlante 5″ con cono in carta"], "100 Hz – 18 kHz", "89 dB (1 W / 1 m)", "100 V o 8 Ω (selettore)", "prese 100 V: 3,75 – 7,5 – 15 – 30 W", "Ø 210 mm (dato Extrasound)", "Ø 210 mm", "155 mm", "2,1 kg", "", "MDT500", "artsound-mdt500-p-diffusore-da-incasso-100v-per-sistemi-audio-multiroom", {"v100": "3,75 / 7,5 / 15 / 30 W", "otto": True, "diff": "La scheda ArtSound non indica il foro; Extrasound indica 210 mm, uguale al diametro esterno dichiarato da ArtSound: da verificare con la dima."}),
 (42895, "MDT600-P", "S", "T", "tondo", "gamma intera", ["altoparlante 6″ con cono in carta"], "80 Hz – 18 kHz", "91 dB (1 W / 1 m)", "solo linea 100 V", "prese 100 V: 3 – 6 – 9 W", "Ø 170 mm", "Ø 200 mm", "80 mm", "0,9 kg", "", "MDT600", "artsound-mdt600-p-diffusore-da-incasso-soffitto-100v-per-multiroom", {"v100": "3 / 6 / 9 W", "molle": True}),
 (41297, "FL101BT", "A", "F", "rett", "2 vie coassiale, attivo + passivo", ["woofer 5,25″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "65 Hz – 20 kHz", "88 dB", "8 Ω", "amplificatore integrato 2 × 45 W in classe D", ["148 mm", "148 mm"], ["170 mm", "170 mm"], "70 mm", "0,95 kg", "", "FL101BT", "artsound-fl101bt-coppia-di-diffusori-da-incasso-bluetooth-1-attivo-1-passivo", {"bt": "coppia"}),
 (40517, "FL502BT Single", "A", "F", "tondo", "2 vie coassiale, attivo", ["woofer 5,25″ in polipropilene e carbonio", "tweeter 0,5″ in policarbonato"], "65 Hz – 20 kHz", "88 dB", "8 Ω", "amplificatore integrato 45 W in classe D", "Ø 180 mm", "Ø 200 mm", "70 mm", "1 kg", "", "FL502BT", "artsound-fl502bt-single-diffusore-da-incasso-bluetooth-attivo-ultra-piatto", {"bt": "single"}),
]

IMG = {
 29843: "Artsound-RO2060.jpg » ArtSound RO2060 senza griglia, con woofer e tweeter in vista ;; artsound-diffusore-incasso-RO2060.jpg » Griglia bianca dell'ArtSound RO2060 ;; Artsound-RO2060-posteriore.jpg » Retro dell'ArtSound RO2060 con ganci di fissaggio e morsetti",
 29834: "artsound-diffusore-incasso-RO2040-3.jpg » ArtSound RO2040 senza griglia, con woofer e tweeter in vista ;; artsound-diffusore-incasso-RO2040-2.jpg » Retro dell'ArtSound RO2040 con ganci di fissaggio e morsetti ;; artsound-diffusore-incasso-RO2040-1.jpg » Griglia bianca dell'ArtSound RO2040",
 29861: "diffusori-incasso-artsound-re2060-2.jpg » ArtSound RE2060 senza griglia, con woofer e tweeter in vista ;; diffusori-incasso-artsound-re2060-1.jpg » Retro dell'ArtSound RE2060 con ganci di fissaggio e morsetti ;; Artsound-RE2060-griglia.jpg » Griglia bianca dell'ArtSound RE2060",
 29870: "diffusori-incasso-artsound-re2080-1.jpg » ArtSound RE2080 senza griglia, con woofer e tweeter in vista ;; diffusori-incasso-artsound-re2080-3.jpg » Retro dell'ArtSound RE2080 con ganci di fissaggio e morsetti ;; diffusori-incasso-artsound-re2080-2.jpg » Griglia bianca dell'ArtSound RE2080",
 2909: "Artsound-RE2040.jpg » ArtSound RE2040 senza griglia, con woofer e tweeter in vista ;; Artsound-RE2040-griglia.jpg » Griglia bianca dell'ArtSound RE2040 ;; Artsound-RE2040-posteriore.jpg » Retro dell'ArtSound RE2040 con ganci di fissaggio e morsetti",
 31048: "Artsound-SQ2060.jpg » ArtSound SQ2060 senza griglia, con woofer e tweeter in vista ;; artsound-diffusore-incasso.intiimi-sq2060-2.jpg » Retro dell'ArtSound SQ2060 con ganci di fissaggio e morsetti ;; artsound-diffusore-incasso.intiimi-sq2060-1.jpg » Griglia bianca dell'ArtSound SQ2060",
 29882: "artsound-initiimi-sq2040-3.jpg » ArtSound SQ2040 senza griglia, con woofer e tweeter in vista ;; artsound-initiimi-sq2040-retro.jpg » Retro dell'ArtSound SQ2040 con ganci di fissaggio e morsetti ;; artsound-initiimi-sq2040-2.jpg » Griglia bianca dell'ArtSound SQ2040",
 32059: "artsound-hpro650.jpg » ArtSound HPRO650 senza griglia, con woofer e tweeter in vista ;; artsound-hpro650-griglia.jpg » Griglia bianca dell'ArtSound HPRO650 ;; artsound-hpro650-retro.jpg » Retro dell'ArtSound HPRO650 con ganci di fissaggio e morsetti",
 32050: "artsound-hpre650.jpg » ArtSound HPRE650 senza griglia, con woofer e tweeter in vista ;; artsound-hpre650-lato-1.jpg » Vista laterale dell'ArtSound HPRE650",
 31975: "Artsound-HPRO525-1.jpg » ArtSound HPRO525 senza griglia, con woofer e tweeter in vista ;; artsound-HPRO525-griglia.jpg » Griglia bianca dell'ArtSound HPRO525 ;; artsound-HPRO525-lato.jpg » Vista laterale dell'ArtSound HPRO525",
 31963: "Artsound-HPSQ525-1.jpg » ArtSound HPSQ525 senza griglia, con woofer e tweeter in vista ;; artsound-hpsq525-retro.jpg » Retro dell'ArtSound HPSQ525 con ganci di fissaggio e morsetti ;; Artsound-HPSQ525-griglia.jpg » Griglia bianca dell'ArtSound HPSQ525",
 31957: "artsound-HPRO550.jpg » ArtSound HPRO550 senza griglia, con woofer e tweeter in vista ;; artsound-HPRO550-griglia.jpg » Griglia bianca dell'ArtSound HPRO550 ;; artsound-HPRO550-lato.jpg » Vista laterale dell'ArtSound HPRO550",
 32142: "artsound-mdc64.jpg » Griglia bianca dell'ArtSound MDC64 ;; artsound-mdc64-lato.jpg » Vista laterale dell'ArtSound MDC64 ;; artsound-mdc64-retro.jpg » Retro dell'ArtSound MDC64 con ganci di fissaggio e morsetti",
 32085: "ARTSOUND-MDC6.jpg » ArtSound MDC6 senza griglia con la griglia bianca accanto ;; ARTSOUND-MDC6-RETR.jpg » Retro dell'ArtSound MDC6 con ganci di fissaggio e morsetti",
 32077: "artsound-mdc620-frontale.jpg » ArtSound MDC620 senza griglia, con woofer e tweeter in vista ;; artsound-mdc620.jpg » ArtSound MDC620 senza griglia con la griglia bianca accanto ;; artsound-mdc620-griglia.jpg » Griglia bianca dell'ArtSound MDC620",
 30404: "artsound-mdc501-diffusore-incasso-1.jpg » ArtSound MDC501 senza griglia, con woofer e tweeter in vista ;; artsound-mdc501-diffusore-incasso.jpg » ArtSound MDC501 senza griglia con la griglia bianca accanto ;; artsound-mdc501-diffusore-incasso-grid.jpg » Griglia bianca dell'ArtSound MDC501",
 30341: "artsound-mdc401-diffusore-incasso.jpg » ArtSound MDC401 senza griglia, con woofer e tweeter in vista ;; artsound-mdc401-diffusore-incasso-2.jpg » ArtSound MDC401 senza griglia con la griglia bianca accanto ;; artsound-mdc401-diffusore-incasso-1.jpg » Retro dell'ArtSound MDC401 con ganci di fissaggio e morsetti",
 32068: "artsound-md30.jpg » Griglia bianca dell'ArtSound MD30 ;; artsound-md30-lato.jpg » Vista laterale dell'ArtSound MD30 ;; artsound-md30-retro.jpg » Retro dell'ArtSound MD30 con ganci di fissaggio e morsetti",
 40043: "artsound-fl501-con-griglia-1000.jpg » ArtSound FL501 senza griglia con la griglia bianca accanto ;; artsound-fl501-laterale-1000.jpg » Vista laterale dell'ArtSound FL501 con ganci di fissaggio e griglia ;; artsound-fl501-retro-1000.jpg » Retro dell'ArtSound FL501 con i ganci di fissaggio",
 39961: "Artsound-FL401.jpg » ArtSound FL401 senza griglia, con woofer e tweeter in vista ;; Artsound-FL401-posteriore.jpg » Retro dell'ArtSound FL401 con ganci di fissaggio e morsetti ;; Artsound-FL401-laterale-griglia.jpg » Vista laterale dell'ArtSound FL401",
 40409: "Artsound-FL101.jpg » ArtSound FL101 senza griglia, con woofer e tweeter in vista ;; Artsound-FL101-altoparlante-griglia.jpg » ArtSound FL101 senza griglia con la griglia bianca accanto ;; Artsound-FL101-griglia.jpg » Griglia bianca dell'ArtSound FL101",
 40687: "Artsound-FL301.jpg » ArtSound FL301 senza griglia, con woofer e tweeter in vista ;; Artsound-FL301-con-griglia.jpg » ArtSound FL301 senza griglia con la griglia bianca accanto ;; Artsound-FL301-griglia.jpg » Griglia bianca dell'ArtSound FL301",
 40834: "Artsound-FL620.jpg » ArtSound FL620 senza griglia, con woofer e tweeter in vista ;; Artsound-FL620-con-griglia.jpg » Vista laterale dell'ArtSound FL620 ;; Artsound-FL620-griglia.jpg » Griglia bianca dell'ArtSound FL620",
 39813: "Artsound-FL550.jpg » ArtSound FL550 senza griglia con la griglia bianca accanto ;; Artsound-FL550-rear.jpg » Retro dell'ArtSound FL550 con ganci di fissaggio e morsetti",
 39776: "Artsound-FL30-griglie.jpg » Griglia bianca dell'ArtSound FL30 ;; Artsound-FL30.jpg » Retro dell'ArtSound FL30 con ganci di fissaggio e morsetti ;; Artsound-FL30-laterale.jpg » Vista laterale dell'ArtSound FL30",
 42875: "Artsound-DC84.jpg » Griglia bianca dell'ArtSound DC84 ;; Artsound-DC84-altoparlante.jpg » Vista laterale dell'ArtSound DC84",
 42885: "Artsound-MDT500-P.jpg » Diffusore da incasso a soffitto ArtSound MDT500-P con griglia ;; Artsound-MDT500-P-laterale.jpg » ArtSound MDT500-P visto di lato ;; Artsound-MDT500-P-posteriore.jpg » Retro dell'ArtSound MDT500-P",
 42895: "Artsound-MDT600-P.jpg » Diffusore da incasso a soffitto ArtSound MDT600-P con griglia ;; Artsound-MDT600-P-posteriore.jpg » Retro dell'ArtSound MDT600-P",
 41297: "Artsound-FL101BT.jpg » ArtSound FL101BT senza griglia con woofer e tweeter coassiale ;; Artsound-FL101BT-attivo.jpg » Retro del diffusore attivo ArtSound FL101BT con il modulo amplificatore ;; Artsound-FL101BT-con-griglia.jpg » ArtSound FL101BT visto di lato con la griglia accanto",
 40517: "Artsound-FL502BT.jpg » ArtSound FL502BT senza griglia con woofer e tweeter coassiale ;; Artsound-FL502BT-posteriore.jpg » Retro dell'ArtSound FL502BT con il modulo amplificatore Bluetooth ;; Artsound-FL502BT-set.jpg » Retro di due ArtSound FL502BT della versione SET",
}

TIPO = {"P": "Diffusore da incasso a parete", "S": "Diffusore da incasso a soffitto", "2": "Diffusore stereo da incasso a soffitto",
        "A": "Diffusore da incasso attivo con Bluetooth"}


def caption(alt):
    a = alt.lower()
    for k, v in (("accanto", "Con griglia"), ("griglia bianca", "Griglia"), ("retro", "Retro"), ("lato", "Lato"), ("set", "Versione SET"), ("senza griglia", "Senza griglia")):
        if k in a:
            return v
    return "Vista"


def scheda(t):
    (id, mod, cat, ser, forma, vie, drv, risp, sens, imp, amp, foro, est, prof, peso, kit, fk, url, ex) = t
    tipo = TIPO[cat]
    if cat == "S" and forma == "rett":
        tipo = "Diffusore da incasso a parete o soffitto"
    serie = "serie " + SERIE[ser]
    f0 = SRC[fk]
    fstr = foro if isinstance(foro, str) else f"{foro[0]} × {foro[1]}"
    I = imgs(IMG[id])

    car = [f"{tipo}, {serie}.", f"Sistema: {vie}."] + [d[0].upper() + d[1:] + "." for d in drv]
    if ex.get("alti"):
        car.append("Tweeter orientabile in una conchiglia acustica e regolazione manuale degli alti.")
    if ex.get("flat") or ser == "I":
        car.append("Griglia magnetica quasi senza cornice (1 mm), verniciabile.")
    if ex.get("umido"):
        car.append("Resistente all'acqua e agli spruzzi: griglia in alluminio a fissaggio magnetico, adatto a bagni, cucine e portici.")
    if ex.get("stagno"):
        car.append("Retro chiuso ermeticamente e materiali resistenti all'acqua: piscine, saune, bagni turchi, giardini. Nessun grado IP dichiarato.")
    if ex.get("ds"):
        car.append("Stereo in un solo diffusore: due tweeter e doppi morsetti, sinistro e destro.")
    if ex.get("v100"):
        car.append("Cassa posteriore chiusa inclusa." if ex.get("otto") else "Fissaggio rapido a molle.")
    if kit:
        car.append(f"Accessori ArtSound: {kit}.")

    acu = [f"Risposta: {risp}.", f"Sensibilità: {sens}.", f"Impedenza: {imp}.",
           (f"Amplificazione: {amp}." if not ex.get("bt") else f"Amplificazione: {amp}."), "Housing in ABS."]
    if ex.get("bt"):
        acu.append("Bluetooth 5.1 con aptX, aptX HD e aptX Adaptive; ingresso AUX." if ex["bt"] == "single" else "Ingressi: Bluetooth e AUX.")
    dim = [f"Foro: {fstr}.", f"Ingombro: {est if isinstance(est, str) else est[0] + ' × ' + est[1]} × {prof} di profondità.", f"Peso: {peso} a pezzo."]
    if id in (29843, 29834, 29861, 29870, 2909, 31048, 29882):
        dim.append("Spessore del diffusore a vista: poco meno di 5 mm.")

    fpulito = lambda s: s.replace("Ø ", "").replace(" (da confermare)", "").replace(" (dato Extrasound)", "")
    if forma == "tondo":
        mis = {"forma": "tondo", "foro": fpulito(foro), "est": est.replace("Ø ", ""), "prof": prof}
    else:
        mis = {"forma": "rett", "foro": foro, "est": est, "prof": prof}
    mis["nota"] = "Foro tratteggiato in rosso. Profondità = ingombro dichiarato da ArtSound; disegno non in scala."

    # collegamenti
    if ex.get("v100"):
        v = [f"Linea a tensione costante 100 V: scegli la presa ({ex['v100']}) in base al livello voluto nella stanza.",
             "La somma delle prese di tutti i diffusori sulla linea non deve superare la potenza dell'amplificatore.",
             "Esempi ArtSound: MX60MKII (60 W) o MX-120M (120 W)."]
        if ex.get("otto"):
            v.insert(1, "Con il selettore su 8 Ω si usa come diffusore normale su un amplificatore a bassa impedenza.")
        col = [{"titolo": "Linea 100 V", "link": "amplificatori.html", "icona": "linea100v", "voci": v}]
    elif ex.get("bt"):
        if ex["bt"] == "coppia":
            v = ["Il diffusore attivo contiene l'amplificatore 2 × 45 W e va alimentato; il passivo si collega con un cavo al diffusore attivo.",
                 "Sorgenti: Bluetooth oppure ingresso AUX. Il modulo prevede anche un ingresso a priorità (PRIORITY).",
                 "Schema di cablaggio e alimentazione da confermare sul manuale ArtSound."]
        else:
            v = ["Diffusore singolo con amplificatore da 45 W in classe D: va alimentato.",
                 "Sorgenti: Bluetooth 5.1 oppure ingresso AUX; il modulo prevede un ingresso a priorità (PRIORITY).",
                 "Versione SET (attivo + passivo) disponibile come opzione. Alimentazione e cablaggio da confermare sul manuale ArtSound."]
        col = [{"titolo": "Alimentazione e sorgenti", "icona": "bluetooth", "voci": v}]
    else:
        v = [f"{imp}: un diffusore per canale su qualsiasi amplificatore da installazione."]
        if imp.startswith("4"):
            v.append("Impedenza fino a 4 Ω: scegli un amplificatore stabile a 4 Ω e non metterne due in parallelo sullo stesso canale.")
        if ex.get("ds"):
            v = ["Due ingressi: canale sinistro e destro dello stesso amplificatore, 8 Ω per canale.",
                 "Per stanze piccole, bagni o corridoi dove c'è posto per un solo diffusore."]
        v.append(f"Amplificazione: {amp}.")
        v.append("Ad esempio con ArtSound AMP850 (4 zone) o Smart Zone 4 AMP.")
        col = [{"titolo": "Amplificazione", "link": "amplificatori.html", "icona": "sorgente", "voci": v}]

    dove = ["Verifica travi, tubi e impianti prima di tagliare."]
    if ex.get("ds"):
        dove.insert(0, "Al centro della stanza: un solo punto di emissione per i due canali.")
    elif cat in ("S", "A") and forma == "tondo":
        dove.insert(0, "Lontano da pareti e angoli quando possibile.")
    if ex.get("alti"):
        dove.append("Orienta il tweeter verso la zona d'ascolto e regola gli alti in base all'ambiente.")
    if kit and not ex.get("v100"):
        dove.append(f"Nei soffitti aperti o per isolare acusticamente il diffusore usa il kit posteriore ArtSound ({kit.split(' · ')[0]}).")
    sist = [{"titolo": "Dove montarlo", "voci": dove}]
    if cat in ("S", "2") and forma == "tondo" and not ex.get("v100"):
        sist[0]["posa"] = {"tipo": "soffitto", "distanza": "lontano dalle pareti", "nota": "zona d'ascolto"}
    if ex.get("ds"):
        sist.append({"titolo": "Schema", "voci": ["Un solo diffusore riceve i due canali dello stesso amplificatore."],
                     "zone": [{"label": f"{mod} · L + R", "tipo": "2"}], "apparecchio": "Amplificatore"})

    passi = [
        ["Traccia", f"Traccia il foro con la dima o con il diffusore: {fstr}."],
        ["Taglia", "Fori rotondi: un foro di partenza all'interno del tracciato; fori quadrati o rettangolari: quattro fori negli angoli. Poi taglia con il seghetto alternativo."],
        ["Collega prima di montare", "Collega il cavo rispettando la polarità marcata prima di inserire il diffusore: correggerla dopo significa smontarlo."],
        ["Fissa", "Inserisci il diffusore e stringi le viti: i ganci si aprono e serrano il pannello." if not ex.get("molle") else "Inserisci il diffusore: le molle lo trattengono in sede."],
        ["Chiudi", "Monta la griglia magnetica. Cornice e griglia si possono verniciare." if (ex.get("flat") or ser in ("I", "H")) else "Monta la griglia."],
    ]
    if ex.get("viti"):
        passi[3] = ["Fissa", "Applica l'anello adesivo antivibrazione (o l'anello copriviti, secondo la versione), inserisci il diffusore e stringi le viti."]
    if ex.get("v100"):
        passi.insert(3, ["Presa", "Prima di montare scegli la presa di potenza sul trasformatore" + (" o la posizione 8 Ω sul selettore." if ex.get("otto") else ".")])
    sist.append({"titolo": "Montaggio", "passi": passi})

    righe0 = f"{vie.split(',')[0]} · {drv[0].split(' in ')[0].split(' con ')[0].split(',')[0]}"
    chiave = [f"{vie.split(',')[0]} · {imp.split(' (')[0]}" if not ex.get("v100") else f"Linea 100 V · {ex['v100']}",
              f"Foro {fstr.replace(' (da confermare)', '').replace(' (dato Extrasound)', '')}", f"Profondità {prof}"]
    nota = f"Dati dalla {f0['label']}, confrontati con la scheda Extrasound. ArtSound non pubblica un manuale di installazione per questa serie: la procedura segue il manuale ArtSound MDC6."
    if ex.get("diff"):
        nota += " " + ex["diff"] + " Fa fede il dato ArtSound."
    intro = [f"L'<strong>ArtSound {mod}</strong> è un {tipo[0].lower() + tipo[1:]} della {serie}: {', '.join(drv)}. Impedenza {imp}.",
             f"Foro <strong>{fstr}</strong>, ingombro in profondità <strong>{prof}</strong>."]
    d = {"id": id, "tipo": "diffusore", "cat": cat, "brand": "ArtSound", "model": mod, "crop": False,
         "meta": f"ArtSound {mod}: {righe0}, {tipo[0].lower() + tipo[1:]}. Foro, profondità e collegamenti per l'installatore.",
         "img": I[0], "chiave": chiave, "righe": [righe0, tipo, serie[0].upper() + serie[1:]], "intro": intro,
         "colonne": [{"titolo": "Caratteristiche", "voci": car}, {"titolo": "Acustica", "voci": acu}, {"titolo": "Dimensioni", "voci": dim}],
         "viste": [vista(i, caption(i["alt"])) for i in I[1:4]], "misure": mis, "collega": col, "sistemi": sist,
         "nota": nota, "extrasound": X + url, "fonti": [f0, SRC["MDC6"]] if fk != "MDC6" else [f0]}
    return salva(d)


# ---------------- amplificatori ----------------
AFONTI = {
 "SZ4": F("manuale ArtSound Smart Zone 4", "https://easylounge.com/pdf/Produits/2056cc68-408f-4c41-a3b7-35fd26c2da3c/smart-zone-4_6451099d37069.pdf"),
 "AMP850": F("scheda ArtSound AMP850 (EasyLounge)", "https://www.easylounge.com/amplificateur-hifi/artsound-amp850-75435"),
 "MX120": F("manuale ArtSound MX-120M (FR)", "https://res.cloudinary.com/sonepar-fr/raw/upload/s--W1UyJVrY--/v1/documents/1110/00021145_mx120M_notice.pdf"),
 "MX60": F("manuale ArtSound MX-60 / MX-60M (FR)", "https://res.cloudinary.com/sonepar-fr/raw/upload/s--xJ3UVoN7--/v1/documents/1110/000014713_mx60M_notice.pdf"),
 "PRL1502": F("scheda tecnica ArtSound PRL-1502 (FR)", "https://res.cloudinary.com/sonepar-fr/raw/upload/s--zg6MyV0k--/v1/documents/1110/00026567_PRL-1502-fr.pdf"),
 "PRL1504": F("scheda ArtSound PRL-1504 (Concerto Audio)", "https://www.concertoaudio.com/gb/power-amps/7967-artsound-prl-1504.html"),
 "HYDE": F("scheda tecnica ArtSound Smart Hyde (FR)", "https://easylounge.com/pdf/Produits/08d9a72e-5bee-40cb-a07a-a5577ba1d75d/SmartHyde_fr.pdf"),
 "ART11": F("scheda tecnica ArtSound ART1.1", "https://homemovie.hu/wp-content/uploads/2018/10/ART1.1_uk.pdf"),
}
AIMG = {
 31908: "artsound-smart-zone-4amp.jpg » ArtSound Smart Zone 4 AMP visto di fronte ;; artsound-smart-zone-4amp-retro.jpg » Pannello posteriore dell'ArtSound Smart Zone 4 AMP con morsetti e ingressi delle zone",
 31903: "artsound-amp850.jpg » ArtSound AMP850 nero visto di tre quarti ;; artsound-amp850-frontale.jpg » ArtSound AMP850 visto di fronte ;; artsound-amp850-retro.jpg » Pannello posteriore dell'ArtSound AMP850 con morsetti e ingressi",
 31889: "artsound-mx-120m.jpg » ArtSound MX-120M nero visto di tre quarti ;; artsound-mx-120m-frontale.jpg » Frontale dell'ArtSound MX-120M con manopole e lettore USB/SD ;; artsound-mx-120m-retro.jpg » Pannello posteriore dell'ArtSound MX-120M con morsetti euroblock e uscite 100 V",
 31885: "Artsound-MX60MKII-frontale.jpg » ArtSound MX60MKII visto di fronte con manopole di volume ;; Artsound-MX60MKII-laterale.jpg » ArtSound MX60MKII visto di lato ;; Artsound-MX60MKII-telecomando.jpg » Telecomando dell'ArtSound MX60MKII",
 31865: "artsound-prl1504.jpg » ArtSound PRL-1504 nero visto di tre quarti ;; artsound-prl1504-frontale.jpg » Frontale dell'ArtSound PRL-1504 con spie dei quattro canali ;; artsound-prl1504-retrio.jpg » Pannello posteriore dell'ArtSound PRL-1504 con quattro ingressi combo",
 31860: "artsound-prl1502.jpg » ArtSound PRL-1502 nero visto di tre quarti ;; artsound-prl1502-frontale.jpg » Frontale dell'ArtSound PRL-1502 con spie di segnale e clip ;; artsound-prl1502-retro.jpg » Pannello posteriore dell'ArtSound PRL-1502 con ingressi combo e uscite",
 31853: "artsound-smrt-hyde.jpg » ArtSound Smart Hyde nero visto di tre quarti ;; artsound-smrt-hyde-uop.jpg » ArtSound Smart Hyde visto dall'alto ;; artsound-smrt-hyde-retro.jpg » Pannello posteriore dell'ArtSound Smart Hyde con ingressi, uscite e morsetti",
 31829: "Artsound-1.1.jpg » ArtSound ART1.1 amplificatore Bluetooth compatto ;; Artsound-1.1-retro.jpg » Retro dell'ArtSound ART1.1 con i morsetti per i diffusori ;; Artsound-1.1-sopra.jpg » ArtSound ART1.1 visto dall'alto",
}
DIFF_LINK = {"titolo": "Diffusori da incasso", "link": "diffusori.html", "icona": "soffitto"}


def amp(id, mod, url, fonti, righe, chiave, intro, car, ing, usc, collega, sistemi, nota, retro_cap=None):
    I = imgs(AIMG[id])
    r = next((i for i in I if "posteriore" in i["alt"].lower() or "retro" in i["alt"].lower()), None)
    d = {"id": id, "tipo": "amplificatore", "cat": "M", "brand": "ArtSound", "model": mod, "crop": True,
         "meta": f"ArtSound {mod}: {righe[0].lower()}, {righe[1].lower()}. Potenze, ingressi, uscite, collegamenti e messa in servizio.",
         "img": I[0], "chiave": chiave, "righe": righe, "intro": intro,
         "colonne": [{"titolo": "Caratteristiche", "voci": car}, {"titolo": "Ingressi", "voci": ing}, {"titolo": "Uscite", "voci": usc}],
         "lato_titolo": "Cosa si collega", "collega": collega, "sistemi": sistemi, "nota": nota, "extrasound": X + url, "fonti": fonti}
    if r and retro_cap:
        d["retro"] = {"src": r["src"], "alt": r["alt"], "titolo": "Pannello posteriore", "caption": retro_cap}
    return salva(d)


def amplificatori():
    out = []
    out.append(amp(31908, "Smart Zone 4 AMP", "artsound-smart-zone-4-amp-amplificatore-multiroom-streaming-4-zone", [AFONTI["SZ4"]],
        ["4 zone · streaming", "Amplificatore multiroom", "Rack"], ["4 zone stereo", "Streaming · AirPlay · Spotify", "Trigger 12 V per zona"],
        ["L'<strong>ArtSound Smart Zone 4 AMP</strong> è un amplificatore streaming multiroom a 4 zone: ogni zona ha la sua sorgente e i suoi morsetti per una coppia di diffusori.",
         "Si comanda dall'app 4STREAM; RS232 bidirezionale per i sistemi di domotica."],
        ["4 zone indipendenti, comandate dall'app 4STREAM (iOS e Android).",
         "Potenza indicata da Extrasound: 2 × 60 W RMS su 8 Ω, 2 × 105 W su 4 Ω (per zona, da confermare: il manuale ArtSound disponibile non riporta la potenza).",
         "Servizi: Spotify Connect, TIDAL, Qobuz, Deezer, Amazon Music, TuneIn, vTuner, iHeartRadio, AirPlay, UPnP/DLNA, USB.",
         "RS232 bidirezionale con porta passante per la domotica.",
         "Rete: Ethernet RJ45 con uscita passante; serve il Wi-Fi per l'app.",
         "Alimentazione 110 – 240 V; 90 × 430 × 300 mm, 9 kg (dati Extrasound)."],
        ["Per zona: Line In RCA (max 2 V RMS) e USB.", "Ingresso master comune a tutte le zone: Line In RCA, coassiale e ottico (fino a 192 kHz / 24 bit).", "Ethernet RJ45, RS232."],
        ["Per zona: morsetti per una coppia di diffusori, Line Out RCA (max 2 V RMS), uscite ottica e coassiale (44,1 kHz / 16 bit).", "Trigger 12 V (150 mA) master e per zona.", "Ogni zona può uscire in stereo, solo L o solo R."],
        [DIFF_LINK | {"voci": ["Una coppia di diffusori per zona, sui morsetti della zona.", "Per un subwoofer: canale L della Line Out della zona verso il subwoofer o il suo amplificatore."]},
         {"titolo": "Sorgenti", "icona": "sorgente", "voci": ["Una sorgente locale per zona, oppure una sorgente comune sull'ingresso master: tutte le zone la ricevono sincronizzate."]},
         {"titolo": "Domotica e rete", "icona": "domotica", "voci": ["RS232 bidirezionale verso la centrale domotica.", "Trigger 12 V per accendere amplificatori esterni: cavo mini-jack mono, non stereo."]}],
        [{"titolo": "4 zone", "voci": ["Ogni zona con la sua sorgente; le zone si raggruppano dall'app trascinando una sull'altra (la prima è la master).", "I gruppi hanno un piccolo ritardo; l'ingresso master invece resta sincronizzato."],
          "zone": [{"label": "Zona 1 · Soggiorno"}, {"label": "Zona 2 · Cucina"}, {"label": "Zona 3 · Camera"}, {"label": "Zona 4 · Bagno"}]},
         {"titolo": "Messa in servizio", "passi": [["Monta", "Rack con le staffe incluse (due viti per lato), vicino agli apparecchi da collegare."],
           ["Collega", "Diffusori ai morsetti di zona; sorgenti locali o master; eventuali trigger."], ["Rete", "Cavo Ethernet al router; eventuale altro apparecchio sull'uscita di rete."],
           ["App", "Installa 4STREAM sullo smartphone nella stessa rete, scegli la zona e la sorgente."], ["Aggiorna", "Se compare l'icona «new», aggiorna il firmware. Reset: tieni premuto il tasto per 8 secondi."]]}],
        "Dati dal manuale ArtSound Smart Zone 4 (stessa piattaforma 4STREAM), confrontati con la scheda Extrasound. Potenza, dimensioni e peso sono dati Extrasound: da confermare con ArtSound.",
        "Ingressi e uscite per zona, ingressi master, rete, RS232 e trigger."))
    out.append(amp(31903, "AMP850", "artsound-amp850-finale-multicanale-8-x-50-w-per-4-zone-stereo", [AFONTI["AMP850"]],
        ["8 canali · 4 zone", "Finale multizona", "Classe D"], ["8 canali · 4 zone stereo", "8 × 50 W / 4 Ω", "Bridge 150 W / 8 Ω"],
        ["L'<strong>ArtSound AMP850</strong> è un finale multizona in classe D a 8 canali per 4 zone stereo, con guadagno regolabile e trigger per zona.",
         "Si abbina a uno streamer multizona come lo Smart Zone 4."],
        ["8 canali in classe D, 4 zone stereo.", "Guadagno regolabile per canale.", "THD inferiore all'1%.", "Massimo 8 diffusori.", "88 × 430 × 335 mm, 9,5 kg."],
        ["8 ingressi RCA sbilanciati, 2 per zona.", "Trigger per ogni zona."],
        ["Potenza: 50 W per canale su 4 Ω.", "Bridge: 150 W per canale su 8 Ω.", "4 uscite di linea RCA."],
        [DIFF_LINK | {"voci": ["Una coppia di diffusori per zona, 4 – 8 Ω.", "In bridge un solo diffusore da 8 Ω per zona."]},
         {"titolo": "Sorgenti", "icona": "sorgente", "voci": ["Uno streamer multizona (es. ArtSound Smart Zone 4) sulle quattro coppie di ingressi."]}],
        [{"titolo": "4 zone stereo", "voci": ["Una sorgente per zona, accensione da trigger."], "zone": [{"label": "Zona 1 · 2 × 50 W"}, {"label": "Zona 2 · 2 × 50 W"}, {"label": "Zona 3 · 2 × 50 W"}, {"label": "Zona 4 · 2 × 50 W"}]}],
        "Dati dalla scheda prodotto EasyLounge (rivenditore ArtSound), confrontati con la scheda Extrasound: manuale ArtSound non trovato. Uscite per diffusori, morsetti e procedura di bridge da confermare.",
        "Ingressi RCA per zona, trigger e morsetti per i diffusori."))
    out.append(amp(31889, "MX-120M", "artsound-mx-120m-amplificatore-mixer-100v-120w-bluetooth-usb-fm", [AFONTI["MX120"]],
        ["120 W · 100 V", "Amplificatore mixer", "Rack 1U"], ["120 W · linea 100 V o 4 – 16 Ω", "4 mic/linea · EMC", "USB · SD · BT · FM"],
        ["L'<strong>ArtSound MX-120M</strong> è un amplificatore mixer da 120 W per musica e annunci, con uscita su linea 100 V o a bassa impedenza (4 – 16 Ω), in formato rack 1U.",
         "Lettore USB/SD, Bluetooth e tuner FM integrati; ingresso di emergenza con la massima priorità."],
        ["Potenza nominale 120 W; risposta 80 Hz – 16 kHz.", "Toni: bassi e alti ±10 dB (100 Hz / 10 kHz).", "Protezioni: temperatura, sovracorrente, cortocircuito; LED PROT, CLIP, SIG.",
         "Rack 1U, ventilazione forzata da davanti a dietro; 484 × 295 × 44 mm, 4,7 kg.", "230 V, 50 Hz; consumo 180 W."],
        ["MIC1 – MIC4: 5 mV, 600 Ω, bilanciati su morsetti europei (MIC4 condiviso con AUX1); phantom selezionabile.", "AUX1, AUX2: 350 mV, 10 kΩ, RCA.", "EMC (emergenza): 775 mV, 10 kΩ, bilanciato.", "Priorità: EMC > MIC1 > MIC2/3/4, AUX, MP3."],
        ["Diffusori: linea 100 V oppure 4 – 16 Ω, con selettore sul retro.", "Mix out: 1 V, 470 Ω, RCA."],
        [{"titolo": "Diffusori 100 V", "link": "diffusori.html", "icona": "linea100v", "voci": ["Selettore su 100 V; la somma delle prese dei diffusori deve restare sotto i 120 W.", "Esempi ArtSound: MDT600-P, MDT500-P."]},
         {"titolo": "Microfoni e sorgenti", "icona": "microfono", "voci": ["Microfoni sui morsetti MIC; sorgenti sugli AUX o dal lettore integrato."]}],
        [{"titolo": "Messa in servizio", "passi": [["Spegni", "Spegni l'MX-120M e gli apparecchi collegati prima di cablare."], ["Uscita", "Imposta il selettore 100 V / 4 – 16 Ω e collega i diffusori; rimonta il coperchio dei morsetti (alta tensione)."],
          ["Terra", "Collega la terra di protezione a una terra vera, mai a un tubo del gas."], ["Accendi", "Volume al minimo, poi accendi; per riaccendere aspetta circa 5 secondi."], ["Ventilazione", "Lascia almeno 10 cm liberi ai lati."]]}],
        "Dati e procedura dal manuale ArtSound MX-120M, confrontati con la scheda Extrasound.", "Morsetti euroblock per microfoni ed emergenza, RCA, uscite diffusori 100 V / 4 – 16 Ω."))
    out.append(amp(31885, "MX60MKII", "artsound-mx60mkii-amplificatore-mixer-60w-bluetooth-per-sistemi-100v", [AFONTI["MX60"]],
        ["60 W · 100 V", "Amplificatore mixer", "Compatto"], ["60 W · 4 – 8 Ω / 70 / 100 V", "2 mic · 2 AUX", "BT · USB · microSD"],
        ["L'<strong>ArtSound MX60MKII</strong> è un amplificatore mixer da 60 W per musica e annunci in una zona, con uscite 4 – 8 Ω, 70 V e 100 V.",
         "Bluetooth, USB e microSD integrati; telecomando incluso."],
        ["Potenza 60 W RMS (8 Ω e 100 V); risposta 60 Hz – 18 kHz (dati Extrasound).", "Toni alti e bassi.", "Alimentazione 100 – 240 V AC o 24 V DC.", "63 × 215 × 285 mm, 1,8 kg (dati Extrasound)."],
        ["2 ingressi microfono, 600 Ω, 10 mV bilanciati; MIC1 con priorità.", "2 ingressi AUX RCA.", "Sorgenti integrate: Bluetooth, USB, microSD."],
        ["Diffusori: 4 – 8 Ω, 70 V, 100 V.", "Uscita di linea RCA.", "Mai usare insieme l'uscita a bassa impedenza e quella 70 / 100 V (indicazione del manuale MX-60)."],
        [{"titolo": "Diffusori 100 V", "link": "diffusori.html", "icona": "linea100v", "voci": ["La somma delle prese dei diffusori deve restare sotto i 60 W.", "Esempi ArtSound: MDT600-P, MDT500-P."]},
         {"titolo": "Microfoni e sorgenti", "icona": "microfono", "voci": ["Due microfoni, due sorgenti RCA e il lettore integrato."]}],
        [{"titolo": "Messa in servizio", "passi": [["Uscita", "Scegli 4 – 8 Ω oppure 70 / 100 V, mai entrambe; somma delle prese entro i 60 W."], ["Terra", "Collega la terra a una terra vera, mai a un tubo del gas."], ["Ventilazione", "Lascia almeno 10 cm liberi ai lati."]]}],
        "Non è disponibile una scheda ArtSound della versione MKII: i dati di prodotto sono quelli Extrasound, le avvertenze di collegamento vengono dal manuale ArtSound MX-60 / MX-60M (modello precedente, con 3 ingressi microfono e dimensioni diverse). Da confermare con ArtSound."))
    prl_proc = [["Monta", "Rack 19″, 1U."], ["Ingressi", "Segnale di linea sui combo XLR / jack."], ["Uscite", "Diffusori su euroblock o Speakon; rispetta la polarità."], ["Livelli", "Volume al minimo all'accensione, poi regola i livelli per canale."]]
    out.append(amp(31860, "PRL-1502", "artsound-prl-1502-amplificatore-finale-professionale-classe-d-2x150w", [AFONTI["PRL1502"]],
        ["2 canali · Classe D", "Finale di potenza", "Rack 1U"], ["2 × 150 W / 4 Ω", "2 × 75 W / 8 Ω", "Bridge 300 W · rack 1U"],
        ["L'<strong>ArtSound PRL-1502</strong> è un finale di potenza a 2 canali in formato rack 1U: 2 × 150 W su 4 Ω, 300 W a ponte.", "Ingressi combo XLR/jack, uscite euroblock e Speakon."],
        ["2 canali; risposta 10 Hz – 30 kHz.", "Indicatori di livello e di clip/protezione.", "Protezioni: sovratensione, cortocircuito dei diffusori, temperatura.", "Alimentazione 100 – 240 V AC.", "Rack 19″ 1U; 44,5 × 483 × 275 mm, 4,2 kg."],
        ["2 ingressi combo XLR / jack 6,3 mm."], ["2 × 150 W su 4 Ω, 2 × 75 W su 8 Ω.", "Bridge: 300 W.", "2 uscite euroblock a 2 poli e 2 Speakon."],
        [DIFF_LINK | {"voci": ["Una coppia di diffusori 4 – 8 Ω, oppure un diffusore in bridge."]}, {"titolo": "Sorgenti", "icona": "sorgente", "voci": ["Mixer, preamplificatore o streamer con uscita di linea."]}],
        [{"titolo": "Messa in servizio", "passi": prl_proc}], "Dati dalla scheda tecnica ArtSound PRL-1502, confrontati con la scheda Extrasound. Uscite 100 V non previste.", "Ingressi combo XLR/jack, uscite euroblock e Speakon."))
    out.append(amp(31865, "PRL-1504", "artsound-prl-1504-amplificatore-finale-professionale-classe-d-4x150w", [AFONTI["PRL1504"]],
        ["4 canali · Classe D", "Finale di potenza", "Rack 1U"], ["4 × 150 W / 4 Ω", "4 × 75 W / 8 Ω", "Bridge 2 × 300 W · rack 1U"],
        ["L'<strong>ArtSound PRL-1504</strong> è un finale di potenza a 4 canali in formato rack 1U: 4 × 150 W su 4 Ω, 2 × 300 W a ponte.", "Pilota due zone stereo."],
        ["4 canali in classe D; risposta 10 Hz – 30 kHz.", "Attenuatore di volume per canale e LED di segnale.", "Protezioni: sovratensione, temperatura, cortocircuito.", "Rack 19″ 1U; 483 × 250 × 44 mm, 4,2 kg."],
        ["4 ingressi XLR / jack 6,3 mm.", "Uscite di rilancio XLR / jack per collegare altri finali in cascata."], ["4 × 150 W su 4 Ω, 4 × 75 W su 8 Ω.", "Bridge: 2 × 300 W.", "Uscite euroblock e Speakon (dato Extrasound)."],
        [DIFF_LINK | {"voci": ["Due coppie di diffusori 4 – 8 Ω, oppure due diffusori in bridge."]}, {"titolo": "Sorgenti", "icona": "sorgente", "voci": ["Una sorgente multizona con due uscite stereo."]}],
        [{"titolo": "2 zone stereo", "voci": ["Canali 1-2 e 3-4 come due zone indipendenti."], "zone": [{"label": "Zona 1 · 2 × 150 W / 4 Ω"}, {"label": "Zona 2 · 2 × 150 W / 4 Ω"}]}, {"titolo": "Messa in servizio", "passi": prl_proc}],
        "Scheda ArtSound non trovata: dati dalla scheda del rivenditore Concerto Audio, confrontati con la scheda Extrasound. Da confermare con ArtSound.", "Quattro ingressi combo e uscite per i diffusori."))
    out.append(amp(31853, "Smart Hyde", "artsound-smart-hyde-amplificatore-multiroom-streaming-2-x-50-w-wifi", [AFONTI["HYDE"]],
        ["2 × 50 W · streaming", "Amplificatore multiroom", "Compatto"], ["2 × 50 W / 4 Ω", "Wi-Fi · LAN · AirPlay", "Uscita subwoofer"],
        ["L'<strong>ArtSound Smart Hyde</strong> è un amplificatore streaming compatto in classe D da 2 × 50 W su 4 Ω per una stanza; più unità sulla stessa rete formano un impianto multiroom.", "Si comanda dall'app 4STREAM."],
        ["Classe D, 2 × 50 W RMS su 4 Ω; THD 0,03% (1 kHz, 1 W).", "Servizi: Spotify Connect, TIDAL, Qobuz, Deezer, TuneIn, vTuner, radio Internet, AirPlay, UPnP/DLNA.", "Bluetooth 5.0, Wi-Fi 802.11 b/g/n, LAN 10/100.", "Alimentazione 110 – 240 V; 158 × 146 × 40 mm, 0,54 kg."],
        ["RCA stereo, ottico, micro USB (DAC), USB (memorie), AUX.", "Rete Wi-Fi o LAN."], ["Morsetti per una coppia di diffusori.", "RCA stereo e uscita subwoofer."],
        [DIFF_LINK | {"voci": ["Una coppia di diffusori da 4 Ω o più."]}, {"titolo": "Subwoofer", "icona": "subwoofer", "voci": ["Subwoofer attivo sull'uscita SUB OUT."]}, {"titolo": "Rete", "icona": "rete", "voci": ["Wi-Fi o cavo LAN; comando dall'app 4STREAM."]}],
        [{"titolo": "Messa in servizio", "passi": [["Collega", "Diffusori ai morsetti, eventuale subwoofer al SUB OUT."], ["Rete", "Collega alla rete via Wi-Fi o LAN."], ["App", "Configura dall'app 4STREAM; più Smart Hyde nella stessa rete si comandano insieme."]]}],
        "Dati dalla scheda tecnica ArtSound Smart Hyde, confrontati con la scheda Extrasound. Montaggio nascosto non specificato da ArtSound.", "Ingressi, uscite, rete e morsetti per i diffusori."))
    out.append(amp(31829, "ART1.1", "artsound-art1-1-amplificatore-bluetooth-compatto-2-x-15-w-per-una-zona", [AFONTI["ART11"]],
        ["2 × 10 W · Bluetooth", "Amplificatore per una zona", "Compatto"], ["2 × 10 W / 8 Ω", "2 × 15 W / 4 Ω", "Bluetooth"],
        ["L'<strong>ArtSound ART1.1</strong> è un amplificatore Bluetooth compatto in classe D per una zona e una coppia di diffusori da incasso: 2 × 10 W su 8 Ω, 2 × 15 W su 4 Ω.", "Si nasconde vicino ai diffusori; nessun Wi-Fi o account."],
        ["Classe D: 2 × 10 W RMS su 8 Ω, 2 × 15 W RMS su 4 Ω.", "Sorgente: Bluetooth.", "Alimentazione 110 – 230 V.", "159,5 × 54 × 35,5 mm, 0,21 kg."],
        ["Bluetooth (unica sorgente)."], ["Morsetti per una coppia di diffusori."],
        [DIFF_LINK | {"voci": ["Una coppia di diffusori da incasso 4 – 8 Ω, per esempio ArtSound FL501 o MDC501."]}, {"titolo": "Sorgente", "icona": "bluetooth", "voci": ["Smartphone o tablet in Bluetooth."]}],
        [{"titolo": "Messa in servizio", "passi": [["Posiziona", "Vicino ai diffusori, in un punto ventilato e raggiungibile dall'alimentazione."], ["Collega", "Diffusori ai morsetti rispettando la polarità."], ["Abbina", "Abbina lo smartphone in Bluetooth (procedura da confermare sul manuale ArtSound)."]]}],
        "Dati dalla scheda tecnica ArtSound ART1.1, confrontati con la scheda Extrasound. Montaggio e abbinamento non descritti da ArtSound.", "Morsetti per i diffusori e alimentazione."))
    return out


if __name__ == "__main__":
    for t in M:
        print(scheda(t))
    for s in amplificatori():
        print(s)
