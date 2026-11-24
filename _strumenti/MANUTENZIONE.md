# Manutenzione del sito Custom Installation di Extrasound

Questa cartella non viene pubblicata (GitHub Pages ignora le cartelle che iniziano con "_").

## Cos'è il sito

- **Pubblico: installatori, non clienti finali.** Niente slogan né frasi promozionali: titoli = nome del prodotto, testi tecnici e asciutti. Vale per tutto ciò che si struttura senza istruzioni precise.

- Vetrina dei servizi di custom installation hi-fi e home cinema di Extrasound Srl (Via Archimede 605, Cesena).
- Il venditore è sempre Extrasound: ogni richiesta di preventivo o sopralluogo arriva a Extrasound.
- Sito gemello per metodo: fabrizioberlati.com (repository matteoextrasound-lang/fabrizioberlati).

## Pubblicazione

- Si lavora sul ramo `bozza`; su `main` (sito pubblico) solo quando Extrasound dice "pubblica".
- Indirizzo provvisorio: matteoextrasound-lang.github.io/extrasound-installazioni (GitHub Pages).
- Il dominio definitivo verrà aggiunto più avanti con un file `CNAME`.
- Link interni sempre relativi (`./`, `contatti.html`), mai con "/" iniziale né `index.html`: così funzionano sia sull'indirizzo provvisorio sia sul dominio definitivo.
- Title fino a ~60 caratteri, meta description fino a 160.

## Modulo di richiesta preventivo

- Il modulo è una pagina WordPress su extrasound.it (Elementor Pro, modello pagina vuota) incorporata nella pagina Contatti di questo sito.
- Le email partono da WordPress verso gli indirizzi di Extrasound. Consenso privacy con link all'informativa di Extrasound; testo da far controllare al consulente privacy.
- Se extrasound.it impedisce l'incorporamento, autorizzare solo il dominio di questo sito (modifica da approvare) oppure aprire il modulo in una pagina di extrasound.it con la stessa grafica.
- Campi proposti: nome, email, telefono, città, tipo di progetto, stato dei lavori, budget a fasce, sopralluogo sì/no, note.

## Regole Extrasound valide anche qui

- Dati tecnici solo da fonti ufficiali del produttore.
- Informazioni non confermate scritte come **[DA CONFERMARE: …]**, mai inventate.
- Link verso extrasound.it in nuova scheda.

## Struttura del sito (13/11)

- Pagine: `index.html` (home), `amplificatori.html`, `diffusori.html`, `contatti.html`.
- Header e footer sono uguali in tutte le pagine e **non si modificano a mano**: si cambiano in `_strumenti/build.py` e si lancia `python3 _strumenti/build.py`. Una pagina nuova va aggiunta alla lista `PAGES` (e a `PRODOTTI` se sta sotto il menu Prodotti).
- Stile in `assets/css/site.css`, animazioni in `assets/js/site.js`. Quando si modificano, alzare il numero `?v=` nei link delle pagine.
- Contenuto centrato con larghezza massima 1200 px (`--max`); le sezioni prodotto sono fasce bianche a tutta larghezza, una attaccata all'altra.
- Footer con i dati legali di Extrasound Srl presi da extrasound.it (P.IVA, REA, capitale sociale): se cambiano lì, aggiornarli in `build.py`.
- Le foto per ora sono collegate da extrasound.it (`wp-content/uploads`).

## Modulo preventivo su extrasound.it

- Pagina WordPress 64517 «Modulo richiesta preventivo – Extrasound Custom», modello Elementor Canvas, noindex. Indirizzo: https://www.extrasound.it/modulo-richiesta-preventivo-extrasound-custom
- Modulo Elementor Pro: invio a info@extrasound.it (mittente email@extrasound.it, risposta all'email del cliente) e copia in Elementor → Invii. Antispam honeypot, consenso privacy obbligatorio.
- Pagina pubblicata il 13/11, noindex/nofollow (Yoast), non presente nei menu.
- La pagina nasconde con il CSS personalizzato di Elementor: sigillo Trusted Shops, banner CookieYes, chat Oct8ne, carrello FunnelKit, popup Klaviyo e popup Elementor.
- L'utente WordPress di Matteo non può salvare script (WordPress li toglie): niente JavaScript nella pagina del modulo.
- Altezza della cornice fissa in `site.css` (`.es-form`, 1120 px): se si aggiungono o tolgono campi, rimisurarla.

## Schede prodotto tecniche (struttura da catalogo, 13/11)

- Modello: `amplificatori.html` (ELAC IS-AMP8100). Parte 1 «il prodotto»: linguetta rossa di categoria, foto grande, marca/modello/righe, introduzione, tre colonne Caratteristiche · Ingressi · Uscite, pannello posteriore. Parte 2 (sfondo grigio chiaro) «cosa si può fare»: colonna «Cosa si collega» + due schemi d'impianto in SVG con zone e watt. Chiusura con preventivo e fonti.
- Classi CSS: `.sheet`, `.sheet-page`, `.cat-tab`, `.model`, `.sheet-cols`, `.col`, `.ticks`, `.acc`, `.system`, `.diagram`. Gli elementi `.reveal` compaiono scorrendo (site.js).
- Titoli in Barlow Condensed (`--display`); il logo resta in Anton (`--logo`).
- Dati IS-AMP8100: sito ELAC dice «fino a 100 W per canale» e bridge 200 W; il manuale 2019 dice 75 W RMS a tutti i canali e bridge 150 W RMS su 8 Ω. In pagina: «fino a 100 W per canale; 75 W RMS con tutti i canali in funzione» e bridge 150 W RMS (dato più prudente).
- Scheda diffusore (`diffusori.html`, ELAC IW-V62): stessa parte 1 (Caratteristiche · Acustica · Dimensioni + 4 viste), parte 2 dedicata al montaggio: disegno quotato, tabella cavi, abbinamento con l'IS-AMP8100, «Dove montarlo» e «Montaggio in 6 passi», tutto dal manuale ELAC Vertex II.
- Pulsanti: in home ogni prodotto ha «Richiedi un preventivo» + «Scheda tecnica» (porta alla scheda interna, `pagina.html#id-prodotto`). Il link a extrasound.it c'è solo in fondo alle schede, come pulsante «Acquista su Extrasound» (nuova scheda).

## GitHub Pages (16/11)

- Attivo dal 16/11 su https://matteoextrasound-lang.github.io/extrasound-installazioni/ e, per ora, pubblica il ramo `bozza` (scelta di Extrasound per vedere il sito in costruzione). Ogni salvataggio su `bozza` va online in 1–2 minuti.
- Quando il sito sarà pronto: unire `bozza` in `main`, impostare Pages su `main`, togliere `noindex` dalle pagine e aggiungere il dominio definitivo (`CNAME`).

## Schede prodotto (16/11/2026)
- 173 schede, una per prodotto custom di extrasound.it (inventario in `_dati/inventario.json`, campo `stato`).
- Ogni marchio ha il suo script in `_strumenti/marchi_*.py` che scrive i JSON in `_dati/prodotti/`; poi `python3 _strumenti/genera_schede.py && python3 _strumenti/build.py`.
- Dati dalle fonti ufficiali del produttore (elencate in fondo a ogni scheda); dove mancano si usa la scheda Extrasound e la scheda lo dice. Le differenze con Extrasound sono scritte nella nota della scheda («Fa fede il dato …»).
- Garvan non pubblica online le schede dei singoli modelli: dati dalla scheda Extrasound.
- Slug uguali: impostare `slug` a mano (es. Rotel C8+ → `rotel-c8-plus`).

## Struttura unica delle schede (17/11/2026)
- Modelli: `scheda-elac-is-amp8100.html` (amplificatori) e `scheda-elac-vertex-ii-iw-v62.html` (diffusori).
- `_strumenti/uniforma.py` porta ogni scheda alla stessa struttura in fase di generazione: colonne fisse, misure, sezione cavi (calcolata se il produttore non la dà), amplificatore/diffusore consigliato con foto e link, «Dove montarlo», «Montaggio in 6 passi», due configurazioni con grafiche, interfaccia e pannello posteriore per gli amplificatori.
- Nuove categorie: `esterno.html` (cat E, `marchi_esterno.py`, Garvan KR16M in `marchi_garvan.py`) e `home-cinema.html` (cat H, `marchi_homecinema.py`).
- Esclusi: Biamp MASK2 (ex-demo), German Maestro (marini per barche).

## Struttura prodotti (dal 17/11/2026)
- Due elenchi: `elettroniche.html` (tutti gli amplificatori: cat M e H) e `diffusori.html` (tutti i diffusori, da esterno compresi).
- `amplificatori.html`, `esterno.html`, `home-cinema.html` sono solo rimandi per i vecchi link.
- Diffusori ed elettroniche divisi per collegamento (per le elettroniche: tipo di uscita): dizionario `LINEA` in `genera_schede.py` (Z impedenza, V tensione costante 70/100 V, ZV entrambi). Default Z. Un nuovo diffusore 70/100 V va aggiunto lì, con la fonte del produttore nel commento.
- Filtri preselezionabili da indirizzo: `diffusori.html#linea=V`, `diffusori.html#cat=E`, `elettroniche.html#cat=H`.
- Logo: immagine `logo-rosso-bianco-extrasound.png` di extrasound.it + "B2B" (costante `LOGO` in `build.py`).

## Lista prodotti B2B (dal 24/11/2026)
- Ogni card e ogni scheda ha "Aggiungi alla lista" (attributo `data-add`); gli impianti tipo hanno "Aggiungi l'impianto alla lista" (`data-add-set`).
- La lista sta nel browser dell'utente (localStorage `esb2b-lista`) e appare in basso a destra (codice in fondo a `assets/js/site.js`).
- "Richiedi preventivo" porta a `richiesta.html` (modulo in `assets/js/richiesta.js`), che invia a
  `https://www.extrasound.it/wp-json/extrasound-b2b/v1/richiesta`.
- L'endpoint è lo snippet Code Snippets n. 45 "B2B - Ricezione liste prodotti" (copia in `_strumenti/wp-snippet-richieste-b2b.php`):
  salva la richiesta in Bacheca > Richieste B2B, manda email a info@extrasound.it e una copia al cliente.
- Se l'endpoint non risponde, la pagina propone un'email precompilata a info@extrasound.it.

## Pulsante "Extrasound B2B" su extrasound.it (dal 24/11/2026)
- Voce di menu id 68589 nel "Secondary Menu" (Aspetto > Menu), classe CSS `es-b2b`, nuova scheda, rel nofollow.
- Stile nello snippet Code Snippets n. 46 "CSS - Testata: icone menu e pulsante Extrasound B2B" (stampa uno <style> in wp_head):
  da computer voce rossa con valigetta, da telefono pillola rossa "B2B" tra logo e carrello.
- Le icone di "Account cliente" e "Carrello" ora sono disegnate dallo stesso snippet: salvando il menu da questo account
  WordPress toglie gli SVG dai titoli delle voci. Non rimettere SVG nei titoli; se si disattiva lo snippet 46 le icone spariscono.
- Snippet n. 45 (ricezione liste) attivo dal 24/11/2026. Prova: richiesta B2B-68590 "TEST Claude – ignorare".
