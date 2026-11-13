# Manutenzione del sito Custom Installation di Extrasound

Questa cartella non viene pubblicata (GitHub Pages ignora le cartelle che iniziano con "_").

## Cos'è il sito

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
