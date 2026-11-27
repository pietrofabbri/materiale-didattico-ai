# Sezione Valutazione: tre livelli.
GRIGLIA = [
 ("Completezza", "0-3", "3: tutti i riquadri compilati · 2: manca un riquadro · 1: ne mancano due o più · 0: foglio quasi vuoto"),
 ("Correttezza", "0-4", "Confronto con le soluzioni delle slide (tasto N). 4: tutto corretto o con errori di distrazione · 3: un errore di procedimento · 2: due errori · 1: corretto solo in parte · 0: nessun risultato corretto"),
 ("Regole", "0-2", "2: rispettate le regole dell'attività (formato delle frasi, protocollo, nessun nome) · 1: una regola non rispettata · 0: più regole non rispettate"),
 ("Controllo finale", "0-1", "1: il riquadro del controllo ha le risposte di tutti i presenti · 0: mancano risposte"),
]

VERIFICA = [
 ("Giornata 1", [
   ("Nella frase «il cane vede il gatto» quante sono le occorrenze e quante le forme?", "5 occorrenze, 4 forme (il compare due volte)."),
   ("Dividi «scrivevamo» in radice e desinenza e di' che cosa indica la desinenza.", "scriv- / -evamo: noi, passato."),
   ("Un chatbot scrive una frase falsa con tono sicuro. Spiega in due righe perché può succedere.", "Sceglie le parole più probabili in base ai testi letti; non verifica se ciò che scrive è vero.")]),
 ("Giornata 2", [
   ("P(E) = 0,3. Quanto vale P(non E)?", "0,7."),
   ("Calcola media e mediana di 2, 3, 3, 4, 38. Quale delle due descrive meglio i dati? Perché?", "Media 10, mediana 3; la mediana, perché 38 è un valore estremo."),
   ("Due grandezze hanno r = 0,9. Si può concludere che una causa l'altra? Fai un esempio.", "No; esempio di causa comune (gelati e annegamenti: il caldo).")]),
 ("Giornata 3", [
   ("Un cronometrista parte sempre in ritardo. Che tipo di errore è? Come si corregge?", "Sistematico; cambiando la procedura (ad esempio chi dà il via cronometra), non ripetendo la misura."),
   ("Uno studente non ha fatto la seconda prova. Che cosa si scrive nella casella? Perché?", "Nulla, si lascia vuota e si annota; 0 sarebbe un valore vero e abbasserebbe la media.")]),
 ("Giornata 4", [
   ("Un modello riconosce 18 immagini su 20. Qual è l'accuratezza?", "0,9 (90%)."),
   ("Un modello addestrato con penne su sfondo bianco sbaglia una penna su sfondo nero. Perché?", "Ha imparato anche lo sfondo: negli esempi non c'erano sfondi diversi.")]),
]

LIVELLI_VAL = {}
LIVELLI_VAL[1] = """
<p>Il voto finale del percorso lo assegna <b>solo il docente di informatica</b>. Gli altri docenti non danno voti e non devono compilare nulla.</p>
<p>A chi conduce un'ora si chiede una sola cosa: a fine ora, <b>ritirare i fogli dell'ora e controllare che in alto siano scritti il numero del gruppo e i numeri del registro dei presenti</b>. Poi i fogli si consegnano al docente di informatica.</p>
<p>Questi numeri servono perché i gruppi cambiano ogni giornata: il punteggio di ogni foglio va agli studenti che erano presenti in quel gruppo, in quell'ora.</p>
<p>Il voto si compone di due parti:</p>
<ul><li>una <b>verifica individuale</b>, nella prima ora della giornata 5;</li><li>i <b>punteggi dei fogli dell'ora</b> dei gruppi in cui lo studente ha lavorato.</li></ul>
<p>Le domande di controllo di fine ora <b>non</b> entrano nel voto: servono solo a capire che cosa riprendere.</p>
"""

def livello2():
    g = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in GRIGLIA)
    return f"""
<h3>1. Il punteggio dei fogli dell'ora</h3>
<p>Ogni foglio dell'ora riceve un punteggio da 0 a 10 con questa griglia.</p>
<table class="tab"><thead><tr><th>Criterio</th><th>Punti</th><th>Come si assegnano</th></tr></thead><tbody>{g}</tbody></table>
<p>Si valutano i fogli delle 12 ore delle giornate 1-4: sei fogli per ora, uno per gruppo. Il punteggio di un foglio va a <b>ogni studente presente</b> in quel gruppo in quell'ora.</p>
<h3>2. La media dei prodotti di ogni studente</h3>
<p>Per ogni studente si fa la media dei punteggi dei fogli delle ore in cui era presente. Le ore di assenza non contano: non abbassano e non alzano la media.</p>
<h3>3. La verifica individuale</h3>
<p>Si svolge nella prima ora della giornata 5, in circa 35 minuti, senza appunti. Si corregge in decimi.</p>
<h3>4. Il voto</h3>
<p class="formula">voto = 0,6 × verifica + 0,4 × media dei fogli</p>
<p>Il risultato si arrotonda al mezzo voto.</p>
<p><b>Esempio.</b> Uno studente è stato presente in 10 ore su 12. I fogli dei suoi gruppi in quelle ore hanno una media di 7,8. Nella verifica ha preso 6,5. Voto: 0,6 × 6,5 + 0,4 × 7,8 = 3,9 + 3,12 = 7,02, arrotondato a 7.</p>
<h3>5. Casi particolari</h3>
<ul>
<li><b>Assente alla verifica:</b> la recupera in un'ora curricolare.</li>
<li><b>Presente in meno di 4 ore:</b> il voto si basa solo sulla verifica, perché la media dei fogli sarebbe poco affidabile.</li>
<li><b>Foglio senza i numeri dei presenti:</b> si ricostruiscono dal registro di classe e dalla composizione dei gruppi mostrata nel sorteggio; per questo conviene fotografare lo schermo del sorteggio a inizio giornata.</li>
<li><b>Foglio non consegnato:</b> vale 0 per i presenti di quel gruppo, salvo cause non dipendenti dagli studenti.</li>
</ul>
<h3>6. Che cosa dire agli studenti</h3>
<p>All'inizio della giornata 1 conviene spiegare la regola in tre frasi: il foglio del gruppo vale per tutti i presenti; i gruppi cambiano, quindi ognuno contribuisce a molti fogli diversi; il voto finale dipende soprattutto dalla verifica individuale della giornata 5.</p>
"""

def livello2b():
    parti = ""
    for g, dom in VERIFICA:
        li = "".join(f"<li>{q}<br><span class='sol'>Risposta attesa: {a}</span></li>" for q, a in dom)
        parti += f"<h3>{g}</h3><ol>{li}</ol>"
    return f"""
<p>La verifica ha una parte per ogni giornata e richiama i concetti principali, non i dettagli. Le domande qui sotto sono un esempio di struttura e di livello: il docente di informatica le adatta a ciò che la classe ha effettivamente svolto.</p>
<p>Punteggio indicativo: 1 punto per le domande di calcolo, 1,5 per quelle che chiedono una spiegazione; il totale si riporta in decimi.</p>
{parti}
<p>Le domande seguono due regole. Chiedono di <b>usare</b> un concetto (calcolare, spiegare, fare un esempio) e non di riconoscere una definizione. Sono simili, ma non identiche, a quelle dei controlli di fine ora: lo studente deve aver capito, non ricordato una risposta.</p>
"""

LIVELLI_VAL[3] = """
<h3>Perché un voto in due parti</h3>
<p>Nel lavoro di gruppo c'è un rischio noto: uno lavora, gli altri guardano. La ricerca sull'apprendimento cooperativo indica due condizioni perché il gruppo funzioni: ognuno ha bisogno degli altri per riuscire, e ognuno risponde del proprio apprendimento. Il voto riflette entrambe: i fogli dell'ora premiano il lavoro comune, la verifica individuale misura ciò che ciascuno ha acquisito. La verifica pesa di più (60%) perché è la sola parte che dipende interamente dallo studente.</p>
<h3>Perché i gruppi che cambiano rendono il voto più giusto</h3>
<p>Con gruppi fissi, uno studente capitato in un gruppo debole avrebbe un voto basso per tutto il percorso. Con gruppi che cambiano a ogni giornata, ogni studente lavora in molti gruppi diversi: la media dei suoi fogli è fatta di punteggi di gruppi diversi, e la fortuna o la sfortuna di un singolo gruppo pesa poco. È lo stesso principio della media delle stime visto nella giornata 4: più misure indipendenti danno un valore più stabile.</p>
<h3>Perché le domande di fine ora non entrano nel voto</h3>
<p>Servono a capire che cosa riprendere. Se valessero per il voto, gli studenti avrebbero interesse a copiare, e il docente perderebbe l'informazione che gli serve. La distinzione tra valutazione formativa (per decidere che cosa fare) e sommativa (per certificare un risultato) è centrale negli studi di Black e Wiliam.</p>
<h3>Perché dirlo agli studenti fin dall'inizio</h3>
<p>Se la regola del voto è chiara dalla prima giornata, gli studenti sanno che il foglio del gruppo conta e che conta anche ciò che imparano da soli. Una regola nota prima è percepita come giusta; una regola scoperta alla fine, no.</p>
<h3>Limiti dello schema</h3>
<ul><li>Il punteggio del foglio non distingue chi ha contribuito di più all'interno del gruppo. Il docente di informatica può correggere il voto finale di mezzo punto in base a ciò che ha osservato, dichiarandolo.</li>
<li>I fogli da valutare sono 72 (12 ore per 6 gruppi): la griglia è breve proprio per questo, circa due minuti a foglio.</li></ul>
"""
