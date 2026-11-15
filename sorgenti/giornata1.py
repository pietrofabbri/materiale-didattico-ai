from g import *

PAR = ("Ogni mattina il treno parte dalla stazione alle sette. Il treno è quasi sempre pieno di studenti che vanno a scuola. "
       "Alcuni studenti leggono, altri ascoltano la musica e molti guardano il telefono. Quando il treno arriva in città, "
       "gli studenti scendono di corsa, perché la prima ora comincia alle otto e il professore di matematica non aspetta nessuno. "
       "La sera il treno riporta tutti a casa.")

def build():
    S, F = [], []
    S.append(titolo_giornata(1, "La lingua come dati",
        "Come fa una macchina a «parlare» se non sa che cosa dice?",
        [("Ora 1 · Italiano", "Le parole come dati: contare, prevedere, capire il contesto"),
         ("Ora 2 · Italiano", "Vero, verosimile, opinione: scriviamo le nostre frasi"),
         ("Ora 3 · Laboratorio", "Dalle nostre frasi a un modello che genera frasi")],
        note="Prima della lezione: tarare il barattolo (B, poi T) e provare il sorteggio dei gruppi. Stampare 6 copie del foglio di ciascuna ora (file fogli-giornata-1.html, A3 orizzontale). Pezzi per l'installazione finale: il corpus della classe e le frasi generate dal pappagallo."))

    # ================================================================ ORA 1
    R = [("R1", "Conteggi", "Occorrenze: ____   Forme diverse: ____   (con l'elenco delle forme e le tacche)", 1),
         ("R2", "Parole più frequenti", "Le 5 parole più frequenti, ciascuna con la frequenza relativa (occorrenze / totale).", 1),
         ("R3", "Radici e desinenze", "Per ogni parola: radice, desinenza, che cosa dice la desinenza.", 1),
         ("R4", "Gioco di Shannon", "La parola che prevedete, una per riga. Alla fine: quante ne avete indovinate?", 1),
         ("R5", "Due significati", "La frase, i due significati, la parola che crea il doppio senso.", 1),
         ("R6", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((1, "Le parole come dati", R))
    S.append(ora(1, "Italiano", "Le parole come dati", "Contare, prevedere, capire il contesto",
        "scoprire perché una macchina può indovinare la parola successiva.",
        note="0-3 min. Accoglienza, presentazione del percorso in una frase: in quattro giornate scopriamo come impara una macchina usando i nostri dati."))
    S.append(obiettivi([
        "contare le <b>occorrenze</b> e le <b>forme diverse</b> di un testo",
        "calcolare la <b>frequenza relativa</b> di una parola",
        "dividere una parola in <b>radice</b> e <b>desinenza</b> e dire che cosa dice la desinenza",
        "<b>prevedere</b> la parola successiva e spiegare perché ci riesci",
        "trovare i <b>due significati</b> di una frase ambigua",
        "dire che cosa fa un <b>pappagallo stocastico</b>"]))
    S.append(sorteggio("Ogni giornata ha gruppi nuovi, sorteggiati con i numeri del registro. Quando compare il vostro gruppo, andate all'isola del suo colore. Avete un minuto.",
        note="Inserire gli assenti e premere Sorteggia. Le isole hanno il cartellino colorato. Nessun nome sullo schermo: solo i numeri del registro."))
    S.append(spiega("Come lavoriamo", occhiello="Le regole delle quattro giornate",
        carte=[("Il foglio dell'ora", ["Un foglio grande per gruppo, con riquadri numerati: R1, R2…", "Le slide dicono in quale riquadro scrivere. Niente nomi: solo il numero del gruppo."], "#2C8BC9"),
               ("Il timer", ["In alto a destra: quanto tempo resta.", "Quando suona, si alza la penna."], "#3A8A3E"),
               ("Il barattolo", ["Sente solo quanto è forte il rumore, non le parole, e non registra niente.", "Se il rumore resta troppo alto, lo schermo si ferma: si riparte quando torna la calma."], "#DB6A1C")],
        note="Il barattolo è quello del Progetto 16. Dire: protegge le voci più basse; vale anche per il docente; nei lavori di gruppo è regolato per la discussione; se scatta: smettere di parlare, appoggiare quello che si ha in mano, fare un respiro."))

    S.append(spiega("Quante parole ci sono?", occhiello="Domanda",
        formula="il gatto e il cane",
        testo=["Scrivete un numero su un foglietto. Poi confrontiamo."],
        risposta=["Due risposte giuste, perché contano cose diverse.",
                  "<b>Occorrenze</b>: tutte le parole, anche ripetute: il, gatto, e, il, cane = <b>5</b>.",
                  "<b>Forme diverse</b>: le parole diverse: il, gatto, e, cane = <b>4</b>."],
        dopo=["Le occorrenze non sono mai meno delle forme. In informatica le occorrenze si chiamano anche token."],
        note="3-6 min. Lasciare scrivere, raccogliere a voce le risposte (di solito 5 e 4), poi freccia per la risposta."))
    S.append(spiega("Le regole per contare", occhiello="Perché tutti i gruppi ottengano lo stesso numero",
        punti=["maiuscole e minuscole sono la stessa forma: «Il» e «il» contano come una forma sola",
               "la punteggiatura non si conta",
               "scritture diverse sono forme diverse: «gatto» e «gatti» sono due forme",
               "una parola con l'apostrofo si conta da sola: «l'» è una forma"],
        esempio=["«Il sole e il mare e il vento»", "Occorrenze: il, sole, e, il, mare, e, il, vento = <b>8</b>.",
                 "Forme: il (3 volte), sole, e (2 volte), mare, vento = <b>5</b>."],
        note="6-7 min. Se la classe propone altre regole, decidere insieme e scriverle alla lavagna prima di contare."))
    S.append(attivita("Contate il paragrafo",
        ["Leggete il paragrafo nella slide successiva (o sul foglio stampato)",
         "Scrivete in R1 l'elenco delle forme: ogni volta che una parola ricompare, aggiungete una tacca",
         "Contate le tacche: questo è il numero delle occorrenze",
         "Contate le righe dell'elenco: questo è il numero delle forme"],
        "gruppo", "R1", "5 minuti", [(300, "Contare")],
        esempio="treno ||||   studenti |||   il ||||| |",
        note="7-12 min. Lasciare questa slide 30 secondi per la consegna, poi passare al paragrafo e avviare il timer lì (anche la slide del paragrafo ha il timer)."))
    S.append(spiega("Il paragrafo", occhiello="Testo da contare", testo=[PAR], timer=[(300, "Contare")], rumore="discussione", fase="gruppo",
        note="Soluzione con le regole della classe: 67 occorrenze, 50 forme diverse. Più frequenti: il 6, treno 4, di 3, studenti 3, la 3, poi alle, a, e 2. Si accetta uno scarto di 3."))
    S.append(spiega("Soluzione, e un numero per confrontare", occhiello="Frequenza relativa",
        tabella=(["", "Valore corretto"], [["Occorrenze", "67"], ["Forme diverse", "50"], ["Parola più frequente", "il, 6 volte"]]),
        formula="frequenza relativa = occorrenze della parola ÷ occorrenze totali",
        esempio="«il»: 6 ÷ 67 ≈ 0,09, cioè circa il 9% delle parole del testo.",
        dopo=["In R2: le 5 parole più frequenti con la loro frequenza relativa (3 minuti, calcolatrice ammessa)."],
        timer=[(180, "R2")], rumore="discussione", fase="gruppo",
        note="12-16 min. Punto a chi è entro 3. Soluzione R2: il 0,09; treno 0,06; di, studenti, la 0,04. Far notare: in cima ci sono parole piccole e comuni e la parola dell'argomento; 41 forme su 50 compaiono una volta sola."))

    S.append(spiega("Le parole hanno dei pezzi", occhiello="Radice e desinenza",
        tabella=(["Parola", "Radice", "Desinenza", "Che cosa dice la desinenza"],
                 [["mangio", "mangi-", "-o", "io, adesso"], ["mangiamo", "mangi-", "-amo", "noi, adesso"], ["mangiavano", "mangi-", "-avano", "loro, nel passato"]]),
        testo=["La <b>radice</b> porta il significato (mangiare). La <b>desinenza</b> porta le informazioni grammaticali: chi, quanti, quando."],
        note="16-18 min. Far leggere la tabella riga per riga."))
    S.append(spiega("Come si trovano, in tre passi", occhiello="Un metodo per i verbi",
        punti=["Trova l'<b>infinito</b> del verbo (la forma che finisce in -are, -ere, -ire)",
               "Togli -are, -ere o -ire: quello che resta è la <b>radice</b>",
               "Nella parola di partenza, quello che viene dopo la radice è la <b>desinenza</b>: chiediti chi, quanti, quando"],
        ordinati=True,
        esempio=["«corriamo» → correre → radice <b>corr-</b> → desinenza <b>-iamo</b>: noi, adesso.",
                 "«dormivano» → dormire → radice <b>dorm-</b> → desinenza <b>-ivano</b>: loro, nel passato."],
        note="18-19 min. Fare un terzo esempio alla lavagna con un verbo proposto dalla classe."))
    S.append(spiega("Anche nomi e aggettivi, ma con eccezioni", occhiello="Oltre i verbi",
        tabella=(["Parola", "Radice", "Desinenza", "Che cosa dice"],
                 [["gatto", "gatt-", "-o", "maschile, uno"], ["gatte", "gatt-", "-e", "femminile, più di uno"], ["bella", "bell-", "-a", "femminile, uno"]]),
        attenzione=["Nei verbi <b>irregolari</b> la radice cambia: «vado» viene da andare, ma non ha la radice and-. Qui il metodo non basta: lo si segnala."],
        note="19-20 min. Altri irregolari utili: essere (sono, ero), fare (faccio), venire (vengo)."))
    S.append(attivita("Radici e desinenze",
        ["Per ogni parola scrivete in R3: radice, desinenza, che cosa dice la desinenza",
         "Verbi: <b>parlavamo, leggete, finiranno, cantai, prendono, apriamo</b>",
         "Nomi e aggettivi: <b>ragazze, verdi, libro</b>",
         "Se una parola è irregolare, scrivetelo"],
        "gruppo", "R3", "4 minuti", [(240, "R3")],
        esempio="corriamo → corr- / -iamo → noi, adesso",
        note="20-24 min. Soluzioni nella slide successiva."))
    S.append(spiega("Soluzioni", occhiello="R3",
        tabella=(["Parola", "Radice", "Desinenza", "Che cosa dice"],
                 [["parlavamo", "parl-", "-avamo", "noi, nel passato"], ["leggete", "legg-", "-ete", "voi, adesso"],
                  ["finiranno", "fin-", "-iranno", "loro, nel futuro"], ["cantai", "cant-", "-ai", "io, nel passato"],
                  ["prendono", "prend-", "-ono", "loro, adesso"], ["apriamo", "apr-", "-iamo", "noi, adesso"],
                  ["ragazze", "ragazz-", "-e", "femminile, più di una"], ["verdi", "verd-", "-i", "più di uno"], ["libro", "libr-", "-o", "maschile, uno"]], True),
        note="Le macchine fanno qualcosa di simile: spezzano il testo in pezzi frequenti (token), a volte più piccoli delle parole. Una parola rara diventa due o tre pezzi comuni."))

    S.append(attivita("Il gioco di Shannon",
        ["Il docente legge una frase una parola alla volta",
         "Prima di ogni parola, il gruppo scrive in R4 quella che secondo lui viene dopo",
         "Il docente dice la parola vera: chi l'ha indovinata fa un segno",
         "Alla fine: quante ne avete indovinate? In quale punto della frase era più facile?"],
        "gruppo", "R4", "5 minuti", [(300, "Shannon")],
        esempio="«Oggi piove, prendo l'…» → ombrello",
        note="24-29 min. Frase da leggere senza proiettarla: «ogni mattina prendo l'autobus per andare a scuola e arrivo sempre in ritardo». Dopo «per andare a» quasi tutti scrivono «scuola». Claude Shannon fece questo esperimento nel 1951. Domanda finale: dove era più facile? Verso la fine, perché c'era più contesto."))
    S.append(spiega("La lingua è prevedibile, ma il contesto conta", occhiello="Che cosa abbiamo scoperto",
        testo=["Spesso la parola successiva si indovina: più parole hai davanti (il <b>contesto</b>), più è facile."],
        formula="«La pesca è buona»",
        dopo=["In R5: scrivete i due significati della frase e la parola che crea il doppio senso (1 minuto)."],
        risposta=["La <b>pesca</b>, il frutto, è buona da mangiare; oppure la <b>pesca</b>, andare a pescare, è andata bene.",
                  "Un altro esempio: «Mi piace il riso» (il cibo, oppure il ridere). Senza contesto non si sa quale significato scegliere."],
        timer=[(60, "R5")], rumore="discussione", fase="gruppo",
        note="29-31 min. La parola pesca ha due significati: si chiama ambiguità. Una macchina che guarda poche parole alla volta può scegliere il significato sbagliato."))
    S.append(spiega("Il pappagallo stocastico", occhiello="Che cosa fa una macchina che scrive",
        testo=["Un chatbot sceglie la parola successiva guardando quanto spesso, nei testi che ha letto, quella parola segue le altre: sceglie la parola <b>probabile</b>.",
               "Per questo qualcuno lo chiama <b>pappagallo stocastico</b>: «stocastico» vuol dire «che dipende dal caso e dalle probabilità»."],
        attenzione="Sceglie la parola probabile. Non controlla se quello che scrive è vero.",
        note="31-33 min. Il termine viene da un articolo del 2021 di Emily Bender, Timnit Gebru e colleghi. Nell'ora 3 la classe costruirà un pappagallo con le proprie frasi."))
    S.append(controllo(
        ["Dividi <b>prendevate</b> in radice e desinenza: che cosa dice la desinenza?",
         "Scrivi i due significati di «Ho visto il riccio».",
         "Completa: «Un pappagallo stocastico sceglie la parola successiva in base a…»"],
        ["prend- / -evate: voi, nel passato",
         "l'animale con gli aculei; oppure il guscio spinoso della castagna (o un ricciolo di capelli)",
         "… a quanto spesso quella parola segue le altre (probabilità); non controlla se è vero"],
        note="33-36 min. Se meno di metà della classe risponde bene a una domanda, riprenderla all'inizio dell'ora 2."))
    S.append(riga("frequenza relativa = occorrenze di una parola ÷ occorrenze totali",
        [("occorrenze", "tutte le parole del testo, anche ripetute"), ("forme", "le parole diverse"),
         ("esempio", "«il» 6 volte su 67 parole: 6 ÷ 67 ≈ 0,09 = 9%")],
        dopo="Consegnate il foglio dell'ora.",
        note="36-40 min. Ritirare i fogli. Se avanza tempo: catena dei pappagalli umani (ognuno aggiunge una parola guardando solo l'ultima)."))

    # ================================================================ ORA 2
    R = [("R1", "Vero o inventato?", "I numeri dei consigli che credete veri.", 1),
         ("R2", "Di che genere è?", "Per ogni testo: il genere e tre parole che lo fanno riconoscere.", 2),
         ("R3", "Le nostre 8 frasi", "Tabella: frase · tipo (fatto, falso, opinione) · fonte (solo per i fatti veri).", 3),
         ("R4", "Gioco del verosimile", "Quali frasi degli altri gruppi erano false? Che cosa le rendeva credibili?", 1),
         ("R5", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((2, "Vero, verosimile, opinione", R))
    S.append(ora(2, "Italiano", "Vero, verosimile, opinione", "Scriviamo le frasi da cui nascerà il nostro modello",
        "scrivere 48 frasi controllate, 8 per gruppo.",
        note="Stessi gruppi dell'ora 1. Il prodotto di quest'ora (R3) serve subito nell'ora 3: i fogli vanno portati in laboratorio."))
    S.append(obiettivi([
        "riconoscere il <b>genere</b> di un testo breve dalle parole che lo fanno riconoscere",
        "distinguere <b>fatto</b>, <b>opinione</b> e <b>falso verosimile</b>",
        "scrivere 8 frasi che rispettano delle <b>regole</b> precise",
        "indicare chi può confermare un fatto: una <b>fonte</b>",
        "dire che cosa rende <b>credibile</b> una frase falsa",
        "distinguere una fonte <b>primaria</b> da una <b>secondaria</b>"]))
    S.append(attivita("Vero o inventato?",
        ["Leggete i cinque consigli: li ha scritti un'intelligenza artificiale",
         "1 Studia nel tuo stile, visivo, uditivo o cinestetico: impari molto di più. · 2 Fai pause continue: l'attenzione dura otto secondi, meno di un pesce rosso. · 3 Rileggi gli appunti tre volte: secondo uno studio di Harvard ricordi il 40% in più. · 4 Interrogati da solo, senza guardare il libro. · 5 Studia un po' ogni giorno, non tutto la sera prima.",
         "Scrivete in R1 i numeri dei consigli che credete veri"],
        "gruppo", "R1", "3 minuti", [(180, "R1")],
        note="3-6 min. Non dare la soluzione ora: arriva alla fine dell'ora. Soluzione: veri il 4 e il 5 (autointerrogazione e studio distribuito sono effetti molto documentati); falsi l'1 e il 2 (gli stili di apprendimento non migliorano l'apprendimento; gli otto secondi sono un mito); inventato il 3 (lo studio non esiste)."))
    S.append(attivita("Di che genere è?",
        ["Per ognuno dei sei testi scrivete in R2 il <b>genere</b>",
         "Scrivete tre parole che lo fanno riconoscere: si chiamano <b>marcatori</b>",
         "I sei testi sono nella slide successiva"],
        "gruppo", "R2", "4 minuti", [(240, "R2")],
        esempio="«il chitarrista accorda le corde prima del concerto» → genere: musica; marcatori: chitarrista, corde, concerto",
        note="6-10 min. Soluzioni: 1 meteo (nuvole, venti, nord); 2 calcio (portiere, rigore, novantesimo); 3 cucina (pizzico, sale, mescolate); 4 fiaba (c'era una volta, re, figlie); 5 scuola (verifica, storia, giovedì); 6 informatica (programma, file, finestra)."))
    S.append(spiega("I sei testi", occhiello="Di che genere è?",
        carte=[("1", "domani nuvole al nord e sole al sud, venti deboli"), ("2", "il portiere para il rigore al novantesimo"),
               ("3", "aggiungete un pizzico di sale e mescolate"), ("4", "c'era una volta un re che aveva tre figlie"),
               ("5", "la verifica di storia è spostata a giovedì"), ("6", "il programma salva il file e chiude la finestra")],
        timer=[(240, "R2")], rumore="discussione", fase="gruppo",
        note="Avviare qui il timer se non è stato avviato nella slide precedente."))
    S.append(spiega("Tre tipi di frase", occhiello="Fatto, opinione, falso verosimile",
        carte=[("Fatto vero", ["Si può controllare, e il controllo dice: vero.", "<i>il po sfocia nel mare adriatico</i>"], "#3A8A3E"),
               ("Opinione", ["Esprime un giudizio: non è né vera né falsa.", "<i>il po è il fiume più bello</i>"], "#2C8BC9"),
               ("Falso verosimile", ["Sembra vero, si può controllare, ma è falso.", "<i>il po nasce in svizzera</i>"], "#DB6A1C")],
        dopo=["«Verificabile» vuol dire che si può controllare, non che è vero: anche un falso verosimile è verificabile."],
        note="10-12 min. Il Po nasce in Piemonte, dal Monviso: la terza frase sembra vera perché le Alpi sono vicine alla Svizzera."))
    S.append(spiega("Le vostre frasi diventeranno un modello", occhiello="Corpus e modello",
        testo=["Un <b>corpus</b> è una raccolta di testi usata come dati.",
               "Un <b>modello</b> è un programma che ha imparato dagli esempi a fare previsioni. Il nostro, nell'ora 3, imparerà dalle vostre frasi quale parola viene dopo un'altra."],
        attenzione="Per questo le frasi devono rispettare delle regole: il modello funziona solo se le parole si ripetono.",
        note="12-13 min."))
    S.append(spiega("Le regole delle 8 frasi", occhiello="Ogni gruppo ha un genere",
        punti=["da <b>4 a 8 parole</b>, con chi fa, che cosa fa, e un complemento",
               "tutto <b>minuscolo</b>, <b>senza punteggiatura</b>",
               "almeno <b>3 parole</b> che si ripetono in più frasi",
               "<b>3 fatti veri</b> (ciascuno con chi lo può confermare), <b>3 falsi verosimili</b>, <b>2 opinioni</b>",
               "vietato copiare i sei testi di prima"],
        tabella=(["Gruppo", "1", "2", "3", "4", "5", "6"], [["Genere", "meteo", "calcio", "cucina", "fiabe", "scuola", "informatica"]]),
        note="13-14 min. La tabella dei generi resta valida qualunque sia il colore del gruppo: gruppo 1 è il primo sorteggiato."))
    S.append(spiega("Un esempio completo: il genere «animali»", occhiello="Esempio prima di scrivere",
        tabella=(["Frase", "Tipo", "Fonte"],
                 [["il gatto dorme molte ore al giorno", "fatto", "un libro di veterinaria"],
                  ["il gatto vede bene al buio", "fatto", "un museo di scienze naturali"],
                  ["il cane sente suoni molto acuti", "fatto", "un'associazione di veterinari"],
                  ["il cane vede tutti i colori", "falso", ""],
                  ["il gatto ha nove vite", "falso", ""],
                  ["il cane dorme in piedi", "falso", ""],
                  ["il gatto è più simpatico del cane", "opinione", ""],
                  ["il cane è l'animale più bello", "opinione", ""]], True),
        dopo=["Parole che si ripetono: il, gatto, cane, dorme, vede. «Internet» o «un chatbot» non valgono come fonte."],
        note="14 min. Mostrare che le parole ripetute permettono al modello di collegare le frasi."))
    S.append(attivita("Scrivete le vostre 8 frasi",
        ["Scrivete le 8 frasi del vostro genere nella tabella di R3",
         "Per ogni frase scrivete il tipo: fatto, falso o opinione",
         "Per i 3 fatti veri scrivete chi li può confermare",
         "Secondo timer: rileggete ogni frase con le regole e correggete"],
        "gruppo", "R3", "10 + 3 minuti", [(600, "Scrivere"), (180, "Controllare")],
        esempio="il cuoco sala la pasta · fatto · un libro di cucina",
        note="14-27 min. Girare tra i gruppi e controllare due errori: opinioni scritte come fatti; fatti che non si possono controllare. Per le fiabe i fatti veri riguardano le fiabe (cappuccetto rosso incontra il lupo nel bosco; fonte: la raccolta dei fratelli Grimm)."))
    S.append(attivita("Il gioco del verosimile",
        ["Un componente del gruppo legge due frasi: una vera e una falsa verosimile, nell'ordine che vuole",
         "Gli altri gruppi scrivono in R4 quale secondo loro è falsa",
         "Un punto al gruppo che inganna, un punto a chi indovina"],
        "tutti", "R4", "4 minuti", [(240, "Gioco")], rumore="spento",
        note="27-31 min. Se il tempo è poco, solo tre gruppi. Scrivere alla lavagna che cosa ha reso credibili le frasi false."))
    S.append(spiega("Perché crediamo a una frase falsa", occhiello="Gli ingredienti del verosimile",
        carte=[("Un nome importante", "«secondo Harvard…»"), ("Un numero preciso", "«il 40% in più»"),
               ("Una data o un luogo", "«nel 2019 a Milano»"), ("Un tono sicuro", "nessun dubbio, nessun forse")],
        attenzione="Nessuno di questi ingredienti è una prova. Il consiglio 3 di inizio ora li aveva quasi tutti.",
        note="31 min."))
    S.append(spiega("Cinque domande prima di fidarsi", occhiello="Le fonti",
        punti=["<b>Chi</b> lo dice?", "<b>Come</b> lo sa?", "<b>Perché</b> lo dice?", "<b>Quando</b> l'ha detto?", "<b>Chi altro</b> lo conferma?"],
        ordinati=True,
        esempio=["Un terremoto: la fonte <b>primaria</b> è l'INGV, che lo misura con i suoi strumenti.",
                 "Il giornale che riporta il dato dell'INGV è una fonte <b>secondaria</b>."],
        attenzione="Un chatbot non è una fonte: si cerca la fonte che conferma quello che dice.",
        note="31-33 min."))
    S.append(controllo(
        ["«Il Po è il fiume più lungo d'Italia»: fatto o opinione?",
         "«Il Po è il fiume più bello d'Italia»: fatto o opinione?",
         "Notizia di un terremoto: è primaria la pagina dell'INGV o l'articolo di un giornale?"],
        ["Fatto (si può controllare, ed è vero)", "Opinione (dipende da chi giudica)",
         "La pagina dell'INGV. E i cinque consigli? Veri il 4 e il 5; falsi l'1 e il 2; inventato il 3"],
        note="33-36 min. Dopo le risposte, dare la soluzione dei cinque consigli."))
    S.append(riga("fatto: si può controllare (e può risultare falso)<br>opinione: né vera né falsa<br>verosimile non vuol dire vero",
        [], dopo="I fogli con le 8 frasi vanno subito in laboratorio.",
        note="36-40 min. Ritirare i fogli: sono il materiale dell'ora 3."))

    # ================================================================ ORA 3
    R = [("R1", "Le coppie di una frase", "Scegliete una vostra frase e scrivete tutte le coppie di parole vicine.", 1),
         ("R2", "Conti e probabilità", "Per due parole: c(a), c(a, b) e P(b | a).", 1),
         ("R3", "La frase del pappagallo", "La frase generata con la regola greedy, e se è vera, falsa o opinione.", 1),
         ("R4", "Controllo", "Le tre risposte del controllo finale.", 3)]
    foglio_ora(R); F.append((3, "Dalle nostre frasi al pappagallo", R))
    S.append(ora(3, "Laboratorio di informatica", "Dalle nostre frasi al pappagallo", "Il primo modello della classe, sul foglio di calcolo",
        "costruire il pappagallo della 1P e farlo parlare.",
        note="Preparare: foglio condiviso «Corpus 1P» (colonne id, gruppo, genere, frase, tipo, fonte; 8 righe per gruppo); per ogni gruppo un foglio «Pappagallo» con le colonne parola e successiva. Un computer per gruppo."))
    S.append(obiettivi([
        "inserire le frasi in un foglio condiviso e salvarle in formato <b>CSV</b>",
        "trasformare una frase in <b>coppie di parole</b>",
        "contare le coppie con una <b>formula</b>",
        "calcolare la <b>probabilità</b> che una parola segua un'altra",
        "generare una frase con la regola <b>greedy</b>",
        "spiegare perché il pappagallo <b>non sa</b> se una frase è vera"]))
    S.append(spiega("Regole oppure esempi", occhiello="Che cos'è l'intelligenza artificiale, in breve",
        carte=[("Programmazione classica", ["Una persona scrive le regole: «se il messaggio contiene gratis, è pubblicità».", "Il computer le esegue."], "#2C8BC9"),
               ("Apprendimento automatico", ["Diamo al computer molti esempi già classificati.", "Il computer ricava da solo le regole: costruisce un modello."], "#3A8A3E")],
        testo=["Oggi costruiamo un modello a mano: impara dalle vostre frasi quale parola viene dopo un'altra."],
        note="3-6 min."))
    S.append(attivita("Le frasi nel foglio condiviso",
        ["Aprite il foglio «Corpus 1P»",
         "Scrivete le vostre 8 frasi <b>solo</b> nelle righe del vostro gruppo, come sono sul foglio",
         "Colonne: id, gruppo, genere, frase, tipo, fonte",
         "Uno scrive, un altro detta, un altro controlla parola per parola"],
        "gruppo", "sul computer, nel foglio «Corpus 1P»", "5 minuti", [(300, "Inserire")],
        esempio="17 · gruppo 3 · cucina · il cuoco sala la pasta · fatto · un libro di cucina",
        note="6-11 min. Controllare che nessuno scriva nelle righe degli altri gruppi."))
    S.append(spiega("Il formato CSV", occhiello="Un formato semplice per i dati",
        testo=["File › Scarica › Valori separati da virgola (.csv). Aperto con un editor di testo, il file è così:"],
        codice="id;gruppo;genere;frase;tipo;fonte\n1;1;meteo;il vento soffia forte al nord;fatto;aeronautica militare\n2;1;meteo;…",
        punti=["una riga per ogni frase", "le colonne separate sempre dallo stesso simbolo (qui il punto e virgola)", "la prima riga contiene i nomi delle colonne"],
        note="11-13 min. Dimostrazione al proiettore. Salvare come corpus_1p.csv nella cartella della classe (pezzo per l'installazione). Il file deve avere 49 righe: i nomi delle colonne più 48 frasi."))
    S.append(spiega("Dalle frasi alle coppie", occhiello="Il primo passo del modello",
        testo=["Frasi: «il cane corre veloce» e «il cane dorme»."],
        tabella=(["parola (a)", "successiva (b)"], [["il", "cane"], ["cane", "corre"], ["corre", "veloce"], ["il", "cane"], ["cane", "dorme"]]),
        attenzione="Una frase di 4 parole dà 3 coppie. Le coppie non attraversano due frasi: «veloce il» non è una coppia.",
        note="13-14 min."))
    S.append(attivita("Le vostre coppie",
        ["Scegliete una vostra frase e scrivete in R1 le sue coppie, a mano",
         "Poi nel foglio «Pappagallo»: colonna A parola, colonna B successiva",
         "Una riga per ogni coppia, frase dopo frase",
         "Controllo: numero di coppie = somma di (parole di ogni frase − 1)"],
        "gruppo", "R1", "6 minuti", [(360, "Coppie")],
        esempio="il cuoco sala la pasta → (il, cuoco) (cuoco, sala) (sala, la) (la, pasta)",
        note="14-20 min. Le 8 frasi di un gruppo danno circa 35 coppie."))
    S.append(spiega("Contare con le formule", occhiello="c(a, b) e c(a)",
        punti=["<b>c(a, b)</b>: quante volte la coppia a, b compare. Colonna C.",
               "<b>c(a)</b>: quante volte la parola a compare con una parola dopo. Colonna D."],
        codice="C2: =CONTA.PIÙ.SE(A:A;A2;B:B;B2)\nD2: =CONTA.SE(A:A;A2)",
        esempio="Con le frasi del cane: c(il, cane) = 2 e c(il) = 2; c(cane, corre) = 1 e c(cane) = 2.",
        dopo=["Si scrive la formula nella riga 2 e la si trascina fino all'ultima coppia."],
        note="20-22 min. In un foglio in inglese: COUNTIFS e COUNTIF, con la virgola al posto del punto e virgola."))
    S.append(spiega("La probabilità che b segua a", occhiello="Dal conteggio alla probabilità",
        formula="P(b | a) = c(a, b) ÷ c(a)",
        testo=["Si legge: «probabilità di b, sapendo che prima c'è a». Nel foglio, colonna E: <span class=\"mono\">=C2/D2</span>"],
        esempio=["P(corre | cane) = 1 ÷ 2 = 0,5 e P(dorme | cane) = 1 ÷ 2 = 0,5.", "Le probabilità delle parole che seguono «cane» sommano a 1."],
        dopo=["In R2: scegliete due parole del vostro foglio e scrivete c(a), c(a, b) e P(b | a)."],
        timer=[(180, "Formule e R2")], rumore="discussione", fase="gruppo",
        note="22-25 min. Controllare su due parole che le probabilità sommano a 1 (le coppie ripetute compaiono su più righe: vanno contate una volta)."))
    S.append(spiega("Far parlare il pappagallo: la regola greedy", occhiello="Generare una frase",
        punti=["partite dalla parola che compare più spesso all'inizio delle vostre frasi",
               "scegliete sempre la parola successiva con la P più alta",
               "a pari probabilità, la prima in ordine alfabetico",
               "fermatevi quando la parola non ha successive, o dopo 8 parole"],
        ordinati=True,
        esempio="il → cane (P = 1) → corre o dorme (0,5 e 0,5: vince corre, prima in ordine alfabetico) → veloce: «il cane corre veloce»",
        dopo=["«Greedy» in inglese vuol dire «ingordo»: prende sempre il pezzo più grande subito. In R3 scrivete la frase generata (3 minuti)."],
        timer=[(180, "R3")], rumore="discussione", fase="gruppo",
        note="25-28 min."))
    S.append(spiega("Indovina il pappagallo", occhiello="Gioco",
        testo=["Un componente di ogni gruppo legge la frase del suo pappagallo. Gli altri gruppi scrivono su un foglietto il genere."],
        dopo=["Di solito si indovina: il pappagallo ripete le parole del suo corpus."],
        fase="tutti",
        note="28-30 min. Un punto a chi indovina."))
    S.append(spiega("Spazzatura dentro, spazzatura fuori", occhiello="Che cosa sa davvero il pappagallo",
        testo=["Il corpus contiene fatti veri, falsi verosimili e opinioni. Il pappagallo li ha contati tutti allo stesso modo.",
               "La vostra frase generata è vera, falsa o un'opinione? Scrivetelo in R3."],
        attenzione="Il pappagallo conosce solo quante volte le parole si seguono. Non sa che cosa è vero.",
        dopo=["Un chatbot vero ha letto moltissimi testi e guarda tutte le parole precedenti, non solo l'ultima; ma sceglie sempre parole probabili. Per fidarsi servono le fonti."],
        note="30-33 min."))
    S.append(controllo(
        ["Se c(il) = 10 e c(il, cane) = 4, quanto vale P(cane | il)?",
         "Che cosa fa la regola greedy?",
         "Il pappagallo sa se una frase è vera? Perché?"],
        ["4 ÷ 10 = 0,4", "Sceglie sempre la parola successiva più probabile",
         "No: conosce solo quante volte le parole si seguono nel corpus"],
        note="33-36 min."))
    S.append(riga("P(b | a) = c(a, b) ÷ c(a)",
        [("c(a, b)", "quante volte la parola b viene subito dopo la parola a"), ("c(a)", "quante volte la parola a ha una parola dopo"),
         ("greedy", "si sceglie sempre la parola b con la probabilità più alta")],
        dopo="Pezzi per l'installazione, nella cartella della classe: corpus_1p.csv e il foglio Pappagallo di ogni gruppo.",
        note="36-40 min. Salvare. Se avanza tempo: generare con un dado invece che con la regola greedy (se due parole hanno 0,5 ciascuna: 1-3 la prima, 4-6 la seconda)."))
    return "IA e dati 1P · Giornata 1 · La lingua come dati", S, F
