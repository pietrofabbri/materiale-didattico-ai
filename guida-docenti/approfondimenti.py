# Approfondimenti per chi conduce: perché, concetto, domande degli studenti, criteri, gestione del tempo.
APP = {}

APP["g1o1"] = dict(
 perche="In quest'ora gli studenti scoprono che, per una macchina, un testo è un elenco di parole con le loro frequenze. Tutte le ore successive partono da questa idea.",
 concetto=["Un modello linguistico stima la probabilità della parola successiva date le parole precedenti, a partire dalle frequenze osservate in una grande raccolta di testi. Il gioco di Shannon mostra che, conoscendo le parole precedenti, le parole possibili dopo sono poche: per questo la previsione diventa più facile man mano che la frase procede.",
  "I sistemi attuali usano contesti di migliaia di parole e reti neurali al posto dei semplici conteggi, ma il compito con cui vengono addestrati è lo stesso: prevedere il pezzo di testo successivo. Non contiene alcuna verifica della verità di ciò che si scrive.",
  "Radice e desinenza preparano il concetto di <i>token</i>: i modelli spezzano le parole in frammenti frequenti (ad esempio «mangi» + «avano»), e questo consente loro di trattare forme mai incontrate."],
 domande=[("«Quindi ChatGPT copia dai testi che ha letto?»", "No. Ricombina: sceglie una parola alla volta in base alle probabilità apprese, e può produrre frasi mai scritte da nessuno, comprese frasi false."),
  ("«Allora perché sembra intelligente?»", "Perché la lingua che produce è fluente e pertinente. Se questo basti a chiamarlo intelligenza è una questione aperta; in quest'ora si osserva il meccanismo, non si risolve il dibattito.")],
 criteri=["R1: occorrenze e forme entro ±3 dal valore corretto", "R2: almeno 4 frequenze su 5 corrette", "R3: almeno 5 forme verbali su 6 divise correttamente; l'irregolare segnalato", "R5: due letture distinte", "R6: la risposta cita la probabilità e il fatto che il modello non verifica il vero"],
 tempo=("Saltare la slide facoltativa sui verbi irregolari; far contare solo i primi due periodi del paragrafo.", "Catena dei pappagalli umani: ogni studente aggiunge una parola guardando soltanto l'ultima scritta dal compagno. Il testo che ne esce mostra il limite di un contesto di una sola parola."))

APP["g1o2"] = dict(
 perche="Gli studenti imparano a distinguere vero, falso e opinione: è proprio la distinzione che il modello costruito nell'ora 3 non sa fare. Le frasi che scrivono diventano i dati di quel modello.",
 concetto=["L'etichetta che i gruppi attribuiscono a ogni frase è un'informazione che il modello a coppie non utilizza: per questo, in laboratorio, genererà frasi che mescolano fatti e falsi.",
  "I sistemi reali condividono questo limite di fondo: la plausibilità linguistica non garantisce la verità. Le cosiddette allucinazioni nascono qui. Gli elementi che rendono credibile un falso (un'istituzione citata, un numero preciso, un tono sicuro) sono proprio ciò che un modello linguistico riproduce con maggiore facilità."],
 domande=[("«Se il chatbot cita una fonte, allora è affidabile?»", "Non necessariamente: può citare fonti inesistenti o attribuire a una fonte ciò che non dice. La fonte va aperta e letta."),
  ("«Un'opinione condivisa da tutti diventa un fatto?»", "No. Resta un giudizio. È un fatto solo ciò che si può verificare, indipendentemente da quante persone lo pensino.")],
 criteri=["R2: genere corretto in almeno 5 testi su 6", "R3: otto frasi conformi alle regole; nessuna opinione etichettata come fatto; tre fonti accettabili", "R4: almeno un ingrediente del verosimile individuato correttamente", "R5: fonte primaria indicata e motivata"],
 tempo=("Gioco del verosimile con tre soli gruppi; le cinque domande sulle fonti lette dal docente senza discussione.", "Ogni gruppo trasforma uno dei propri fatti veri in un falso verosimile aggiungendo un solo ingrediente, e la classe individua quale."))

APP["g1o3"] = dict(
 perche="Gli studenti costruiscono un piccolo modello che genera frasi. Scoprono che, in questo caso, «addestrare» un modello significa contare.",
 concetto=["Il modello costruito è un modello a bigrammi, cioè una catena di Markov del primo ordine: la parola successiva dipende solo da quella precedente. La stima P(b | a) = c(a, b) ÷ c(a) è la stima di massima verosimiglianza.",
  "La regola greedy produce sempre la stessa frase. Scegliendo invece a caso secondo le probabilità (l'estensione con il dado) si ottengono frasi diverse a ogni esecuzione: è il comportamento regolato, nei chatbot, dal parametro detto <i>temperatura</i>.",
  "Con 48 frasi molte coppie compaiono una sola volta: è il problema della scarsità dei dati, che i modelli reali affrontano con quantità enormi di testo."],
 domande=[("«Perché genera sempre la stessa frase?»", "Perché la regola greedy è deterministica: sceglie sempre il massimo. Con il dado la scelta diventa casuale e le frasi cambiano."),
  ("«Con più frasi diventerebbe più intelligente?»", "Più fluente, non più veritiero: continuerebbe a contare le parole senza conoscere la verità di ciò che scrive.")],
 criteri=["File corpus_1p.csv con 49 righe", "Coppie: n parole → n − 1 coppie, nessuna coppia tra due frasi", "Le probabilità che seguono una stessa parola sommano a 1", "Ogni passo della generazione sceglie il massimo della tabella", "R4: la spiegazione cita le frequenze, non la verità"],
 tempo=("Ogni gruppo calcola le probabilità solo per due parole a scelta; la generazione si fa insieme al proiettore.", "Generazione con il dado: con due parole a 0,5, da 1 a 3 la prima e da 4 a 6 la seconda."))

APP["g2o1"] = dict(
 perche="Dà un significato preciso alla parola «probabile» usata nella giornata 1, e introduce l'aggiornamento di una convinzione alla luce di un'osservazione: un meccanismo presente in molti sistemi che imparano.",
 concetto=["Si incontrano due modi di intendere la probabilità: quello classico, fondato sulla simmetria dei casi, e quello frequentista, fondato sulla frequenza a lungo termine. I lanci della classe li mettono a confronto.",
  "L'albero della moneta è il teorema di Bayes senza formula: probabilità iniziale 1/2 per ciascuna moneta; probabilità di testa 1 per la truccata e 1/2 per la normale; dopo una testa la truccata sale a 2/3. Una sola osservazione incompatibile (croce) azzera l'ipotesi.",
  "I filtri antispam e molti classificatori aggiornano le probabilità esattamente in questo modo, parola dopo parola o indizio dopo indizio."],
 domande=[("«Dopo cinque teste di fila, è più probabile croce?»", "No. È l'errore del giocatore: i lanci sono indipendenti e la moneta non ha memoria."),
  ("«Con cento teste, è certo che la moneta è truccata?»", "Quasi certo, mai certo: la probabilità si avvicina a 1 senza raggiungerlo.")],
 criteri=["R1: almeno 5 eventi su 6 nell'ordine corretto", "R2: riconosce che con più prove la frequenza si avvicina a 0,5", "R3: conosce il criterio della serie più lunga", "R5: 2/3, 4/5, 8/9", "R6: spiega perché una croce porta a 0 e perché senza croci non si arriva mai a 1"],
 tempo=("Omettere il docente indovino (R3) e ridurre a tre i lanci della moneta del docente.", "Calcolare insieme la probabilità dopo cinque teste (32/33) e discutere quante teste servirebbero per superare il 99%."))

APP["g2o2"] = dict(
 perche="I modelli lavorano con riassunti numerici dei dati. Media, dispersione e correlazione sono gli strumenti con cui, nella giornata 4, la classe analizzerà le proprie misure.",
 concetto=["La media è sensibile ai valori estremi, la mediana no: per questo la mediana descrive meglio redditi e tempi di attesa.",
  "La deviazione standard misura la distanza tipica dei valori dalla media. Nel percorso si usa quella «di popolazione», che divide per n.",
  "Punteggio z e normalizzazione min-max rendono confrontabili grandezze con unità diverse: è un passaggio obbligato quando un modello confronta caratteristiche eterogenee, e lo si ritrova nella giornata 5 con i frutti.",
  "Il coefficiente r misura soltanto legami di tipo rettilineo: un valore vicino a 0 non esclude legami di altra forma. Una correlazione, anche forte, può dipendere da una causa comune."],
 domande=[("«Perché elevare al quadrato invece di usare il valore assoluto?»", "Si potrebbe, ed esiste lo scarto medio assoluto. Il quadrato pesa di più gli scarti grandi e ha proprietà matematiche più comode."),
  ("«r = 0 significa che non c'è alcun legame?»", "Significa che non c'è un legame rettilineo; un legame di altra forma può esistere.")],
 criteri=["R1: valori corretti; scelta della mediana motivata", "R3: deviazione standard corretta entro ±0,02", "R4: z e min-max corretti al secondo decimale", "R5: segno di r corretto in almeno 5 grafici su 6", "R6: una spiegazione non causale plausibile"],
 tempo=("Metà dei gruppi calcola σ di B, l'altra metà di C; si confrontano i risultati senza ripetere il calcolo.", "La classe propone due grandezze scolastiche (ad esempio ore di sonno e ritardi) e stima il segno di r prima di discutere le possibili cause."))

APP["g2o3"] = dict(
 perche="Fissa un'idea centrale dell'informatica: una formula scritta una volta si riusa. Il calcolatore torna nella giornata 4 sui dati veri. Il collaudo sulla 1Z insegna a verificare uno strumento su dati di cui si conosce la risposta.",
 concetto=["Il riferimento assoluto ($B$2) resta fermo quando si trascina la formula, quello relativo (B2) si sposta. La somma cumulata richiede entrambi.",
  "I dati della 1Z sono generati da una retta nota con l'aggiunta di rumore casuale. La regressione stima pendenza e intercetta ma non le ritrova esattamente: è la differenza tra stima e valore vero, che ritorna in ogni giornata.",
  "Verificare un metodo su dati sintetici, di cui si conosce la verità, è una pratica comune anche nello sviluppo dei modelli di apprendimento automatico."],
 domande=[("«Se la retta non coincide con la formula nascosta, abbiamo sbagliato?»", "No: con il rumore e pochi dati la stima differisce sempre un poco dal valore vero. Con più dati si avvicinerebbe.")],
 criteri=["Formule corrette fino all'ultima riga", "Collaudo: 4,10 · 1,497 · −0,84 · −0,51 · 9,92", "Modificando un dato, tutto si aggiorna senza riscrivere formule", "R3: almeno una ragione della differenza tra stima e verità"],
 tempo=("Distribuire il calcolatore con metà delle formule già scritte.", "Raddoppiare i dati della 1Z con la stessa formula nascosta e osservare la stima avvicinarsi al valore vero."))

APP["g3o1"] = dict(
 perche="Ogni dato è il risultato di una misura fatta da qualcuno, e ogni misura contiene un errore. In quest'ora gli studenti lo vedono con i propri numeri e imparano a proteggere i dati delle persone.",
 concetto=["L'errore casuale si riduce ripetendo e facendo la media; l'errore sistematico no, perché sposta tutte le misure nello stesso verso, e si corregge solo cambiando la procedura. Un modello addestrato su dati affetti da errore sistematico lo eredita.",
  "Il protocollo garantisce la riproducibilità: misure confrontabili solo se raccolte nello stesso modo.",
  "Il codice estratto a sorte è una pseudonimizzazione: i dati restano riconducibili alla persona solo per chi conosce la corrispondenza. Per questo l'elenco codice-nome non si scrive da nessuna parte.",
  "Il bersaglio nascosto riproduce l'apprendimento per rinforzo e il suo dilemma tipico: insistere su ciò che ha funzionato o esplorare alternative."],
 domande=[("«Se ripetiamo tante volte, l'errore sparisce?»", "Solo quello casuale. Quello sistematico resta identico a ogni ripetizione."),
  ("«Perché non usare i nomi, visto che siamo tra noi?»", "Per abitudine alla protezione dei dati: si raccolgono solo le informazioni necessarie e nel modo meno identificabile possibile.")],
 criteri=["R1: scarto calcolato correttamente", "R2: i due errori distinti, con un rimedio", "R3: protocollo eseguibile da un altro gruppo senza domande", "R4: strategia eseguibile e punteggio totale corretto", "R5: agente, azione, ricompensa, strategia: 4 su 4"],
 tempo=("Bersaglio nascosto con tre soli volontari.", "Confrontare due strategie diverse sullo stesso volontario e discutere quale ha imparato più in fretta."))

APP["g3o2"] = dict(
 perche="Produce il dataset della classe e mette alla prova i protocolli scritti nell'ora precedente.",
 concetto=["Un dato mancante non è uno zero: scrivere 0 abbasserebbe la media e introdurrebbe un errore invisibile.",
  "Le note sono metadati: conservano informazioni che il numero da solo non contiene (una prova disturbata, un cronometro partito in ritardo).",
  "Controllare la qualità al momento della raccolta costa molto meno che correggere dopo."],
 domande=[("«Se perdo l'equilibrio dopo due secondi posso rifare?»", "Si segue il protocollo scritto nell'ora 1. Se prevede una ripetizione, la si annota nelle note."),
  ("«Devo per forza fare la prova?»", "No. La casella resta vuota e si annota il motivo, senza ulteriori dettagli.")],
 criteri=["Nessun nome sui fogli", "Nessuno 0 al posto di una prova mancante", "Anomalie annotate nelle note", "Mancanze individuate prima della consegna"],
 tempo=("Una sola prova di equilibrio a testa.", "Ogni gruppo misura due volte lo stesso compagno per stimare l'errore della propria postazione."))

APP["g3o3"] = dict(
 perche="Trasforma i fogli di carta in un dataset affidabile e mostra un fatto poco noto: la parte più lunga del lavoro con i dati è la pulizia.",
 concetto=["La convalida impone vincoli di dominio (un tempo tra 0 e 60 secondi). Non intercetta però tutti gli errori: un valore possibile ma sbagliato passa.",
  "Le condizioni E e O e la loro relazione (legge di De Morgan) sono il linguaggio con cui si scrivono i controlli.",
  "Il registro delle modifiche garantisce la tracciabilità: ogni correzione è visibile e motivata.",
  "Il doppio inserimento degli stessi fogli permette di stimare l'errore di trascrizione, di solito qualche punto percentuale."],
 domande=[("«Perché non correggere a occhio i valori strani?»", "Perché una correzione non documentata è una modifica invisibile ai dati, e nessuno potrà più verificarla.")],
 criteri=["Il rifiuto del valore 600 letto e spiegato", "Quattro controlli funzionanti", "Ogni modifica registrata con il motivo", "Percentuale di errori di trascrizione calcolata correttamente", "R4: O(x < 0; x > 60)"],
 tempo=("Il confronto tra i due inserimenti lo esegue il docente al proiettore.", "Gli studenti scrivono da soli la regola di convalida per la colonna dei lanci."))

APP["g4o1"] = dict(
 perche="Riporta tutti gli strumenti delle giornate precedenti sui dati veri della classe e insegna a formulare una conclusione insieme al suo limite.",
 concetto=["La media delle stime individuali è spesso vicina al valore vero, più della maggior parte delle stime singole: il fenomeno è detto saggezza della folla.",
  "Una tabella pivot raggruppa e riassume; il numero di persone in ogni gruppo va sempre riportato, perché un gruppo piccolo produce medie instabili.",
  "Scrivere la previsione sul segno di r prima di calcolarlo evita di adattare a posteriori la spiegazione al risultato."],
 domande=[("«Chi usa la mano sinistra lancia meglio?»", "I dati della classe possono suggerirlo, ma con gruppi così piccoli non lo dimostrano: è il limite da scrivere accanto alla scoperta.")],
 criteri=["R1: confronto tra stima, valore calcolato e media delle stime", "R3: pivot con media e conteggio", "R4: previsione scritta prima del calcolo", "R5: scoperta con un numero, un grafico e un limite pertinente"],
 tempo=("Il grafico di dispersione si costruisce insieme al proiettore.", "Ogni gruppo cerca una seconda scoperta e la presenta in trenta secondi."))

APP["g4o2"] = dict(
 perche="È il primo contatto diretto con un modello che impara dagli esempi, e mostra che le sue prestazioni dipendono interamente dagli esempi ricevuti.",
 concetto=["Nell'apprendimento supervisionato ogni esempio è accompagnato dalla risposta corretta. Il modello si valuta su esempi che non ha mai visto: è l'unico modo di sapere se ha imparato o se ha solo memorizzato.",
  "L'esempio ingannevole funziona quando sfrutta ciò che gli esempi di addestramento non mostravano: uno sfondo diverso, un'illuminazione diversa, un oggetto nuovo. È lo stesso meccanismo dei pregiudizi nei modelli reali."],
 domande=[("«Il modello ha capito che cos'è una penna?»", "Ha imparato a riconoscere le immagini simili a quelle che ha visto. Se tutte le penne erano su sfondo bianco, potrebbe aver imparato lo sfondo.")],
 criteri=["R1: esempio ed etichetta individuati correttamente", "R2: tre classi, almeno 20 esempi ciascuna, nessun volto né corpo", "R3: risposte corrette scritte prima del test", "R4: accuratezza calcolata correttamente", "R5: spiegazione fondata sugli esempi di addestramento"],
 tempo=("Due classi invece di tre.", "Ripetere l'addestramento con esempi più vari e confrontare le due accuratezze."))

APP["g4o3"] = dict(
 perche="Obbliga ogni gruppo a ricostruire il senso del percorso e a comunicarlo con precisione, distinguendo ciò che i dati mostrano da ciò che non possono mostrare.",
 concetto=["Il biglietto finale sulla differenza tra stima e verità è la verifica più diretta dell'obiettivo del percorso: chi lo scrive bene ha colto il punto."],
 domande=[("«Che cosa dobbiamo dire se ci fanno una domanda a cui non sappiamo rispondere?»", "Dichiarare il limite: «i nostri dati non permettono di dirlo». È una risposta corretta."),],
 criteri=["Scheda completa con soli dati aggregati", "Osservazione motivata nella prova incrociata", "Presentazione entro 60 secondi", "Biglietto: esempio corretto di differenza tra stima e verità"],
 tempo=("Presentazioni di tre gruppi soltanto.", "La classe vota la domanda più difficile ricevuta e la discute insieme."))

APP["g5"] = dict(
 perche="La giornata si apre con la verifica individuale, su cui si basa il voto finale. Nel resto del tempo si recupera ciò che è rimasto indietro, oppure si costruisce un classificatore completo.",
 concetto=["Il metodo dei k vicini classifica un elemento guardando i k elementi noti più simili. «Simile» significa vicino secondo una distanza, che dipende dalle unità di misura: senza normalizzazione il peso in grammi domina la larghezza in centimetri.",
  "Il torneo sui frutti segreti, eseguito senza modificare il modello, è la stessa procedura con cui si valutano i modelli reali. L'errore sul frutto S7 mostra che nessun modello può usare un'informazione che non ha ricevuto: il colore."],
 domande=[("«Quale k è il migliore?»", "Dipende dai dati: k troppo piccolo segue il rumore, k troppo grande cancella le differenze. Per questo si sceglie motivando e si verifica su dati nuovi.")],
 criteri=["Distanza calcolata correttamente", "Spiegazione del cambio di verdetto che cita le unità di misura", "Tre scelte di progetto motivate e una previsione scritta", "Accuratezza corretta; errore di S7 spiegato con il dato mancante"],
 tempo=("La verifica non si riduce. Se la classe è indietro, le ore 2 e 3 servono al recupero.", "Aggiungere il colore come caratteristica e ripetere il torneo."))
