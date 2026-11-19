# Materiale didattico: intelligenza artificiale e dati

Percorso «Intelligenza artificiale e dati» per una classe prima di Informatica (corso quadriennale), IIS Copernico-Carpeggiani di Ferrara. Docente referente: Pietro Fabbri (A041).

**Si lavora con un solo file: [`index.html`](index.html).** Online: https://pietrofabbri.github.io/materiale-didattico-ai/

Il file contiene tutto: le slide delle cinque giornate, gli stili, i font, le immagini, il barattolo del rumore, i timer e i fogli dell'ora da stampare. Si può scaricare e aprire offline con Chrome o Edge.

## Il percorso

| Giornata | Ore 1 e 2 | Ora 3 (laboratorio) |
|---|---|---|
| 1 · La lingua come dati | Italiano: parole e frequenze, radice e desinenza, fatto e opinione | Un modello che genera frasi dalle frasi della classe |
| 2 · Incertezza e misura | Matematica: probabilità, media, deviazione standard, correlazione | Un calcolatore statistico sul foglio di calcolo |
| 3 · Il corpo come fonte di dati | Educazione fisica in aula: misure, errori di misura, raccolta anonima | Dai fogli di carta a dati puliti |
| 4 · Dai dati alle scoperte | Laboratorio: analisi dei dati, Teachable Machine | Preparazione di «Dentro la macchina», l'installazione della classe |
| 5 · Recupero o primo modello | Laboratorio, condotta dal docente di informatica | Classificatore a k vicini |

Ogni ora dura 40 minuti: avvio, attività, tre domande di controllo, consegna del foglio dell'ora. I gruppi cambiano a ogni giornata; il prodotto finale è della classe intera.

## Come si usa

1. Aprire `index.html` (online o scaricato). Il menu iniziale porta a ogni giornata e stampa i fogli dell'ora (A3 orizzontale, una copia per gruppo; consentire i popup).
2. Premere **B** e fare la taratura del barattolo del rumore.
3. Tasti: **frecce** avanti e indietro · **spazio** avvia o ferma il timer, e quando è finito avvia il successivo · **R** riavvia il timer · **N** note per il docente · **H** aiuto · **Home** torna al menu · **B T U M K** barattolo.

Il microfono funziona sicuramente dalla versione online (https). Aprendo il file scaricato, se il browser non concede il microfono: `python3 -m http.server 8017` nella cartella e poi `http://localhost:8017/`.

## Privacy

Nessun dato degli studenti, nessun nome e nessun audio viene salvato o trasmesso. Il barattolo misura solo il livello del suono, in memoria. Il sorteggio dei gruppi usa solo i numeri del registro.

## Come si modificano le slide

Ogni giornata si rivede come presentazione modificabile su claude.ai (tipo Slides). Quando è pronta, il deck si scarica in `artefatti/gN/project/` e `python3 sorgenti/unico.py` lo converte nelle slide di `index.html`, aggiungendo timer, barattolo, note e sorteggio. Le impostazioni di ogni slide stanno nella **prima riga delle note**, in questa forma (si possono cambiare a mano nell'editor):

```
IMPOSTAZIONI: rumore=discussione | fase=gruppo | timer=300 Contare; 180 R2 | logica=sorteggio
```

`rumore` = silenzio, discussione o spento (barattolo) · `fase` = solo, gruppo o tutti · `timer` = secondi e nome di ciascun timer, separati da punto e virgola · `logica=sorteggio` = la slide del sorteggio dei gruppi. Le giornate non ancora rivedute vengono dal generatore (`sorgenti/giornataN.py`).

Stato: giornata 1 dal deck; giornate 2-5 dal generatore.

## Struttura e rigenerazione

| Cartella | Contenuto |
|---|---|
| `sorgenti/` | Il generatore: `g.py` (tipi di slide), `giornata1.py` … `giornata5.py` (contenuti), `unico.py` (costruisce `index.html`) |
| `comune/` | Motore delle slide (`motore.js`), stile (`stile.css`); barattolo del rumore, palette e font Atkinson Hyperlegible dal repository [progetto-16](https://github.com/pietrofabbri/progetto-16) |
| `artefatti/` | I deck delle giornate rivedute su claude.ai (`gN/project/`); `sorgenti/artefatto.py` crea un deck dal generatore, `sorgenti/da_artefatto.py` lo riconverte |
| `img/`, `dati/` | Grafici di «Indovina r» (giornata 2) e dati dei frutti (giornata 5) |

Per modificare il contenuto: cambiare `sorgenti/giornataN.py`, poi `cd sorgenti && python3 unico.py`, che riscrive `index.html`. Il font Atkinson Hyperlegible è distribuito con licenza SIL Open Font License.

## Giornata 1, versione 2 (15/11/2026)

- La giornata 1 è scritta con `sorgenti/g2.py` + `sorgenti/giornata1.py` (la v1 resta in `giornata1_v1.py`): ogni funzione produce direttamente una slide del deck. `python3 sorgenti/artefatto2.py 1` scrive il deck in `artefatti/g1/project/` con lo stile `sorgenti/stile_deck.css`.
- Ogni slide ha un'**importanza**, nella riga IMPOSTAZIONI: `importanza=essenziale | consigliata | facoltativa`. Nell'HTML compare nella **barra dell'ora** in basso (blu essenziale, ambra consigliata, grigio facoltativa: si può saltare); un clic su un segmento porta a quella slide. Nel deck la stessa informazione è la striscia colorata in fondo alla slide.
- Nuovi blocchi: riquadro «Ricorda» (richiamo di un concetto non banale), tasselli di parole, catene di coppie, barre di probabilità, animazioni brevi all'apertura della slide.
- Palette (19/11): carta #F5F1E8 a puntini, inchiostro #22192F, notte #1E1630, petrolio #0E7C7B (essenziale), zafferano #F4A259 (consigliata), corallo #F25C54, muschio #5B8E4F, lilla #7B6CD9, magenta #B5487A; lilla grigio #CFC8D9 (facoltativa). Le slide non nominano le materie: si indica solo «in aula» o «in laboratorio».
