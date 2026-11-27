"""Costruisce guida.html: guida interattiva per i docenti (un solo file, immagini incorporate)."""
import base64, html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contenuti import ORE, GLOSSARIO

SHOTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "immagini") + "/"
def img(nome, alt):
    b = base64.b64encode(open(SHOTS + nome + ".webp", "rb").read()).decode()
    return f'<img src="data:image/webp;base64,{b}" alt="{html.escape(alt)}" loading="lazy">'

RUOLI = {"it": "Italiano", "ma": "Matematica", "ef": "Educazione fisica", "in": "Informatica"}

def piu(titolo, corpo, aperto=False):
    return f'<details class="piu"{" open" if aperto else ""}><summary>{titolo}</summary><div class="piu-c">{corpo}</div></details>'

S = []  # schermate: (id, sezione, titolo menu, ruoli, html)
def schermata(sid, sez, menu, corpo, ruoli=("tutti",)):
    S.append((sid, sez, menu, list(ruoli), corpo))

# ---------------------------------------------------------------- PROGETTO
schermata("inizio", "Il progetto", "Benvenuti", f"""
<p class="occhiello">Intelligenza artificiale e dati · Classe 1P</p>
<h1>Guida per i docenti</h1>
<p class="lead">Tutto ciò che serve per condurre le ore, in poche schermate.<br>Il testo essenziale è sempre visibile; i dettagli si aprono con un clic.</p>
<div class="scelta">
  <p class="et">Per iniziare, indicare la propria materia:</p>
  <div class="ruoli">
    <button data-ruolo="it">Italiano</button><button data-ruolo="ma">Matematica</button>
    <button data-ruolo="ef">Educazione fisica</button><button data-ruolo="in">Informatica</button>
    <button data-ruolo="tutti" class="sec">Vedo tutto</button>
  </div>
  <p class="nota">La scelta evidenzia nel menu le ore che riguardano la propria materia. Si può cambiare in qualsiasi momento.</p>
</div>
<div class="come">
  <span><kbd>→</kbd> schermata successiva</span><span><kbd>←</kbd> precedente</span><span><b class="mini-piu">+</b> apre un approfondimento</span>
</div>""")

schermata("idea", "Il progetto", "L'idea", f"""
<p class="occhiello">Il progetto in una frase</p>
<blockquote class="grande">Una macchina non sa che cosa è vero.<br>Sa soltanto che cosa è <em>frequente</em> nei dati che ha ricevuto.</blockquote>
<p class="lead">In quattro giornate la classe fa ciò che fanno i sistemi di intelligenza artificiale: <b>raccoglie dati, li conta, sceglie il più probabile</b>. Con le proprie mani e con i propri dati.</p>
{piu("Perché è importante", "<p>Gli studenti usano già chatbot e sistemi di raccomandazione. Capire come funzionano dall'interno permette loro di valutarne le risposte invece di subirle.</p><p>Ne derivano due conseguenze educative: <b>la qualità dei dati è decisiva</b>; <b>le risposte di una macchina vanno sempre verificate</b>.</p>")}
{piu("Che cosa sanno fare gli studenti alla fine", "<ul><li>contare e misurare con metodo</li><li>distinguere un fatto da un'opinione</li><li>leggere una probabilità</li><li>riconoscere un errore di misura</li><li>proteggere i propri dati personali</li></ul>")}
{piu("Il ruolo delle materie", "<p>I contenuti disciplinari sono <b>cenni funzionali alle attività</b>, non lezioni formali. Prima del percorso è prevista una riunione preparatoria di circa 30 minuti.</p>")}
""")

TESSERE = [
 (1, "La lingua come dati", "Una macchina che scrive", "it", "Italiano · Italiano · Laboratorio"),
 (2, "Incertezza e misura", "Una macchina che stima", "ma", "Matematica · Matematica · Laboratorio"),
 (3, "Il corpo come fonte di dati", "I dati di partenza", "ef", "Ed. fisica · Ed. fisica · Laboratorio"),
 (4, "Dai dati alle scoperte", "Una macchina che impara", "in", "Laboratorio · Laboratorio · Laboratorio"),
 (5, "Recupero o primo modello", "Facoltativa", "in", "Laboratorio, se la classe è in pari"),
]
tess = "".join(f'<a class="tessera r-{r}" href="#{"g5" if n == 5 else f"g{n}o1"}"><span class="n">{n}</span><b>{t}</b><span>{s}</span><small>{o}</small></a>' for n, t, s, r, o in TESSERE)
schermata("giornate", "Il progetto", "Le cinque giornate", f"""
<p class="occhiello">La struttura</p>
<h2>Cinque giornate, tre ore ciascuna</h2>
<p class="lead">Le prime due ore in aula, la terza in laboratorio. La quinta giornata è facoltativa.</p>
<div class="tessere">{tess}</div>
<p class="nota">Cliccando una giornata si apre la sua prima ora.</p>
{piu("Che cosa aggiunge ogni giornata", "<ol><li><b>Le parole:</b> la macchina sceglie la parola più probabile, non quella vera.</li><li><b>I numeri:</b> probabile non significa certo; una stima non è la verità.</li><li><b>Le misure:</b> dati affidabili nascono da misure fatte bene.</li><li><b>I modelli:</b> la macchina impara dagli esempi e sbaglia dove mancano.</li><li><b>Recupero o primo modello:</b> un classificatore costruito dalla classe.</li></ol>")}
""")

CONTRIB = {
 "it": ("La porta d'ingresso", "Le due ore mostrano che la lingua, per una macchina, è fatta di parole da contare. Le 48 frasi scritte dai gruppi diventano i dati del primo modello della classe.", "it"),
 "ma": ("Il linguaggio dell'incertezza", "Probabilità, media, deviazione standard e correlazione servono poi per controllare e analizzare le misure della classe.", "ma"),
 "ef": ("I dati veri del percorso", "Le prove motorie producono il dataset della classe e mostrano, sul proprio corpo, come si impara per tentativi.", "ef"),
 "in": ("Dalle idee alle macchine", "La terza ora di ogni giornata trasforma il lavoro in aula in dati e modelli funzionanti; la giornata 4 tira le fila.", "in"),
}
carte = "".join(f'<div class="carta r-{r}"><p class="tag">{RUOLI[k]}</p><h3>{t}</h3><p>{d}</p></div>' for k, (t, d, r) in CONTRIB.items())
schermata("contributo", "Il progetto", "Il contributo di ognuno", f"""
<p class="occhiello">Chi fa che cosa</p>
<h2>Il contributo di ogni docente</h2>
<div class="carte">{carte}</div>
{piu("La presenza dei colleghi", "<p>È <b>facoltativa</b>: il docente di informatica può condurre tutte le ore. Un collega presente arricchisce le proprie due ore con esempi della sua materia, senza preparare nulla di nuovo.</p>")}
""")

schermata("ora-tipo", "Il progetto", "Com'è fatta un'ora", f"""
<p class="occhiello">Ogni ora, sempre uguale</p>
<h2>40 minuti progettati, più un margine</h2>
<div class="linea-ora">
  <div style="flex:3" class="f1"><b>Apertura</b><span>3 min</span></div>
  <div style="flex:30" class="f2"><b>Attività</b><span>30 min</span></div>
  <div style="flex:3" class="f3"><b>Controllo</b><span>3</span></div>
  <div style="flex:4" class="f4"><b>Chiusura</b><span>4</span></div>
  <div style="flex:8" class="f5"><b>Margine</b><span>5-10 min</span></div>
</div>
<p class="lead">Il modulo orario è più lungo di 40 minuti: restano sempre <b>5-10 minuti</b> per domande e rallentamenti, senza saltare attività.</p>
{piu("Ogni attività segue la stessa sequenza", "<ol><li>consegna</li><li>con chi si lavora (da soli, nel gruppo, tutti)</li><li>dove si scrive (il riquadro del foglio)</li><li>un esempio svolto</li><li>il timer</li><li>la soluzione</li></ol>")}
{piu("Il foglio dell'ora", "<p>Un foglio A3 per gruppo, diviso in riquadri numerati R1, R2… La slide mostra una piccola mappa del foglio con il riquadro da usare evidenziato. L'ultimo riquadro è sempre il controllo finale. Il foglio si consegna a fine ora.</p>")}
{piu("I gruppi", "<p>Sei gruppi di 4-5 studenti, <b>nuovi in ogni giornata</b>, estratti dalle slide con i numeri del registro. Nessun ruolo fisso: tutti fanno tutto.</p>")}
""")

schermata("regole", "Il progetto", "Le regole", f"""
<p class="occhiello">Tre regole, sempre</p>
<h2>Le regole del percorso</h2>
<div class="regole">
  <div><span class="ico">◉</span><b>Privacy</b><p>Mai nomi: solo numeri del gruppo o codici anonimi.</p></div>
  <div><span class="ico">≠</span><b>Nessuna classifica</b><p>I dati servono a imparare a misurare, non a confrontare le persone.</p></div>
  <div><span class="ico">✕</span><b>Nessun chatbot</b><p>Gli studenti non usano chatbot nelle attività.</p></div>
</div>
{piu("Privacy nel dettaglio", "<ul><li>Non si raccolgono peso, altezza o informazioni sulla salute.</li><li>Nei modelli non si usano volti o corpi.</li><li>Nessun dato degli studenti viene caricato su servizi esterni.</li><li>I risultati si mostrano solo in forma aggregata.</li></ul>")}
""")

# ---------------------------------------------------------------- SLIDE
schermata("aprire", "Le slide", "Aprire le slide", f"""
<p class="occhiello">Le slide · 1</p>
<h2>Aprire le slide in quattro passi</h2>
<ol class="passi">
  <li><b>Aprire Chrome o Edge</b> e andare al <a href="https://pietrofabbri.github.io/materiale-didattico-ai/" target="_blank" rel="noopener">sito delle slide</a>.</li>
  <li><b>Premere F11</b> per lo schermo intero (F11 di nuovo per uscire).</li>
  <li><b>Scegliere la giornata</b> nel menu e cliccare «Apri le slide».</li>
  <li><b>Consentire il microfono</b> se il browser lo chiede.</li>
</ol>
{piu("Vedere il menu iniziale", img("menu", "Il menu iniziale delle slide"))}
{piu("Che cosa serve", "<ul><li>Un computer collegato al proiettore o alla lavagna interattiva.</li><li>Il browser Chrome o Edge: il programma con cui si aprono le pagine internet. Firefox e Safari sono sconsigliati.</li><li>Un microfono: quello del portatile basta.</li><li>Nulla da installare.</li></ul>")}
{piu("Senza internet", "<p>Si può aprire con un doppio clic il file <code>index.html</code>, scaricabile dallo stesso sito: le slide funzionano anche offline. In questo caso alcuni browser non concedono il microfono: il barattolo resta spento, il resto funziona.</p>")}
{piu("Il microfono è sicuro?", "<p>Sì. Misura soltanto il <b>volume</b> dell'aula, istante per istante. Nessun suono viene registrato o salvato.</p>")}
""")

LEG = [("1", "Modalità di lavoro", "da soli, nel gruppo, tutti insieme"),
       ("2", "Timer", "il tempo che resta e il nome dell'attività"),
       ("3", "Barattolo del rumore", "il volume della classe"),
       ("4", "Barra dell'ora", "le slide dell'ora e la loro importanza"),
       ("5", "Numero della slide", "rispetto al totale del file"),
       ("6", "Contenuto", "la consegna, il testo, l'esempio")]
leg = "".join(f'<li><span class="num">{n}</span><b>{t}</b> · {d}</li>' for n, t, d in LEG)
schermata("schermo", "Le slide", "Che cosa si vede", f"""
<p class="occhiello">Le slide · 2</p>
<h2>Che cosa si vede sullo schermo</h2>
<div class="due"><div class="fig">{img("schermo", "Una slide di attività con gli strumenti numerati")}</div><ol class="legenda">{leg}</ol></div>
{piu("La barra dell'ora, in dettaglio", "<p>Un segmento per ogni slide dell'ora. A sinistra «Ora 1 · 8/19»: ora e posizione. Il segmento più alto è la slide attuale; quelli sbiaditi sono già stati visti. Cliccando un segmento si va a quella slide.</p><div class='imp'><span class='e'>essenziale</span><span class='c'>consigliata</span><span class='f'>facoltativa: si può saltare</span></div>")}
""")

TASTI = [("→", "avanti"), ("←", "indietro"), ("spazio", "avvia o ferma il timer"), ("N", "note per il docente")]
tasti = "".join(f'<div class="tasto"><kbd>{k}</kbd><span>{d}</span></div>' for k, d in TASTI)
ALTRI = [("Pag giù / telecomando", "come la freccia destra"), ("R", "riporta il timer all'inizio"), ("H", "aiuto con l'elenco dei tasti"),
         ("Home", "torna al menu iniziale"), ("B", "accende e spegne il barattolo"), ("T", "taratura del barattolo"),
         ("U oppure Esc", "sblocca subito lo schermo"), ("M", "modalità del barattolo solo per questa slide"), ("K", "disattiva il blocco per tutta la lezione")]
altri = "".join(f"<tr><td><kbd>{k}</kbd></td><td>{d}</td></tr>" for k, d in ALTRI)
schermata("tasti", "Le slide", "I tasti", f"""
<p class="occhiello">Le slide · 3</p>
<h2>Quattro tasti bastano</h2>
<div class="tasti">{tasti}</div>
<p class="lead">La freccia destra fa comparire anche le <b>risposte nascoste</b>: prima la domanda, poi la risposta.</p>
{piu("Vedere una risposta nascosta", img("risposta", "La stessa slide prima e dopo la freccia destra"))}
{piu("Tutti gli altri tasti", f"<table class='t'>{altri}</table><p class='nota'>Se un tasto non fa nulla, cliccare una volta sulla slide e riprovare.</p>")}
{piu("Le note per il docente (N)", "<p>Contengono minuti, che cosa dire e soluzioni. Sono visibili anche alla classe se lo schermo è proiettato: conviene leggerle prima della lezione o aprirle per un istante.</p>")}
""")

schermata("barattolo", "Le slide", "Il barattolo del rumore", f"""
<p class="occhiello">Le slide · 4</p>
<h2>Il barattolo del rumore</h2>
<p class="lead">Un vaso di brillantini sul lato destro dello schermo: <b>si agita quando la classe alza la voce</b>. Si regola da solo su ogni slide.</p>
<div class="stati"><div class="s1"><b>Calma</b><span>verde, brillantini sul fondo</span></div><div class="s2"><b>Attenzione</b><span>giallo, brillantini agitati</span></div><div class="s3"><b>Blocco</b><span>lo schermo si ferma</span></div></div>
{piu("Vedere i tre stati", img("barattolo", "I tre stati del barattolo"))}
{piu("Il blocco, in dettaglio", "<p>Se il volume resta oltre il limite per circa 3 secondi, il barattolo copre lo schermo con la scritta «Smetti di parlare. Appoggia quello che hai in mano.» e suona una campana. Riparte da solo dopo circa <b>10 secondi di silenzio</b>. Tra due blocchi passano almeno 60 secondi.</p><p><kbd>U</kbd> o <kbd>Esc</kbd> sbloccano subito; <kbd>K</kbd> disattiva il blocco per tutta la lezione.</p>")}
{piu("Le tre modalità", "<ul><li><b>Spento:</b> durante le spiegazioni del docente, così la sua voce non lo fa reagire.</li><li><b>Silenzio:</b> lavoro individuale e controllo; limite basso.</li><li><b>Discussione:</b> lavoro di gruppo; limite più alto.</li></ul>")}
{piu("La taratura: 2 minuti all'inizio di ogni giornata", "<ol><li>Premere <kbd>B</kbd>: si apre il pannello.</li><li>Silenzio assoluto, poi «1 · Misura il silenzio» (5 secondi).</li><li>Gruppi che parlano a voce normale, poi «2 · Misura una discussione normale» (5 secondi).</li><li>«Salva e chiudi». Tutto il resto si lascia com'è.</li></ol>" + img("taratura", "Il pannello di taratura"))}
""")

schermata("altro", "Le slide", "Timer, gruppi, stampa", f"""
<p class="occhiello">Le slide · 5</p>
<h2>Timer, gruppi e fogli</h2>
<div class="carte">
 <div class="carta"><h3>Il timer</h3><p>Non parte da solo: si avvia con la <kbd>barra spaziatrice</kbd> dopo la consegna e l'esempio.</p></div>
 <div class="carta"><h3>Il sorteggio</h3><p>Nella quarta slide di ogni giornata: si scrivono gli assenti e si clicca «Sorteggia».</p></div>
 <div class="carta"><h3>I fogli dell'ora</h3><p>Dal menu, «Stampa i fogli dell'ora»: A3 orizzontale, 6 copie per ora.</p></div>
</div>
{piu("Il timer, in dettaglio", "<p>Il cerchio si svuota man mano che il tempo passa. Una slide può avere più timer in sequenza («1 di 2»): finito il primo, la barra spaziatrice avvia il secondo. Se il barattolo blocca lo schermo, il timer si ferma. Il timer è un riferimento, non un obbligo.</p>")}
{piu("Il sorteggio, in dettaglio", "<p>Nel campo «Assenti» si scrivono i numeri del registro, separati da virgole (ad esempio 4, 17). Compaiono sei gruppi colorati con i numeri dei componenti, mai i nomi. Ogni gruppo raggiunge i banchi del proprio colore.</p>")}
{piu("Se la stampa non parte", "<p>Il browser può bloccare la finestra di stampa: consentire le finestre a comparsa (popup) per la pagina e riprovare.</p>")}
""")

# ---------------------------------------------------------------- ORE
def ora_html(k, o):
    tot = 40
    seg = "".join(f'<a class="seg" href="#{k}-{i}" style="flex:{max(b - a, 2)}" title="{html.escape(t)}"><span>{a}-{b}</span></a>' for i, (a, b, t, r, d) in enumerate(o["att"]) if o["ora"])
    att = ""
    for i, (a, b, t, r, d) in enumerate(o["att"]):
        righe = "".join(f'<div class="riga"><span class="k">{kk}</span><span>{vv}</span></div>' for kk, vv in d["r"])
        tempo = f"{a}-{b}′" if o["ora"] else ""
        rq = f'<span class="rq">{r}</span>' if r not in ("—", "") else ""
        att += f'<details class="att" id="{k}-{i}"><summary><span class="min">{tempo}</span><b>{t}</b>{rq}</summary><div class="att-c">{righe}</div></details>'
    sa = "".join(f"<li>{x}</li>" for x in o["sa"])
    ruolo = " · ".join(RUOLI[r] for r in o["ruoli"])
    testa = f'Giornata {o["giornata"]}' + (f' · Ora {o["ora"]}' if o["ora"] else "") + f' · {o["luogo"]}'
    return f"""
<p class="occhiello">{testa}<span class="chip r-{o['ruoli'][0]}">{ruolo}</span></p>
<h2>{o['titolo']}</h2>
<p class="lead">{o['obiettivo']}</p>
{f'<div class="scaletta">{seg}</div>' if o['ora'] else ''}
<div class="attivita">{att}</div>
{piu("Che cosa sa fare lo studente alla fine dell'ora", f"<ul>{sa}</ul>")}
"""

TITOLI_G = {1: "Giornata 1", 2: "Giornata 2", 3: "Giornata 3", 4: "Giornata 4", 5: "Giornata 5"}
for k, o in ORE.items():
    menu = (f"Ora {o['ora']} · " if o["ora"] else "") + o["titolo"]
    schermata(k, TITOLI_G[o["giornata"]], menu, ora_html(k, o), o["ruoli"])

# ---------------------------------------------------------------- PREPARAZIONE
PREP = {
 "tutti": ["Partecipare alla riunione preparatoria o leggere questa guida", "Scorrere le slide della propria giornata con le note (tasto N)", "Stampare i fogli dell'ora: A3 orizzontale, 6 copie per ora", "All'inizio della giornata: taratura del barattolo (2 minuti)"],
 "ma": ["Una moneta per coppia e due per il docente: una normale e una con due teste (o una faccia coperta da un adesivo)", "Un sacchetto opaco", "10 gettoni per gruppo"],
 "ef": ["3 cronometri (va bene il telefono)", "Nastro adesivo di carta, 3 cestini, 30 palline di carta, una benda", "Un'urna con 29 codici anonimi", "Banchi lungo le pareti; linee di lancio a 2 metri; cerchi a terra per il bersaglio", "Ora 2: sei postazioni, tre di equilibrio e tre di lanci"],
 "in": ["Cartella condivisa della classe", "Giornata 1: foglio «Corpus 1P» e un foglio «Pappagallo» per gruppo", "Giornata 2: foglio «Lanci» e un «Calcolatore» per gruppo con i dati della 1Z", "Giornata 3: foglio «Prove 1P» con la convalida, fogli «Parallelo» e «Registro»", "Giornata 4: verificare che Teachable Machine si apra e che le webcam funzionino", "Un computer per gruppo e il proiettore"],
}
prep = ""
for r, voci in PREP.items():
    nome = "Per tutti" if r == "tutti" else RUOLI[r]
    li = "".join(f'<li><label><input type="checkbox"> {v}</label></li>' for v in voci)
    prep += f'<div class="prep r-{r}"><h3>{nome}</h3><ul class="check">{li}</ul></div>'
schermata("preparazione", "Strumenti", "Preparazione", f"""
<p class="occhiello">Prima della giornata</p>
<h2>Che cosa preparare</h2>
<div class="preps">{prep}</div>
<p class="nota">Le spunte servono solo come promemoria su questo schermo e non vengono salvate.</p>""")

glos = "".join(f'<div class="voce"><b>{t}</b><span>{d}</span></div>' for t, d in GLOSSARIO)
schermata("glossario", "Strumenti", "Glossario", f"""
<p class="occhiello">Le parole dell'informatica</p>
<h2>Glossario</h2>
<input class="cerca" placeholder="Cerca un termine…" aria-label="Cerca nel glossario">
<div class="glossario">{glos}</div>""")

# ---------------------------------------------------------------- PAGINA
menu = ""
sez = None
for sid, s, m, ruoli, _ in S:
    if s != sez:
        menu += f'<p class="sez">{s}</p>'
        sez = s
    menu += f'<a href="#{sid}" data-ruoli="{" ".join(ruoli)}">{m}</a>'
pagine = "".join(f'<section class="pag" id="p-{sid}" data-id="{sid}">{c}</section>' for sid, s, m, r, c in S)
ordine = json.dumps([s[0] for s in S])

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "guida.css")).read()
JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "guida.js")).read().replace("__ORDINE__", ordine)
out = f"""<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>IA e dati · 1P · Guida per i docenti</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body>
<aside class="menu"><p class="marchio">IA e dati · 1P</p><p class="sotto">Guida per i docenti</p><div class="filtro"></div><nav>{menu}</nav></aside>
<main><div class="barra"><div class="riemp"></div></div>
<div class="pagine">{pagine}</div>
<footer class="naviga"><button class="prec" aria-label="Precedente">←</button><span class="pos"></span><button class="succ" aria-label="Successiva">→</button></footer>
</main>
<script>{JS}</script></body></html>"""
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "guida.html"), "w").write(out)
print(len(S), "schermate,", len(out) // 1024, "KB")
