"""Schede dei diffusori da esterno (categoria E). Dati dalle schede Extrasound, verificati con le schede dei
produttori dove reperibili (fonti in ogni scheda). Eseguire dalla radice: python3 _strumenti/marchi_esterno.py"""
import sys; sys.path.insert(0, '_strumenti')
from schede_util import *

X = 'https://www.extrasound.it/'
def F(l, u): return {"label": l, "url": u}
JBL_XD = F("scheda tecnica JBL Stage XD rev. 2.0", "https://www.rapalloav.co.nz/wp-content/uploads/2022/12/Spec-Sheet-JBL-Stage-XD-Rev2.0-20220801.pdf")
MURO = F("manuale ELAC Muro Outdoor", "https://elac.com/download/muroo/muro-outdoor-manual.pdf")
VENT = F("scheda KEF Ventura", "https://www.poulissen.nl/sites/default/files/product/bijlagen/ventura_en_0.pdf")
OD6 = F("scheda prodotto Focal 100 OD6", "https://homemovie.hu/wp-content/uploads/2023/03/100od6_fiche-produit.pdf")
RAIN = F("scheda tecnica Elipson Rain", "https://cdn.shopify.com/s/files/1/0055/9906/8206/files/elipson-rain-spec-sheet.pdf")
ASW65 = F("scheda tecnica ArtSound ASW65.2", "https://www.telecontrol.ro/domains/telecontrol.ro/files/download_files/asw652b-0-pdf7473.pdf")
KURV = F("manuale ArtSound Kurv", "https://stylesound.com/wp-content/uploads/2024/01/KURV_manual_uk.pdf")
SAT = F("scheda Polk Atrium Sat300", "https://gibbyselectronicsupermarket.ca/cdn/shop/files/Polk_Atrium_Sat300_Info_Sheet.pdf")

STAFFA_GEN = "Fissa la staffa a una superficie solida con viti e tasselli adatti al supporto (muratura, legno); sul cartongesso solo su un montante."
CAVO_EST = "Usa cavo per esterni (da interramento se corre nel terreno). Lascia un'ansa sotto il diffusore, così l'acqua gocciola via prima dei morsetti."


def passi(staffa, collega, orienta, finale, punto=None):
    return [["Scegli il punto", punto or "Al riparo dalla pioggia diretta quando possibile, all'altezza delle orecchie o più in alto con il diffusore inclinato verso la zona d'ascolto."],
            ["Fissa la staffa", staffa], ["Porta i cavi", CAVO_EST], ["Collega", collega], ["Monta e orienta", orienta], ["Chiudi", finale]]


POL = "Rispetta la polarità: + sul morsetto rosso, − sul nero, uguale su tutti i diffusori."

# id, brand, modello, vendita, sistema, driver[], risposta, sens, imp, amp, ip, (L, A, P), peso, colonne extra, staffa/montaggio, passi, fonti, url, img, opzioni
M = [
 (62549, "JBL", "Stage XD-5", "coppia", "2 vie", ["woofer 13 cm in polipropilene caricato con grafite", "tweeter 25 mm a cupola in alluminio con guida d'onda HDI"], "75 Hz – 25 kHz (−6 dB)", "86 dB (2,83 V / 1 m)", "4 Ω", "20 – 100 W RMS", "IP67, da −35 a +75 °C",
  ("179 mm", "250 mm", "162 mm"), None, ["Griglia magnetica senza cornice; logo ruotabile."], "staffa orientabile, sporgenza 71 mm",
  passi(STAFFA_GEN, POL, "Aggancia il diffusore alla staffa e regola l'inclinazione verso gli ascoltatori. Verticale o orizzontale: ruota il logo.", "Monta la griglia magnetica."),
  [JBL_XD], "jbl-stage-xd-5-coppia-di-diffusori-da-esterno-ip67-a-2-vie-con-woofer-da-13-cm",
  "jbl-stage-xd-5-nero-tre-quarti-senza-griglia-1000.jpg » JBL Stage XD-5 nero di tre quarti senza griglia ;; jbl-stage-xd-5-finiture-1000.jpg » JBL Stage XD-5 nelle finiture nero e bianco ;; jbl-stage-xd-5-nero-laterale-con-staffa-1000.jpg » JBL Stage XD-5 nero visto di lato con la staffa",
  {"diff": "Impedenza: la scheda Extrasound indica 6 Ω, la scheda JBL Stage XD rev. 2.0 4 Ω; scegli un amplificatore stabile a 4 Ω.", "z": 4}),
 (62566, "JBL", "Stage XD-6", "coppia", "2 vie", ["woofer 16,5 cm in polipropilene caricato con grafite", "tweeter 25 mm a cupola in alluminio con guida d'onda HDI"], "55 Hz – 25 kHz (−6 dB)", "88 dB (2,83 V / 1 m)", "4 Ω", "20 – 100 W RMS", "IP67, da −35 a +75 °C",
  ("222 mm", "299 mm", "194 mm"), None, ["Griglia magnetica senza cornice; logo ruotabile."], "staffa orientabile, sporgenza 71 mm",
  passi(STAFFA_GEN, POL, "Aggancia il diffusore alla staffa e regola l'inclinazione verso gli ascoltatori. Verticale o orizzontale: ruota il logo.", "Monta la griglia magnetica."),
  [JBL_XD], "jbl-stage-xd-6-coppia-di-diffusori-da-esterno-ip67-a-2-vie-con-woofer-da-165-cm",
  "jbl-stage-xd-6-nero-tre-quarti-senza-griglia-1000.jpg » JBL Stage XD-6 nero di tre quarti senza griglia ;; jbl-stage-xd-6-finiture-1000.jpg » JBL Stage XD-6 nelle finiture nero e bianco ;; jbl-stage-xd-6-nero-laterale-con-staffa-1000.jpg » JBL Stage XD-6 nero visto di lato con la staffa",
  {"diff": "Impedenza: la scheda Extrasound indica 6 Ω, la scheda JBL Stage XD rev. 2.0 4 Ω; scegli un amplificatore stabile a 4 Ω.", "z": 4}),
 (43607, "ELAC", "Muro OD-M61", "coppia", "2 vie, cassa chiusa o bass-reflex", ["woofer 165 mm in polipropilene, sospensione in gomma", "tweeter 25 mm a cupola in seta, bobina CCAW a 2 strati"], "80 Hz – 20 kHz (−3 dB); 65 Hz (−10 dB)", "86 dB (2,83 V / 1 m)", "8 Ω", "30 – 100 W; tenuta 80 W, 130 W di picco", "IP66",
  ("200 mm", "310 mm", "235 mm"), "3,5 kg", ["Incrocio 2.160 Hz.", "Tappi reflex rimovibili: chiusi = cassa chiusa, aperti = bass-reflex.", "Morsetti a vite a 5 vie sotto il coperchio posteriore con passacavo a tenuta.", "Non esiste versione 70 / 100 V."], "staffa con tacche ogni 15°",
  passi("Fissa la staffa con due viti M6–M8 × 50 mm (o #14–#20 × 2″): nel cartongesso su un montante, nella muratura con tasselli.", "Spegni l'impianto. Spella 12 mm, inserisci nei morsetti a 5 vie rispettando la polarità, fai passare il cavo nel passacavo e stringilo per sigillare.", "Allenta i bulloni laterali, ruota il diffusore verso gli ascoltatori (tacche ogni 15°) e riserra. Parete, soffitto o angolo; verticale o orizzontale.", "Aggancia un cavo di sicurezza all'occhiello sul retro. Per il bass-reflex togli le viti della griglia e i tappi: conviene con la bella stagione."),
  [MURO], "elac-muro-od-m61-coppia-di-diffusori-outdoor-indoor-2-vie-ip66",
  "ELAC-OD-M61.jpg » Coppia di ELAC Muro OD-M61 nero e bianco di tre quarti ;; ELAC-OD-M61-frontale.jpg » ELAC Muro OD-M61 nero e bianco visti di fronte ;; ELAC-OD-M61-orizzontale.jpg » ELAC Muro OD-M61 nero montato in orizzontale",
  {"cavi": {"intestazione": "Lunghezza (ELAC)", "righe": [["Fino a 30 m", "18 AWG"], ["Fino a 45 m", "16 AWG"], ["Fino a 80 m", "14 AWG"], ["Fino a 122 m", "12 AWG"]]}}),
 (42654, "ELAC", "Muro OD-M81", "coppia", "2 vie, cassa chiusa o bass-reflex", ["woofer 203 mm in polipropilene, sospensione in gomma", "tweeter 25 mm a cupola in seta, bobina CCAW a 2 strati"], "70 Hz – 20 kHz (−3 dB); 55 Hz (−10 dB)", "87 dB (2,83 V / 1 m)", "8 Ω", "30 – 150 W; tenuta 100 W, 150 W di picco", "IP66",
  ("250 mm", "390 mm", "285 mm"), "5 kg", ["Incrocio 2.160 Hz.", "Tappi reflex rimovibili: chiusi = cassa chiusa, aperti = bass-reflex.", "Morsetti a vite a 5 vie sotto il coperchio posteriore con passacavo a tenuta.", "Non esiste versione 70 / 100 V."], "staffa con tacche ogni 15°",
  passi("Fissa la staffa con due viti M6–M8 × 50 mm (o #14–#20 × 2″): nel cartongesso su un montante, nella muratura con tasselli.", "Spegni l'impianto. Spella 12 mm, inserisci nei morsetti a 5 vie rispettando la polarità, fai passare il cavo nel passacavo e stringilo per sigillare.", "Allenta i bulloni laterali, ruota il diffusore verso gli ascoltatori (tacche ogni 15°) e riserra. Parete, soffitto o angolo; verticale o orizzontale.", "Aggancia un cavo di sicurezza all'occhiello sul retro. Per il bass-reflex togli le viti della griglia e i tappi: conviene con la bella stagione."),
  [MURO], "elac-muro-od-m81-diffusori-outdoor-waterproof-coppia-da-parete",
  "ELAC-OD-M81.jpg » Coppia di ELAC Muro OD-M81 nelle finiture nero e bianco ;; ELAC-OD-M81-M61-bianco.jpg » Due ELAC Muro bianchi di tre quarti ;; ELAC-OD-M81-M61-nero.jpg » Due ELAC Muro neri di tre quarti",
  {"cavi": {"intestazione": "Lunghezza (ELAC)", "righe": [["Fino a 30 m", "18 AWG"], ["Fino a 45 m", "16 AWG"], ["Fino a 80 m", "14 AWG"], ["Fino a 122 m", "12 AWG"]]},
   "diff": "La scheda Extrasound indica un'amplificazione di 30 – 180 W; il manuale ELAC 30 – 150 W."}),
 (1770, "KEF", "Ventura 5", "coppia", "2 vie, cassa chiusa", ["woofer 130 mm", "tweeter 25 mm in alluminio raffreddato a fluido"], "60 Hz – 20 kHz", "89 dB (2,83 V / 1 m)", "6 Ω", "10 – 100 W", "IP65; nebbia salina oltre 1.200 ore; da −40 a +70 °C",
  ("194 mm", "260 mm", "165 mm"), "3,3 kg", ["Incrocio 3,8 kHz.", "Cassa in ABS trattato anti-UV; griglia e staffa in alluminio, minuterie in acciaio inox e ottone.", "Due inserti filettati 1/4″-20 sul retro per staffe di terze parti."], "staffa a cricchetto, rotazione fino a 180°",
  passi(STAFFA_GEN, POL, "Monta il diffusore sulla staffa a cricchetto e ruotalo verso la zona d'ascolto (fino a 180°).", "Controlla che la staffa sia bloccata e il cavo non tiri sui morsetti."),
  [VENT], "diffusori-2-vie-100w-da-esterno-ventura-5-kef",
  "KEF-Ventura-5-casse-acustiche-esterno.jpg » KEF Ventura 5, coppia di diffusori da esterno ;; KEK-Ventura-posteriore.jpg » KEF Ventura, retro con asole per la staffa ;; kef-ventura-5-diffusore-outdoor-lifestyle.jpg » KEF Ventura 5 installati vicino a una piscina",
  {"diff": "La scheda Extrasound indica 2,85 kg e una risposta ±6 dB; la scheda KEF indica 3,3 kg e 60 Hz – 20 kHz a ±3 dB."}),
 (1771, "KEF", "Ventura 6", "coppia", "2 vie, cassa chiusa", ["woofer 160 mm", "tweeter 25 mm in alluminio raffreddato a fluido"], "54 Hz – 20 kHz", "90 dB (2,83 V / 1 m)", "6 Ω", "10 – 125 W", "IP65; nebbia salina oltre 1.200 ore; da −40 a +70 °C",
  ("226 mm", "298 mm", "183 mm"), "3,8 kg", ["Incrocio 3 kHz.", "Cassa in ABS trattato anti-UV; griglia e staffa in alluminio, minuterie in acciaio inox e ottone.", "Due inserti filettati 1/4″-20 sul retro per staffe di terze parti."], "staffa a cricchetto, rotazione fino a 180°",
  passi(STAFFA_GEN, POL, "Monta il diffusore sulla staffa a cricchetto e ruotalo verso la zona d'ascolto (fino a 180°).", "Controlla che la staffa sia bloccata e il cavo non tiri sui morsetti."),
  [VENT], "diffusori-2-vie-125w-da-esterno-ventura-6-kef",
  "KEK-Ventura6.jpg » KEF Ventura 6, coppia di diffusori da esterno ;; KEK-Ventura-posteriore.jpg » KEF Ventura, retro con asole per la staffa ;; kef-ventura-5-diffusore-outdoor-lifestyle.jpg » Diffusori KEF Ventura installati vicino a una piscina", {}),
 (48842, "Focal", "100 OD6", "singolo", "2 vie", ["woofer 16,5 cm impermeabile in polipropilene Polyglass", "tweeter a cupola rovesciata in alluminio"], "65 Hz – 23 kHz (±3 dB); −6 dB a 55 Hz", "87 dB (2,83 V / 1 m)", "8 Ω (minimo 6,7 Ω)", "20 – 120 W", "IP66, trattato anti-UV",
  ("224 mm", "319 mm", "256 mm"), "4,1 kg con staffa", ["Incrocio 2.800 Hz.", "Cassa in polipropilene ad alta densità, griglia in alluminio con logo ruotabile; verniciabile.", "Morsetti a molla con protezione in silicone.", "Versione 100 OD6-T con trasformatore: prese 70 V 7,5 / 15 / 30 W (dato Extrasound)."], "staffa in alluminio, rotazione 180°",
  passi(STAFFA_GEN, POL + " Due diffusori si possono collegare sulla stessa uscita dell'amplificatore (Focal).", "Staffa a U in alluminio con fissaggio a tacche, articolata a 180°: verticale o orizzontale.", "Ruota il logo sulla griglia secondo il verso di montaggio."),
  [OD6], "focal-100-od6-diffusore-da-esterno-ip66",
  "focal-100-od6-nero-bianco-tre-quarti.jpg » Focal 100 OD6 nero e bianco senza griglia ;; focal-100-od6-nero-bianco-griglia.jpg » Focal 100 OD6 nero e bianco con la griglia in alluminio ;; focal-100-od6-nero-bianco-profilo.jpg » Focal 100 OD6 visti di lato con la staffa a U", {}),
 (48847, "Focal", "100 OD8", "singolo", "2 vie", ["woofer 21 cm impermeabile in polipropilene Polyglass", "tweeter a cupola rovesciata in alluminio"], "60 Hz – 23 kHz (±3 dB); −6 dB a 45 Hz", "88 dB (2,83 V / 1 m)", "8 Ω (minimo 6,7 Ω)", "20 – 150 W", "IP66, trattato anti-UV",
  ("258 mm", "390 mm", "280 mm"), "5,8 kg con staffa", ["Incrocio 2.800 Hz.", "Cassa in polipropilene ad alta densità, griglia in alluminio con logo ruotabile; verniciabile.", "Morsetti a molla con protezione in silicone.", "Versione 100 OD8-T con trasformatore: prese 70 V 15 / 30 / 60 W (dato Extrasound)."], "staffa in alluminio, rotazione 180°",
  passi(STAFFA_GEN, POL + " Due diffusori si possono collegare sulla stessa uscita dell'amplificatore.", "Staffa a U in alluminio con fissaggio a tacche, articolata a 180°: verticale o orizzontale.", "Ruota il logo sulla griglia secondo il verso di montaggio."),
  [], "focal-100-od8-diffusore-da-esterno-ip66",
  "focal-100-od8-nero-bianco-tre-quarti.jpg » Focal 100 OD8 nero e bianco senza griglia ;; focal-100-od8-nero-bianco-griglia.jpg » Focal 100 OD8 nero e bianco con la griglia in alluminio ;; focal-100-od8-nero-bianco-orizzontale-2.jpg » Focal 100 OD8 montati in orizzontale sulla staffa",
  {"nota": "Dati dalla scheda Extrasound; la scheda Focal del 100 OD8 non è stata reperita online, i dati comuni coincidono con quella del 100 OD6."}),
 (31740, "Elipson", "Rain 4", "coppia", "2 vie", ["medio-basso 100 mm", "tweeter 25 mm"], "100 Hz – 20 kHz (±3 dB)", "87 dB (1 W / 1 m)", "8 Ω", "80 W massimi", "IPX4",
  ("154 mm", "230 mm", "145 mm"), None, ["Incrocio 3.250 Hz.", "Supporto a parete integrato, orientabile a 180°.", "Trattamenti antiruggine e anti-UV."], "supporto integrato orientabile 180°",
  passi(STAFFA_GEN, POL, "Aggancia il diffusore al supporto e orientalo verso la zona d'ascolto.", "Controlla il serraggio del supporto."),
  [RAIN], "elipson-rain-4-coppia-diffusori-outdoor-2-vie-da-parete",
  "elipson-rain-4.jpg » Coppia di Elipson Rain 4 bianca e nera ;; elipson-rain-4-retro.jpg » Retro dell'Elipson Rain 4 con il supporto ;; elipson-rain-4-lato.jpg » Elipson Rain 4 vista di lato",
  {"diff": "Protezione: la scheda Extrasound indica IP66, la scheda tecnica Elipson IPX4 (spruzzi d'acqua). Da verificare prima di installarlo esposto alla pioggia."}),
 (31763, "Elipson", "Rain 6", "coppia", "2 vie", ["medio-basso 165 mm", "tweeter 25 mm"], "80 Hz – 20 kHz (±3 dB)", "89 dB (1 W / 1 m)", "8 Ω", "120 W massimi", "IPX4",
  ("195 mm", "285 mm", "183 mm"), None, ["Incrocio 3.000 Hz.", "Supporto a parete integrato, orientabile a 180°.", "Trattamenti antiruggine e anti-UV."], "supporto integrato orientabile 180°",
  passi(STAFFA_GEN, POL, "Aggancia il diffusore al supporto e orientalo verso la zona d'ascolto.", "Controlla il serraggio del supporto."),
  [RAIN], "elipson-rain-6-coppia-diffusori-outdoor-2-vie-da-parete",
  "elipson-rain-6.jpg » Coppia di Elipson Rain 6 nera e bianca ;; elipson-rain-6-staffa.jpg » Elipson Rain 6 con il supporto a parete smontato ;; elipson-rain-6-lato.jpg » Due Elipson Rain 6 viste di lato",
  {"diff": "Protezione: la scheda Extrasound indica IP66, la scheda tecnica Elipson IPX4 (spruzzi d'acqua). Da verificare prima di installarlo esposto alla pioggia."}),
 (31772, "Elipson", "Rain 8", "coppia", "2 vie", ["medio-basso 200 mm", "tweeter 25 mm"], "70 Hz – 20 kHz (±3 dB)", "90 dB (1 W / 1 m)", "8 Ω", "150 W massimi", "IPX4",
  ("244 mm", "355 mm", "230 mm"), None, ["Incrocio 3.200 Hz.", "Supporto a parete integrato, orientabile a 180°.", "Trattamenti antiruggine e anti-UV."], "supporto integrato orientabile 180°",
  passi(STAFFA_GEN, POL, "Aggancia il diffusore al supporto e orientalo verso la zona d'ascolto.", "Controlla il serraggio del supporto."),
  [RAIN], "elipson-rain-8-coppia-diffusori-outdoor-2-vie-150-w",
  "elipson-rain-8.jpg » Coppia di Elipson Rain 8 bianca e nera ;; elipson-rain-8-lato.jpg » Due Elipson Rain 8 viste di lato con il supporto ;; elipson-rain-8-retro.jpg » Retro dell'Elipson Rain 8 con il supporto a parete",
  {"diff": "Protezione: la scheda Extrasound indica IP66, la scheda tecnica Elipson IPX4 (spruzzi d'acqua). Da verificare prima di installarlo esposto alla pioggia."}),
 (42965, "ArtSound", "ASW45.2", "coppia", "2 vie bass-reflex", ["woofer 3,5″ in polimica", "tweeter 0,5″ a cupola in PEI"], "95 Hz – 20 kHz", "86 dB", "8 Ω", "10 – 80 W", "per esterni e ambienti umidi; ambienti fino a 30 m²",
  ("150 mm", "200 mm", "110 mm"), "1,35 kg", ["Cassa in ABS; nero o bianco.", "Staffa a U inclusa."], "staffa a U",
  passi(STAFFA_GEN, POL, "Monta il diffusore nella staffa a U e stringi i pomelli all'angolo voluto.", "Verifica che i pomelli siano ben stretti."),
  [], "artsound-asw45-2-coppia-diffusori-outdoor-2-vie-ip54-con-staffa",
  "artsound-asw45-2-coppia-1000.jpg » Coppia di ArtSound ASW45.2 neri con staffa a U ;; artsound-asw45-2-laterale-1000.jpg » ArtSound ASW45.2 visto di lato sulla staffa ;; artsound-asw45-2-retro-1000.jpg » Retro dell'ArtSound ASW45.2 con i morsetti", {"nota": "Dati dalla scheda Extrasound: scheda ArtSound del modello non reperita online."}),
 (42959, "ArtSound", "ASW55.2", "coppia", "2 vie bass-reflex", ["woofer 5,25″ in polimica", "tweeter 0,5″ a cupola in PEI"], "75 Hz – 20 kHz", "87 dB", "8 Ω", "20 – 120 W", "per esterni e ambienti umidi; ambienti fino a 40 m²",
  ("190 mm", "240 mm", "150 mm"), "2,3 kg", ["Cassa in ABS; nero o bianco.", "Staffa a U inclusa."], "staffa a U",
  passi(STAFFA_GEN, POL, "Monta il diffusore nella staffa a U e stringi i pomelli all'angolo voluto.", "Verifica che i pomelli siano ben stretti."),
  [], "artsound-asw55-2-coppia-diffusori-outdoor-2-vie-ip54-con-staffa",
  "artsound-asw55-2-coppia-1000.jpg » Coppia di ArtSound ASW55.2 neri con staffa a U ;; artsound-asw55-2-laterale-1000.jpg » ArtSound ASW55.2 visto di lato sulla staffa ;; artsound-asw55-2-retro-1000.jpg » Retro dell'ArtSound ASW55.2 con i morsetti", {"nota": "Dati dalla scheda Extrasound: scheda ArtSound del modello non reperita online."}),
 (42942, "ArtSound", "ASW65.2", "coppia", "2 vie bass-reflex", ["woofer 6,5″ in polimica", "tweeter 1″ a cupola in PEI al neodimio"], "43 Hz – 20 kHz", "87 dB", "8 Ω", "175 W massimi (ArtSound)", "impermeabile (grado IP non dichiarato); ambienti fino a 50 m²",
  ("240 mm", "310 mm", "180 mm"), "3,13 kg", ["Cassa in ABS, schermata magneticamente; nero o bianco.", "Selettore interno / esterno; il reflex si chiude con il tubo fornito.", "Staffa a U inclusa."], "staffa a U",
  passi(STAFFA_GEN, POL, "Monta il diffusore nella staffa a U e stringi i pomelli all'angolo voluto. Imposta il selettore interno / esterno.", "Se serve, chiudi il reflex con il tubo in dotazione."),
  [ASW65], "artsound-asw65-2-coppia-diffusori-outdoor-2-vie-ip54-con-staffa",
  "Artsound-ASW-65-2.jpg » Coppia di ArtSound ASW65.2 bianco e nero ;; Artsound-ASW-65-2-bianco-posteriore.jpg » Retro dell'ArtSound ASW65.2 bianco ;; Artsound-ASW-65-2-nero-posteriore.jpg » Retro dell'ArtSound ASW65.2 nero",
  {"diff": "La scheda Extrasound indica un'amplificazione di 20 – 140 W; ArtSound dichiara 175 W massimi."}),
 (42938, "ArtSound", "ASW550", "coppia", "2 vie bass-reflex", ["woofer 5,25″ in polipropilene", "tweeter 0,79″ a cupola in seta"], "75 Hz – 20 kHz", "84 dB", "8 Ω", "40 – 180 W", "IP66; ambienti fino a 55 m²",
  ("181 mm", "288 mm", "136 mm"), "2,23 kg", ["Cassa in ABS, griglia in alluminio.", "Staffa brevettata orientabile a 180°."], "staffa orientabile 180°",
  passi(STAFFA_GEN, POL, "Monta il diffusore sulla staffa e orientalo (fino a 180°).", "Verifica il serraggio della staffa."),
  [], "artsound-asw550-diffusori-outdoor-compatti-da-esterno-resistenti-coppia",
  "artsound-asw550-coppia-1000.jpg » Coppia di ArtSound ASW550 neri con staffa a parete ;; artsound-asw550-frontale-1000.jpg » ArtSound ASW550 visto di fronte con la griglia in alluminio ;; Artsound-ASW550-morsetti.jpg » Morsetti dell'ArtSound ASW550", {"nota": "Dati dalla scheda Extrasound: scheda ArtSound del modello non reperita online."}),
 (42921, "ArtSound", "ASW800", "coppia", "2 vie bass-reflex", ["woofer 8″ in polipropilene", "tweeter 1″ a cupola in seta"], "65 Hz – 20 kHz", "87 dB", "8 Ω", "60 – 220 W", "IP66 (IP67 nella tabella ArtSound); ambienti fino a 65 m²",
  ("250 mm", "395 mm", "180 mm"), "3,4 kg", ["Cassa in ABS, griglia in alluminio.", "Staffa brevettata orientabile a 180°."], "staffa orientabile 180°",
  passi(STAFFA_GEN, POL, "Monta il diffusore sulla staffa e orientalo (fino a 180°).", "Verifica il serraggio della staffa."),
  [], "artsound-asw800-diffusori-outdoor-da-esterno-resistenti-alle-intemperie-coppia",
  "Artsound-ASW800.jpg » Coppia di diffusori da esterno ArtSound ASW800 ;; Artsound-ASW800-frontale.jpg » ArtSound ASW800 visto di fronte ;; Artsound-ASW800-morsetti.jpg » Morsetti dell'ArtSound ASW800", {"nota": "Dati dalla scheda Extrasound: scheda ArtSound del modello non reperita online."}),
 (42910, "ArtSound", "UNI40", "coppia", "2 vie bass-reflex", ["woofer 5,25″ in polipropilene e mica", "tweeter 0,5″ in PEI"], "60 Hz – 20 kHz", "90 dB", "8 Ω", "20 – 100 W", "per interno ed esterno; ambienti fino a 40 m²",
  ("146 mm", "230 mm", "142 mm"), "1,9 kg", ["Staffa multifunzione con snodo a sfera; morsetti a vite.", "Nero o bianco; verticale o orizzontale."], "staffa con snodo a sfera",
  passi(STAFFA_GEN, POL, "Monta il diffusore sullo snodo a sfera e orientalo; blocca lo snodo.", "Verifica il serraggio dello snodo."),
  [], "artsound-uni40-diffusori-on-wall-compatti-universali-per-interno-ed-esterno-coppia",
  "Artsound-UNI40.jpg » Diffusori da parete ArtSound UNI40 bianco e nero ;; Artsound-UNI40-orizzontale-bianco.jpg » ArtSound UNI40 bianco montato in orizzontale ;; Artsound-UNI40-orizzontale-nero.jpg » ArtSound UNI40 nero montato in orizzontale", {"nota": "Dati dalla scheda Extrasound: scheda ArtSound del modello non reperita online."}),
 (42904, "ArtSound", "UNI75", "singolo", "2 vie bass-reflex", ["2 woofer 5″", "tweeter 1″ a tromba"], "65 Hz – 20 kHz", "dichiarata da ArtSound 122 dB (valore da verificare)", "4 – 8 Ω", "200 – 380 W", "per interno ed esterno; locali ed eventi",
  ("170 mm", "430 mm", "230 mm"), "7,5 kg", ["Mobile in multistrato da 15 mm con rivestimento in poliuretano, schermato.", "Collegamento Speakon.", "Staffa a U inclusa."], "staffa a U",
  passi(STAFFA_GEN + " Il diffusore pesa 7,5 kg.", "Collega con cavo Speakon rispettando la polarità.", "Monta il diffusore nella staffa a U e stringi i pomelli all'angolo voluto.", "Aggiungi un cavo di sicurezza quando il diffusore è sopra le persone."),
  [], "artsound-uni75-diffusore-on-wall-universale-per-interno-ed-esterno",
  "Artsound-UNI75.jpg » Diffusore da parete ArtSound UNI75 con staffa ;; Artsound-UNI75-frontale.jpg » ArtSound UNI75 visto di fronte ;; Artsound-UNI75-laterale.jpg » ArtSound UNI75 visto di lato", {"nota": "Dati dalla scheda Extrasound: scheda ArtSound del modello non reperita online.", "amp": "artsound-prl-1502"}),
 (42640, "ArtSound", "Kurv", "singolo", "2 vie coassiale", ["woofer 5,25″ in polipropilene", "tweeter 0,75″ a cupola in seta coassiale"], "60 Hz – 20 kHz", "85 dB", "6 Ω o linea 100 V", "10 – 100 W", "IP66; ambienti fino a 50 m²",
  ("391 mm", "308 mm", "212 mm"), "4,9 kg", ["Da appoggio, emissione verso il basso a 360°.", "Corpo in LLDPE, griglia in alluminio; bianco o quarzo.", "Collegamento a bassa impedenza o su linea 100 V."], None,
  [["Scegli il punto", "A terra, su un piano stabile, al centro della zona da sonorizzare: il suono esce verso il basso a 360°."], ["Prepara il passaggio", "Porta il cavo fino al punto, interrato in un corrugato se attraversa il giardino."], ["Porta i cavi", CAVO_EST], ["Collega", "Scegli bassa impedenza (6 Ω) o linea 100 V secondo l'impianto e collega rispettando la polarità (schemi «Connecting stereo» e «Connecting 100V» del manuale ArtSound)."], ["Posiziona", "Appoggia il Kurv e verifica che il cavo non resti teso."], ["Chiudi", "Controlla la tenuta dei passacavi."]],
  [KURV], "artsound-kurv-diffusore-outdoor-di-design-ip66-360-8-ohm-100v",
  "Artsund-Kurv.jpg » Diffusore da esterno ArtSound Kurv ;; Artsund-Kurv-bianco-sotto.jpg » ArtSound Kurv bianco visto dal basso ;; Artsund-Kurv-bianco-lifestyle.jpg » ArtSound Kurv bianco in giardino", {"posa": "appoggio", "amp": "artsound-amp850"}),
 (37516, "Polk Audio", "Atrium 4", "coppia", "2 vie", ["woofer 11,4 cm Dynamic Balance, cono in polimero caricato con minerali", "tweeter 19 mm a cupola in alluminio anodizzato"], "75 Hz – 25 kHz", "89 dB (1 W / 1 m)", "compatibile con uscite da 8 Ω", "10 – 80 W", "test ASTM D5894 (UV e nebbia salina), MIL-STD 810 (immersione)",
  ("144 mm", "219 mm", "170 mm"), "1,63 kg", ["Staffa Speed-Lock in alluminio: verticale o orizzontale, rotazione 180°, inclinazione 45° verso il basso.", "Morsetti a 5 vie dorati; viteria inox e ottone; verniciabile."], "staffa Speed-Lock",
  passi(STAFFA_GEN, POL, "Aggancia il diffusore alla staffa Speed-Lock, ruotalo (180°) e inclinalo fino a 45° verso il basso.", "Blocca i pomelli della staffa."),
  [], "diffusore-da-esterno-polk-atrium-4",
  "polk-atrium-4-nero-bianco-1000.jpg » Polk Atrium 4 nero senza griglia e bianco con griglia ;; polk-atrium-4-lato-staffa-1000.jpg » Polk Atrium 4 visto di lato con la staffa Speed-Lock ;; polk-atrium-4-retro-1000.jpg » Retro del Polk Atrium 4 con i morsetti dorati", {"nota": "Dati dalla scheda Extrasound, ricavata dalla documentazione Polk."}),
 (37534, "Polk Audio", "Atrium 5", "coppia", "2 vie", ["woofer 12,7 cm Dynamic Balance, cono in polimero caricato con minerali", "tweeter 19 mm a cupola in alluminio anodizzato"], "60 Hz – 25 kHz", "90 dB (1 W / 1 m)", "compatibile con uscite da 8 Ω", "10 – 100 W", "test ASTM D5894 (UV e nebbia salina), MIL-STD 810 (immersione)",
  ("171 mm", "262 mm", "197 mm"), "2,09 kg", ["Staffa Speed-Lock in alluminio: verticale o orizzontale, rotazione 180°, inclinazione 45° verso il basso.", "Morsetti a 5 vie dorati; viteria inox e ottone; verniciabile."], "staffa Speed-Lock",
  passi(STAFFA_GEN, POL, "Aggancia il diffusore alla staffa Speed-Lock, ruotalo (180°) e inclinalo fino a 45° verso il basso.", "Blocca i pomelli della staffa."),
  [], "diffusore-da-esterno-polk-atrium-5",
  "polk-atrium-5-nero-bianco-1000.jpg » Polk Atrium 5 nero senza griglia e bianco con griglia ;; polk-atrium-5-lato-staffa-1000.jpg » Polk Atrium 5 visto di lato con la staffa Speed-Lock ;; polk-atrium-5-retro-1000.jpg » Retro del Polk Atrium 5 con i morsetti dorati", {"nota": "Dati dalla scheda Extrasound, ricavata dalla documentazione Polk."}),
 (37699, "Polk Audio", "Atrium 6", "coppia", "2 vie con PowerPort", ["woofer 13,3 cm Dynamic Balance in polipropilene aerato", "tweeter 25 mm a cupola in alluminio anodizzato"], "50 Hz – 27 kHz", "90 dB (1 W / 1 m)", "compatibile con uscite da 8 Ω", "10 – 100 W", "test ASTM D5894 (UV e nebbia salina), MIL-STD 810 (immersione)",
  ("195 mm", "297 mm", "222 mm"), "2,45 kg", ["Condotto PowerPort resistente all'acqua.", "Staffa Speed-Lock in alluminio: verticale o orizzontale, rotazione 180°, inclinazione 45° verso il basso.", "Morsetti a 5 vie dorati; verniciabile."], "staffa Speed-Lock",
  passi(STAFFA_GEN, POL, "Aggancia il diffusore alla staffa Speed-Lock, ruotalo (180°) e inclinalo fino a 45° verso il basso.", "Blocca i pomelli della staffa."),
  [], "diffusori-da-esterno-polk-atrium-6",
  "polk-atrium-6-nero-bianco-1000.jpg » Coppie di Polk Atrium 6 nero e bianco ;; polk-atrium-6-senza-griglia-1000.jpg » Polk Atrium 6 senza griglia ;; polk-atrium-6-lato-staffa-1000.jpg » Polk Atrium 6 visto di lato con la staffa Speed-Lock", {"nota": "Dati dalla scheda Extrasound, ricavata dalla documentazione Polk."}),
 (37708, "Polk Audio", "Atrium 8 SDI", "singolo", "2 vie stereo (SDI) con PowerPort", ["woofer 16,5 cm a doppia bobina mobile", "2 tweeter 25 mm a cupola in alluminio anodizzato"], "45 Hz – 27 kHz", "91 dB (1 W / 1 m)", "compatibile con uscite da 8 Ω", "10 – 125 W × 2", "test ASTM D5894 (UV e nebbia salina), MIL-STD 810 (immersione)",
  ("216 mm", "327 mm", "233 mm"), "4,4 kg", ["Commutatore SDI: doppio ingresso (stereo da un diffusore) o ingresso singolo (sinistro o destro di una coppia).", "Staffa Speed-Lock in alluminio; morsetti a 5 vie dorati."], "staffa Speed-Lock",
  passi(STAFFA_GEN, "Con il commutatore SDI su doppio ingresso collega sinistro e destro allo stesso diffusore; su ingresso singolo un solo canale. " + POL, "Aggancia il diffusore alla staffa Speed-Lock, ruotalo e inclinalo verso la zona d'ascolto.", "Blocca i pomelli della staffa."),
  [], "diffusori-da-esterno-polk-atrium-8-sdi",
  "polk-atrium-8-sdi-nero-bianco-1000.jpg » Polk Atrium 8 SDI nero e bianco ;; polk-atrium-8-sdi-tre-quarti-1000.jpg » Polk Atrium 8 SDI di tre quarti con la staffa ;; polk-atrium-8-sdi-retro-1000.jpg » Retro del Polk Atrium 8 SDI con i morsetti e il commutatore SDI", {"nota": "Dati dalla scheda Extrasound, ricavata dalla documentazione Polk.", "ds": True}),
 (37473, "Polk Audio", "Atrium Sat300", "singolo", "2 vie", ["medio-basso 8,9 cm Dynamic Balance", "tweeter 19 mm al neodimio"], "100 Hz – 22 kHz (−3 dB: 115 Hz – 20 kHz)", "83 dB (1 W / 1 m)", "8 Ω", "10 – 100 W", "IP66",
  ("140 mm", "178 mm", "213 mm"), "1,47 kg", ["Da giardino: picchetto con piastra di sicurezza, staffa a parete o sospensione.", "Mobile in polipropilene, griglia in alluminio, viteria inox; marrone verniciabile.", "Si abbina al subwoofer Atrium SUB100."], None,
  [["Scegli il punto", "Tra le piante o sotto una gronda, puntato verso la zona d'ascolto."], ["Fissa", "Pianta il picchetto con la piastra di sicurezza, oppure usa la staffa a parete o l'occhiello per la sospensione (dima inclusa)."], ["Porta i cavi", CAVO_EST], ["Collega", "Unisci il cavo con i connettori Faston o i morsetti a cappuccio inclusi, rispettando la polarità."], ["Orienta", "Ruota il diffusore verso la zona d'ascolto."], ["Chiudi", "Proteggi le giunzioni dall'acqua."]],
  [SAT], "diffusore-da-esterno-polk-atrium-300-br",
  "polk-atrium-sat300-tre-quarti-1000.jpg » Polk Atrium Sat300 marrone di tre quarti con la staffa ;; polk-atrium-sat300-picchetto-1000.jpg » Polk Atrium Sat300 sul picchetto da giardino ;; polk-atrium-sat300-sospeso-1000.jpg » Polk Atrium Sat300 montato in sospensione", {"posa": "giardino"}),
 (37718, "Polk Audio", "Atrium SUB100", "singolo", "subwoofer passivo", ["woofer 10″ (25,4 cm) a lunga escursione, rivolto verso il basso, doppia bobina 2″"], "", "", "doppia bobina", "200 W", "IPX66",
  ("428 mm", "279 mm", "428 mm"), None, ["Filtri passa-basso integrati.", "Cavo da interramento CL3 a 4 conduttori da 1 m; scatola di giunzione stagna inclusa.", "Terracotta o grigio, verniciabile."], None,
  [["Scegli il punto", "Tra le piante o a ridosso di un muretto: la posizione del subwoofer si sente poco."], ["Interra", "Interra il subwoofer secondo il manuale Polk, con la griglia in alluminio in alto."], ["Porta i cavi", CAVO_EST], ["Collega", "Collega il cavo a 4 conduttori nella scatola di giunzione stagna con i morsetti a cappuccio inclusi."], ["Collega i satelliti", "I filtri passa-basso sono integrati: il subwoofer si abbina ai satelliti Atrium Sat300."], ["Chiudi", "Chiudi la scatola di giunzione."]],
  [], "subwoofer-da-esterno-polk-atrium-sub-100",
  "polk-atrium-sub100-terracotta-grigio-1000.jpg » Polk Atrium SUB100 terracotta e grigio ;; polk-atrium-sub100-woofer-1000.jpg » Polk Atrium SUB100 visto dal basso con il woofer ;; polk-atrium-sub100-dotazione-1000.jpg » Polk Atrium SUB100 con la scatola di giunzione", {"nota": "Dati dalla scheda Extrasound. Sensibilità e impedenza non sono dichiarate; procedura di collegamento da verificare sul manuale Polk.", "posa": "giardino", "nocavi": True, "amp": "elac-is-amp8100"}),
 (57230, "Gallo", "Micro Habitat", "singolo", "una via, senza crossover", ["altoparlante 3″ impermeabile, cono in polipropilene e mica"], "100 Hz – 20 kHz (sito Gallo; il manuale indica 18 kHz)", "86 dB ±2 dB (1 m)", "8 Ω", "50 W a gamma intera, 100 W con crossover", "IP66, da −20 a +50 °C",
  ("Ø 100 mm", "Ø 100 mm", "sfera"), "745 g senza cavo", ["Sfera da 4″ in acciaio inox marino 316.", "Cavo impermeabile fisso, 2 m.", "Accessori Gallo: staffa a parete per esterni, picchetto da terreno."], None,
  passi("Fissa la staffa a parete Gallo per esterni con viti e tasselli adatti, oppure usa il picchetto da terreno.", "Unisci il cavo fisso da 2 m alla linea dell'amplificatore con una giunzione stagna, rispettando la polarità.", "Orienta la sfera verso la zona d'ascolto e blocca lo snodo.", "Proteggi la giunzione dall'acqua."),
  [], "gallo-micro-habitat-diffusore-da-esterno-ip66-in-acciaio-inox-singolo",
  "Gallo-Micro-Habitat-finiture-1000-1.jpg » Gallo Micro Habitat nelle finiture bianca, nera e acciaio ;; Gallo-Micro-Habitat-2-1000.jpg » Gallo Micro Habitat bianco su un muro sotto la pioggia ;; Gallo-Micro-Habitat-3-1000.jpg » Gallo Micro Habitat in acciaio con la staffa", {"nota": "Dati dalla scheda Extrasound, ricavata dal sito e dal manuale Gallo.", "amp": "yamaha-xda-qs5400rk", "sfera": "Ø 4″ (circa 100 mm)"}),
 (57238, "Gallo", "A'Diva Habitat", "singolo", "una via, senza crossover", ["altoparlante 3″ impermeabile, cono in polipropilene e mica"], "80 Hz – 22 kHz (sito Gallo; il manuale indica 20 kHz)", "85 dB ±2 dB (1 m)", "8 Ω", "50 W a gamma intera, 100 W con crossover", "IP66, da −20 a +50 °C",
  ("Ø 125 mm", "Ø 125 mm", "sfera"), "970 g senza cavo", ["Sfera da 5″ in acciaio inox marino 316.", "Cavo impermeabile fisso, 2 m.", "Accessori Gallo: staffa a parete per esterni, picchetto da terreno."], None,
  passi("Fissa la staffa a parete Gallo per esterni con viti e tasselli adatti, oppure usa il picchetto da terreno.", "Unisci il cavo fisso da 2 m alla linea dell'amplificatore con una giunzione stagna, rispettando la polarità.", "Orienta la sfera verso la zona d'ascolto e blocca lo snodo.", "Proteggi la giunzione dall'acqua."),
  [], "gallo-adiva-habitat-diffusore-da-esterno-ip66-in-acciaio-inox-singolo",
  "Gallo-ADiva-Habitat-finiture-1000-1.jpg » Gallo A'Diva Habitat nelle finiture bianca, nera e acciaio ;; Gallo-ADiva-Habitat-2-1000.jpg » Gallo A'Diva Habitat bianco a parete all'esterno ;; Gallo-ADiva-Habitat-3-1000.jpg » Gallo A'Diva Habitat in acciaio con la staffa", {"nota": "Dati dalla scheda Extrasound, ricavata dal sito e dal manuale Gallo.", "amp": "yamaha-xda-qs5400rk", "sfera": "Ø 5″ (circa 125 mm)"}),
 (47582, "Garvan", "SN120", "singolo", "omnidirezionale 360°, larga banda", ["altoparlante a larga banda da 200 mm"], "61 Hz – 12 kHz (−3 dB); 56 Hz – 15 kHz (−10 dB)", "93 dB", "8 Ω", "120 W AES (240 W continui)", "IP35, da −25 a +70 °C",
  ("Ø 260 mm", "622 mm", "Ø 260 mm"), "6,9 kg (polietilene), 28 kg (cemento)", ["Collezione Loto™; corpo in polietilene o cemento.", "Supporto e griglia in acciaio inox.", "Luce LED bianca o RGB opzionale.", "SPL massimo calcolato 126 dB."], None,
  [["Scegli il punto", "Al centro della zona da sonorizzare: il suono esce a 360°."], ["Prepara la base", "Piano stabile; per la versione in cemento (28 kg) prevedi il trasporto e la posa."], ["Porta i cavi", CAVO_EST], ["Collega", POL], ["Posiziona", "Appoggia il diffusore e verifica che sia in bolla."], ["Luce (opzionale)", "Con il LED opzionale porta anche l'alimentazione della luce secondo le istruzioni Garvan."]],
  [], "garvan-sn120-diffusore-da-giardino-360-120w",
  "Garvan-Loto-SN.jpg » Due Garvan SN120, uno bianco e uno in cemento grigio ;; Garvan-Loto-finiture-SN.jpg » Finiture del Garvan SN120 in polietilene e cemento ;; Garvan-Loto-Polietilene-griglia.jpg » Dettaglio della griglia in acciaio del Garvan SN120", {"nota": "Garvan non pubblica online la scheda tecnica: dati dalla scheda Extrasound.", "posa": "appoggio"}),
]


def cap(alt):
    a = alt.lower()
    for k, v in (("retro", "Retro"), ("morsetti", "Morsetti"), ("lato", "Lato"), ("staffa", "Con la staffa"), ("supporto", "Supporto"), ("griglia", "Con griglia"), ("orizzontale", "In orizzontale"), ("finiture", "Finiture"), ("piscina", "Installato"), ("giardino", "Installato"), ("muro", "Installato"), ("parete", "Installato"), ("picchetto", "Sul picchetto"), ("sospensione", "Sospeso")):
        if k in a:
            return v
    return "Vista"


def scheda(t):
    (id, b, mod, vend, sis, drv, risp, sens, imp, amp, ip, dim, peso, extra, staffa, pas, fonti, url, img, o) = t
    I = imgs(img)
    sub = "subwoofer" in sis
    tipo = "Subwoofer da esterno" if sub else ("Diffusore da giardino" if o.get("posa") in ("giardino", "appoggio") else "Diffusore da esterno")
    l, a, p = dim
    car = [f"{tipo}, {sis}.", *[d[0].upper() + d[1:] + "." for d in drv], f"Protezione: {ip}.", *extra, f"Venduto {'in coppia' if vend == 'coppia' else 'singolarmente'}."]
    acu = [x for x in [f"Risposta: {risp}." if risp else "", f"Sensibilità: {sens}." if sens else "", f"Impedenza: {imp}.", f"Amplificazione: {amp}."] if x]
    dimv = [f"Ingombro (L × A × P): {l} × {a} × {p}." if not o.get("sfera") else f"Sfera {o['sfera']}.", *( [f"Peso: {peso}."] if peso else []), *( [f"Montaggio: {staffa}."] if staffa else [])]
    mis = {"forma": "box", "l": l, "a": a, "p": p} if not o.get("sfera") else None
    if mis and staffa and "71 mm" in staffa:
        mis["staffa"] = "+71 mm"
    righe0 = f"{sis.split(',')[0]} · {' '.join(drv[0].split()[:3])}"
    z = o.get("z")
    v = []
    if o.get("ds"):
        v.append("Con il commutatore SDI su doppio ingresso un solo diffusore riceve sinistro e destro.")
    v.append(f"{imp}: un diffusore per canale.")
    v.append(f"Amplificazione: {amp}.")
    col = [{"titolo": "Amplificazione", "icona": "sorgente", "voci": v}]
    dove_voci = ["All'altezza delle orecchie o più in alto, inclinato verso la zona d'ascolto.", "Al riparo dalla pioggia diretta e dal sole pieno quando possibile: dura di più.", "Coppie a 2–3 m l'una dall'altra; per giardini grandi meglio più diffusori a volume basso."]
    if o.get("posa") in ("giardino", "appoggio"):
        dove_voci = ["Tra le piante o al centro della zona da sonorizzare.", "Per giardini grandi meglio più diffusori a volume basso che pochi ad alto volume."]
    dove = {"titolo": "Dove montarlo", "voci": dove_voci, "posa": {"tipo": "parete", "distanza": "spazio libero", "nota": "zona d'ascolto"}}
    sist = [dove, {"titolo": "Montaggio in 6 passi", "passi": pas}]
    if o.get("ds"):
        sist.append({"titolo": "Schema", "voci": ["Un solo diffusore riceve i due canali."], "zone": [{"label": f"{mod} · L + R", "tipo": "2"}], "apparecchio": "Amplificatore"})
    nota = (o.get("nota") or (("Dati dal " if fonti[0]["label"].startswith("manuale") else "Dati dalla ") + fonti[0]["label"] + ", confrontati con la scheda Extrasound.")) + (" " + o["diff"] if o.get("diff") else "")
    fs = f"Ingombro {l} × {a} × {p}" if not o.get("sfera") else f"Sfera {o['sfera']}"
    d = {"id": id, "tipo": "diffusore", "cat": "E", "tab": "Diffusori<br>da esterno", "brand": b, "model": mod, "crop": False,
         "meta": f"{b} {mod}: {tipo.lower()}, {sis}. Ingombro, staffa, collegamenti e montaggio per l'installatore.",
         "img": I[0], "chiave": [f"{sis.split(',')[0]} · {imp.split(' (')[0]}", fs, ip.split(',')[0].split(';')[0]], "righe": [righe0, tipo, b],
         "intro": [f"{'L' + chr(39) if b[0] in 'AEIOU' else 'Il '}<strong>{b} {mod}</strong> è un {tipo.lower()} {sis}: {', '.join(drv)}. {imp}, {ip.split(';')[0]}.",
                   (f"Ingombro <strong>{l} × {a} × {p}</strong>" + (f", {peso}" if peso else "") + (f"; {staffa}." if staffa else ".")) if not o.get("sfera") else f"Sfera <strong>{o['sfera']}</strong> in acciaio inox, {peso}."],
         "colonne": [{"titolo": "Caratteristiche", "voci": car}, {"titolo": "Acustica", "voci": acu}, {"titolo": "Dimensioni", "voci": dimv}],
         "viste": [vista(i, cap(i["alt"])) for i in I[1:4]], "misure": mis, "collega": col, "sistemi": sist, "nota": nota,
         "extrasound": X + url, "fonti": fonti, "lista": "esterno.html", "lista_label": "Da esterno", "tipo_label": tipo}
    if o.get("cavi"):
        d["cavi"] = o["cavi"]
    if o.get("amp"):
        d["amp"] = o["amp"]
    if o.get("nocavi"):
        d["cavi"] = None
    return salva(d)


if __name__ == "__main__":
    for t in M:
        print(scheda(t))
