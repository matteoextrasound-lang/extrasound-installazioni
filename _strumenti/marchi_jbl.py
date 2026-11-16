import sys; sys.path.insert(0,'_strumenti')
from schede_util import *
X='https://www.extrasound.it/'
STAGE_SPEC={"label":"scheda tecnica JBL Stage Architectural (rev. 2.0)","url":"https://kh.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw45c5fc7c/pdfs/Spec Sheet - JBL Stage Architectural - rev2.0 - 20220829.pdf"}
STAGE_INST={"label":"guida di installazione JBL Stage 2 Architectural","url":"https://kr.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw6dc95c94/pdfs/Install Guide - JBL Stage 2 Architectural - rev1.2 - 20221128-EN.pdf"}
S2_SPEC={"label":"scheda tecnica JBL Studio 2","url":"https://de.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw19140134/pdfs/Specification Sheet - JBL Studio 2 Series (English).pdf"}
S2_MAN={"label":"manuale JBL Studio 2 Architectural","url":"https://cdn.shopify.com/s/files/1/0055/9906/8206/files/jbl-studio2-architectural-user-manual.pdf"}
S6_SPEC={"label":"scheda tecnica JBL Studio 6","url":"https://cdn.shopify.com/s/files/1/0636/8224/8931/files/JBL_Studio6_series_Spec_Sheet_English.pdf"}
CON_MAN={"label":"manuale JBL Conceal Series","url":"https://be.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dwff8964cc/pdfs/JBL Conceal Series OM - EN.pdf"}
DA_MAN={"label":"manuale JBL DA850 / DA1650","url":"https://kh.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw862b484c/pdfs/OM-JBLDA850DA1650-EN.pdf"}
JCAV={"intestazione":"Lunghezza del cavo","righe":[["Fino a 15 m","16 AWG (circa 1,3 mm²)"],["Da 15 a 30 m","12 AWG (circa 3,3 mm²)"],["Oltre 30 m","10 AWG (circa 5,3 mm²)"]]}
def pStage(foro): return [
 ["Traccia il foro",f"Appoggia la dima e traccia il contorno: {foro}. Tienila alla stessa distanza dai montanti, così le gambe XL-2 si aprono del tutto; lascia almeno 19 mm tra dima e montanti."],
 ["Taglia","Taglia all'interno del tracciato con un seghetto per cartongesso. Spessore del pannello: da 13 a 51 mm, in grado di reggere il peso del diffusore."],
 ["Sicurezza e cavi","Aggancia il cavo di sicurezza a un montante tramite l'occhiello. Fai passare i cavi; collega l'amplificatore solo a impianto finito."],
 ["Collega","Spella 6,5 mm. Prima il nero (−), poi il rosso (+): premi il morsetto, infila, rilascia."],
 ["Fissa","Gambe XL-2 rientrate nel telaio; inserisci il diffusore, tienilo premuto contro la superficie e stringi le viti delle gambe. Non stringere troppo: si spanano le gambe."],
 ["Chiudi","Appoggia la griglia magnetica finché i magneti scattano. Distanza dall'isolante: 26 mm se non infiammabile, 78 mm se infiammabile."]]
def pS2(foro,ct="soffitto"): return [
 ["Verifica il vano",f"Controlla montanti, travi, tubi e condotte. Pannello da 13 a 51 mm; almeno 25,4 mm tra il bordo della dima e qualsiasi ostacolo."],
 ["Traccia e taglia",f"Segna il foro con la dima e taglia: {foro}."],
 ["Collega","+ sul morsetto rosso, − sul nero: premi, infila il filo, rilascia. Nessun trefolo deve toccare il telaio. Spegni l'impianto prima di installare."],
 ["Fissa","Le 4 staffe devono essere in posizione «pronta». Aggancia la linguetta antisismica a un cavo di sostegno, inserisci il diffusore dritto e stringi le viti sul frontale: le staffe ruotano e fanno presa. Fermati quando senti resistenza; usa una coppia bassa, mai stringere troppo."],
 ["Orienta e regola","Orienta il tweeter premendo sull'anello esterno (mai sulla membrana). Livello alti: + per stanze molto assorbenti, 0 nella maggior parte dei casi, − per stanze riflettenti o senza griglia."],
 ["Griglia","Per verniciarla togli la tela, spruzza una mano leggera tenendo liberi i fori, poi incolla una tela nuova (adesivo sulla griglia, mai sulla tela)."]]
def amp8(min_r=None):
    v=["8 Ω: un diffusore per canale su qualsiasi amplificatore da installazione, ad esempio JBL DA850 o DA1650."]
    if min_r: v.append(min_r)
    return {"titolo":"Amplificazione","link":"amplificatori.html","icona":"sorgente","voci":v}
def spk(id,model,cat,serie,righe0,tipo_r,intro,car,ac,dim,imgspec,views,urlx,fonti,misure,passi,dove,cavi=JCAV,posa=None,collega=None,nota=None,chiave=None,crop=False,extra_sys=[]):
    I=imgs(imgspec)
    d={"id":id,"tipo":"diffusore","cat":cat,"brand":"JBL","model":model,"crop":crop,
       "meta":f"JBL {model}: {righe0.lower()}, {tipo_r.lower()}. Foro, profondità, fissaggio e collegamenti per l'installatore.",
       "img":I[0],"chiave":chiave,"righe":[righe0,tipo_r,serie],"intro":intro,
       "colonne":[{"titolo":"Caratteristiche","voci":car},{"titolo":"Acustica","voci":ac},{"titolo":"Dimensioni","voci":dim}],
       "viste":[vista(I[i],c) for i,c in views],"misure":misure,"cavi":cavi,"collega":collega or [amp8()],
       "sistemi":[{"titolo":"Dove montarlo","voci":dove}|({"posa":posa} if posa else {})]+extra_sys+[{"titolo":"Montaggio","passi":passi}],
       "nota":nota or "Dati e procedura dai documenti ufficiali JBL, confrontati con la scheda Extrasound.","extrasound":X+urlx,"fonti":fonti}
    salva(d)
def ac(r,s,z,amp,xo=None,extra=[]):
    v=[f"Risposta: {r}.",f"Sensibilità: {s}.",f"Impedenza nominale: {z}.",f"Amplificazione consigliata: {amp}."]
    if xo: v.append(f"Frequenza di incrocio: {xo}.")
    return v+extra
