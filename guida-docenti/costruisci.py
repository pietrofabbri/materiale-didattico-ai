"""Costruisce guida.html: manuale interattivo per i docenti del percorso «IA e dati» (1P)."""
import base64, html, json, os, sys
QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
from contenuti import ORE, GLOSSARIO
from approfondimenti import APP

SHOTS = os.environ.get("SHOTS", "/home/claude/shots/")
def img(nome, alt, didascalia=""):
    b = base64.b64encode(open(os.path.join(SHOTS, nome + ".webp"), "rb").read()).decode()
    cap = f"<figcaption>{didascalia}</figcaption>" if didascalia else ""
    return f'<figure><img src="data:image/webp;base64,{b}" alt="{html.escape(alt)}" loading="lazy">{cap}</figure>'

RUOLI = {"it": "Italiano", "ma": "Matematica", "ef": "Educazione fisica", "in": "Informatica"}

def nota(titolo, corpo, aperta=False):
    return f'<details class="nota"{" open" if aperta else ""}><summary><span>{titolo}</span></summary><div class="nota-c">{corpo}</div></details>'

S = []
def pagina(sid, sez, menu, corpo, margine="", ruoli=("tutti",)):
    S.append((sid, sez, menu, list(ruoli), corpo, margine))

# =============================================================== I. IL PERCORSO
pagina("inizio", "I. Il percorso", "Premessa", """
<p class="testatina">Intelligenza artificiale e dati · Classe 1P · Anno scolastico 2026/27</p>
<h1>Guida per chi conduce le ore</h1>
<p class="lede">Questa guida accompagna i docenti che conducono una o più ore del percorso. Ogni pagina contiene un testo di base, sufficiente a condurre l'ora senza altro materiale. Le voci contrassegnate dalla freccia aprono approfondimenti facoltativi: il perché di un'attività, il concetto che vi sta dietro, le domande che gli studenti pongono più spesso.</p>
<div class="materia">
  <label for="materia">Materia di chi legge</label>
  <select id="materia"><option value="tutti">Tutte</option><option value="it">Italiano</option><option value="ma">Matematica</option><option value="ef">Educazione fisica</option><option value="in">Informatica</option></select>
  <p>La scelta segna nell'indice le ore di propria competenza.</p>
</div>
<p class="istruzioni">Si sfoglia con i tasti <kbd>←</kbd> <kbd>→</kbd> oppure dall'indice a sinistra.</p>
""", """<p class="m-tit">In sintesi</p><p>Quattro giornate di tre ore, più una quinta facoltativa. Due ore in aula con il docente della materia, la terza in laboratorio di informatica.</p><p>Classe 1P, 29 studenti, sei gruppi diversi in ogni giornata.</p>""")

pagina("idea", "I. Il percorso", "L'idea", f"""
<p class="testatina">I · 1</p>
<h2>L'idea del percorso</h2>
<p class="tesi">Una macchina non sa che cosa è vero. Sa soltanto che cosa è frequente nei dati che ha ricevuto.</p>
<p>I sistemi oggi più diffusi, come i chatbot, sono addestrati a un compito preciso: prevedere la parola successiva di un testo, sulla base delle frequenze osservate in enormi raccolte di testi. Nulla, in questo compito, verifica la verità di ciò che viene scritto. Il percorso fa ripetere agli studenti, su scala ridotta e con i propri dati, le tre operazioni che stanno alla base di questi sistemi: <b>raccogliere</b> dati, <b>contare</b>, <b>scegliere il più probabile</b>.</p>
<p>Ne derivano le due acquisizioni che il percorso intende lasciare: la qualità di una risposta dipende dalla qualità dei dati; le risposte di una macchina vanno verificate.</p>
{nota("Perché costruire invece di spiegare", "<p>Spiegare come funziona un modello linguistico a studenti di quattordici anni produce, nel migliore dei casi, una definizione ripetuta. Costruirne uno con le proprie frasi, e vederlo generare una frase falsa con la stessa sicurezza di una vera, produce una convinzione. Ogni giornata è progettata perché la conclusione arrivi dall'esperienza degli studenti e non dalla voce del docente.</p>")}
{nota("Che cosa non è questo percorso", "<p>Non è un corso di programmazione né un corso sull'uso dei chatbot: gli studenti non usano chatbot durante le attività. Non richiede competenze informatiche ai docenti delle ore in aula: il foglio di calcolo e i modelli si incontrano solo in laboratorio.</p>")}
""", """<p class="m-tit">Acquisizioni attese</p><ul><li>contare e misurare con metodo</li><li>distinguere un fatto da un'opinione</li><li>leggere una probabilità</li><li>riconoscere un errore di misura</li><li>proteggere i propri dati</li></ul>""")

FILO = [
 ("1", "La lingua come dati", "Come fa una macchina a scrivere?", "Un modello che genera frasi dalle 48 frasi della classe", "Le probabilità ritornano nella giornata 2; il corpus nella presentazione finale"),
 ("2", "Incertezza e misura", "Che cosa vuol dire «probabile»?", "Un calcolatore statistico sul foglio di calcolo", "Il calcolatore si riusa nella giornata 4 sui dati veri"),
 ("3", "Il corpo come fonte di dati", "Da dove vengono i dati?", "Il dataset delle prove motorie, controllato e documentato", "Il dataset si analizza nella giornata 4"),
 ("4", "Dai dati alle scoperte", "Come impara una macchina dagli esempi?", "Un'analisi con i suoi limiti; un modello che riconosce oggetti", "Presentazione finale del lavoro"),
 ("5", "Recupero o primo modello", "Come si valuta un modello?", "Un classificatore a vicini", "Facoltativa: solo se la classe è in pari"),
]
righe = "".join(f'<tr><td class="n">{n}</td><td><a href="#{"g5" if n == "5" else "g" + n + "o1"}">{t}</a></td><td><i>{q}</i></td><td>{c}</td><td class="pic">{r}</td></tr>' for n, t, q, c, r in FILO)
pagina("filo", "I. Il percorso", "Il filo delle giornate", f"""
<p class="testatina">I · 2</p>
<h2>Il filo delle giornate</h2>
<p>Ogni giornata risponde a una domanda e lascia un prodotto che la giornata successiva riprende. Il percorso si regge su questa continuità: un'ora saltata indebolisce le successive.</p>
<table class="tab filo"><thead><tr><th></th><th>Giornata</th><th>Domanda</th><th>Che cosa si costruisce</th><th>Dove ritorna</th></tr></thead><tbody>{righe}</tbody></table>
{nota("Perché questo ordine", "<p>Si parte dalla lingua perché è l'esperienza che gli studenti hanno dei chatbot. La matematica arriva subito dopo per dare precisione alla parola «probabile» appena usata. Le misure sul corpo vengono dopo, quando la classe ha gli strumenti per controllarle. L'apprendimento dagli esempi chiude, perché richiede tutto ciò che precede: dati raccolti bene, strumenti per descriverli, consapevolezza dei limiti.</p>")}
""", """<p class="m-tit">Struttura di ogni giornata</p><p>Ore 1 e 2: in aula, con il docente della materia.</p><p>Ora 3: in laboratorio, con il docente di informatica.</p><p>La giornata 4 si svolge interamente in laboratorio.</p>""")

CONTRIB = {
 "it": ("La giornata 1 apre il percorso: mostra che la lingua, per una macchina, è fatta di parole da contare e da prevedere, e porta gli studenti a distinguere con precisione fatto, opinione e falso credibile. Le 48 frasi scritte dai gruppi sono i dati del primo modello della classe.",
        ["Radice e desinenza: verbi irregolari, desinenza e suffisso, parole alterate", "Ambiguità: omografia, ruolo del contesto nella comprensione", "Genere testuale: registro e marcatori dei testi affrontati in classe", "Fatto e opinione: espressioni che segnalano un giudizio", "Fonti: come si cita; notizia e commento"]),
 "ma": ("La giornata 2 dà alla classe il linguaggio dell'incertezza. Probabilità, aggiornamento delle convinzioni, media, dispersione e correlazione servono poi per controllare e analizzare le misure raccolte nella giornata 3.",
        ["Probabilità: eventi incompatibili, spazio dei casi di due dadi", "Frequenza: frazioni, decimali, percentuali; legge dei grandi numeri", "Albero: prodotto lungo i rami, rapporto tra rami", "Media e Σ: lettura dei simboli e proprietà", "Correlazione e retta: piano cartesiano, pendenza, intercetta"]),
 "ef": ("La giornata 3 produce i dati veri del percorso: misure del corpo raccolte dagli studenti stessi, con un protocollo e un codice al posto del nome. Con il bersaglio nascosto gli studenti sperimentano sul proprio corpo l'apprendimento per tentativi.",
        ["Le prove: equilibrio statico, precisione nel lancio, esecuzione corretta", "Il protocollo: posizione di partenza, avvio, criterio di arresto", "Il bersaglio: apprendimento motorio, ruolo del feedback", "La raccolta: controllo dell'esecuzione alle postazioni"]),
 "in": ("Le ore di laboratorio trasformano il lavoro in aula in dati e modelli funzionanti, e la giornata 4 conduce alla presentazione finale. Il docente di informatica può condurre tutte le ore del percorso.",
        ["Foglio di calcolo condiviso, CSV, riferimenti", "Convalida, pulizia, tracciabilità dei dati", "Apprendimento supervisionato e valutazione su dati nuovi", "Metodo dei k vicini e normalizzazione"]),
}
blocchi = ""
for k, (t, agg) in CONTRIB.items():
    li = "".join(f"<li>{a}</li>" for a in agg)
    blocchi += f'<div class="ruolo r-{k}"><h3>{RUOLI[k]}</h3><p>{t}</p>{nota("Che cosa si può aggiungere dalla propria materia", f"<ul>{li}</ul><p>Bastano due o tre minuti nei punti indicati nelle pagine delle ore.</p>")}</div>'
pagina("ruoli", "I. Il percorso", "Il contributo delle materie", f"""
<p class="testatina">I · 3</p>
<h2>Il contributo delle materie</h2>
<p>I contenuti disciplinari sono trattati come cenni funzionali alle attività, non come lezioni formali. La presenza dei colleghi di italiano, matematica ed educazione fisica è facoltativa: le slide consentono al docente di informatica di condurre ogni ora. Un collega presente rende le proprie due ore più ricche, intervenendo con esempi della sua disciplina.</p>
{blocchi}
""", """<p class="m-tit">Riunione preparatoria</p><p>Prima del percorso è prevista una riunione di circa trenta minuti con i docenti interessati.</p>""")

pagina("ora", "I. Il percorso", "La struttura dell'ora", f"""
<p class="testatina">I · 4</p>
<h2>La struttura dell'ora</h2>
<p>Ogni ora è progettata per <b>40 minuti</b> di attività. Il modulo orario è più lungo: restano quindi sempre <b>5-10 minuti</b> di margine, da usare per le domande degli studenti e per assorbire i rallentamenti senza dover rinunciare ad attività.</p>
<div class="asse"><span style="flex:3">apertura</span><span style="flex:30" class="pieno">attività</span><span style="flex:3">controllo</span><span style="flex:4">chiusura</span><span style="flex:8" class="margine">margine</span></div>
<div class="asse-n"><span style="flex:3">0</span><span style="flex:30">3</span><span style="flex:3">33</span><span style="flex:4">36</span><span style="flex:8">40</span></div>
<p>Ogni attività segue la stessa sequenza, visibile nelle slide: consegna; modalità di lavoro (da soli, nel gruppo, tutti insieme); riquadro del foglio in cui scrivere; un esempio svolto; tempo a disposizione; soluzione. La ripetizione della sequenza riduce le domande organizzative e lascia spazio a quelle di contenuto.</p>
{nota("Il foglio dell'ora", "<p>Un foglio A3 per gruppo, diviso in riquadri numerati R1, R2… Le slide mostrano una mappa del foglio con il riquadro da usare evidenziato. L'ultimo riquadro contiene sempre le tre risposte del controllo finale. A fine ora il foglio si ritira: è la traccia del lavoro di ogni gruppo.</p>")}
{nota("I gruppi", "<p>Sei gruppi di 4-5 studenti, estratti dalle slide all'inizio di ogni giornata con i numeri del registro. I gruppi cambiano a ogni giornata e non prevedono ruoli fissi: chi scrive cambia a ogni attività. Ne risulta che ogni studente lavora con quasi tutti i compagni nel corso del percorso.</p>")}
""", """<p class="m-tit">Se il tempo manca</p><p>Le slide facoltative, segnate in grigio nella barra in basso, si possono saltare senza conseguenze. Ogni pagina delle ore indica che cosa ridurre.</p>""")

pagina("valutazione", "I. Il percorso", "Osservazione e criteri", f"""
<p class="testatina">I · 5</p>
<h2>Osservazione e criteri di riuscita</h2>
<p>Ogni ora si chiude con tre domande individuali che verificano gli obiettivi dell'ora. Le risposte, scritte nell'ultimo riquadro del foglio, permettono al docente di capire subito se un concetto va ripreso: se meno della metà della classe risponde correttamente a una domanda, l'argomento si riprende all'inizio dell'ora successiva.</p>
<p>Ogni pagina delle ore riporta, sotto la voce <i>Criteri di riuscita</i>, ciò che si osserva nei riquadri del foglio per stabilire se l'obiettivo è stato raggiunto. I criteri sono pensati per un'osservazione formativa; l'eventuale uso per la valutazione resta a discrezione di ciascun docente.</p>
{nota("Che cosa raccogliere", "<p>I fogli dell'ora di ogni gruppo, conservati per giornata. Contengono i conteggi, le frasi, le misure e le risposte ai controlli: un materiale sufficiente a ricostruire il percorso di ogni gruppo.</p>")}
""", """<p class="m-tit">Biglietto finale</p><p>Al termine della giornata 4 ogni studente scrive, con un esempio, la differenza tra stima e verità. È la verifica più diretta dell'obiettivo del percorso.</p>""")

pagina("regole", "I. Il percorso", "Regole", f"""
<p class="testatina">I · 6</p>
<h2>Regole</h2>
<dl class="regole">
<dt>Riservatezza</dt><dd>Sui fogli e sullo schermo non compaiono nomi, ma solo numeri del gruppo o codici estratti a sorte. Non si raccolgono peso, altezza o informazioni sulla salute. Nei modelli non si usano volti né corpi. Nessun dato degli studenti viene caricato su servizi esterni.</dd>
<dt>Nessuna classifica</dt><dd>Le misure servono a imparare a misurare, non a confrontare le persone. I risultati si esaminano solo in forma aggregata.</dd>
<dt>Nessun chatbot</dt><dd>Gli studenti non usano chatbot durante le attività: il percorso li osserva dall'interno, non li adopera.</dd>
</dl>
{nota("Perché il codice estratto e non il nome", "<p>Il codice rende le misure non immediatamente riconducibili alla persona. La corrispondenza tra codice e nome la conosce solo lo studente, che lo annota sul proprio diario: non esiste un elenco. È un esempio concreto del principio di minimizzazione dei dati, che la classe incontra così in pratica prima che in teoria.</p>")}
""")

# =============================================================== II. LE SLIDE
pagina("aprire", "II. Le slide", "Aprire le slide", f"""
<p class="testatina">II · 1</p>
<h2>Aprire le slide</h2>
<ol class="passi">
<li>Aprire il browser <b>Chrome</b> o <b>Edge</b> e andare al <a href="https://pietrofabbri.github.io/materiale-didattico-ai/" target="_blank" rel="noopener">sito delle slide</a>.</li>
<li>Premere <kbd>F11</kbd> per lo schermo intero; di nuovo <kbd>F11</kbd> per uscire.</li>
<li>Nel menu iniziale scegliere la giornata e fare clic su «Apri le slide».</li>
<li>Se il browser chiede di usare il microfono, rispondere «Consenti».</li>
</ol>
{img("menu", "Il menu iniziale delle slide", "Il menu iniziale: per ogni giornata, le slide e i fogli dell'ora da stampare.")}
{nota("Senza connessione a internet", "<p>Dallo stesso sito si può scaricare il file <code>index.html</code> e aprirlo con un doppio clic: le slide funzionano anche offline. In questo caso alcuni browser non concedono il microfono e il barattolo resta spento; tutto il resto funziona.</p>")}
""", """<p class="m-tit">Che cosa serve</p><p>Un computer collegato al proiettore o alla lavagna interattiva, Chrome o Edge, il microfono del portatile. Non occorre installare nulla.</p><p class="m-tit">Il microfono</p><p>Misura soltanto il volume dell'aula, istante per istante. Nessun suono viene registrato o salvato.</p>""")

pagina("schermo", "II. Le slide", "Lo schermo", f"""
<p class="testatina">II · 2</p>
<h2>Che cosa compare sullo schermo</h2>
{img("schermo", "Una slide di attività con gli strumenti numerati", "Una slide di attività. 1 modalità di lavoro · 2 timer · 3 barattolo del rumore · 4 barra dell'ora · 5 numero della slide · 6 contenuto.")}
<p>La <b>barra dell'ora</b> (4) mostra un segmento per ogni slide dell'ora in corso. Il segmento più alto è la slide attuale, quelli sbiaditi sono già stati visti. Il colore indica l'importanza: <span class="sw e"></span> essenziale, <span class="sw c"></span> consigliata, <span class="sw f"></span> facoltativa. Un clic su un segmento porta direttamente a quella slide.</p>
""", """<p class="m-tit">Come usare la barra</p><p>In caso di ritardo, le slide grigie si possono saltare. Le slide essenziali contengono i passaggi su cui si costruiscono le ore successive.</p>""")

ALTRI = [("<kbd>→</kbd> <kbd>←</kbd>", "avanti e indietro; la freccia destra fa comparire prima le risposte nascoste"), ("<kbd>spazio</kbd>", "avvia o ferma il timer; a timer finito, avvia il successivo"),
         ("<kbd>N</kbd>", "note per il docente: minuti, che cosa dire, soluzioni"), ("<kbd>R</kbd>", "riporta il timer all'inizio"), ("<kbd>H</kbd>", "riquadro di aiuto con tutti i tasti"),
         ("<kbd>Home</kbd>", "torna al menu iniziale"), ("<kbd>B</kbd>", "accende o spegne il barattolo"), ("<kbd>T</kbd>", "taratura del barattolo"),
         ("<kbd>U</kbd> o <kbd>Esc</kbd>", "sblocca subito lo schermo"), ("<kbd>M</kbd>", "modalità del barattolo solo per la slide attuale"), ("<kbd>K</kbd>", "disattiva il blocco per tutta la lezione")]
tab = "".join(f"<tr><td>{k}</td><td>{d}</td></tr>" for k, d in ALTRI)
pagina("tasti", "II. Le slide", "I tasti", f"""
<p class="testatina">II · 3</p>
<h2>I tasti</h2>
<table class="tab tasti">{tab}</table>
<p>Se un tasto non produce effetto, fare clic una volta sulla slide e riprovare. Il telecomando per presentazioni funziona come le frecce.</p>
{img("risposta", "La stessa slide prima e dopo la freccia destra", "Molte slide mostrano prima la domanda; la risposta compare con la freccia destra.")}
""", """<p class="m-tit">Le note (N)</p><p>Sono visibili anche alla classe se lo schermo è proiettato: conviene leggerle prima della lezione, oppure aprirle solo per un istante.</p>""")

pagina("barattolo", "II. Le slide", "Il barattolo del rumore", f"""
<p class="testatina">II · 4</p>
<h2>Il barattolo del rumore</h2>
<p>È un vaso di brillantini sul lato destro dello schermo. Misura il volume dell'aula e si comporta come un barattolo di brillantini scosso: più rumore, più i brillantini si agitano. Ogni slide ne imposta da sola la sensibilità: <b>spento</b> durante le spiegazioni del docente, <b>silenzio</b> nel lavoro individuale, <b>discussione</b> nel lavoro di gruppo.</p>
{img("barattolo", "I tre stati del barattolo", "Calma, attenzione, blocco.")}
<p>Se il volume resta oltre il limite per circa tre secondi, il barattolo copre lo schermo e suona una campana. La lezione riprende da sola dopo circa dieci secondi di silenzio; tra due blocchi passano almeno sessanta secondi. <kbd>U</kbd> sblocca subito; <kbd>K</kbd> disattiva il blocco per l'intera lezione.</p>
{nota("La taratura, all'inizio di ogni giornata", "<p>Il barattolo deve conoscere il silenzio e il brusio normale dell'aula in cui si trova. Premendo <kbd>B</kbd> la prima volta si apre il pannello: 1 · con la classe in silenzio, «Misura il silenzio»; 2 · con i gruppi che parlano a voce normale, «Misura una discussione normale»; 3 · «Salva e chiudi». Le altre impostazioni restano come sono. Richiede circa due minuti.</p>" + img("taratura", "Il pannello di taratura", "Il pannello di taratura: le tre operazioni sono numerate."))}
{nota("Perché funziona", "<p>Il barattolo sposta la regolazione del volume dalla voce del docente a uno strumento neutro e visibile a tutti. Il blocco non punisce nessuno in particolare: interrompe l'attività di tutti per pochi secondi, e la classe impara presto a regolarsi da sé.</p>")}
""", """<p class="m-tit">Nelle ore rumorose</p><p>Durante le prove motorie e in laboratorio un certo brusio è inevitabile. Se il blocco interrompe troppo spesso, <kbd>K</kbd> lo disattiva senza spegnere il barattolo.</p>""")

pagina("strumenti-slide", "II. Le slide", "Timer, sorteggio, fogli", f"""
<p class="testatina">II · 5</p>
<h2>Timer, sorteggio, fogli dell'ora</h2>
<dl class="regole">
<dt>Timer</dt><dd>Non parte da solo: si avvia con la barra spaziatrice dopo aver letto la consegna e mostrato l'esempio. Alcune slide hanno più timer in sequenza («1 di 2»). Se il barattolo blocca lo schermo, il timer si ferma. Il timer è un riferimento, non un vincolo.</dd>
<dt>Sorteggio</dt><dd>Nella quarta slide di ogni giornata. Nel campo «Assenti» si scrivono i numeri del registro, separati da virgole; un clic su «Sorteggia» forma sei gruppi colorati, mostrati con i soli numeri.</dd>
<dt>Fogli dell'ora</dt><dd>Dal menu iniziale, «Stampa i fogli dell'ora»: formato A3 orizzontale, sei copie per ogni ora. Se il browser blocca la finestra di stampa, consentire le finestre a comparsa per la pagina.</dd>
</dl>
""")

# =============================================================== III. LE ORE
TIT_G = {1: "La lingua come dati", 2: "Incertezza e misura", 3: "Il corpo come fonte di dati", 4: "Dai dati alle scoperte", 5: "Recupero o primo modello"}
def ora_html(k, o):
    ap = APP[k]
    righe = ""
    for i, (a, b, t, r, d) in enumerate(o["att"]):
        det = "".join(f'<p><span class="k">{kk}</span> {vv}</p>' for kk, vv in d["r"])
        tempo = f"{a}–{b}" if o["ora"] else ""
        rq = r if r not in ("—", "") else ""
        righe += f'<details class="riga" id="{k}-{i}"><summary><span class="t">{tempo}</span><span class="a">{t}</span><span class="r">{rq}</span></summary><div class="riga-c">{det}</div></details>'
    conc = "".join(f"<p>{c}</p>" for c in ap["concetto"])
    dom = "".join(f'<p class="q">{q}</p><p class="ans">{a}</p>' for q, a in ap["domande"])
    crit = "".join(f"<li>{c}</li>" for c in ap["criteri"])
    testa = f'Giornata {o["giornata"]} · ' + (f'Ora {o["ora"]} · ' if o["ora"] else "") + o["luogo"]
    corpo = f"""
<p class="testatina">{testa} · {" · ".join(RUOLI[r] for r in o["ruoli"])}</p>
<h2>{o['titolo']}</h2>
<p class="lede">{o['obiettivo']}</p>
<p class="perche">{ap['perche']}</p>
<h4>Scaletta{' (minuti)' if o['ora'] else ''}</h4>
<div class="scaletta">{righe}</div>
{nota("Il concetto, per chi conduce", conc)}
{nota("Domande che gli studenti pongono", dom)}
{nota("Criteri di riuscita", f"<ul>{crit}</ul>")}
"""
    sa = "".join(f"<li>{x}</li>" for x in o["sa"])
    margine = f"""<p class="m-tit">Alla fine dell'ora lo studente sa</p><ul>{sa}</ul>
<p class="m-tit">Se il tempo manca</p><p>{ap['tempo'][0]}</p>
<p class="m-tit">Se il tempo avanza</p><p>{ap['tempo'][1]}</p>"""
    return corpo, margine

for k, o in ORE.items():
    c, m = ora_html(k, o)
    menu = (f"Ora {o['ora']} · " if o["ora"] else "") + o["titolo"]
    pagina(k, f"III. Giornata {o['giornata']} · {TIT_G[o['giornata']]}", menu, c, m, o["ruoli"])

# =============================================================== IV. STRUMENTI
PREP = {
 "tutti": ["Partecipare alla riunione preparatoria o leggere questa guida", "Scorrere le slide della propria giornata con le note (N)", "Stampare i fogli dell'ora: A3 orizzontale, sei copie per ora", "All'inizio della giornata: taratura del barattolo"],
 "ma": ["Una moneta per coppia; per il docente una moneta normale e una con due teste (oppure una faccia coperta da un adesivo)", "Un sacchetto opaco", "Dieci gettoni per gruppo"],
 "ef": ["Tre cronometri (il telefono è sufficiente)", "Nastro adesivo di carta, tre cestini, trenta palline di carta, una benda", "Un'urna con 29 codici", "Banchi lungo le pareti; linee di lancio a 2 m; cerchi a terra per il bersaglio", "Ora 2: tre postazioni di equilibrio e tre di lanci"],
 "in": ["Cartella condivisa della classe", "Giornata 1: foglio «Corpus 1P» e un foglio «Pappagallo» per gruppo", "Giornata 2: foglio «Lanci» e un «Calcolatore» per gruppo con i dati della 1Z", "Giornata 3: foglio «Prove 1P» con convalida, fogli «Parallelo» e «Registro»", "Giornata 4: verificare Teachable Machine e le webcam", "Un computer per gruppo; proiettore"],
}
prep = ""
for r, voci in PREP.items():
    li = "".join(f'<li><label><input type="checkbox"> {v}</label></li>' for v in voci)
    prep += f'<div class="prep r-{r}"><h3>{"Per tutti" if r == "tutti" else RUOLI[r]}</h3><ul class="check">{li}</ul></div>'
pagina("preparazione", "IV. Strumenti", "Preparazione", f"""
<p class="testatina">IV · 1</p>
<h2>Preparazione</h2>
<div class="preps">{prep}</div>
<p class="piccolo">Le spunte sono un promemoria su questo schermo e non vengono salvate.</p>""")

glos = "".join(f'<div class="voce"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in GLOSSARIO)
pagina("glossario", "IV. Strumenti", "Glossario", f"""
<p class="testatina">IV · 2</p>
<h2>Glossario</h2>
<input class="cerca" placeholder="Cerca un termine" aria-label="Cerca nel glossario">
<dl class="glossario">{glos}</dl>""")

# =============================================================== PAGINA
indice, sez = "", None
for sid, s, m, ruoli, _, _ in S:
    if s != sez:
        indice += f'<p class="sez">{s}</p>'; sez = s
    indice += f'<a href="#{sid}" data-ruoli="{" ".join(ruoli)}">{m}</a>'
pag = "".join(f'<section class="pag" id="p-{sid}" data-id="{sid}"><div class="testo">{c}</div><aside class="margine">{m}</aside></section>' for sid, s, mm, r, c, m in S)
CSS = open(os.path.join(QUI, "guida.css")).read()
JS = open(os.path.join(QUI, "guida.js")).read().replace("__ORDINE__", json.dumps([s[0] for s in S]))
out = f"""<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>IA e dati · 1P · Guida per i docenti</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body>
<nav class="indice"><p class="titolo-ind">Guida per i docenti</p><p class="sotto-ind">IA e dati · 1P</p>{indice}</nav>
<main><div class="pagine">{pag}</div>
<footer class="piede"><button class="prec" aria-label="Pagina precedente">← precedente</button><span class="pos"></span><button class="succ" aria-label="Pagina successiva">successiva →</button></footer></main>
<script>{JS}</script></body></html>"""
open(os.path.join(QUI, "guida.html"), "w").write(out)
print(len(S), "pagine,", len(out) // 1024, "KB")
