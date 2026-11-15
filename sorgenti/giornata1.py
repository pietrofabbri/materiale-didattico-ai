"""Giornata 1 · La lingua come dati (v2: testi brevi, richiami, importanza per slide).

Scritta con g2.py: ogni slide è già una slide del deck (tipo Slides di Claude).
build() -> (titolo, S, F): S = lista di (id, html della slide del deck), F = fogli dell'ora da stampare.
Importanza: imp="e" essenziale, "c" consigliata, "f" facoltativa (si salta se manca tempo).
"""
from g2 import *

PAR = ("Ogni mattina il treno parte dalla stazione alle sette. Il treno è quasi sempre pieno di studenti che vanno a scuola. "
       "Alcuni studenti leggono, altri ascoltano la musica e molti guardano il telefono. Quando il treno arriva in città, "
       "gli studenti scendono di corsa, perché la prima ora comincia alle otto e il professore di matematica non aspetta nessuno. "
       "La sera il treno riporta tutti a casa.")

def build():
    S, F = [], []
    S.append(copertina(1, "La lingua come dati",
        "Come fa una macchina a scrivere frasi, se non sa che cosa dice?",
        [("Ora 1 · Italiano", "Contare le parole e prevedere la successiva"),
         ("Ora 2 · Italiano", "Fatti, opinioni, falsi: scriviamo le nostre frasi"),
         ("Ora 3 · Laboratorio", "Dalle nostre frasi a un modello che scrive")],
        note="Prima della lezione: tarare il barattolo (B, poi T) e provare il sorteggio. Stampare 6 copie dei fogli di ciascuna ora (A3 orizzontale). Barra in basso: blu essenziale, ambra consigliata, grigio facoltativa (si salta se manca tempo)."))

    # ================================================================ ORA 1
    R = [("R1", "Conteggi", "Occorrenze: ____   Forme diverse: ____   (elenco delle forme con le tacche)", 1),
         ("R2", "Parole più frequenti", "Le 5 parole più frequenti e la loro frequenza relativa.", 1),
         ("R3", "Radici e desinenze", "Per ogni parola: radice, desinenza, che cosa dice la desinenza.", 1),
         ("R4", "Gioco di Shannon", "Le parole che prevedete, una per riga. Quante ne avete indovinate?", 1),
         ("R5", "Due significati", "La frase, i due significati, la parola che crea il doppio senso.", 1),
         ("R6", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((1, "Le parole come dati", R))
    S.append(ora(1, "Italiano", "Le parole come dati", "Contare, prevedere, capire il contesto",
        "capire perché una macchina riesce a indovinare la parola che viene dopo.",
        note="0-3 min. Presentare il percorso in una frase: in quattro giornate scopriamo come impara una macchina, usando i nostri dati."))
    S.append(obiettivi([
        "contare <b>occorrenze</b> e <b>forme</b> di un testo",
        "calcolare la <b>frequenza relativa</b> di una parola",
        "dividere una parola in <b>radice</b> e <b>desinenza</b>",
        "<b>prevedere</b> la parola successiva e dire perché ci riesci",
        "spiegare che cosa fa un <b>pappagallo stocastico</b>"]))
    S.append(sorteggio("Ogni giornata ha gruppi nuovi, estratti con i numeri del registro. Quando compare il vostro gruppo, andate all'isola del suo colore: avete un minuto.",
        note="Inserire gli assenti e premere Sorteggia. Sullo schermo solo numeri del registro, nessun nome."))
    S.append(slide("Come lavoriamo",
        Carte([("Il foglio dell'ora", "Un foglio grande per gruppo, diviso in riquadri: R1, R2… La slide dice dove scrivere.", "indaco"),
               ("Il timer", "In alto a destra: il tempo che resta. Quando suona, si alza la penna.", "salvia"),
               ("Il barattolo", "Misura solo il volume, non le parole, e non registra. Se il rumore resta alto, lo schermo si ferma.", "corallo")]),
        occhiello="Le regole delle quattro giornate", imp="c",
        note="Il barattolo è quello del Progetto 16. Se scatta: si smette di parlare, si appoggia quello che si ha in mano, si fa un respiro. Vale anche per il docente."))

    S.append(slide("Quante parole ci sono?",
        Tasselli(["il", "gatto", "e", "il", "cane"], {"il": "indaco"}),
        P("Scrivete un numero su un foglietto."),
        Risposta(["<b>Occorrenze</b>: tutte le parole, anche ripetute = <b>5</b>.",
                  "<b>Forme</b>: le parole diverse = <b>4</b>. «il» è una forma che compare due volte."]),
        occhiello="Domanda",
        note="3-6 min. Raccogliere le risposte (di solito 5 e 4): sono giuste entrambe, contano cose diverse. In informatica le occorrenze si chiamano anche token."))
    S.append(slide("Le regole per contare",
        Lista(["«Il» e «il» sono la stessa forma: le maiuscole non contano",
               "la punteggiatura non si conta",
               "«gatto» e «gatti» sono due forme diverse",
               "«l'» conta come una parola"]),
        Esempio(["«Il sole e il mare e il vento» → <b>8</b> occorrenze, <b>5</b> forme (il, sole, e, mare, vento)."]),
        occhiello="Così tutti i gruppi trovano lo stesso numero", imp="c",
        note="6-7 min. Se la classe propone altre regole, decidere insieme e scriverle alla lavagna."))
    S.append(attivita("Contate il paragrafo",
        ["Leggete il paragrafo (slide successiva)",
         "In R1 scrivete ogni parola nuova; se ricompare, una tacca",
         "Tacche in tutto = <b>occorrenze</b>",
         "Righe dell'elenco = <b>forme</b>"],
        "gruppo", "R1", "5 minuti", [(300, "Contare")],
        esempio="treno ||||   studenti |||   il ||||| |",
        note="7-12 min. Lasciare la consegna 30 secondi, poi passare al paragrafo: il timer è anche lì."))
    S.append(slide("Il paragrafo", P(PAR, "testo-lungo"), occhiello="Testo da contare", rumore="discussione", fase="gruppo", timer=[(300, "Contare")],
        note="Soluzione: 67 occorrenze, 50 forme. Più frequenti: il 6, treno 4, di 3, studenti 3, la 3. Si accetta uno scarto di 3."))
    S.append(slide("Quanto pesa una parola nel testo?",
        Formula("frequenza relativa = occorrenze della parola ÷ occorrenze totali", True),
        Barre([("il", 6 / 67 / 0.1, "6 ÷ 67 ≈ 0,09"), ("treno", 4 / 67 / 0.1, "≈ 0,06"), ("studenti", 3 / 67 / 0.1, "≈ 0,04")]),
        Ricorda("0,09 vuol dire 9 su 100: circa una parola su undici è «il»."),
        P("In R2: le vostre 5 parole più frequenti, con la frequenza relativa. Calcolatrice ammessa.", "piccolo"),
        occhiello="Soluzione: 67 occorrenze, 50 forme · Frequenza relativa", rumore="discussione", fase="gruppo", timer=[(180, "R2")],
        note="12-16 min. Barre in scala: la più lunga è il 9%. Far notare: in cima ci sono parole piccole e comuni, poi la parola dell'argomento (treno). 41 forme su 50 compaiono una volta sola."))

    S.append(slide("Le parole hanno due pezzi",
        Tasselli(["mangi", "o"], {"mangi": "indaco", "o": "corallo"}),
        Tasselli(["mangi", "amo"], {"mangi": "indaco", "amo": "corallo"}),
        Tasselli(["mangi", "avano"], {"mangi": "indaco", "avano": "corallo"}),
        P("La <b>radice</b> (blu) porta il significato: mangiare. La <b>desinenza</b> (rosso) dice <b>chi</b>, <b>quanti</b>, <b>quando</b>: io adesso, noi adesso, loro nel passato."),
        occhiello="Radice e desinenza",
        note="16-18 min. Chiedere alla classe di dire che cosa cambia tra le tre parole."))
    S.append(slide("Come si trovano, in tre passi",
        Lista(["Trova l'<b>infinito</b>", "Togli -are, -ere, -ire: resta la <b>radice</b>",
               "Il resto della parola è la <b>desinenza</b>: chi, quanti, quando?"], True),
        Ricorda("L'<b>infinito</b> è la forma del verbo che trovi sul dizionario: mangiare, correre, dormire."),
        Esempio(["«corriamo» → correre → <b>corr-</b> + <b>-iamo</b>: noi, adesso.",
                 "«dormivano» → dormire → <b>dorm-</b> + <b>-ivano</b>: loro, nel passato."], True),
        occhiello="Un metodo per i verbi",
        note="18-19 min. Un terzo esempio alla lavagna con un verbo proposto dalla classe."))
    S.append(slide("Nomi, aggettivi e verbi irregolari",
        Tabella(["Parola", "Radice", "Desinenza", "Che cosa dice"],
                [["gatto", "gatt-", "-o", "maschile, uno"], ["gatte", "gatt-", "-e", "femminile, più di uno"], ["bella", "bell-", "-a", "femminile, uno"]]),
        Attenzione("Nei verbi <b>irregolari</b> la radice cambia: «vado» viene da andare. Il metodo non basta: lo si scrive."),
        occhiello="Oltre i verbi", imp="f",
        note="19-20 min. Si può saltare se si è in ritardo: le parole irregolari dell'attività si segnalano a voce."))
    S.append(attivita("Radici e desinenze",
        ["Per ogni parola, in R3: radice, desinenza, che cosa dice",
         "<b>parlavamo · leggete · finiranno · cantai · prendono · apriamo</b>",
         "<b>ragazze · verdi · libro</b>",
         "Parola irregolare? Scrivetelo"],
        "gruppo", "R3", "4 minuti", [(240, "R3")],
        esempio="corriamo → corr- / -iamo → noi, adesso",
        note="20-24 min."))
    S.append(slide("Soluzioni",
        Tabella(["Parola", "Radice", "Desinenza", "Che cosa dice"],
                [["parlavamo", "parl-", "-avamo", "noi, nel passato"], ["leggete", "legg-", "-ete", "voi, adesso"],
                 ["finiranno", "fin-", "-iranno", "loro, nel futuro"], ["cantai", "cant-", "-ai", "io, nel passato"],
                 ["prendono", "prend-", "-ono", "loro, adesso"], ["apriamo", "apr-", "-iamo", "noi, adesso"],
                 ["ragazze", "ragazz-", "-e", "femminile, più di una"], ["verdi", "verd-", "-i", "più di uno"]], True),
        occhiello="R3", imp="c",
        note="Le macchine fanno qualcosa di simile: spezzano il testo in pezzi frequenti (token), a volte più piccoli delle parole. libro: libr- / -o, maschile, uno."))

    S.append(attivita("Il gioco di Shannon",
        ["Il docente legge una frase, una parola alla volta",
         "Prima di ogni parola, in R4 scrivete quella che secondo voi arriva",
         "Il docente dice la parola vera: se l'avete indovinata, un segno",
         "Alla fine: dove era più facile indovinare?"],
        "gruppo", "R4", "5 minuti", [(300, "Shannon")],
        esempio="«Oggi piove, prendo l'…» → ombrello",
        note="24-29 min. Frase da leggere senza proiettarla: «ogni mattina prendo l'autobus per andare a scuola e arrivo sempre in ritardo». Dopo «per andare a» quasi tutti scrivono «scuola». Claude Shannon fece questo esperimento nel 1951."))
    S.append(slide("Più parole hai davanti, più è facile",
        P("Le parole che vengono prima si chiamano <b>contesto</b>. Ma il contesto può non bastare:"),
        Tasselli(["La", "pesca", "è", "buona"], {"pesca": "ambra"}),
        P("In R5: i due significati e la parola che crea il doppio senso. 1 minuto.", "piccolo"),
        Risposta(["Il frutto è buono da mangiare, oppure: la pesca con la canna è andata bene.",
                  "Una parola con due significati crea <b>ambiguità</b>. Altro esempio: «Mi piace il riso»."]),
        occhiello="Che cosa abbiamo scoperto", rumore="discussione", fase="gruppo", timer=[(60, "R5")],
        note="29-31 min. Una macchina che guarda poche parole alla volta può scegliere il significato sbagliato."))
    S.append(slide("Il pappagallo stocastico",
        P("Un chatbot sceglie la parola successiva guardando quanto spesso, nei testi letti, segue le parole di prima."),
        Ricorda("<b>Stocastico</b> vuol dire «che dipende dal caso e dalle probabilità». <b>Probabile</b> vuol dire «che capita spesso»."),
        Attenzione("Sceglie la parola probabile. Non controlla se quello che scrive è vero.", True),
        occhiello="Che cosa fa una macchina che scrive",
        note="31-33 min. Il termine viene da un articolo del 2021 di Emily Bender, Timnit Gebru e colleghi. Nell'ora 3 la classe costruisce il suo pappagallo."))
    S.append(controllo(
        ["Dividi <b>prendevate</b>: radice, desinenza, che cosa dice?",
         "Due significati di «Ho visto il riccio».",
         "Un pappagallo stocastico sceglie la parola in base a…"],
        ["prend- / -evate: voi, nel passato", "l'animale con gli aculei, o il guscio della castagna",
         "quanto spesso segue le altre; non controlla se è vero"],
        note="33-36 min. Se meno di metà della classe risponde bene a una domanda, riprenderla all'inizio dell'ora 2."))
    S.append(riga("frequenza relativa = occorrenze di una parola ÷ occorrenze totali",
        [("occorrenze", "tutte le parole, anche ripetute"), ("forme", "le parole diverse"), ("esempio", "«il» 6 volte su 67: 6 ÷ 67 ≈ 0,09")],
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
        "scrivere 48 frasi controllate: 8 per gruppo.",
        note="Stessi gruppi dell'ora 1. I fogli con R3 vanno portati in laboratorio per l'ora 3."))
    S.append(obiettivi([
        "riconoscere il <b>genere</b> di un testo dalle sue parole",
        "distinguere <b>fatto</b>, <b>opinione</b> e <b>falso verosimile</b>",
        "scrivere 8 frasi che rispettano delle <b>regole</b>",
        "indicare chi può confermare un fatto: la <b>fonte</b>",
        "dire che cosa rende <b>credibile</b> una frase falsa"]))
    S.append(slide("Cinque consigli per studiare",
        Lista(["Studia nel tuo stile, visivo, uditivo o cinestetico: impari molto di più.",
               "Fai pause continue: l'attenzione dura otto secondi, meno di un pesce rosso.",
               "Rileggi gli appunti tre volte: secondo uno studio di Harvard ricordi il 40% in più.",
               "Interrogati da solo, senza guardare il libro.",
               "Studia un po' ogni giorno, non tutto la sera prima."], True),
        P("Li ha scritti un'intelligenza artificiale. In R1: i numeri di quelli che credete veri.", "piccolo"),
        occhiello="Vero o inventato? · Nel gruppo · R1", rumore="discussione", fase="gruppo", timer=[(180, "R1")],
        note="3-6 min. La soluzione arriva alla fine dell'ora: veri il 4 e il 5; falsi l'1 e il 2 (stili di apprendimento e otto secondi sono miti); inventato il 3 (lo studio non esiste)."))
    S.append(attivita("Di che genere è?",
        ["Per ognuno dei sei testi, in R2: il <b>genere</b>",
         "Tre parole che lo fanno riconoscere: i <b>marcatori</b>",
         "I testi sono nella slide successiva"],
        "gruppo", "R2", "4 minuti", [(240, "R2")],
        esempio="«il chitarrista accorda le corde prima del concerto» → musica: chitarrista, corde, concerto",
        note="6-10 min. Soluzioni: 1 meteo; 2 calcio; 3 cucina; 4 fiaba; 5 scuola; 6 informatica."))
    S.append(slide("I sei testi",
        Carte([("1", "domani nuvole al nord e sole al sud, venti deboli"), ("2", "il portiere para il rigore al novantesimo"),
               ("3", "aggiungete un pizzico di sale e mescolate"), ("4", "c'era una volta un re che aveva tre figlie"),
               ("5", "la verifica di storia è spostata a giovedì"), ("6", "il programma salva il file e chiude la finestra")]),
        occhiello="Di che genere è?", rumore="discussione", fase="gruppo", timer=[(240, "R2")],
        note="Avviare qui il timer se non è partito nella slide precedente."))
    S.append(slide("Tre tipi di frase",
        Carte([("Fatto vero", ["Si può controllare, e il controllo dice: vero.", "<i>il po sfocia nel mare adriatico</i>"], "salvia"),
               ("Opinione", ["È un giudizio: non è né vera né falsa.", "<i>il po è il fiume più bello</i>"], "cielo"),
               ("Falso verosimile", ["Sembra vero, si può controllare, ma è falso.", "<i>il po nasce in svizzera</i>"], "corallo")]),
        Ricorda("<b>Verificabile</b> vuol dire «si può controllare», non «è vero». Anche un falso verosimile è verificabile."),
        occhiello="Fatto, opinione, falso verosimile",
        note="10-12 min. Il Po nasce in Piemonte, dal Monviso: la terza frase sembra vera perché le Alpi confinano con la Svizzera."))
    S.append(slide("Le vostre frasi diventeranno un modello",
        P("Un <b>corpus</b> è una raccolta di testi usata come dati."),
        P("Un <b>modello</b> è un programma che ha imparato dagli esempi a fare previsioni."),
        Esempio("Nell'ora 3 il nostro modello imparerà dalle vostre frasi quale parola viene dopo un'altra."),
        Attenzione("Il modello funziona solo se le parole si ripetono: per questo le frasi hanno delle regole.", True),
        occhiello="Corpus e modello",
        note="12-13 min."))
    S.append(slide("Le regole delle 8 frasi",
        Lista(["da <b>4 a 8 parole</b>: chi fa, che cosa fa, un complemento",
               "tutto <b>minuscolo</b>, <b>senza punteggiatura</b>",
               "almeno <b>3 parole</b> che si ripetono in più frasi",
               "<b>3 fatti veri</b> con la fonte, <b>3 falsi verosimili</b>, <b>2 opinioni</b>"]),
        Tabella(["Gruppo", "1", "2", "3", "4", "5", "6"], [["Genere", "meteo", "calcio", "cucina", "fiabe", "scuola", "informatica"]], True),
        occhiello="Ogni gruppo ha un genere",
        note="13-14 min. Gruppo 1 è il primo sorteggiato. Vietato copiare i sei testi di prima."))
    S.append(slide("Un esempio completo: il genere «animali»",
        Tabella(["Frase", "Tipo", "Fonte"],
                [["il gatto dorme molte ore al giorno", "fatto", "un libro di veterinaria"],
                 ["il cane sente suoni molto acuti", "fatto", "un'associazione di veterinari"],
                 ["il cane vede tutti i colori", "falso", ""],
                 ["il gatto ha nove vite", "falso", ""],
                 ["il gatto è più simpatico del cane", "opinione", ""]], True),
        P("Parole ripetute: il, gatto, cane. «Internet» o «un chatbot» non valgono come fonte.", "piccolo"),
        occhiello="Esempio prima di scrivere", imp="c",
        note="14 min. Le parole ripetute permettono al modello di collegare le frasi."))
    S.append(attivita("Scrivete le vostre 8 frasi",
        ["Le 8 frasi del vostro genere, nella tabella di R3",
         "Per ogni frase il tipo: fatto, falso o opinione",
         "Per i 3 fatti veri: chi li può confermare",
         "Secondo timer: rileggete con le regole e correggete"],
        "gruppo", "R3", "10 + 3 minuti", [(600, "Scrivere"), (180, "Controllare")],
        esempio="il cuoco sala la pasta · fatto · un libro di cucina",
        note="14-27 min. Controllare due errori: opinioni scritte come fatti; fatti che non si possono controllare. Per le fiabe i fatti riguardano le fiabe (fonte: la raccolta dei fratelli Grimm)."))
    S.append(attivita("Il gioco del verosimile",
        ["Un gruppo legge due frasi: una vera e una falsa, nell'ordine che vuole",
         "Gli altri gruppi scrivono in R4 quale è falsa",
         "Un punto a chi inganna, un punto a chi indovina"],
        "tutti", "R4", "4 minuti", [(240, "Gioco")], imp="c", rumore="spento",
        note="27-31 min. Con poco tempo, solo tre gruppi. Scrivere alla lavagna che cosa ha reso credibili le frasi false."))
    S.append(slide("Perché crediamo a una frase falsa",
        Carte([("Un nome importante", "«secondo Harvard…»", "indaco"), ("Un numero preciso", "«il 40% in più»", "ambra"),
               ("Una data o un luogo", "«nel 2019 a Milano»", "salvia"), ("Un tono sicuro", "nessun dubbio, nessun forse", "corallo")]),
        Attenzione("Nessuno di questi è una prova. Il consiglio 3 li aveva quasi tutti.", True),
        occhiello="Gli ingredienti del verosimile", imp="c",
        note="31 min."))
    S.append(slide("Cinque domande prima di fidarsi",
        Lista(["<b>Chi</b> lo dice?", "<b>Come</b> lo sa?", "<b>Perché</b> lo dice?", "<b>Quando</b>?", "<b>Chi altro</b> lo conferma?"], True),
        Ricorda(["Fonte <b>primaria</b>: chi ha misurato o visto (l'INGV per un terremoto).",
                 "Fonte <b>secondaria</b>: chi lo riporta (il giornale)."]),
        Attenzione("Un chatbot non è una fonte: si cerca la fonte che conferma.", True),
        occhiello="Le fonti",
        note="31-33 min. L'INGV è l'Istituto nazionale di geofisica e vulcanologia: misura i terremoti con i suoi strumenti."))
    S.append(controllo(
        ["«Il Po è il fiume più lungo d'Italia»: fatto o opinione?",
         "«Il Po è il fiume più bello d'Italia»: fatto o opinione?",
         "Terremoto: è primaria la pagina dell'INGV o l'articolo di giornale?"],
        ["Fatto: si può controllare, ed è vero", "Opinione: dipende da chi giudica",
         "La pagina dell'INGV. Consigli: veri 4 e 5, falsi 1 e 2, inventato 3"],
        note="33-36 min. Dopo le risposte, dare la soluzione dei cinque consigli."))
    S.append(riga("fatto: si può controllare · opinione: né vera né falsa · verosimile non vuol dire vero",
        [], dopo="I fogli con le 8 frasi vanno subito in laboratorio.",
        note="36-40 min. Ritirare i fogli: sono il materiale dell'ora 3."))

    # ================================================================ ORA 3
    R = [("R1", "Le coppie di una frase", "Una vostra frase e tutte le sue coppie di parole vicine.", 1),
         ("R2", "Conti e probabilità", "Per due parole: c(a), c(a, b) e P(b | a).", 1),
         ("R3", "La frase del pappagallo", "La frase generata con la regola greedy, e se è vera, falsa o opinione.", 1),
         ("R4", "Controllo", "Le tre risposte del controllo finale.", 3)]
    foglio_ora(R); F.append((3, "Dalle nostre frasi al pappagallo", R))
    S.append(ora(3, "Laboratorio di informatica", "Dalle nostre frasi al pappagallo", "Il primo modello della classe, sul foglio di calcolo",
        "costruire il pappagallo della 1P e farlo parlare.",
        note="Preparare: foglio condiviso «Corpus 1P» (colonne id, gruppo, genere, frase, tipo, fonte; 8 righe per gruppo); per ogni gruppo un foglio «Pappagallo» con le colonne parola e successiva. Un computer per gruppo."))
    S.append(obiettivi([
        "salvare le frasi in un file <b>CSV</b>",
        "trasformare una frase in <b>coppie di parole</b>",
        "contare le coppie con una <b>formula</b>",
        "calcolare la <b>probabilità</b> che una parola segua un'altra",
        "generare una frase con la regola <b>greedy</b>"]))
    S.append(slide("Regole oppure esempi",
        Carte([("Programmazione classica", ["Una persona scrive le regole.", "«Se il messaggio contiene gratis, è pubblicità»."], "cielo"),
               ("Apprendimento automatico", ["Diamo al computer molti esempi.", "Il computer ricava le regole da solo: costruisce un <b>modello</b>."], "salvia")]),
        Ricorda("<b>Modello</b>: un programma che ha imparato dagli esempi a fare previsioni."),
        occhiello="Che cos'è l'intelligenza artificiale, in breve", imp="c",
        note="3-6 min. Oggi costruiamo un modello a mano."))
    S.append(attivita("Le frasi nel foglio condiviso",
        ["Aprite il foglio «Corpus 1P»",
         "Scrivete le 8 frasi <b>solo</b> nelle righe del vostro gruppo",
         "Colonne: id, gruppo, genere, frase, tipo, fonte",
         "Uno scrive, uno detta, uno controlla"],
        "gruppo", "sul computer, foglio «Corpus 1P»", "5 minuti", [(300, "Inserire")],
        esempio="17 · 3 · cucina · il cuoco sala la pasta · fatto · un libro di cucina",
        note="6-11 min. Controllare che nessuno scriva nelle righe degli altri gruppi."))
    S.append(slide("Il formato CSV",
        Codice("id;gruppo;genere;frase;tipo;fonte\n1;1;meteo;il vento soffia forte al nord;fatto;aeronautica militare"),
        Lista(["una riga per ogni frase", "le colonne separate dallo stesso simbolo (qui il punto e virgola)", "la prima riga: i nomi delle colonne"]),
        Ricorda("CSV vuol dire «valori separati da virgola»: un file di solo testo che qualsiasi programma sa leggere."),
        occhiello="File › Scarica › Valori separati da virgola", imp="c",
        note="11-13 min. Dimostrazione al proiettore. Salvare corpus_1p.csv nella cartella della classe (pezzo per l'installazione): 49 righe, i nomi delle colonne più 48 frasi."))
    S.append(slide("Dalle frasi alle coppie",
        Catena(["il", "cane", "corre", "veloce"]),
        P("Coppie: (il, cane) · (cane, corre) · (corre, veloce)"),
        Catena(["il", "cane", "dorme"], True),
        P("Coppie: (il, cane) · (cane, dorme)", "fragment"),
        Attenzione("Una frase di 4 parole dà 3 coppie. Una coppia non passa da una frase all'altra.", True),
        occhiello="Il primo passo del modello",
        note="13-14 min. «veloce il» non è una coppia: sono due frasi diverse."))
    S.append(attivita("Le vostre coppie",
        ["Una vostra frase: in R1 le sue coppie, a mano",
         "Foglio «Pappagallo»: colonna A parola, colonna B successiva",
         "Una riga per coppia, frase dopo frase",
         "Controllo: coppie = somma di (parole − 1)"],
        "gruppo", "R1", "6 minuti", [(360, "Coppie")],
        esempio="il cuoco sala la pasta → (il, cuoco) (cuoco, sala) (sala, la) (la, pasta)",
        note="14-20 min. Le 8 frasi di un gruppo danno circa 35 coppie."))
    S.append(slide("Contare con le formule",
        Codice("C2: =CONTA.PIÙ.SE(A:A;A2;B:B;B2)\nD2: =CONTA.SE(A:A;A2)"),
        Lista(["<b>c(a, b)</b>, colonna C: quante volte compare la coppia", "<b>c(a)</b>, colonna D: quante volte compare la parola a"]),
        Ricorda("<b>CONTA.SE</b> conta le righe che rispettano una condizione; <b>CONTA.PIÙ.SE</b> quelle che ne rispettano due insieme."),
        Esempio("c(il, cane) = 2 e c(il) = 2 · c(cane, corre) = 1 e c(cane) = 2", True),
        occhiello="c(a, b) e c(a)",
        note="20-22 min. Si scrive la formula nella riga 2 e la si trascina giù. Foglio in inglese: COUNTIFS e COUNTIF, con la virgola."))
    S.append(slide("La probabilità che b segua a",
        Formula("P(b | a) = c(a, b) ÷ c(a)"),
        P("Si legge «probabilità di b, sapendo che prima c'è a». Colonna E: =C2/D2"),
        Barre([("cane → corre", 0.5, "1 ÷ 2 = 0,5"), ("cane → dorme", 0.5, "1 ÷ 2 = 0,5")], True),
        P("Le probabilità delle parole che seguono «cane» sommano a 1: 0,5 + 0,5 = 1.", "fragment"),
        P("In R2: due parole del vostro foglio con c(a), c(a, b), P(b | a).", "piccolo"),
        occhiello="Dal conteggio alla probabilità", rumore="discussione", fase="gruppo", timer=[(180, "Formule e R2")],
        note="22-25 min. Controllo: su due parole le probabilità sommano a 1 (le coppie ripetute compaiono su più righe: vanno contate una volta)."))
    S.append(slide("Far parlare il pappagallo: la regola greedy",
        Lista(["partite dalla parola che apre più spesso le vostre frasi",
               "scegliete sempre la successiva con la P più alta",
               "a pari probabilità: la prima in ordine alfabetico",
               "fermatevi quando non ci sono successive, o dopo 8 parole"], True),
        Catena(["il", "cane", "corre", "veloce"], True),
        Ricorda("<b>Greedy</b> in inglese vuol dire «ingordo»: prende subito il pezzo più grande."),
        P("In R3: la frase del vostro pappagallo. 3 minuti.", "piccolo"),
        occhiello="Generare una frase", rumore="discussione", fase="gruppo", timer=[(180, "R3")],
        note="25-28 min. Nell'esempio: dopo cane, corre e dorme hanno 0,5: vince corre, prima in ordine alfabetico."))
    S.append(slide("Indovina il pappagallo",
        P("Un componente di ogni gruppo legge la frase del suo pappagallo. Gli altri scrivono su un foglietto il genere."),
        Risposta("Di solito si indovina: il pappagallo ripete le parole del suo corpus."),
        occhiello="Gioco", imp="f", fase="tutti",
        note="28-30 min. Un punto a chi indovina. Si salta se si è in ritardo."))
    S.append(slide("Spazzatura dentro, spazzatura fuori",
        P("Il corpus contiene fatti veri, falsi e opinioni. Il pappagallo li ha contati tutti allo stesso modo."),
        P("La vostra frase generata è vera, falsa o un'opinione? Scrivetelo in R3."),
        Attenzione("Il pappagallo sa solo quante volte le parole si seguono. Non sa che cosa è vero.", True),
        Ricorda("Un chatbot vero ha letto moltissimi testi e guarda tutte le parole precedenti, ma sceglie sempre parole probabili. Per fidarsi servono le fonti.", True),
        occhiello="Che cosa sa davvero il pappagallo",
        note="30-33 min."))
    S.append(controllo(
        ["c(il) = 10 e c(il, cane) = 4: quanto vale P(cane | il)?",
         "Che cosa fa la regola greedy?",
         "Il pappagallo sa se una frase è vera? Perché?"],
        ["4 ÷ 10 = 0,4", "sceglie sempre la parola più probabile", "no: sa solo quante volte le parole si seguono"],
        note="33-36 min."))
    S.append(riga("P(b | a) = c(a, b) ÷ c(a)",
        [("c(a, b)", "quante volte b viene subito dopo a"), ("c(a)", "quante volte a ha una parola dopo"),
         ("greedy", "si sceglie sempre la b più probabile")],
        dopo="Nella cartella della classe: corpus_1p.csv e il foglio Pappagallo di ogni gruppo.",
        note="36-40 min. Salvare. Se avanza tempo: generare con un dado invece che con la regola greedy (due parole a 0,5: 1-3 la prima, 4-6 la seconda)."))
    return "IA e dati 1P · Giornata 1 · La lingua come dati", S, F
