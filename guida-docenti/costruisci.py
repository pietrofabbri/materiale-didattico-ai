"""Guida per i docenti del percorso «IA e dati» (1P): pagina unica, navigazione a livelli.
Ogni pagina ha un livello (1 = che cosa fare … 4 = a fondo). Si scende con «Scendi», si risale con «Risali»,
si passa alla pagina accanto con ← →. Uso: python3 costruisci.py  (SHOTS = cartella delle immagini .webp)"""
import base64, html, json, os, sys
QUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, QUI)
from contenuti import ORE, GLOSSARIO
from approfondimenti import APP
from principi import PRINCIPI
from scelte import SCELTE
import valutazione as V

SHOTS = os.environ.get("SHOTS", "/home/claude/shots/")
def img(nome, alt, cap=""):
    b = base64.b64encode(open(os.path.join(SHOTS, nome + ".webp"), "rb").read()).decode()
    return f'<figure><img src="data:image/webp;base64,{b}" alt="{html.escape(alt)}" loading="lazy">' + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>"

RUOLI = {"it": "Italiano", "ma": "Matematica", "ef": "Educazione fisica", "in": "Informatica"}
P = {}      # id -> dict(titolo, capitolo, corpo, livello, su, giu, prec, succ, ruoli, scala)
ORD = []
def pag(pid, titolo, capitolo, corpo, livello=1, su=None, ruoli=("tutti",), scala=None):
    P[pid] = dict(titolo=titolo, capitolo=capitolo, corpo=corpo, livello=livello, su=su, giu=None, prec=None, succ=None, ruoli=list(ruoli), scala=scala)
    ORD.append(pid)
    if su: P[su]["giu"] = pid
def catena(ids):
    for a, b in zip(ids, ids[1:]):
        P[a]["succ"] = b; P[b]["prec"] = a

def det(titolo, corpo):
    return f'<details class="nota"><summary>{titolo}</summary><div class="nota-c">{corpo}</div></details>'
def link(pid, testo=None):
    return f'<a href="#{pid}">{testo or P[pid]["titolo"]}</a>' if pid in P else (testo or pid)

# ================================================================= HOME
pag("home", "Guida per i docenti", "", "")  # corpo scritto alla fine, quando tutte le pagine esistono

# ================================================================= IL PERCORSO
C = "Il percorso"
pag("idea", "L'idea del percorso", C, """
<p class="tesi">Una macchina non sa che cosa è vero. Sa solo che cosa è frequente nei dati con cui è stata costruita.</p>
<p>I chatbot, come ChatGPT, sono costruiti per fare una cosa: prevedere la parola successiva di un testo. Per farlo usano le frequenze osservate in enormi quantità di testi. Nessuna parte di questo procedimento controlla se ciò che scrivono è vero.</p>
<p>Nel percorso gli studenti fanno le stesse operazioni su scala piccola, con dati prodotti da loro: raccolgono dati, li contano, scelgono la risposta più probabile. Alla fine devono sapere due cose: la qualità di una risposta dipende dalla qualità dei dati; le risposte di una macchina vanno verificate.</p>
<p><b>Organizzazione.</b> Quattro giornate di tre ore, più una quinta. In ogni giornata le prime due ore si svolgono in aula, la terza in laboratorio di informatica. La giornata 4 si svolge tutta in laboratorio. La prima ora della giornata 5 è la verifica individuale.</p>
""")
pag("idea2", "Come funziona un chatbot, spiegato con precisione", C, """
<p>Questa pagina serve a chi conduce le ore, per rispondere con sicurezza alle domande degli studenti.</p>
<h3>1. L'addestramento</h3>
<p>Un modello linguistico viene addestrato su una grande quantità di testi. L'esercizio è sempre lo stesso: si nasconde la parola successiva di una frase e il modello deve indovinarla. Ogni volta che sbaglia, i suoi parametri (miliardi di numeri) vengono corretti di poco. Dopo moltissimi esercizi, il modello assegna a ogni possibile parola successiva una probabilità.</p>
<h3>2. La generazione</h3>
<p>Quando risponde, il modello scrive una parola alla volta: guarda tutto il testo scritto fino a quel punto, calcola le probabilità della parola successiva, ne sceglie una, la aggiunge e ricomincia. La scelta non è sempre la più probabile: un parametro, la «temperatura», regola quanto spazio lasciare a parole meno probabili.</p>
<h3>3. Che cosa ne consegue</h3>
<ul><li>Il modello produce testi fluenti, perché ha visto moltissimi esempi di lingua corretta.</li>
<li>Può scrivere cose false con lo stesso tono di quelle vere, perché la verità non entra nel calcolo. Questi errori si chiamano «allucinazioni».</li>
<li>Riproduce ciò che è frequente nei testi di partenza, compresi stereotipi ed errori diffusi.</li></ul>
<h3>4. Che cosa costruiscono gli studenti</h3>
<p>Nella giornata 1 costruiscono la versione più semplice possibile: un modello che guarda solo la parola precedente e sceglie la successiva più frequente. Tecnicamente è un modello a bigrammi. I chatbot reali guardano migliaia di parole precedenti e usano reti neurali invece di conteggi, ma il compito è lo stesso.</p>
<h3>5. Le altre giornate</h3>
<p>Le giornate successive affrontano gli altri ingredienti: la probabilità (giornata 2), la qualità delle misure da cui nascono i dati (giornata 3), l'apprendimento dagli esempi e la valutazione di un modello (giornate 4 e 5).</p>
""", 2, su="idea")
principi_link = " · ".join(f'<a href="#pr-{k}">{v["titolo"]}</a>' for k, v in PRINCIPI.items())
pag("idea3", "Le scelte didattiche di fondo", C, f"""
<p>Il percorso è costruito su alcune scelte didattiche, ognuna con una ragione precisa. Ogni scelta rimanda a un principio descritto nella sezione Principi didattici, con le fonti.</p>
<h3>Gli studenti costruiscono, non ascoltano una spiegazione</h3>
<p>Spiegare a quattordicenni come funziona un modello linguistico produce, nel migliore dei casi, una definizione ripetuta. Costruirne uno con le proprie frasi, e vederlo scrivere una frase falsa con la stessa sicurezza di una vera, lascia un'idea che si ricorda. {link("pr-costruire", "Principio: imparare costruendo")}.</p>
<h3>Prima a mano, poi al computer</h3>
<p>Ogni procedimento si esegue prima a mano su un esempio piccolo, in aula, e poi al computer su tutti i dati, in laboratorio. Così il computer non appare come una scatola magica. {link("pr-unplugged", "Principio: prima a mano")}.</p>
<h3>Ogni attività ha la stessa sequenza</h3>
<p>Consegna, con chi, dove si scrive, esempio svolto, tempo, soluzione. La ripetizione riduce le domande organizzative e lascia attenzione per il contenuto. {link("pr-regole", "Principio: routine prevedibili")}; {link("pr-esempio", "principio: esempio svolto")}.</p>
<h3>Si scrive una previsione prima di ogni risultato</h3>
<p>Una previsione scritta rende visibile l'idea dello studente; il risultato la conferma o la smentisce. {link("pr-prevedere", "Principio: prevedere prima di verificare")}.</p>
<h3>Si verifica la comprensione alla fine di ogni ora</h3>
<p>Tre domande individuali, con una regola di decisione: se meno di metà classe risponde bene, si riprende. {link("pr-formativa", "Principio: verificare durante")}; {link("pr-recupero", "principio: richiamare dalla memoria")}.</p>
<h3>Gruppi che cambiano, responsabilità individuale</h3>
<p>Gruppi diversi a ogni giornata; un foglio comune per gruppo; domande finali e verifica individuali. {link("pr-gruppi", "Principio: il lavoro di gruppo che funziona")}.</p>
<p class="piccolo">Tutti i principi: {principi_link}.</p>
""", 3, su="idea2")

FILO = [("1", "La lingua come dati", "Come fa una macchina a scrivere?", "Un modello che genera frasi dalle 48 frasi della classe", "Il corpus e le probabilità tornano nelle giornate 2 e 4"),
 ("2", "Incertezza e misura", "Che cosa vuol dire «probabile»?", "Un calcolatore statistico sul foglio di calcolo", "Il calcolatore si usa nella giornata 4 sui dati veri"),
 ("3", "Il corpo come fonte di dati", "Da dove vengono i dati?", "Il dataset delle prove motorie, controllato", "Si analizza nella giornata 4"),
 ("4", "Dai dati alle scoperte", "Come impara una macchina dagli esempi?", "Un'analisi con i suoi limiti; un modello che riconosce oggetti; una presentazione", "Tutto confluisce nella verifica della giornata 5"),
 ("5", "Verifica e primo modello", "Che cosa ho imparato? Come si valuta un modello?", "La verifica individuale; un classificatore a vicini", "")]
righe = "".join(f'<tr><td class="n">{n}</td><td><b>{t}</b><br><i>{q}</i></td><td>{c}</td><td class="pic">{r}</td></tr>' for n, t, q, c, r in FILO)
pag("filo", "Il filo delle giornate", C, f"""
<p>Ogni giornata risponde a una domanda e lascia un prodotto che la giornata successiva riprende. Per questo un'ora saltata rende più difficili le successive.</p>
<table class="tab"><thead><tr><th></th><th>Giornata e domanda</th><th>Che cosa si costruisce</th><th>Dove ritorna</th></tr></thead><tbody>{righe}</tbody></table>
<p><b>Perché quest'ordine.</b> Si parte dalla lingua perché è l'esperienza che gli studenti hanno dei chatbot. La matematica viene subito dopo per dare un significato preciso a «probabile». Le misure arrivano quando la classe ha gli strumenti per controllarle. L'apprendimento dagli esempi viene per ultimo perché richiede tutto il resto.</p>
""")

CONTRIB = {
 "it": ("Giornata 1, ore 1 e 2", "Gli studenti imparano a guardare un testo come un insieme di parole da contare e a distinguere fatto, opinione e falso credibile. Le 48 frasi che scrivono sono i dati del modello costruito in laboratorio.", ["Radice e desinenza: verbi irregolari, desinenza e suffisso, parole alterate.", "Ambiguità: omografia, ruolo del contesto.", "Genere testuale: registro e marcatori.", "Fatto e opinione: espressioni che segnalano un giudizio.", "Fonti: come si cita, notizia e commento."]),
 "ma": ("Giornata 2, ore 1 e 2", "Gli studenti danno un significato preciso a «probabile», aggiornano una convinzione dopo un'osservazione e descrivono molti dati con pochi numeri. Sono gli strumenti usati poi per analizzare le misure della classe.", ["Probabilità: eventi incompatibili, lancio di due dadi.", "Frequenza: frazioni, decimali, percentuali.", "Albero: prodotto lungo i rami.", "Media e simbolo Σ.", "Retta: pendenza e intercetta."]),
 "ef": ("Giornata 3, ore 1 e 2", "Gli studenti eseguono due prove motorie con un protocollo, misurano l'errore e producono il dataset della classe. Con il bersaglio nascosto provano l'apprendimento per tentativi.", ["Le prove: equilibrio statico, precisione nel lancio.", "Il protocollo: partenza, avvio, criterio di arresto.", "Il bersaglio: apprendimento motorio e ruolo del feedback.", "La raccolta: controllo dell'esecuzione."]),
 "in": ("Terza ora di ogni giornata; giornate 4 e 5", "Le ore di laboratorio trasformano il lavoro in aula in dati e modelli funzionanti. Il docente di informatica può condurre tutte le ore del percorso e assegna il voto finale.", ["Foglio di calcolo condiviso, CSV, riferimenti.", "Convalida e pulizia dei dati.", "Apprendimento supervisionato e valutazione.", "k vicini e normalizzazione."]),
}
blocchi = "".join(f'<div class="ruolo r-{k}"><h3>{RUOLI[k]} <span>· {q}</span></h3><p>{t}</p>{det("Che cosa si può aggiungere dalla propria materia", "<ul>" + "".join(f"<li>{a}</li>" for a in agg) + "</ul><p>Bastano due o tre minuti, nei punti indicati nelle pagine delle ore.</p>")}</div>' for k, (q, t, agg) in CONTRIB.items())
pag("materie", "Il contributo delle materie", C, f"""
<p>I contenuti delle materie sono trattati come cenni legati alle attività, non come lezioni. La presenza dei colleghi di italiano, matematica ed educazione fisica è facoltativa: le slide permettono al docente di informatica di condurre ogni ora. Un collega presente arricchisce le sue due ore con esempi della propria disciplina. Prima del percorso è prevista una riunione di circa trenta minuti.</p>
{blocchi}""")

pag("ora", "La struttura di ogni ora", C, """
<p>Ogni ora è progettata per <b>40 minuti</b> di attività. Il modulo orario è più lungo: restano sempre <b>5-10 minuti</b> per le domande degli studenti e per i rallentamenti.</p>
<div class="asse"><span style="flex:3">apertura</span><span style="flex:30" class="pieno">attività</span><span style="flex:3">controllo</span><span style="flex:4">chiusura</span><span style="flex:8" class="marg">margine</span></div>
<div class="asse-n"><span style="flex:3">0</span><span style="flex:30">3</span><span style="flex:3">33</span><span style="flex:4">36</span><span style="flex:8">40</span></div>
<ol><li><b>Apertura</b> (3 minuti): titolo, obiettivi; nella prima ora della giornata, il sorteggio dei gruppi.</li>
<li><b>Attività</b> (circa 30 minuti). Ogni attività ha sempre la stessa sequenza: consegna; con chi si lavora; in quale riquadro del foglio si scrive; un esempio svolto; il tempo; la soluzione.</li>
<li><b>Controllo</b> (3 minuti): tre domande, a cui ognuno risponde da solo nell'ultimo riquadro del foglio. Se meno di metà classe risponde bene a una domanda, l'argomento si riprende all'inizio dell'ora successiva.</li>
<li><b>Chiusura</b> (4 minuti): una riga da copiare nel formulario; ritiro dei fogli.</li></ol>
<p><b>Il foglio dell'ora.</b> Un foglio A3 per gruppo, diviso in riquadri numerati R1, R2… In alto si scrivono il numero del gruppo e i numeri del registro dei presenti. A fine ora il foglio si ritira e si consegna al docente di informatica.</p>
<p><b>I gruppi.</b> Sei gruppi di 4-5 studenti, estratti dalle slide all'inizio di ogni giornata. I gruppi cambiano ogni giornata e non hanno ruoli fissi: chi scrive cambia a ogni attività.</p>
""")
pag("ora2", "Perché ogni ora è uguale", C, f"""
<p>Una struttura sempre uguale riduce il tempo perso a spiegare che cosa fare e diminuisce i comportamenti di disturbo, che spesso nascono dall'incertezza. Gli studenti imparano la routine nella prima giornata e dalla seconda la eseguono quasi da soli.</p>
<p>Ogni elemento ha una funzione precisa:</p>
<ul><li><b>Esempio svolto prima del timer</b>: riduce il carico per chi affronta un compito nuovo. {link("pr-esempio", "Principio")}.</li>
<li><b>Timer visibile</b>: il tempo diventa un dato condiviso, non un'impressione del docente.</li>
<li><b>Riquadro indicato dalla slide</b>: nessun gruppo si chiede dove scrivere; il foglio finale è ordinato e confrontabile.</li>
<li><b>Tre domande finali individuali</b>: il docente sa che cosa riprendere; gli studenti fissano il concetto. {link("pr-formativa", "Principio")}; {link("pr-recupero", "principio")}.</li>
<li><b>Margine di 5-10 minuti</b>: una lezione progettata per l'intero modulo arriva sempre in ritardo; una lezione con margine finisce in tempo anche quando qualcosa si inceppa.</li></ul>
<p>{link("pr-regole", "Principio: routine prevedibili")}.</p>
""", 2, su="ora")

pag("regole", "Le regole del percorso", C, f"""
<dl class="regole">
<dt>Niente nomi</dt><dd>Sui fogli e sullo schermo compaiono solo numeri del gruppo, numeri del registro (solo sul foglio, per il docente) e codici estratti a sorte. Non si raccolgono peso, altezza o informazioni sulla salute. Nei modelli non si usano volti né corpi. Nessun dato degli studenti viene caricato su servizi esterni.</dd>
<dt>Niente classifiche</dt><dd>Le misure servono a imparare a misurare, non a confrontare le persone. Si mostrano solo risultati dell'intera classe.</dd>
<dt>Niente chatbot</dt><dd>Gli studenti non usano chatbot durante le attività.</dd>
<dt>Voti solo dal docente di informatica</dt><dd>Gli altri docenti non valutano. Vedi la sezione {link("val1", "Valutazione")}.</dd>
</dl>
<p>{link("pr-dati", "Principio: dati personali, raccogliere il minimo")}.</p>
""")
catena(["idea", "filo", "materie", "ora", "regole"])

# ================================================================= LE SLIDE
C = "Le slide"
pag("aprire", "Aprire le slide", C, f"""
<ol class="passi"><li>Aprire il browser <b>Chrome</b> o <b>Edge</b> e andare al <a href="https://pietrofabbri.github.io/materiale-didattico-ai/" target="_blank" rel="noopener">sito delle slide</a>.</li>
<li>Premere <kbd>F11</kbd> per lo schermo intero. Si esce premendo di nuovo <kbd>F11</kbd>.</li>
<li>Nel menu iniziale, fare clic su «Apri le slide» nella giornata da svolgere.</li>
<li>Se il browser chiede di usare il microfono, rispondere «Consenti». Il microfono misura solo il volume; non registra nulla.</li></ol>
{img("menu", "Il menu iniziale", "Il menu iniziale: per ogni giornata, le slide e i fogli dell'ora da stampare.")}
<p><b>Che cosa serve:</b> un computer collegato al proiettore o alla lavagna interattiva, Chrome o Edge, il microfono del portatile. Non si installa nulla.</p>
<p><b>Senza internet:</b> dallo stesso sito si scarica il file <code>index.html</code>, che si apre con un doppio clic. In questo caso alcuni browser non concedono il microfono: il barattolo resta spento, il resto funziona.</p>
""")
pag("schermo", "Che cosa si vede sullo schermo", C, f"""
{img("schermo", "Una slide di attività", "1 modalità di lavoro · 2 timer · 3 barattolo del rumore · 4 barra dell'ora · 5 numero della slide · 6 contenuto.")}
<p>La <b>barra dell'ora</b> (4) ha un segmento per ogni slide dell'ora. Il segmento più alto è la slide attuale; quelli sbiaditi sono già stati visti. Colori: <span class="sw e"></span> essenziale, <span class="sw c"></span> consigliata, <span class="sw f"></span> facoltativa. Le slide facoltative si possono saltare se manca tempo. Un clic su un segmento porta a quella slide.</p>
""")
TASTI = [("→ ←", "avanti e indietro; la freccia destra mostra prima le risposte nascoste"), ("spazio", "avvia o ferma il timer; a timer finito, avvia il successivo"), ("N", "note per il docente: minuti, che cosa dire, soluzioni"), ("R", "riporta il timer all'inizio"), ("H", "aiuto con l'elenco dei tasti"), ("Home", "torna al menu iniziale"), ("B", "accende o spegne il barattolo"), ("T", "taratura del barattolo"), ("U o Esc", "sblocca subito lo schermo"), ("M", "modalità del barattolo solo per la slide attuale"), ("K", "disattiva il blocco del barattolo per tutta la lezione")]
pag("tasti", "I tasti", C, f"""
<table class="tab">{"".join(f"<tr><td><kbd>{k}</kbd></td><td>{d}</td></tr>" for k, d in TASTI)}</table>
<p>Se un tasto non funziona, fare clic una volta sulla slide e riprovare. Il telecomando per presentazioni funziona come le frecce.</p>
<p>Le note (<kbd>N</kbd>) sono visibili anche alla classe se lo schermo è proiettato: conviene leggerle prima della lezione.</p>
{img("risposta", "Risposta nascosta", "La risposta compare con la freccia destra.")}
""")
pag("barattolo", "Il barattolo del rumore", C, f"""
<p>È un vaso di brillantini sul lato destro dello schermo. Il microfono misura il volume dell'aula: più rumore c'è, più i brillantini si agitano. Non registra nulla.</p>
<p>Ogni slide imposta da sola la sensibilità: <b>spento</b> quando spiega il docente, <b>silenzio</b> nel lavoro individuale, <b>discussione</b> nel lavoro di gruppo.</p>
{img("barattolo", "Tre stati", "Calma, attenzione, blocco.")}
<p>Se il volume resta oltre il limite per circa tre secondi, il barattolo copre lo schermo e suona una campana. Lo schermo torna da solo dopo circa dieci secondi di silenzio. <kbd>U</kbd> sblocca subito; <kbd>K</kbd> disattiva il blocco per tutta la lezione.</p>
<p><b>All'inizio di ogni giornata</b> serve la taratura (due minuti): si veda la pagina successiva, scendendo.</p>
""")
pag("barattolo2", "La taratura e le regolazioni", C, f"""
<p>Il barattolo deve conoscere il livello del silenzio e quello di una discussione normale nell'aula in cui si trova. La prima volta che si preme <kbd>B</kbd> si apre il pannello.</p>
<ol><li>Chiedere silenzio alla classe e fare clic su «1 · Misura il silenzio». Dura 5 secondi.</li>
<li>Chiedere ai gruppi di parlare a voce normale e fare clic su «2 · Misura una discussione normale». Dura 5 secondi.</li>
<li>Fare clic su «Salva e chiudi». Le altre impostazioni si lasciano come sono.</li></ol>
{img("taratura", "Il pannello di taratura", "Le tre operazioni sono numerate.")}
<p><b>Quando il blocco interrompe troppo.</b> Nelle prove motorie e in laboratorio un certo brusio è normale. Il tasto <kbd>K</kbd> disattiva il blocco ma lascia il barattolo attivo: i brillantini continuano a segnalare il volume.</p>
<p><b>Perché funziona.</b> Il barattolo sposta la regolazione del volume dalla voce del docente a un segnale neutro, visibile a tutti. Il blocco interrompe tutti per pochi secondi, senza individuare nessuno. Dopo i primi blocchi le classi tendono a regolarsi da sole guardando i brillantini.</p>
""", 2, su="barattolo")
pag("altri", "Timer, sorteggio, fogli dell'ora", C, """
<dl class="regole"><dt>Timer</dt><dd>Non parte da solo: si avvia con la barra spaziatrice dopo la consegna e l'esempio. Alcune slide hanno più timer in sequenza. Se il barattolo blocca lo schermo, il timer si ferma. Il timer si può mettere in pausa per rispondere a una domanda.</dd>
<dt>Sorteggio</dt><dd>Nella quarta slide di ogni giornata. Nel campo «Assenti» si scrivono i numeri del registro separati da virgole; con «Sorteggia» compaiono sei gruppi colorati con i numeri dei componenti. Conviene fotografare lo schermo: serve al docente di informatica per la valutazione.</dd>
<dt>Fogli dell'ora</dt><dd>Dal menu iniziale, «Stampa i fogli dell'ora»: A3 orizzontale, sei copie per ogni ora. Se il browser blocca la finestra di stampa, consentire le finestre a comparsa per la pagina.</dd></dl>
""")
catena(["aprire", "schermo", "tasti", "barattolo", "altri"])

# ================================================================= LE ORE
C = "Le ore"
LIV = {1: "Che cosa fare", 2: "Perché è fatta così", 3: "Che cosa dice la ricerca", 4: "Il concetto a fondo"}
ore_ids = list(ORE.keys())
for k in ore_ids:
    o, ap, sc = ORE[k], APP[k], SCELTE[k]
    testa = f'Giornata {o["giornata"]}' + (f' · Ora {o["ora"]}' if o["ora"] else "") + f' · {o["luogo"]} · {", ".join(RUOLI[r] for r in o["ruoli"])}'
    titolo = (f'G{o["giornata"]} · Ora {o["ora"]} · ' if o["ora"] else f'G{o["giornata"]} · ') + o["titolo"]
    righe = ""
    for i, (a, b, t, r, d) in enumerate(o["att"]):
        dd = "".join(f'<p><span class="k">{kk}</span> {vv}</p>' for kk, vv in d["r"])
        righe += f'<details class="riga" id="{k}-{i}"><summary><span class="t">{f"{a}–{b}" if o["ora"] else ""}</span><span class="a">{t}</span><span class="r">{"" if r in ("—", "") else r}</span></summary><div class="riga-c">{dd}</div></details>'
    sa = "".join(f"<li>{x}</li>" for x in o["sa"])
    l1 = f"""<p class="sopra">{testa}</p>
<p class="lede">{o['obiettivo']}</p>
<p>{ap['perche']}</p>
<h3>Scaletta</h3><p class="piccolo">Fare clic su un'attività per vedere consegna, che cosa dire e soluzione.</p>
<div class="scaletta">{righe}</div>
<h3>Alla fine dell'ora lo studente sa</h3><ul>{sa}</ul>
<h3>Se il tempo manca</h3><p>{ap['tempo'][0]}</p>
<h3>Se il tempo avanza</h3><p>{ap['tempo'][1]}</p>"""
    pag(k, titolo, C, l1, 1, ruoli=o["ruoli"], scala=k)
    l2 = "<p>Ogni attività dell'ora è il risultato di una scelta. Qui le scelte principali, con la loro ragione.</p><ol class='scelte'>" + "".join(
        f"<li><p><b>{s}</b></p><p>{w}</p>" + (f'<p class="rim">Principio: <a href="#pr-{pid}">{PRINCIPI[pid]["titolo"]}</a></p>' if pid else "") + "</li>" for s, w, pid in sc) + "</ol>"
    pag(k + "-2", titolo, C, f'<p class="sopra">{testa}</p>' + l2, 2, su=k, ruoli=o["ruoli"], scala=k)
    usati = []
    for _, _, pid in sc:
        if pid and pid not in usati: usati.append(pid)
    l3 = "<p>I principi didattici su cui si reggono le scelte di quest'ora. Per ciascuno: che cosa dice la ricerca e come compare qui. Ogni principio ha una pagina completa con le fonti.</p>"
    for pid in usati:
        pr = PRINCIPI[pid]
        qui = [s for s, _, p in sc if p == pid]
        l3 += f'<div class="princ"><h3>{pr["titolo"]}</h3><p>{pr["breve"]}</p><p>{pr["ricerca"][0]}</p><p class="rim">In quest\'ora: {" ".join(x[0].lower()+x[1:] for x in qui)}</p><p class="rim"><a href="#pr-{pid}">Leggi il principio per intero, con le fonti</a></p></div>'
    pag(k + "-3", titolo, C, f'<p class="sopra">{testa}</p>' + l3, 3, su=k + "-2", ruoli=o["ruoli"], scala=k)
    conc = "".join(f"<p>{c}</p>" for c in ap["concetto"])
    dom = "".join(f'<p class="q">{q}</p><p class="ans">{a}</p>' for q, a in ap["domande"])
    crit = "".join(f"<li>{c}</li>" for c in ap["criteri"])
    l4 = f"""<h3>Il concetto</h3>{conc}
<h3>Domande che gli studenti fanno</h3>{dom}
<h3>Criteri di riuscita</h3><p>Che cosa osservare nei riquadri del foglio per dire che l'obiettivo è raggiunto.</p><ul>{crit}</ul>"""
    pag(k + "-4", titolo, C, f'<p class="sopra">{testa}</p>' + l4, 4, su=k + "-3", ruoli=o["ruoli"], scala=k)
for lv in ("", "-2", "-3", "-4"):
    catena([k + lv for k in ore_ids])

# ================================================================= VALUTAZIONE
C = "Valutazione"
pag("val1", "La valutazione: che cosa sapere", C, V.LIVELLI_VAL[1])
pag("val2", "Come si calcola il voto", C, "<p class='sopra'>Per il docente di informatica</p>" + V.livello2(), 2, su="val1", ruoli=("in",))
pag("val3", "La verifica della giornata 5", C, "<p class='sopra'>Per il docente di informatica</p>" + V.livello2b(), 3, su="val2", ruoli=("in",))
pag("val4", "Perché il voto è costruito così", C, V.LIVELLI_VAL[3], 4, su="val3")

# ================================================================= PRINCIPI
C = "Principi didattici"
elenco = "".join(f'<li><a href="#pr-{k}">{v["titolo"]}</a><br><span class="piccolo">{v["breve"]}</span></li>' for k, v in PRINCIPI.items())
pag("principi", "I principi didattici", C, f"<p>Le scelte del percorso si appoggiano a risultati noti della ricerca sull'insegnamento. Ogni pagina spiega il principio, dice dove compare nel percorso, ne indica i limiti e riporta le fonti principali.</p><ul class='elenco'>{elenco}</ul>")
pr_ids = []
for k, v in PRINCIPI.items():
    corpo = f"""<p class="lede">{v['breve']}</p>
<h3>Che cosa dice la ricerca</h3>{"".join(f"<p>{x}</p>" for x in v['ricerca'])}
<h3>Dove compare nel percorso</h3><ul>{"".join(f"<li>{x}</li>" for x in v['percorso'])}</ul>
<h3>Limiti e attenzioni</h3><ul>{"".join(f"<li>{x}</li>" for x in v['limiti'])}</ul>
<h3>Fonti</h3><ul class="fonti">{"".join(f"<li>{x}</li>" for x in v['fonti'])}</ul>"""
    pag("pr-" + k, v["titolo"], C, corpo, 2, su="principi")
    pr_ids.append("pr-" + k)
catena(pr_ids)
for pid in pr_ids: pass
P["principi"]["giu"] = pr_ids[0]

# ================================================================= STRUMENTI
C = "Strumenti"
PREP = {"tutti": ["Partecipare alla riunione preparatoria o leggere questa guida", "Scorrere le slide della propria giornata con le note (tasto N)", "Stampare i fogli dell'ora: A3 orizzontale, sei copie per ora", "All'inizio della giornata: taratura del barattolo", "A fine ora: ritirare i fogli e controllare numero del gruppo e numeri dei presenti"],
 "ma": ["Una moneta per coppia; per il docente una moneta normale e una con due teste (oppure una faccia coperta da un adesivo)", "Un sacchetto opaco", "Dieci gettoni per gruppo"],
 "ef": ["Tre cronometri (basta il telefono)", "Nastro adesivo di carta, tre cestini, trenta palline di carta, una benda", "Un'urna con 29 codici", "Banchi lungo le pareti; linee di lancio a 2 m; cerchi a terra per il bersaglio", "Ora 2: tre postazioni di equilibrio e tre di lanci"],
 "in": ["Cartella condivisa della classe", "Giornata 1: fogli «Corpus 1P» e «Pappagallo»", "Giornata 2: fogli «Lanci» e «Calcolatore» con i dati della 1Z", "Giornata 3: foglio «Prove 1P» con convalida, «Parallelo», «Registro»", "Giornata 4: verificare Teachable Machine e webcam", "Giornata 5: verifica stampata, una copia per studente", "Foglio per registrare i punteggi dei fogli dell'ora"]}
prep = "".join(f'<div class="prep r-{r}"><h3>{"Per tutti" if r == "tutti" else RUOLI[r]}</h3><ul class="check">{"".join(f"<li><label><input type=checkbox> {v}</label></li>" for v in vv)}</ul></div>' for r, vv in PREP.items())
pag("prep", "Preparazione", C, f'<div class="preps">{prep}</div><p class="piccolo">Le spunte sono un promemoria su questo schermo e non vengono salvate.</p>')
pag("glossario", "Glossario", C, '<input class="cerca" placeholder="Cerca un termine" aria-label="Cerca">' + '<dl class="glossario">' + "".join(f'<div class="voce"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in GLOSSARIO) + "</dl>")
catena(["prep", "glossario"])

# ================================================================= HOME (scritta per ultima)
def gruppo_ore(g):
    return "".join(f'<li data-ruoli="{" ".join(ORE[k]["ruoli"])}"><a href="#{k}">{P[k]["titolo"].split(" · ", 1)[1]}</a></li>' for k in ore_ids if ORE[k]["giornata"] == g)
ore_home = "".join(f'<div class="g"><p class="gt">Giornata {g}</p><ul>{gruppo_ore(g)}</ul></div>' for g in range(1, 6))
P["home"]["corpo"] = f"""
<p class="lede">Questa guida serve a condurre le ore del percorso «Intelligenza artificiale e dati» nella classe 1P.</p>
<p>Ogni pagina ha un <b>testo di base</b>, sufficiente per condurre l'ora. Chi vuole capire di più trova in fondo alla pagina il pulsante <b>Scendi</b>, che porta a un livello più profondo: perché l'attività è fatta così, che cosa dice la ricerca, il concetto spiegato a fondo. Si può scendere fino al quarto livello e risalire in qualsiasi momento.</p>
<div class="materia"><label for="materia">La mia materia</label>
<select id="materia"><option value="tutti">Tutte</option><option value="it">Italiano</option><option value="ma">Matematica</option><option value="ef">Educazione fisica</option><option value="in">Informatica</option></select>
<span class="piccolo">Le ore della propria materia vengono evidenziate.</span></div>
<div class="mappa">
<div><h3>Il percorso</h3><ul><li>{link("idea")}</li><li>{link("filo")}</li><li>{link("materie")}</li><li>{link("ora")}</li><li>{link("regole")}</li></ul></div>
<div><h3>Le slide</h3><ul><li>{link("aprire")}</li><li>{link("schermo")}</li><li>{link("tasti")}</li><li>{link("barattolo")}</li><li>{link("altri")}</li></ul></div>
<div><h3>Valutazione</h3><ul><li>{link("val1")}</li><li>{link("val2")}</li><li>{link("val3")}</li></ul></div>
<div><h3>Approfondire e preparare</h3><ul><li>{link("principi")}</li><li>{link("prep")}</li><li>{link("glossario")}</li></ul></div>
</div>
<h2 class="h-ore">Le ore</h2><div class="ore-home">{ore_home}</div>
"""

# ================================================================= USCITA
dati = {pid: {k: P[pid][k] for k in ("titolo", "capitolo", "livello", "su", "giu", "prec", "succ", "ruoli", "scala")} for pid in P}
sezioni = "".join(f'<section class="pag" id="p-{pid}" data-id="{pid}">{P[pid]["corpo"]}</section>' for pid in ORD)
CSS = open(os.path.join(QUI, "guida.css")).read()
JS = open(os.path.join(QUI, "guida.js")).read().replace("__DATI__", json.dumps(dati, ensure_ascii=False)).replace("__LIV__", json.dumps(LIV, ensure_ascii=False))
out = f"""<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>IA e dati · 1P · Guida per i docenti</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header class="barra"><a href="#home" class="marchio">Guida per i docenti</a><nav class="briciole"></nav><button class="apri-indice">Indice</button></header>
<div class="corpo"><aside class="profondita"></aside><main>
<p class="capitolo"></p><h1 class="titolo"></h1>
<div class="pagine">{sezioni}</div>
<nav class="giu"></nav>
<nav class="lato"><a class="prec"></a><a class="succ"></a></nav>
</main></div>
<div class="indice" hidden><div class="indice-c"><button class="chiudi">Chiudi</button><div class="indice-l"></div></div></div>
<script>{JS}</script></body></html>"""
open(os.path.join(QUI, "guida.html"), "w").write(out)
print(len(P), "pagine,", len(out) // 1024, "KB")
