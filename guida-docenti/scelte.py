# Livello 2: perché ogni ora è fatta così. Ogni scelta: (che cosa, perché, principio collegato o None)
SCELTE = {}

SCELTE["g1o1"] = [
 ("Si comincia con una domanda che ha due risposte giuste («quante parole ci sono?»).", "La domanda sembra banale e quasi tutti rispondono. Le due risposte diverse (5 e 4) obbligano a distinguere due modi di contare: occorrenze e forme. Il concetto nasce da un disaccordo reale, non da una definizione.", "prevedere"),
 ("Le regole di conteggio si fissano prima di contare.", "Senza regole comuni ogni gruppo ottiene un numero diverso e il confronto diventa inutile. È la prima volta che la classe incontra un'idea che tornerà nella giornata 3: per confrontare misure serve un protocollo.", "regole"),
 ("Il paragrafo si conta a mano, con le tacche.", "Contare a mano 67 parole richiede cinque minuti e fa capire che cosa farà il computer nell'ora 3. Lo studente che ha contato a mano sa che cosa significa il numero che il computer gli darà.", "unplugged"),
 ("Radice e desinenza hanno un metodo in tre passi, con un esempio svolto.", "Molti studenti di prima non hanno un procedimento per scomporre una parola. Il metodo li rende autonomi; l'esempio svolto mostra i tre passi prima dell'esercizio.", "esempio"),
 ("Il gioco di Shannon si fa senza mostrare la frase sulla LIM.", "Se la frase fosse visibile, il gioco perderebbe senso. La difficoltà di prevedere le prime parole e la facilità delle ultime è l'esperienza che spiega il ruolo del contesto.", None),
 ("L'ora si chiude con tre domande individuali.", "Servono al docente per sapere se riprendere un concetto e agli studenti per fissarlo richiamandolo a memoria.", "recupero"),
]
SCELTE["g1o2"] = [
 ("Si apre con cinque consigli scritti da un'intelligenza artificiale, senza dire subito quali sono falsi.", "Gli studenti giudicano i consigli prima di avere gli strumenti per farlo. Alla fine dell'ora rileggono il proprio giudizio alla luce di ciò che hanno imparato su fatti, falsi e fonti.", "prevedere"),
 ("Ogni gruppo scrive frasi su un genere assegnato, con regole precise.", "Le regole (4-8 parole, minuscolo, parole ripetute) non sono un vincolo formale: servono perché il modello dell'ora 3 possa funzionare. Gli studenti scrivono frasi che diventeranno dati, e lo sanno.", "costruire"),
 ("Ogni frase riceve un'etichetta: fatto, falso verosimile, opinione.", "Etichettare obbliga a ragionare su ogni frase. Inoltre prepara ciò che si osserva nell'ora 3: il modello genera frasi senza usare le etichette.", None),
 ("Si chiede la fonte di ogni fatto, e «internet» non vale.", "Indicare una fonte precisa costringe a chiedersi chi può confermare un'affermazione. È la competenza che gli studenti useranno davanti alle risposte di un chatbot.", None),
 ("Il gioco del verosimile chiede di ingannare i compagni.", "Per scrivere un falso credibile bisogna capire che cosa rende credibile una frase. Gli studenti scoprono da soli gli ingredienti (numeri, istituzioni, tono sicuro) prima che il docente li nomini.", "errori"),
]
SCELTE["g1o3"] = [
 ("Il modello si costruisce sul foglio di calcolo, non con un programma già pronto.", "Ogni passo (coppie, conteggi, probabilità) è una colonna visibile. Lo studente vede che il modello è una tabella di numeri e non una scatola chiusa.", "costruire"),
 ("Prima si scrivono a mano le coppie di una sola frase.", "Una frase a mano chiarisce che cosa deve fare il foglio; senza questo passo le formule CONTA.SE restano incomprensibili.", "unplugged"),
 ("La generazione usa la regola greedy, non il caso.", "La regola greedy è deterministica: tutti i gruppi possono verificare il risultato. Il caso (con il dado) si introduce solo se avanza tempo, come estensione.", None),
 ("L'ora si chiude chiedendo se la frase generata è vera.", "È il punto d'arrivo della giornata: il modello ha usato fatti, falsi e opinioni senza distinguerli. La risposta la danno gli studenti, guardando le proprie etichette.", "prevedere"),
]
SCELTE["g2o1"] = [
 ("Si comincia ordinando eventi su una scala da 0 a 1.", "Gli studenti hanno già un'idea intuitiva di «probabile». Ordinare eventi familiari collega quell'intuizione a un numero, prima di qualsiasi formula.", "prevedere"),
 ("Ogni coppia scrive 20 risultati, e alcune li inventano.", "Le sequenze inventate rivelano un'idea sbagliata molto diffusa sul caso: chi inventa alterna troppo. Il docente lo dimostra indovinando quali fogli sono inventati.", "errori"),
 ("La probabilità della moneta truccata si aggiorna con i gettoni prima che con l'albero.", "I gettoni trasformano la fiducia in una quantità che si sposta. L'albero arriva dopo, come modo preciso di fare ciò che i gruppi hanno già fatto a intuito.", "frequenze"),
 ("Si fa notare che la probabilità non arriva mai a 1.", "È l'idea più importante dell'ora: molte conferme rendono un'ipotesi più credibile ma non certa. Collega la matematica al modo di ragionare delle scienze e al limite dei modelli.", None),
]
SCELTE["g2o2"] = [
 ("Si apre con un esempio estremo: nove stipendi normali e un miliardario.", "Un esempio estremo rende evidente in pochi secondi perché la media può ingannare. La mediana viene introdotta come risposta a un problema, non come nuova definizione.", "prevedere"),
 ("La deviazione standard si calcola a mano su cinque numeri, in cinque passi.", "Cinque numeri bastano per eseguire tutti i passi senza perdersi nei conti. Dopo averla calcolata a mano, la funzione del foglio di calcolo non è più una scatola chiusa.", "unplugged"),
 ("Prima si scommette su quale insieme è più disperso, poi si calcola.", "La scommessa fa emergere l'intuizione (spesso sbagliata: si sceglie l'insieme con valori tutti diversi). Il calcolo la smentisce e rende interessante il risultato.", "prevedere"),
 ("La stima di r è un gioco a punti.", "Stimare r da un grafico richiede molti esempi. Il gioco permette di vederne sei in pochi minuti, con un riscontro immediato.", "recupero"),
]
SCELTE["g2o3"] = [
 ("Il calcolatore si costruisce una volta e si riusa nella giornata 4.", "Gli studenti scoprono il valore di uno strumento generale: le stesse formule funzionano su dati diversi.", "costruire"),
 ("Si collauda su dati di cui si conosce la risposta.", "Verificare uno strumento prima di usarlo su dati veri è una pratica professionale. Inoltre la differenza tra la retta trovata e quella nascosta introduce la distinzione tra stima e verità.", None),
]
SCELTE["g3o1"] = [
 ("Tre persone cronometrano la stessa prova.", "Tre numeri diversi per la stessa prova mostrano l'errore di misura meglio di qualsiasi spiegazione. Gli studenti vedono che un dato contiene sempre un margine di incertezza.", "prevedere"),
 ("Ogni gruppo scrive un protocollo che un altro gruppo deve poter eseguire.", "Il criterio è concreto e verificabile. Scrivere per un lettore esterno obbliga alla precisione.", "regole"),
 ("Si usano codici estratti a sorte al posto dei nomi.", "Gli studenti applicano la protezione dei dati prima di studiarla, sulle proprie misure.", "dati"),
 ("Il bersaglio nascosto si gioca con il corpo.", "L'apprendimento per rinforzo è un'idea astratta. Lanciare bendati e correggersi solo in base al punteggio la rende un'esperienza fisica che si ricorda.", "unplugged"),
]
SCELTE["g3o2"] = [
 ("La raccolta avviene a postazioni, in due turni.", "Sei postazioni permettono a tutti di eseguire le prove in un'ora senza code. I turni distribuiscono il rumore e lo spazio.", "regole"),
 ("Una casella vuota non si riempie con 0.", "È un errore molto comune anche negli adulti. Fissare la regola prima della raccolta evita di dover correggere dopo.", "errori"),
 ("Prima di consegnare si controlla la completezza.", "Il controllo alla fonte insegna che la qualità dei dati si costruisce durante la raccolta.", "formativa"),
]
SCELTE["g3o3"] = [
 ("Il foglio rifiuta i valori impossibili.", "Gli studenti vedono il computer bloccare un errore prima che entri nei dati: capiscono a che cosa serve una regola di convalida.", None),
 ("Ogni correzione si scrive nel registro.", "Abitua a rendere visibili le modifiche ai dati. Un dato corretto senza traccia è un dato di cui non ci si può più fidare.", "dati"),
 ("Gli stessi fogli si inseriscono due volte.", "Misurare l'errore di trascrizione della classe trasforma un'avvertenza («attenzione agli errori») in un numero concreto.", "prevedere"),
]
SCELTE["g4o1"] = [
 ("Si stima prima di calcolare.", "La stima scritta prima del calcolo rende interessante il risultato e mostra che la media delle stime è spesso vicina al vero.", "prevedere"),
 ("Ogni risultato deve avere un limite.", "Abitua a separare ciò che i dati mostrano da ciò che non possono mostrare. È la stessa prudenza richiesta davanti alle risposte di un modello.", None),
]
SCELTE["g4o2"] = [
 ("I gruppi addestrano un modello vero con oggetti, mai con volti.", "Si vede un modello che impara dagli esempi senza esporre dati personali.", "dati"),
 ("La risposta giusta si scrive prima del test.", "Impedisce di adattare il giudizio a ciò che il modello risponde. È la procedura corretta di valutazione di un modello.", "prevedere"),
 ("Si chiede di ingannare il modello, spiegando prima come.", "Per ingannarlo bisogna capire che cosa ha imparato davvero. È il modo più diretto per scoprire i suoi limiti.", "costruire"),
]
SCELTE["g4o3"] = [
 ("Ogni gruppo presenta un'esperienza in un minuto.", "Spiegare in poco tempo obbliga a scegliere l'essenziale. Le domande dei compagni verificano se l'essenziale è chiaro.", "recupero"),
 ("Il biglietto finale chiede la differenza tra stima e verità.", "È l'idea che attraversa tutte le giornate. Scriverla con un esempio scelto dallo studente mostra se è stata capita.", "recupero"),
]
SCELTE["g5"] = [
 ("La prima parte della giornata è la verifica individuale.", "Dopo quattro giornate di lavoro in gruppo, la verifica mostra che cosa ha acquisito ciascuno. È la condizione di responsabilità individuale del lavoro cooperativo.", "gruppi"),
 ("Il modello si valuta su frutti mai visti, senza poterlo modificare.", "È la stessa regola usata per valutare i modelli reali: un modello si giudica su dati nuovi.", "costruire"),
]
