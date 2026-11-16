"""Schede KEF Ci. Dati dalla KEF Ci Group Specification Sheet (QLM/RLM dalla spec sheet KEF Ci distribuita da Stassen,
Ci3-80QT dalla brochure KEF). Eseguire dalla radice del repository: python3 _strumenti/marchi_kef.py"""
import sys; sys.path.insert(0, '_strumenti')
from schede_util import *

X = 'https://www.extrasound.it/'
GROUP = {"label": "KEF Ci Group Specification Sheet", "url": "https://assets.kef.com/pdf_doc/ci/Ci_Group_Specification_Sheet.pdf"}
STASSEN = {"label": "scheda tecnica KEF Ci (QLM / RLM)", "url": "https://www.stassen.nl/images/kef_ci_specsheet.pdf"}
QT = {"label": "brochure KEF Ci3-80QT", "url": "https://assets.kef.com/uploads/files/en/ci/ci3_80qt_brochure.pdf"}

SERIE = {"Q": "Ci-Q Series", "C": "Ci-C Series", "E": "Ci-E Series", "T": "Ci-T Series", "R": "Ci-R Series · THX",
         "QT": "Ci-Q Series · THX", "M": "Ci Motorised", "S": "Ci Series"}

# id, modello, cat, serie, forma, driver, risposta, sens, imp, amp, spl, xo, foro, est, prof_tot, prof, vol(ideale,min), cert, peso, url, extra
M = [
 (46754, "Ci160.2CL", "P", "C", "rett", ["Uni-Q 160 mm", "tweeter 16 mm"], "52 Hz – 20 kHz", "89 dB", "8 Ω", "10 – 100 W", "104 dB", "2,5 kHz", ["274 mm", "194 mm"], ["303 mm", "223 mm"], "91 mm", "84,5 mm", (35, 20), "IP64", "1,87 kg", "kef-ci160-2cl-diffusore-in-wall-uni-q-160mm", {}),
 (46686, "Ci130QR", "S", "Q", "tondo", ["Uni-Q 130 mm", "tweeter 19 mm"], "45 Hz – 34 kHz", "87 dB", "8 Ω", "10 – 100 W", "103 dB", "3,8 kHz", "Ø 158 mm", "Ø 193,4 mm", "83,3 mm", "77,8 mm", (15, 10), "IP64", "1,35 kg", "kef-ci130qr-diffusore-in-ceiling-uni-q-130mm", {}),
 (46668, "Ci200QL", "P", "Q", "rett", ["Uni-Q 200 mm", "tweeter 25 mm"], "35 Hz – 34 kHz", "90 dB", "8 Ω", "10 – 150 W", "107 dB", "2,5 kHz", ["334 mm", "238 mm"], ["369 mm", "273 mm"], "106 mm", "99,8 mm", (60, 35), "IP64", "2,6 kg", "kef-ci200ql-diffusore-incasso-uni-q-200mm", {}),
 (46655, "Ci3120QLM-THX", "L", "QT", "orizz", ["3 vie", "2 woofer 120 mm", "medio Uni-Q 100 mm", "tweeter 19 mm in alluminio ventilato"], "50 Hz – 20 kHz", "89 dB", "4 Ω", "25 – 250 W", "105 dB", "440 Hz e 2,75 kHz", ["513 mm", "163 mm"], ["536 mm", "186 mm"], "96 mm", "90 mm", (40, 20), "THX Certified Select · IP64", "6,2 kg", "kef-ci3120qlm-thx-diffusore-in-wall-3-vie", {"fonte": STASSEN}),
 (46650, "Ci5120QLM-THX", "L", "QT", "orizz", ["3 vie", "4 woofer 120 mm", "medio Uni-Q 100 mm", "tweeter 19 mm in alluminio ventilato"], "45 Hz – 20 kHz", "89 dB", "4 Ω", "25 – 250 W", "105 dB", "450 Hz e 2,75 kHz", ["795 mm", "163 mm"], ["818 mm", "186 mm"], "96 mm", "90 mm", (70, 35), "THX Certified Ultra · IP64", "9,7 kg", "kef-ci5120qlm-thx-diffusore-in-wall-3-vie", {"fonte": STASSEN}),
 (35522, "Ci5160RLM-THX", "L", "R", "orizz", ["3 vie", "4 woofer 160 mm", "medio Uni-Q 160 mm", "tweeter 25 mm in alluminio ventilato"], "40 Hz – 28 kHz", "89 dB", "4 Ω", "50 – 350 W", "110 dB", "680 Hz e 2,6 kHz", ["1052 mm", "209 mm"], ["1070 mm", "230 mm"], "105,7 mm", "99 mm", (90, 40), "THX Certified Ultra", "18,7 kg", "diffusore-incasso-3-vie-certificato-thx-kef-ci5160rlm", {"fonte": STASSEN, "rif": "RIF5160L"}),
 (35514, "Ci3160RLM-THX", "L", "R", "orizz", ["3 vie", "2 woofer 160 mm", "medio Uni-Q 160 mm", "tweeter 25 mm in alluminio ventilato"], "43 Hz – 28 kHz", "89 dB", "4 Ω", "50 – 350 W", "110 dB", "640 Hz e 2,6 kHz", ["660 mm", "209 mm"], ["680 mm", "230 mm"], "105,7 mm", "99 mm", (60, 30), "THX Certified Ultra", "12 kg", "diffusore-incasso-3-vie-certificato-thx-kef-ci3160rlm", {"fonte": STASSEN, "rif": "RIF3160L"}),
 (35463, "Ci250RRM-THX", "S", "R", "tondo", ["3 vie", "woofer 250 mm", "medio Uni-Q 100 mm", "tweeter 19 mm in alluminio ventilato con MAT"], "28 Hz – 20 kHz", "89 dB", "8 Ω", "50 – 250 W", "111 dB", "540 Hz e 2,6 kHz", "Ø 300 mm", "Ø 346 mm", "175 mm", "168 mm", (150, 80), "THX Certified Ultra · IP64", "6 kg", "kef-ci250rrm-thx-diffusore-in-ceiling-3-vie-thx-ultra", {}),
 (28303, "Ci200ER", "S", "E", "tondo", ["Uni-Q 200 mm", "tweeter 16 mm"], "45 Hz – 20 kHz", "90 dB", "8 Ω", "10 – 125 W", "106 dB", "2,8 kHz", "Ø 240 mm", "Ø 289,6 mm", "103,3 mm", "97,2 mm", (60, 30), "IP64", "1,6 kg", "diffusore-da-incasso-2-vie-woofer-200mm-uni-q-kef-ci200er", {"coppia": True, "hpf": "40 Hz"}),
 (28287, "Ci160ER", "S", "E", "tondo", ["Uni-Q 160 mm", "tweeter 16 mm"], "52 Hz – 20 kHz", "89 dB", "8 Ω", "10 – 100 W", "104 dB", "2,8 kHz", "Ø 196 mm", "Ø 234,6 mm", "88,7 mm", "85,2 mm", (35, 20), "IP64", "1,4 kg", "diffusore-da-incasso-2-vie-woofer-160mm-uni-q-kef-ci160er", {"coppia": True}),
 (28281, "Ci130ER", "S", "E", "tondo", ["Uni-Q 130 mm", "tweeter 16 mm"], "52 Hz – 20 kHz", "87 dB", "8 Ω", "10 – 80 W", "102 dB", "2,8 kHz", "Ø 158 mm", "Ø 193,4 mm", "81 mm", "77,5 mm", (20, 12), "IP64", "1,2 kg", "diffusore-da-incasso-2-vie-woofer-130mm-uni-q-kef-ci130er", {"coppia": True, "diff": "La scheda Extrasound indica 90 dB di sensibilità; KEF dichiara 87 dB."}),
 (28261, "Ci200.2CR", "S", "C", "tondo", ["Uni-Q 200 mm", "tweeter 16 mm"], "45 Hz – 20 kHz", "90 dB", "8 Ω", "10 – 125 W", "106 dB", "2,4 kHz", "Ø 240 mm", "Ø 289,6 mm", "103,3 mm", "97,2 mm", (60, 30), "IP64", "1,6 kg", "diffusore-da-incasso-2-vie-woofer-200mm-uni-q-kef-ci200-2cr", {}),
 (28246, "Ci130.2CR", "S", "C", "tondo", ["Uni-Q 130 mm", "tweeter 16 mm"], "52 Hz – 20 kHz", "87 dB", "8 Ω", "10 – 80 W", "102 dB", "2,8 kHz", "Ø 158 mm", "Ø 193,4 mm", "81 mm", "77,5 mm", (20, 12), "IP64", "1,2 kg", "diffusore-da-incasso-2-vie-woofer-130mm-uni-q-kef-ci130-2cr", {"diff": "La scheda Extrasound indica 77,7 mm di profondità; KEF dichiara 77,5 mm."}),
 (28234, "Ci160.2CR", "S", "C", "tondo", ["Uni-Q 160 mm", "tweeter 16 mm"], "52 Hz – 20 kHz", "89 dB", "8 Ω", "10 – 100 W", "104 dB", "2,8 kHz", "Ø 196 mm", "Ø 234,6 mm", "88,7 mm", "85,2 mm", (35, 20), "IP64", "1,4 kg", "diffusore-da-incasso-2-vie-woofer-160mm-uni-q-kef-ci160-2cr", {"diff": "La scheda Extrasound indica 84,5 mm di profondità; KEF dichiara 85,2 mm."}),
 (28193, "Ci130QSfl", "S", "Q", "rett", ["Uni-Q 130 mm", "tweeter 19 mm"], "45 Hz – 34 kHz (a retro aperto)", "87 dB", "8 Ω", "10 – 100 W", "103 dB", "3,8 kHz", ["158 mm", "158 mm"], ["200,5 mm", "200,5 mm"], "103,6 mm", "101 mm", (15, 10), "", "1,6 kg", "diffusore-da-incasso-2-vie-woofer-130mm-uni-q-kef-ci130qsfl", {"flush": True}),
 (28185, "Ci200QR", "S", "Q", "tondo", ["Uni-Q 200 mm", "tweeter 25 mm"], "35 Hz – 34 kHz", "90 dB", "8 Ω", "10 – 150 W", "107 dB", "2,2 kHz", "Ø 240 mm", "Ø 289,6 mm", "109,8 mm", "103,3 mm", (60, 35), "IP64", "2,4 kg", "diffusore-da-incasso-2-vie-woofer-200mm-uni-q-kef-ci200qr", {}),
 (28178, "Ci200QS", "S", "Q", "rett", ["Uni-Q 200 mm", "tweeter 25 mm"], "35 Hz – 34 kHz", "90 dB", "8 Ω", "10 – 150 W", "107 dB", "2,5 kHz", ["238 mm", "238 mm"], ["273 mm", "273 mm"], "106 mm", "99,8 mm", (60, 35), "IP64", "2,4 kg", "diffusore-da-incasso-2-vie-woofer-200mm-uni-q-kef-ci200qs", {"diff": "La scheda Extrasound indica una risposta di 45 Hz – 20 kHz; KEF dichiara 35 Hz – 34 kHz."}),
 (28145, "Ci130QRfl", "S", "Q", "tondo", ["Uni-Q 130 mm", "tweeter 19 mm"], "45 Hz – 34 kHz (a retro aperto)", "87 dB", "8 Ω", "10 – 100 W", "103 dB", "3,8 kHz", "Ø 158 mm", "Ø 200,6 mm", "104,6 mm", "101 mm", (15, 10), "", "1,45 kg", "diffusore-da-incasso-2-vie-woofer-130mm-uni-q-kef-ci130qrfl", {"flush": True}),
 (28140, "Ci160QR", "S", "Q", "tondo", ["Uni-Q 160 mm", "tweeter 19 mm"], "38 Hz – 34 kHz", "89 dB", "8 Ω", "10 – 125 W", "105 dB", "3,0 kHz", "Ø 196 mm", "Ø 234,6 mm", "98 mm", "91 mm", (25, 15), "IP64", "1,8 kg", "diffusore-da-incasso-2-vie-woofer-160mm-uni-q-kef-ci160qr-copia", {}),
 (28135, "Ci160QL", "P", "Q", "rett", ["Uni-Q 160 mm", "tweeter 19 mm"], "38 Hz – 34 kHz", "89 dB", "8 Ω", "10 – 125 W", "105 dB", "3,0 kHz", ["274 mm", "194 mm"], ["303 mm", "223 mm"], "97,5 mm", "91 mm", (25, 15), "IP64", "2,05 kg", "diffusore-da-incasso-2-vie-woofer-160mm-uni-q-kef-ci160ql", {}),
 (28117, "Ci100.2QR", "S", "S", "tondo", ["Uni-Q 75 mm", "tweeter 16 mm"], "90 Hz – 27 kHz a retro aperto; 130 Hz – 27 kHz con cassa posteriore", "83 dB", "4 Ω", "10 – 50 W", "99 dB", "3,5 kHz", "Ø 118 mm", "Ø 135,6 mm", "107,5 mm", "52 mm (103,1 mm con cassa posteriore)", (5, 0.75), "IP64", "0,5 kg", "diffusore-da-incasso-2-vie-woofer200mm-uni-q-kef-ci100-2qr-2", {}),
 (28062, "Ci160CSds", "2", "C", "rett", ["woofer 160 mm a doppia bobina", "2 tweeter 19 mm"], "50 Hz – 20 kHz", "91 dB", "8 Ω", "10 – 80 W", "106 dB", "3,2 kHz", ["194 mm", "194 mm"], ["223 mm", "223 mm"], "90,5 mm", "84,5 mm", (35, 20), "IP64", "1,8 kg", "diffusore-incasso-2-vie-woofer-160mm-kef-ci160csds", {"ds": True}),
 (28055, "Ci200TRb", "W", "T", "tondo", ["woofer 200 mm a doppia bobina"], "42 – 120 Hz passivo; 32 – 120 Hz con KASA500", "87 dB", "2 × 8 Ω (stereo) · 16 Ω (mono)", "10 – 125 W", "109 dB", "", "Ø 240 mm", "Ø 290 mm", "63 mm", "59 mm", (60, 35), "IP64", "1,7 kg", "subwoofer-incasso-woofer-200mm-doppia-bobina-8-ohm-kef-ci200trb", {"sub": "trb"}),
 (28046, "Ci160TS", "P", "T", "rett", ["medio-basso 115 mm a doppio strato", "tweeter 25 mm"], "110 Hz – 24 kHz", "87 dB", "8 Ω", "10 – 100 W", "101 dB", "1,7 kHz", ["194 mm", "194 mm"], ["222,8 mm", "222,8 mm"], "41 mm", "meno di 36 mm", (3, 1), "IP64", "1,05 kg", "kef-ci160ts-diffusore-in-wall-ultra-sottile", {"diff": "La scheda Extrasound indica una risposta di «110 Hz – 24 Hz»: il limite alto corretto è 24 kHz."}),
 (28039, "Ci200QSb-THX", "W", "QT", "rett", ["woofer 200 mm"], "40 – 100 Hz passivo (crossover inserito); 30 – 140 Hz con KASA500", "85 dB (passivo)", "6 Ω (passivo)", "10 – 150 W (passivo)", "104 dB", "100 Hz (passivo)", ["238 mm", "238 mm"], ["273 mm", "273 mm"], "106 mm", "101,6 mm", (32, 20), "THX Certified Ultra e Select · IP64", "3,3 kg", "subwoofer-bobina-8-ohm-woofer-200mm-uni-q-kef-ci200qsb", {"sub": "qsb", "coppia": True}),
 (28021, "Ci250RRb-THX", "W", "R", "tondo", ["woofer 250 mm"], "da 25 Hz al taglio impostato sul KASA500", "da confermare", "da confermare", "solo KEF KASA500", "109 dB", "", "da confermare", "Ø 346 mm", "", "147 mm", (100, 60), "THX Certified Ultra e Select · IP64", "5,6 kg", "diffusore-incasso-2-vie-driver-25cm-uni-q-kef-ci250rrb", {"sub": "kasa"}),
 (28016, "Ci200RS-THX", "P", "R", "rett", ["Uni-Q 200 mm", "tweeter 38 mm"], "33 Hz – 28 kHz", "90 dB", "4 Ω", "10 – 190 W", "106 dB", "2,2 kHz", ["240 mm", "240 mm"], ["273 mm", "273 mm"], "132,6 mm", "127 mm", (20, 10), "THX Certified Ultra · IP64", "3,6 kg", "diffusore-incasso-2-vie-woofer-200mm-uni-q-kef-ci200rs", {}),
 (28008, "Ci200RR-THX", "S", "R", "tondo", ["Uni-Q 200 mm", "tweeter 38 mm"], "33 Hz – 28 kHz", "90 dB", "4 Ω", "10 – 190 W", "106 dB", "2,2 kHz", "Ø 238 mm", "Ø 290 mm", "132,6 mm", "126,5 mm", (20, 10), "THX Certified Ultra · IP64", "3,6 kg", "diffusore-incasso-2-vie-uni-q-kef-ci200rr-thx", {}),
 (27995, "Ci160RR-THX", "S", "R", "tondo", ["Uni-Q 165 mm", "tweeter 25 mm"], "52 Hz – 24 kHz", "90 dB", "4 Ω", "10 – 190 W", "105 dB", "2,1 kHz", "Ø 196 mm", "Ø 236 mm", "115 mm", "110 mm", (20, 10), "THX Certified Ultra", "2,94 kg", "diffusore-incasso-2-vie-uni-q-kef-ci160rr-thx", {}),
 (2967, "Ci130.2CS", "S", "C", "rett", ["Uni-Q 130 mm", "tweeter 16 mm"], "52 Hz – 20 kHz", "87 dB", "8 Ω", "10 – 80 W", "102 dB", "2,8 kHz", ["158 mm", "158 mm"], ["184 mm", "184 mm"], "83 mm", "77,1 mm", (20, 12), "IP64", "1,35 kg", "diffusore-incasso-quadrato-2-vie-kef-ci130-2cs", {}),
 (2920, "Ci4100QL-THX", "L", "QT", "orizz", ["3 woofer 100 mm", "Uni-Q 100 mm", "tweeter 19 mm"], "55 Hz – 28 kHz", "89 dB", "4 Ω", "10 – 150 W", "104 dB", "2,2 kHz", ["476 mm", "114 mm"], ["490 mm", "128 mm"], "81 mm", "76 mm", (15, 7), "THX Certified Select · IP64", "3 kg", "diffusore-incasso-3-woofer-lcr-ci4100ql-thx-kef", {}),
 (2918, "Ci3160RLb-THX", "W", "R", "orizz", ["3 woofer 160 mm"], "20 – 140 Hz", "92 dB", "4 Ω", "solo KEF KASA500", "112 dB", "", ["660 mm", "209 mm"], ["680 mm", "230 mm"], "96 mm", "88,5 mm", (80, 40), "THX Certified Ultra e Select", "10,9 kg", "subwoofer-da-incasso-3-woofer-ci3160rlb-thx-kef", {"sub": "kasa", "diff": "La scheda Extrasound indica un foro di 661 × 210 mm; KEF dichiara 660 × 209 mm."}),
 (1764, "Ci160TR", "S", "T", "tondo", ["medio-basso 115 mm a doppio strato", "tweeter 25 mm"], "110 Hz – 24 kHz", "87 dB", "8 Ω", "10 – 100 W", "101 dB", "1,7 kHz", "Ø 196 mm", "Ø 234,6 mm", "40 mm", "meno di 36 mm", (3, 1), "IP64", "1 kg", "diffusore-2-vie-incasso-ultra-sottile-ci160tr-kef", {}),
 (1763, "Ci160CRds", "2", "C", "tondo", ["woofer 160 mm a doppia bobina", "2 tweeter 19 mm"], "50 Hz – 20 kHz", "91 dB", "8 Ω", "10 – 80 W", "106 dB", "3,2 kHz", "Ø 196 mm", "Ø 234,6 mm", "93 mm", "86 mm", (35, 20), "IP64", "1,8 kg", "diffusore-stereofonico-2-vie-incasso-ci160crds-kef", {"ds": True}),
 (1760, "Ci160.2CS", "S", "C", "rett", ["Uni-Q 160 mm", "tweeter 16 mm"], "52 Hz – 20 kHz", "89 dB", "8 Ω", "10 – 100 W", "104 dB", "2,8 kHz", ["194 mm", "194 mm"], ["223 mm", "223 mm"], "90,5 mm", "84,5 mm", (35, 20), "IP64", "1,7 kg", "diffusore-2-vie-ati-incasso-quadrato-ci160cs-kef", {}),
 (1759, "Ci130QS", "S", "Q", "rett", ["Uni-Q 130 mm", "tweeter 19 mm"], "45 Hz – 34 kHz", "87 dB", "8 Ω", "10 – 100 W", "103 dB", "3,8 kHz", ["158 mm", "158 mm"], ["184 mm", "184 mm"], "84 mm", "77,9 mm", (15, 10), "IP64", "1,4 kg", "diffusore-2-vie-incasso-tangerine-ci130qs-kef", {}),
 (1758, "Ci160QS", "S", "Q", "rett", ["Uni-Q 160 mm", "tweeter 19 mm"], "38 Hz – 34 kHz", "89 dB", "8 Ω", "10 – 125 W", "105 dB", "3,0 kHz", ["194 mm", "194 mm"], ["223 mm", "223 mm"], "97 mm", "91 mm", (25, 15), "IP64", "1,88 kg", "diffusore-2-vie-incasso-driver-uni-q-ci160qs-kef", {}),
 (1757, "Ci3-80QT", "S", "M", "orizz", ["3 vie", "2 woofer 75 mm", "medio Uni-Q 75 mm", "tweeter 15 mm"], "87 Hz – 30 kHz (con cassa posteriore)", "87 dB", "8 Ω", "10 – 100 W", "102 dB", "300 Hz e 3 kHz", ["354 mm", "112 mm"], ["377 mm", "128 mm"], "125 mm", "120 mm", None, "", "3,3 kg", "diffusore-3-vie-incasso-motorizzato-ci3-80qt-kef", {"fonte": QT, "qt": True, "diff": "La scheda Extrasound indica una risposta fino a 27 kHz; la brochure KEF dichiara 87 Hz – 30 kHz."}),
 (1265, "Ci100QS", "S", "S", "rett", ["Uni-Q 100 mm", "tweeter 19 mm"], "80 Hz – 27 kHz (a retro aperto)", "88 dB", "4 Ω", "10 – 50 W", "103 dB", "3 kHz", ["112 mm", "112 mm"], ["127 mm", "127 mm"], "76 mm", "72 mm (senza cassa posteriore)", (6, 2.5), "IP64", "0,67 kg", "diffusore-2-vie-incasso-uni-q-12x12-ci100qs-kef", {}),
]

IMG = {
 46754: "KEF-Ci160-2CL-frontale.jpg » KEF Ci160.2CL diffusore in-wall 2 vie Uni-Q 6,5 pollici ;; KEF-Ci160-2CL-griglia.jpg » KEF Ci160.2CL con griglia magnetica Ultra-Thin Bezel ;; KEF-Ci160-2CL-laterale-angolato.jpg » KEF Ci160.2CL vista frontale diffusore rettangolare da incasso",
 46686: "KEF-Ci130QR-frontale.jpg » KEF Ci130QR diffusore in-ceiling 2 vie Uni-Q 5,25 pollici ;; KEF-Ci130QR-griglia.jpg » KEF Ci130QR vista frontale con Uni-Q da 130 mm ;; KEF-Ci130QR-posteriore.jpg » KEF Ci130QR vista posteriore diffusore da soffitto",
 46668: "KEF-Ci200QL-frontale.jpg » KEF Ci200QL diffusore da incasso 2 vie Uni-Q 8 pollici ;; kef-ci200ql-con-griglia-1000.jpg » KEF Ci200QL con la griglia montata, vista frontale ;; KEF-Ci200QL-posteriore.jpg » Retro del KEF Ci200QL con i morsetti e le alette di fissaggio",
 46655: "KEF-Ci3120QLM-THX-frontale.jpg » KEF Ci3120QLM-THX diffusore in-wall 3 vie THX Select Uni-Q MAT ;; KEF-Ci3120QLM-THX-laterale.jpg » KEF Ci3120QLM-THX vista laterale diffusore architetturale ;; KEF-Ci3120QLM-THX-particolare.jpg » KEF Ci3120QLM-THX dettaglio Uni-Q con tecnologia MAT",
 46650: "KEF-Ci5120QLM-THX-frontale.jpg » KEF Ci5120QLM-THX diffusore in-wall 3 vie THX Ultra Uni-Q MAT ;; KEF-Ci5120QLM-THX-laterale.jpg » KEF Ci5120QLM-THX vista laterale diffusore architetturale ;; KEF-Ci5120QLM-THX-particolare.jpg » KEF Ci5120QLM-THX dettaglio Uni-Q con tecnologia MAT",
 35522: "KEF-Ci5160RLM-THX.jpg » KEF Ci5160RLM-THX diffusore da incasso 3 vie THX Ultra MAT ;; KEF-Ci5160RLM-THX-frontale.jpg » KEF Ci5160RLM-THX vista frontale con quattro woofer da 160 mm ;; KEF-Ci5160RLM-THX-laterale.jpg » KEF Ci5160RLM-THX vista laterale diffusore in-wall ;; KEF-Ci5160RLM-THX-griglia.jpg » KEF Ci5160RLM-THX con griglia magnetica verniciabile",
 35514: "KEF-Ci3160RLM-THX.jpg » KEF Ci3160RLM-THX diffusore da incasso 3 vie THX Ultra MAT ;; KEF-Ci3160RLM-THX-frontale.jpg » KEF Ci3160RLM-THX vista frontale con due woofer da 160 mm ;; KEF-Ci3160RLM-THX-laterale.jpg » KEF Ci3160RLM-THX vista laterale diffusore in-wall ;; KEF-Ci3160RLM-THX-griglia.jpg » KEF Ci3160RLM-THX con griglia magnetica verniciabile",
 35463: "KEF-Ci250RR.jpg » KEF Ci250RRM-THX diffusore in-ceiling 3 vie THX Ultra ;; KEF-Ci250RR-laterale-tri-no-griglia.jpg » KEF Ci250RRM-THX vista laterale, profondità di incasso 168 mm ;; KEF-Ci250RR-laterale-tri.jpg » KEF Ci250RRM-THX con griglia per installazione a soffitto",
 28303: "CI200ER.jpg » KEF Ci200ER vista frontale diffusore Uni-Q da 200 mm ;; ci200er-POSTERIORE.jpg » KEF Ci200ER vista posteriore diffusore da incasso ;; ci200er-LATERALE-2.jpg » KEF Ci200ER vista laterale diffusore Uni-Q da 200 mm",
 28287: "CI160ER.jpg » KEF Ci160ER vista frontale diffusore Uni-Q da 160 mm ;; ci160er-POSTERIORE.jpg » KEF Ci160ER vista posteriore diffusore da incasso ;; CI160ER-LATERALE.jpg » KEF Ci160ER dettaglio tweeter in alluminio da 16 mm",
 28281: "CI130ER-FRONTALE.jpg » KEF Ci130ER vista frontale diffusore Uni-Q da 130 mm ;; CI130ER-POSTERIORE.jpg » KEF Ci130ER vista posteriore diffusore da incasso ;; CI130ER-LATO-GRIGLIA.jpg » KEF Ci130ER griglia magnetica Ultra-Thin Bezel",
 28261: "ci2002CR-FRONTE.jpg » KEF Ci200.2CR vista frontale con Uni-Q da 200 mm ;; ci2002CR-LATERALE.jpg » KEF Ci200.2CR vista laterale diffusore da incasso ;; ci2002CR-GRIGLIA.jpg » KEF Ci200.2CR griglia magnetica Ultra-Thin Bezel",
 28246: "CI1302CR.jpg » KEF Ci130.2CR vista frontale con Uni-Q da 130 mm ;; CI1302CR-LATO.jpg » KEF Ci130.2CR dettaglio tweeter da 16 mm ;; CI1302CR-GRIGLIA.jpg » KEF Ci130.2CR con griglia magnetica Ultra-Thin Bezel",
 28234: "CI1602CR.jpg » KEF Ci160.2CR diffusore in-ceiling 2 vie Uni-Q 6,5 pollici ;; ci160.2cr-griglia.jpg » KEF Ci160.2CR con griglia magnetica Ultra-Thin Bezel ;; CI1602CR-POSTERIORE.jpg » KEF Ci160.2CR vista posteriore diffusore da incasso",
 28193: "ci130qsfl.jpg » KEF Ci130QSfl diffusore da incasso a filo quadrato 2 vie Uni-Q 5,25 pollici ;; ci130qsf-lato-griglia.jpg » KEF Ci130QSfl vista laterale con Uni-Q da 130 mm e griglia ;; ci130qsf-lato.jpg » KEF Ci130QSfl vista laterale con Uni-Q da 130 mm",
 28185: "CI200QR.jpg » KEF Ci200QR diffusore in-ceiling 2 vie Uni-Q 8 pollici ;; ci200qr-griglia.jpg » KEF Ci200QR con griglia magnetica Ultra-Thin Bezel ;; ci200qr-retro.webp » KEF Ci200QR vista posteriore diffusore da soffitto",
 28178: "ci200qs.webp » KEF Ci200QS diffusore da incasso quadrato 2 vie Uni-Q 8 pollici ;; ci200qs-lato.webp » KEF Ci200QS dettaglio tweeter centrale da 25 mm ;; ci200qs-griglia.jpg » KEF Ci200QS con griglia Ultra-Thin Bezel",
 28145: "ci130QRfl.jpg » KEF Ci130QRfl diffusore flush-mount 2 vie Uni-Q 5,25 pollici ;; Ci130QRfl-griglia.jpg » KEF Ci130QRfl con griglia a filo soffitto ;; ci130QRf-retro.jpg » KEF Ci130QRfl vista posteriore diffusore da incasso senza cornice",
 28140: "ci160qr.jpg » KEF Ci160QR diffusore in-ceiling 2 vie Uni-Q 6,5 pollici ;; ci160qr-retro.jpg » KEF Ci160QR vista posteriore diffusore da soffitto ;; kef-ci160qr-griglia-1000.jpg » KEF Ci160QR con la griglia montata solo a metà: si vedono l’altoparlante e la griglia",
 28135: "ci160QL-fronte.jpg » KEF Ci160QL diffusore da incasso 2 vie Uni-Q 6,5 pollici ;; ci160ql-griglia.jpg » KEF Ci160QL con griglia Ultra-Thin Bezel ;; kef-ci160ql-griglia-1000.jpg » KEF Ci160QL con la griglia montata solo a metà: si vedono l’altoparlante e la griglia",
 28117: "KEF-Ci100-2QR-frontale.jpg » KEF Ci100.2QR diffusore in-ceiling 2 vie Uni-Q 3 pollici ;; KEF-Ci100-2QR-frontale-griglia.jpg » KEF Ci100.2QR vista frontale con Uni-Q da 75 mm ;; KEF-Ci100-2QR-griglia-laterale.jpg » KEF Ci100.2QR vista laterale con cassa posteriore",
 28062: "ci160csds.jpg » KEF Ci160CSds diffusore stereo da incasso quadrato 6,5 pollici ;; ci160csds-lato.jpg » KEF Ci160CSds woofer doppia bobina da 160 mm ;; ci160csds-griglia.jpg » KEF Ci160CSds con griglia magnetica quadrata",
 28055: "ci200trb.jpg » KEF Ci200TRB vista frontale con woofer da 200 mm ;; ci200trb-lato-2.jpg » KEF Ci200TRB retro con doppia bobina da 8 Ohm ;; ci200trb-lato.jpg » KEF Ci200TRB vista laterale con profondità ultra-sottile",
 28046: "ci160ts.jpg » KEF Ci160TS diffusore in-wall ultra-sottile 2 vie da 36 mm ;; ci160ts-retro.jpg » KEF Ci160TS dettaglio driver T Series da 115 mm ;; ci160ts-lato.jpg » KEF Ci160TS vista laterale profondità inferiore a 36 mm",
 28039: "ci200qsb.jpg » KEF Ci200QSb-THX coppia vista frontale con due woofer da 200 mm ;; ci200qsb-lato.jpg » KEF Ci200QSb-THX vista laterale subwoofer passivo da incasso ;; ci200qsb-lato-2.jpg » KEF Ci200QSb-THX dettaglio woofer sub-basso da 200 mm",
 28021: "ci250rrb.jpg » KEF Ci250RRb-THX subwoofer da incasso 10 pollici con amplificatore KASA500 ;; ci250rrb-griglia-laterale.jpg » KEF Ci250RRb-THX vista laterale subwoofer architetturale ;; ci250rrb-griglia.jpg » KEF Ci250RRb-THX con griglia per installazione a soffitto",
 28016: "ci200-1.jpg » KEF Ci200RS-THX diffusore in-wall 2 vie Uni-Q 8 pollici THX Ultra ;; ci200-griglia-1.jpg » KEF Ci200RS-THX con griglia magnetica verniciabile ;; kef-ci200rs-thx-griglia-1000.jpg » KEF Ci200RS-THX con la griglia montata solo a metà: si vedono l’altoparlante e la griglia",
 28008: "ci200.jpg » KEF Ci200RR-THX diffusore in-ceiling 2 vie Uni-Q 8 pollici THX Ultra ;; ci200-lato.jpg » KEF Ci200RR-THX dettaglio tweeter 38 mm ;; ci200-griglia.jpg » KEF Ci200RR-THX con griglia per installazione a soffitto",
 27995: "ci160rr.jpg » KEF Ci160RR-THX diffusore da incasso 2 vie Uni-Q 6,5 pollici THX Ultra ;; ci160rr-griglia.jpg » KEF Ci160RR-THX con griglia magnetica verniciabile ;; ci160rr-retro.jpg » KEF Ci160RR-THX vista posteriore diffusore architetturale",
 2967: "virtuemart/product/KEF-Ci130-2CS-incasso-quadrato-fronte.jpg » KEF Ci130.2CS diffusore da incasso quadrato 2 vie Uni-Q 5,25 pollici ;; virtuemart/product/KEF-Ci130-2CS-altoparlante-incasso-quadrato.jpg » KEF Ci130.2CS vista frontale con Uni-Q da 130 mm ;; virtuemart/product/KEF-Ci130-2CS-incasso-quadrato-griglia.jpg » KEF Ci130.2CS con griglia magnetica Ultra-Thin Bezel",
 2920: "virtuemart/product/KEF-Ci4100QL-THX-diffusore-LCR-incasso.jpg » KEF Ci4100QL-THX diffusore in-wall LCR THX Select Uni-Q ;; virtuemart/product/KEF-Ci4100QL-THX-diffusore-LCR-incasso-griglia.jpg » KEF Ci4100QL-THX con griglia magnetica verniciabile ;; virtuemart/product/KEF-Ci4100QL-THX-diffusore-LCR-frontale.jpg » KEF Ci4100QL-THX vista frontale con tre woofer da 100 mm",
 2918: "KEF-Ci3160RLb-THX-frontale.jpg » KEF Ci3160RLb-THX subwoofer da incasso con tre woofer da 160 mm ;; KEF-Ci3160RLb-THX-laterale.jpg » KEF Ci3160RLb-THX vista laterale subwoofer in-wall sottile ;; KEF-Ci3160RLb-THX-particolare.jpg » Particolare di un woofer del KEF Ci3160RLb-THX montato sul pannello in alluminio",
 1764: "virtuemart/product/KEF-Ci160TR-frontale.jpg » KEF Ci160TR vista frontale diffusore circolare ultrasottile ;; virtuemart/product/KEF-Ci160TR-frontale-griglia-laterale.jpg » KEF Ci160TR con griglia magnetica Ultra-Thin Bezel ;; kef-ci-160tr.jpg » KEF Ci160TR diffusore da incasso ultrasottile",
 1763: "virtuemart/product/KEF-Ci160CRds-frontale.jpg » KEF Ci160CRds vista frontale diffusore stereo da incasso ;; virtuemart/product/KEF-Ci160CRds-frontale-griglia.jpg » KEF Ci160CRds diffusore in-ceiling stereo con doppio tweeter 6,5 pollici",
 1760: "virtuemart/product/KEF-Ci160-2CS-diffusore-incasso.jpg » KEF Ci160.2CS vista frontale con Uni-Q da 160 mm ;; virtuemart/product/KEF-Ci160-2CS-griglia.jpg » KEF Ci160.2CS con griglia magnetica Ultra-Thin Bezel ;; virtuemart/product/KEF-Ci160-2CS-laterale.jpg » KEF Ci160.2CS vista laterale con Uni-Q da 160 mm",
 1759: "virtuemart/product/kef-ci-130qs.jpg » KEF Ci130QS diffusore da incasso quadrato 2 vie Uni-Q 5,25 pollici ;; virtuemart/product/KEF-Ci130QS-griglia.jpg » KEF Ci130QS con griglia Ultra-Thin Bezel ;; virtuemart/product/KEF-Ci130QS-frontale-griglia.jpg » KEF Ci130QS vista frontale con Uni-Q da 130 mm",
 1758: "virtuemart/product/kef-ci-160qs.jpg » KEF Ci160QS diffusore da incasso quadrato 2 vie Uni-Q 6,5 pollici ;; virtuemart/product/KEF-Ci160QS-fronte-griglia.jpg » KEF Ci160QS vista frontale con Uni-Q da 160 mm ;; virtuemart/product/KEF-Ci160QS-laterale.jpg » KEF Ci160QS con griglia magnetica Ultra-Thin Bezel",
 1757: "KEF-Ci3-80QT-motorizzato.jpg » KEF Ci3-80QT diffusore in-ceiling motorizzato 3 vie Uni-Q ;; KEF-Ci3-80QT-soffitto.jpg » KEF Ci3-80QT aperto con sistema motorizzato a soffitto ;; KEF-Ci3-80QT-lifestyle.jpg » KEF Ci3-80QT installato in una sala Home Cinema",
 1265: "virtuemart/product/kef_ci100qs_012.jpg » KEF Ci100QS diffusore da incasso quadrato 2 vie Uni-Q 4 pollici ;; virtuemart/product/kef_ci100qs_03.jpg » KEF Ci100QS vista posteriore diffusore quadrato compatto ;; virtuemart/product/kef_ci100qs_04.jpg » KEF Ci100QS con griglia da incasso quadrata",
}

TIPO = {"P": "Diffusore da incasso a parete", "S": "Diffusore da incasso a soffitto", "L": "Diffusore LCR da incasso a parete",
        "2": "Diffusore stereo da incasso", "W": "Subwoofer da incasso"}


def caption(alt):
    a = alt.lower()
    for k, v in (("metà", "Griglia a metà"), ("griglia", "Con griglia"), ("posteriore", "Retro"), ("retro", "Retro"),
                 ("laterale", "Lato"), ("lato", "Lato"), ("particolare", "Dettaglio"), ("dettaglio", "Dettaglio"),
                 ("aperto", "Aperto"), ("installato", "Installato"), ("frontale", "Frontale")):
        if k in a:
            return v
    return "Vista"


def n(x):
    return float(x.replace(",", ".").split()[0]) if x and x[0].isdigit() else None


def scheda(t):
    (id, mod, cat, ser, forma, drv, risp, sens, imp, amp, spl, xo, foro, est, ptot, prof, vol, cert, peso, url, ex) = t
    soff = cat == "S" or (cat == "2" and forma == "tondo")
    tipo = TIPO[cat] if not (cat == "2" and not soff) else "Diffusore stereo da incasso a parete o soffitto"
    if cat == "S" and forma == "rett":
        tipo = "Diffusore da incasso a parete o soffitto"
    sub = ex.get("sub")
    vie = "3 vie" if drv[0] == "3 vie" else ("subwoofer" if sub else "2 vie")
    drv_txt = [d for d in drv if d != "3 vie"]
    fstr = foro if isinstance(foro, str) else f"{foro[0]} × {foro[1]}"
    fdis = foro if isinstance(foro, str) else (f"{foro[0]} × {foro[1]}" if foro[0] != foro[1] else f"{foro[0]} × {foro[1]} (quadrato)")
    serie = SERIE[ser]
    righe0 = f"{vie} · {drv_txt[0]}"
    I = imgs(IMG[id])
    f0 = ex.get("fonte", GROUP)

    car = [f"{tipo}, {serie}.", *[d[0].upper() + d[1:] + "." for d in drv_txt]]
    if "Uni-Q" in " ".join(drv_txt):
        car.append("Driver coassiale Uni-Q: tweeter al centro del medio o del woofer, stessa dispersione su tutta l'area d'ascolto.")
    if ex.get("ds"):
        car.append("Stereo in un solo diffusore: woofer a doppia bobina mobile e due tweeter, uno per canale.")
    if ex.get("flush"):
        car.append("Versione a filo (flush): senza cornice visibile, la griglia resta a filo della superficie.")
    if ex.get("qt"):
        car.append("Motorizzato: scende dal soffitto in funzione e rientra a filo quando è spento. Motore a 12 V.")
    if cert:
        car.append(f"{cert}.")
    if ex.get("coppia"):
        car.append("Su Extrasound è venduto in coppia.")

    acu = [f"Risposta (±6 dB): {risp}.", f"Sensibilità (2,83 V / 1 m): {sens}.", f"Impedenza nominale: {imp}.",
           f"Amplificazione consigliata: {amp}.", f"SPL massimo: {spl}."]
    if xo:
        acu.append(f"Incrocio: {xo}.")
    if ex.get("hpf"):
        acu.append(f"Filtro passa-alto consigliato da KEF: {ex['hpf']}.")
    if ex.get("qt"):
        acu.append("Filtro passa-alto consigliato da KEF: 100 Hz. Copertura nominale 170°.")

    dim = [f"Foro: {fstr}.", f"Ingombro esterno: {est if isinstance(est, str) else est[0] + ' × ' + est[1]}" + (f" × {ptot}." if ptot else "."),
           f"Profondità di montaggio: {prof}."]
    if vol:
        dim.append(f"Volume posteriore: ideale {str(vol[0]).replace('.', ',')} L, minimo {str(vol[1]).replace('.', ',')} L.")
    dim.append(f"Peso: {peso}.")

    if forma == "tondo":
        mis = {"forma": "tondo", "foro": foro.replace("Ø ", ""), "est": est.replace("Ø ", ""), "prof": prof.split(" (")[0]}
    else:
        if forma == "orizz":
            mis = {"forma": "rett", "orizzontale": True, "foro": foro, "est": est, "prof": prof.split(" (")[0]}
        else:
            mis = {"forma": "rett", "foro": [foro[1], foro[0]], "est": [est[1], est[0]], "prof": prof.split(" (")[0]}
    if ptot:
        mis["prof_tot"] = ptot
    mis["nota"] = "Foro tratteggiato in rosso. Misure KEF; disegno non in scala."
    if sub == "kasa" and forma == "tondo":
        mis = None

    # collegamenti
    zmin = n(imp)
    if sub in ("kasa",):
        col = [{"titolo": "KEF KASA500", "icona": "subwoofer", "voci": [
            "Subwoofer passivo da alimentare solo con l'amplificatore KEF KASA500, che gestisce taglio ed equalizzazione dedicata.",
            "Ingresso del KASA500 dall'uscita subwoofer / LFE del processore."]}]
    elif sub == "qsb":
        col = [{"titolo": "Due modi d'uso", "icona": "subwoofer", "voci": [
            "Passivo con crossover interno inserito (taglio 100 Hz): si collega in parallelo ai diffusori su un canale di potenza, 6 Ω.",
            "Con amplificatore KEF KASA500: risposta estesa a 30 – 140 Hz."]}]
    elif sub == "trb":
        col = [{"titolo": "Due modi d'uso", "icona": "subwoofer", "voci": [
            "Doppia bobina: in stereo 2 × 8 Ω (una bobina per canale) oppure in mono 16 Ω.",
            "Passivo: 42 – 120 Hz con amplificazione da 10 – 125 W. Con KEF KASA500: 32 – 120 Hz."]}]
    else:
        v = [f"{imp} nominali: un diffusore per canale su qualsiasi amplificatore da installazione."]
        if zmin and zmin < 6:
            v.append("Carico da 4 Ω: scegli un amplificatore dichiarato stabile a 4 Ω; non metterlo in bridge né in parallelo con altri diffusori.")
        if ex.get("ds"):
            v = ["Due ingressi: canale sinistro e destro dello stesso amplificatore, 8 Ω per canale.",
                 "Per stanze piccole o corridoi dove c'è posto per un solo diffusore."]
        v.append(f"Amplificazione consigliata da KEF: {amp}.")
        col = [{"titolo": "Amplificazione", "link": "amplificatori.html", "icona": "sorgente", "voci": v}]
    if ex.get("qt"):
        col.append({"titolo": "Motore", "icona": "domotica", "voci": [
            "Il meccanismo è a 12 V e richiede un'alimentazione a 12 V separata.",
            "Modalità di comando (trigger, contatti) da confermare sul manuale KEF Ci3-80QT."]})

    # dove montarlo
    if cat == "L":
        dove = ["Sinistro e destro ai lati dello schermo, centrale sopra o sotto.", "Montaggio orizzontale (come nei disegni KEF): verifica che il foro stia tra i montanti."]
    elif sub:
        dove = ["Anche nascosto in parete o a soffitto: il subwoofer non è direzionale.", "Rispetta il volume posteriore indicato: è quello che fissa l'estensione in basso."]
    elif soff:
        dove = ["Lontano da pareti e angoli quando possibile.", "Verifica travi, tubi e impianti prima di tagliare."]
    else:
        dove = ["Parete o soffitto; il tweeter coassiale non richiede orientamento.", "Verifica montanti, tubi e impianti prima di tagliare."]
    if vol:
        dove.append(f"Volume dietro il diffusore: ideale {str(vol[0]).replace('.', ',')} L, minimo {str(vol[1]).replace('.', ',')} L.")
    if ex.get("rif"):
        dove.append(f"Per le nuove costruzioni KEF prevede il telaio di predisposizione {ex['rif']}.")
    sist = [{"titolo": "Dove montarlo", "voci": dove}]
    if soff and not sub:
        sist[0]["posa"] = {"tipo": "soffitto", "distanza": "lontano dalle pareti", "nota": "zona d'ascolto"}
    if ex.get("ds"):
        sist.append({"titolo": "Schema", "voci": ["Un solo diffusore riceve i due canali dello stesso amplificatore."],
                     "zone": [{"label": f"{mod} · L + R", "tipo": "2"}], "apparecchio": "Amplificatore"})

    passi = [
        ["Verifica il vano", f"Profondità libera di almeno {prof.split(' (')[0]}" + (f" e, se possibile, {str(vol[0]).replace('.', ',')} L di volume dietro il diffusore." if vol else ".")],
        ["Traccia e taglia", f"Usa la dima fornita e taglia il foro: {fdis}."],
        ["Collega", "Positivo sul morsetto rosso (+), negativo sul nero (−). Stessa polarità su tutti i diffusori."],
        ["Inserisci e fissa", "Inserisci il diffusore e stringi le viti dei fermi: le alette ruotano e serrano il pannello. Non stringere troppo."],
        ["Chiudi", "Monta la griglia magnetica. Per verniciare cornice o griglia proteggi i driver con la maschera fornita."],
    ]
    if ex.get("flush"):
        passi[3] = ["Inserisci e rasa", "Versione a filo: il telaio va rasato nel cartongesso. Procedura e materiali da confermare sul manuale KEF della versione flush."]
    if ex.get("qt"):
        passi = [["Verifica il vano", "Profondità libera di almeno 120 mm sopra il soffitto; peso 3,3 kg."],
                 ["Traccia e taglia", "Foro rettangolare 354 × 112 mm."],
                 ["Collega", "Cavo di potenza ai morsetti (fino a Ø 2,5 mm) rispettando la polarità; alimentazione del motore a 12 V."],
                 ["Fissa", "Procedura di fissaggio da confermare sul manuale di installazione KEF."]]
    sist.append({"titolo": "Montaggio", "passi": passi})

    chiave = [f"{vie} · {drv_txt[0]} · {imp.split(' (')[0]}" if not sub else f"Subwoofer · {drv_txt[0]}",
              f"Foro {fstr}", f"Profondità {prof.split(' (')[0]}"]
    nota = f"Dati dalla {f0['label']}, confrontati con la scheda Extrasound."
    if ex.get("diff"):
        nota += " " + ex["diff"] + " Fa fede il dato KEF."
    intro = [f"Il <strong>KEF {mod}</strong> è un {tipo[0].lower() + tipo[1:]} della {serie}: {', '.join(drv_txt)}. Impedenza {imp}" + (f", {cert}." if cert else "."),
             f"Foro <strong>{fstr}</strong>, profondità di montaggio <strong>{prof}</strong>."]
    fonti = [f0]
    d = {"id": id, "tipo": "diffusore", "cat": cat, "brand": "KEF", "model": mod, "crop": False,
         "meta": f"KEF {mod}: {righe0}, {tipo[0].lower() + tipo[1:]}. Foro, profondità, volume posteriore e collegamenti per l'installatore.",
         "img": I[0], "chiave": chiave, "righe": [righe0, tipo, serie], "intro": intro,
         "colonne": [{"titolo": "Caratteristiche", "voci": car}, {"titolo": "Acustica", "voci": acu}, {"titolo": "Dimensioni", "voci": dim}],
         "viste": [vista(i, caption(i["alt"])) for i in I[1:4]], "misure": mis, "collega": col, "sistemi": sist,
         "nota": nota, "extrasound": X + url, "fonti": fonti}
    return salva(d)


if __name__ == "__main__":
    for t in M:
        print(scheda(t))
