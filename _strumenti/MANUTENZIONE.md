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
