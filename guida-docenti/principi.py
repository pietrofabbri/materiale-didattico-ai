# Livello 3: principi didattici su cui si regge il percorso.
# Ogni principio: titolo, in breve, che cosa dice la ricerca, dove compare nel percorso, limiti e attenzioni, fonti.
PRINCIPI = {}

PRINCIPI["esempio"] = dict(
 titolo="L'esempio svolto prima dell'esercizio",
 breve="Uno studente che affronta un compito nuovo impara di più se vede prima un esempio risolto passo per passo.",
 ricerca=["Chi impara qualcosa di nuovo ha una memoria di lavoro limitata: riesce a tenere a mente pochi elementi alla volta. Se deve contemporaneamente capire la consegna, inventare un procedimento e controllarlo, la memoria si satura e impara poco.",
  "Un esempio svolto toglie una parte di questo carico: lo studente vede il procedimento già fatto e può concentrarsi sul capirlo. Gli studi di John Sweller e colleghi, a partire dagli anni Ottanta, hanno mostrato che i principianti che studiano esempi svolti ottengono risultati migliori di quelli che risolvono subito problemi da soli. In letteratura si parla di <i>worked example effect</i>.",
  "L'effetto si riduce, fino a invertirsi, quando lo studente diventa esperto: a quel punto l'esempio è ridondante. Per questo gli esempi vanno poi ritirati gradualmente."],
 percorso=["Ogni attività ha un esempio svolto subito dopo la consegna e prima del timer. È una regola fissa del percorso.",
  "Le attività successive di uno stesso tipo hanno esempi più brevi: ad esempio, in radice e desinenza, il primo esempio mostra tutti e tre i passi, l'esercizio chiede di applicarli senza aiuto."],
 limiti=["Un esempio troppo simile all'esercizio porta a copiare la forma senza capire il procedimento. Gli esempi del percorso usano parole o numeri diversi da quelli dell'esercizio.",
  "L'esempio va commentato a voce in pochi secondi: indicare il passo che di solito si sbaglia."],
 fonti=["Sweller J., Cooper G. A. (1985), The use of worked examples as a substitute for problem solving in learning algebra, Cognition and Instruction.", "Sweller J., Ayres P., Kalyuga S. (2011), Cognitive Load Theory, Springer."])

PRINCIPI["prevedere"] = dict(
 titolo="Prevedere prima di verificare",
 breve="Chiedere agli studenti di scrivere una previsione prima di un calcolo o di un esperimento rende visibile ciò che pensano davvero.",
 ricerca=["Gli studenti arrivano in classe con idee proprie su come funzionano le cose. Se si mostra direttamente il risultato, queste idee restano nascoste e spesso sopravvivono alla lezione.",
  "La sequenza prevedere, osservare, spiegare (in inglese <i>Predict, Observe, Explain</i>), descritta da White e Gunstone, obbliga lo studente a impegnarsi su una risposta. Quando il risultato contraddice la previsione, la discrepanza diventa l'occasione per correggere l'idea.",
  "Una previsione scritta ha più effetto di una detta a voce, perché non si può aggiustare dopo aver visto il risultato."],
 percorso=["Giornata 2: scommessa su quale insieme è più disperso, prima di calcolare la deviazione standard.", "Giornata 2: stima di r dai grafici prima del valore vero.", "Giornata 4: segno della correlazione scritto prima del calcolo; stima della media prima del calcolo.", "Giornata 5: previsione dell'accuratezza prima del torneo."],
 limiti=["La previsione non va valutata come giusta o sbagliata: serve a far emergere il ragionamento. Se si penalizza l'errore, gli studenti smettono di sbilanciarsi.", "Dopo il risultato bisogna sempre chiedere: perché la previsione era diversa? È questa domanda che produce apprendimento."],
 fonti=["White R., Gunstone R. (1992), Probing Understanding, Falmer Press."])

PRINCIPI["recupero"] = dict(
 titolo="Richiamare dalla memoria",
 breve="Ricordare un'informazione senza guardarla la consolida più che rileggerla.",
 ricerca=["Lo sforzo di recuperare un'informazione dalla memoria rafforza il ricordo. In un esperimento noto di Roediger e Karpicke, gli studenti che dopo una lettura si erano messi alla prova ricordavano a distanza di una settimana molto più di quelli che avevano riletto il testo più volte.",
  "Il fenomeno si chiama <i>effetto del test</i> o <i>pratica di recupero</i>. Funziona anche con prove brevi e senza voto."],
 percorso=["Le tre domande di controllo alla fine di ogni ora, a cui si risponde da soli e senza guardare il foglio.", "La riga del formulario, copiata a fine ora e ripresa nella giornata successiva.", "La verifica individuale della giornata 5, che richiama i concetti di tutte le giornate."],
 limiti=["Le domande devono chiedere di ricordare e usare un concetto, non di riconoscere una parola. Le domande del percorso chiedono un calcolo, un esempio o una spiegazione breve."],
 fonti=["Roediger H. L., Karpicke J. D. (2006), Test-enhanced learning, Psychological Science.", "Agarwal P. K., Bain P. M. (2019), Powerful Teaching, Jossey-Bass."])

PRINCIPI["formativa"] = dict(
 titolo="Verificare durante, non solo alla fine",
 breve="Raccogliere spesso informazioni su che cosa la classe ha capito, e cambiare la lezione di conseguenza.",
 ricerca=["La revisione di Black e Wiliam (1998) ha raccolto numerosi studi sulla valutazione usata durante l'apprendimento, detta formativa. La conclusione è che migliora i risultati, soprattutto quando il docente usa davvero le informazioni raccolte per modificare l'insegnamento.",
  "Una verifica formativa non serve a dare un voto: serve a decidere che cosa fare dopo."],
 percorso=["Le tre domande di fine ora hanno una regola di decisione esplicita: se meno di metà classe risponde correttamente a una domanda, l'argomento si riprende all'inizio dell'ora successiva.", "I fogli dell'ora mostrano al docente, gruppo per gruppo, dove il lavoro si è inceppato."],
 limiti=["Se gli studenti sanno che le domande di fine ora entrano nel voto, tendono a copiare. Nel percorso il voto deriva dalla verifica della giornata 5 e dai prodotti dei gruppi, non dalle domande di controllo."],
 fonti=["Black P., Wiliam D. (1998), Assessment and classroom learning, Assessment in Education.", "Wiliam D. (2011), Embedded Formative Assessment, Solution Tree."])

PRINCIPI["errori"] = dict(
 titolo="Le idee sbagliate più frequenti",
 breve="Alcuni errori non nascono da distrazione ma da intuizioni sbagliate molto diffuse. Vanno fatti emergere e discussi apertamente.",
 ricerca=["Sulla probabilità sono documentati errori sistematici anche negli adulti. Il più noto è la <i>fallacia del giocatore</i>: dopo una serie di teste si pensa che croce sia più probabile. Tversky e Kahneman hanno descritto questi errori come effetti di scorciatoie mentali.",
  "Un altro errore frequente è credere che una sequenza «disordinata» sia più casuale di una con lunghe serie uguali. Chi inventa sequenze casuali alterna troppo, ed è per questo che il docente riesce a riconoscere i fogli inventati.",
  "Sui dati, l'errore più comune è confondere correlazione e causa."],
 percorso=["Giornata 2, ora 1: l'attività dei dati inventati fa emergere l'idea sbagliata di casualità; la domanda «dopo cinque teste è più probabile croce?» affronta la fallacia del giocatore.", "Giornata 2, ora 2: gelati e annegamenti per correlazione e causa.", "Giornata 1: «il chatbot cita una fonte, quindi è affidabile»."],
 limiti=["Correggere un'idea sbagliata a voce raramente basta. Funziona meglio quando lo studente vede un risultato che contraddice la propria idea (vedi «Prevedere prima di verificare»)."],
 fonti=["Tversky A., Kahneman D. (1974), Judgment under uncertainty: heuristics and biases, Science."])

PRINCIPI["frequenze"] = dict(
 titolo="Contare casi invece di moltiplicare frazioni",
 breve="I ragionamenti sulle probabilità diventano molto più facili se si esprimono come numeri di casi.",
 ricerca=["Gigerenzer e Hoffrage hanno mostrato che molte persone sbagliano i problemi di probabilità condizionata quando sono scritti con percentuali, e li risolvono molto più spesso quando gli stessi dati sono scritti come frequenze («su 100 casi, 10…»).",
  "Questo formato si chiama <i>frequenze naturali</i>. Non cambia la matematica: cambia il modo in cui il problema si presenta."],
 percorso=["Giornata 2, ora 1: i gettoni spostati tra «normale» e «truccata» rappresentano la fiducia come quantità contabile.", "L'albero si può leggere anche così: su 4 lanci immaginari, 1 dà testa con la moneta normale e 2 con la truccata; quindi, sapendo che è uscita testa, 2 casi su 3 sono della truccata."],
 limiti=["Il formato a frequenze aiuta a capire, ma gli studenti devono poi saper passare alle frazioni: la verifica chiede entrambi."],
 fonti=["Gigerenzer G., Hoffrage U. (1995), How to improve Bayesian reasoning without instruction: frequency formats, Psychological Review."])

PRINCIPI["costruire"] = dict(
 titolo="Imparare costruendo",
 breve="Si capisce a fondo come funziona una cosa quando la si costruisce, anche in una versione molto semplice.",
 ricerca=["Seymour Papert chiamò <i>costruzionismo</i> l'idea che si impari particolarmente bene costruendo oggetti concreti e condivisibili. L'oggetto costruito rende il ragionamento visibile e discutibile.",
  "Gli studi sull'apprendimento attivo nelle discipline scientifiche (ad esempio la meta-analisi di Freeman e colleghi, 2014) mostrano che le lezioni in cui gli studenti lavorano attivamente producono risultati migliori della sola lezione frontale."],
 percorso=["Gli studenti non ricevono una spiegazione di che cos'è un modello linguistico: ne costruiscono uno (giornata 1), costruiscono un calcolatore (giornata 2), un dataset (giornata 3), un modello che riconosce oggetti (giornata 4), un classificatore (giornata 5)."],
 limiti=["Costruire senza guida porta a perdersi. Ogni costruzione del percorso è guidata passo per passo, con esempi svolti: l'autonomia arriva alla fine (giornata 5), non all'inizio."],
 fonti=["Papert S. (1980), Mindstorms, Basic Books.", "Freeman S. et al. (2014), Active learning increases student performance in science, engineering, and mathematics, PNAS."])

PRINCIPI["unplugged"] = dict(
 titolo="Prima a mano, poi al computer",
 breve="Un procedimento eseguito a mano su un esempio piccolo si capisce meglio di uno eseguito subito dal computer.",
 ricerca=["Il progetto CS Unplugged, nato in Nuova Zelanda negli anni Novanta, propone di insegnare i concetti dell'informatica con attività senza computer: carte, corde, giochi di movimento.",
  "L'idea è separare il concetto dallo strumento. Se il computer esegue il calcolo prima che lo studente l'abbia capito, il risultato appare come una magia."],
 percorso=["Si contano le parole a mano (giornata 1, ora 1) prima di contarle con il foglio di calcolo (ora 3).", "Le coppie di una frase si scrivono a mano in R1 prima di inserirle nel foglio.", "La deviazione standard si calcola su cinque numeri prima di usare la funzione DEV.ST.POP.", "Il bersaglio nascosto mostra l'apprendimento per rinforzo con il corpo."],
 limiti=["L'esempio a mano deve essere piccolo: pochi numeri o una frase. Il computer serve proprio quando i dati sono troppi per farlo a mano, ed è utile farlo notare."],
 fonti=["Bell T., Witten I. H., Fellows M. (1998, edizioni successive), Computer Science Unplugged, csunplugged.org."])

PRINCIPI["gruppi"] = dict(
 titolo="Il lavoro di gruppo che funziona",
 breve="Un gruppo lavora bene quando ognuno ha bisogno degli altri per riuscire e quando il contributo di ciascuno è visibile.",
 ricerca=["David e Roger Johnson, dopo decenni di studi sull'apprendimento cooperativo, indicano due condizioni principali: l'interdipendenza positiva (il gruppo riesce solo se tutti contribuiscono) e la responsabilità individuale (ognuno risponde del proprio apprendimento).",
  "Senza la seconda condizione compare il fenomeno noto: uno lavora, gli altri guardano."],
 percorso=["Interdipendenza: un solo foglio per gruppo, con riquadri da completare insieme; chi scrive cambia a ogni attività.", "Responsabilità individuale: le tre domande di fine ora sono individuali; la verifica della giornata 5 è individuale; nel voto finale il prodotto del gruppo pesa meno della prova individuale.", "Gruppi diversi a ogni giornata: ogni studente lavora con quasi tutti i compagni, e i gruppi non si cristallizzano in ruoli fissi (chi fa sempre, chi non fa mai)."],
 limiti=["Il percorso non assegna ruoli fissi (segretario, portavoce…): è una scelta per semplicità, ma richiede che il docente controlli girando tra i banchi che la penna passi di mano.", "Gruppi casuali possono mettere insieme studenti in conflitto: il docente può sempre correggere il sorteggio prima di confermarlo."],
 fonti=["Johnson D. W., Johnson R. T. (2009), An educational psychology success story: social interdependence theory and cooperative learning, Educational Researcher."])

PRINCIPI["regole"] = dict(
 titolo="Routine prevedibili",
 breve="Se ogni ora ha la stessa struttura, gli studenti spendono meno energia per capire che cosa fare e più per capire il contenuto.",
 ricerca=["Barak Rosenshine ha riassunto in dieci principi i comportamenti dei docenti più efficaci, ricavati dalla ricerca e dall'osservazione in classe. Tra questi: presentare il nuovo materiale a piccoli passi, fornire esempi, guidare la pratica, controllare spesso la comprensione.",
  "Le routine prevedibili riducono il tempo perso nelle transizioni e i comportamenti di disturbo che nascono dall'incertezza."],
 percorso=["Ogni attività ha la stessa sequenza: consegna, con chi, dove si scrive, esempio, tempo, soluzione.", "Il timer rende visibile il tempo; il barattolo del rumore rende visibile il volume. Entrambi spostano la regolazione dalla voce del docente a un segnale neutro."],
 limiti=["La routine non deve diventare rigidità: il timer si può fermare, il blocco del barattolo si può disattivare (tasto K)."],
 fonti=["Rosenshine B. (2012), Principles of Instruction, American Educator."])

PRINCIPI["dati"] = dict(
 titolo="Dati personali: raccogliere il minimo",
 breve="Si raccolgono solo i dati necessari, nel modo meno riconducibile alla persona, e li si usa solo per lo scopo dichiarato.",
 ricerca=["Il Regolamento europeo sulla protezione dei dati (GDPR, articolo 5) stabilisce il principio di minimizzazione: i dati devono essere adeguati, pertinenti e limitati a quanto necessario.",
  "A scuola il principio ha anche un valore educativo: gli studenti, che producono ogni giorno dati sulle piattaforme, vedono applicata una regola che li riguarda."],
 percorso=["Codici estratti a sorte al posto dei nomi; nessun elenco codice-nome.", "Nessun dato su peso, altezza o salute.", "Nessun volto nei modelli di riconoscimento.", "Sullo schermo solo dati aggregati; nessuna classifica."],
 limiti=["I numeri del registro scritti sul foglio dell'ora servono solo al docente di informatica per attribuire il punteggio del prodotto; non compaiono mai sullo schermo."],
 fonti=["Regolamento (UE) 2016/679, articolo 5."])

PRINCIPI["attesa"] = dict(
 titolo="Il tempo di attesa dopo una domanda",
 breve="Dopo una domanda alla classe conviene aspettare almeno tre secondi prima di dare la parola o la risposta.",
 ricerca=["Mary Budd Rowe registrò centinaia di lezioni di scienze. In media i docenti aspettavano circa un secondo tra la domanda e l'intervento successivo: se nessuno rispondeva subito, riformulavano, davano un indizio o rispondevano da soli.",
  "Nelle classi in cui i docenti impararono ad aspettare tre secondi o più, le risposte diventarono più lunghe, risposero più studenti, diminuirono i «non lo so» e aumentarono le risposte motivate.",
  "Un secondo basta solo per ricordare. Per ragionare serve più tempo; chi non ha questo tempo smette di provare e lascia rispondere i più veloci."],
 percorso=["Le domande alla classe si pongono, si aspetta, poi si chiama un numero di registro estratto a sorte.", "Le tre domande di controllo si scrivono da soli, quindi ognuno ha il proprio tempo."],
 limiti=["Il silenzio dopo una domanda può sembrare tempo perso: va annunciato («vi do qualche secondo per pensare»).", "Per domande di puro richiamo (una definizione) l'attesa lunga non serve."],
 fonti=["Rowe M. B. (1974), Wait-time and rewards as instructional variables, Journal of Research in Science Teaching, 11(2).", "Rowe M. B. (1986), Wait time: slowing down may be a way of speeding up!, Journal of Teacher Education, 37(1)."])

PRINCIPI["tutti"] = dict(
 titolo="Domande a tutti, non solo a chi alza la mano",
 breve="Se rispondono solo i volontari, il docente sa che cosa hanno capito i volontari, non la classe.",
 ricerca=["Quando si chiede «chi lo sa?», alzano la mano quasi sempre gli stessi studenti, di solito quelli che hanno già capito. Gli altri imparano che possono non pensare alla domanda.",
  "Dylan Wiliam propone di non usare le mani alzate per le domande di verifica: si sceglie lo studente a caso, oppure si chiede a tutti una risposta scritta. Così ogni studente ha un motivo per pensare e il docente riceve un'informazione rappresentativa.",
  "Tra i principi di Rosenshine c'è lo stesso punto: fare molte domande e controllare le risposte di tutti gli studenti."],
 percorso=["Il sorteggio dei gruppi e le domande alla classe usano i numeri del registro estratti a sorte.", "Le domande di controllo di fine ora sono individuali e scritte: il docente vede le risposte di tutti, non solo di chi parla."],
 limiti=["Chiamare a caso funziona se l'errore non viene punito: chi sbaglia va ringraziato, perché la sua risposta è utile alla classe.", "Uno studente in difficoltà può dire «passo», a patto che poi ripeta la risposta di un compagno."],
 fonti=["Wiliam D. (2011), Embedded Formative Assessment, Solution Tree.", "Rosenshine B. (2012), Principles of Instruction, American Educator."])

PRINCIPI["feedback"] = dict(
 titolo="Il riscontro sul lavoro, non sulla persona",
 breve="Un riscontro aiuta se dice allo studente dove deve arrivare, a che punto è e quale passo fare adesso.",
 ricerca=["Kluger e DeNisi hanno analizzato più di seicento confronti sperimentali: in media il riscontro migliora i risultati, ma in circa un caso su tre li peggiora. Peggiora soprattutto quando sposta l'attenzione dal compito alla persona, come le lodi generiche o i giudizi sul carattere.",
  "Hattie e Timperley riassumono un riscontro utile in tre domande: dove sto andando? A che punto sono? Qual è il passo successivo? Il riscontro più efficace riguarda il compito e il procedimento («la frequenza relativa va divisa per il totale delle parole, non per le parole diverse»), non la persona («sei bravo»)."],
 percorso=["Girando tra i gruppi, il docente commenta i riquadri del foglio: che cosa è corretto, che cosa manca, quale passo fare.", "Le soluzioni sulle slide (tasto freccia) permettono a ogni gruppo di confrontare subito il proprio lavoro.", "La griglia di valutazione dei fogli guarda il lavoro (completezza, correttezza, regole), non chi l'ha fatto."],
 limiti=["Un riscontro che arriva troppo tardi (giorni dopo) serve poco: per questo le soluzioni sono nella stessa ora.", "Dare subito la soluzione a un gruppo bloccato toglie il ragionamento: meglio indicare il primo passo."],
 fonti=["Kluger A. N., DeNisi A. (1996), The effects of feedback interventions on performance, Psychological Bulletin, 119(2).", "Hattie J., Timperley H. (2007), The power of feedback, Review of Educational Research, 77(1)."])

PRINCIPI["impalcatura"] = dict(
 titolo="L'aiuto graduato",
 breve="Si aiuta lo studente quanto basta per fare il passo che da solo non farebbe, e poi si toglie l'aiuto.",
 ricerca=["Vygotskij chiamava «zona di sviluppo prossimale» la distanza tra ciò che uno studente sa fare da solo e ciò che sa fare con l'aiuto di qualcuno più esperto. L'insegnamento è utile soprattutto in questa zona.",
  "Wood, Bruner e Ross osservarono come un adulto aiutava bambini a costruire una piramide di blocchi. Chiamarono «scaffolding» (impalcatura) il suo modo di aiutare: semplificare il compito, indicare ciò che conta, tenere la direzione, mostrare come si fa, e intervenire sempre meno man mano che il bambino riusciva da solo.",
  "Il punto decisivo è togliere l'aiuto. Un aiuto che resta sempre uguale crea dipendenza."],
 percorso=["Il foglio dell'ora divide il compito in riquadri piccoli e ordinati.", "Gli esempi svolti si accorciano nel corso dell'ora.", "Con un gruppo bloccato il docente procede per gradi: rilegge la consegna; indica l'esempio; chiede il primo passo; solo alla fine mostra il primo passo."],
 limiti=["Se l'aiuto è troppo, lo studente esegue senza capire. Se è troppo poco, rinuncia. Si regola guardando il riquadro del foglio, non chiedendo «avete capito?»."],
 fonti=["Wood D., Bruner J. S., Ross G. (1976), The role of tutoring in problem solving, Journal of Child Psychology and Psychiatry, 17(2).", "Vygotskij L. S. (1934), Pensiero e linguaggio (trad. it. Laterza)."])
