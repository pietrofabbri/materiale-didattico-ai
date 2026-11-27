from g import *

def build():
    S, F = [], []
    S.append(titolo_giornata(3, "Il corpo come fonte di dati",
        "Come si raccolgono dati veri, e perché non sono mai perfetti?",
        [("Ora 1 · In aula", "Misurare bene, e imparare per tentativi"),
         ("Ora 2 · In aula", "La raccolta dei dati, in aula"),
         ("Ora 3 · In laboratorio", "Dal foglio di carta a un archivio pulito")],
        note="Tutto si fa in aula. Materiale: 3 cronometri (o il cronometro del telefono del docente), nastro adesivo di carta, 3 cestini, 30 palline di carta (fogli riciclati appallottolati), una benda, un'urna con 29 codici (lettera + cifra). Prima della giornata: concordare con il collega di educazione fisica, se partecipa, le due prove e il contratto dei dati. Pezzi per l'installazione: il dataset pulito e l'errore di misura stimato."))

    # ================================================================ ORA 1
    R = [("R1", "Tre cronometri", "I tre tempi della stessa prova e lo scarto (più grande − più piccolo).", 1),
         ("R2", "Errore che sposta tutto", "Che cosa è andato storto e come si rimedia.", 1),
         ("R3", "Il nostro protocollo", "Che cosa si misura · come · con quale unità · quante prove.", 1),
         ("R4", "Bersaglio nascosto", "La strategia «se… allora…», i punteggi dei lanci, il totale R.", 2),
         ("R5", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((1, "Misurare bene", R))
    S.append(ora(1, "In aula", "Misurare bene", "Errori di misura, protocollo, privacy; imparare per tentativi",
        "decidere come si misura, prima di misurare.",
        note="Spostare i banchi lungo le pareti se serve spazio. Segnare con il nastro: una linea di lancio a 2 metri da un cestino; per il bersaglio nascosto, un cerchio piccolo (3 punti) dentro un cerchio grande (1 punto) sul pavimento."))
    S.append(obiettivi([
        "calcolare lo <b>scarto</b> tra misure ripetute: l'<b>errore casuale</b>",
        "riconoscere un <b>errore sistematico</b> e proporre un rimedio",
        "scrivere un <b>protocollo</b> di misura in quattro righe",
        "usare un <b>codice</b> al posto del nome, per la <b>privacy</b>",
        "scrivere una <b>strategia</b> e calcolare il punteggio totale R",
        "dire che cosa sono <b>agente</b>, <b>azione</b>, <b>ricompensa</b> e <b>strategia</b>"]))
    S.append(sorteggio("Gruppi nuovi anche oggi.", note="Inserire gli assenti e premere Sorteggia."))
    S.append(spiega("Le due prove che misureremo", occhiello="Si fanno in aula",
        carte=[("Equilibrio su un piede", ["Su un piede a scelta, mani sui fianchi, occhi aperti.", "Si misurano i secondi, fino a un massimo di 60. Due prove."], "#2C8BC9"),
               ("Lanci di precisione", ["10 palline di carta nel cestino, da 2 metri.", "Si contano i centri: da 0 a 10."], "#3A8A3E")],
        attenzione="Nessuna classifica: i dati servono a studiare la misura, non a giudicare le persone. Chi non vuole fare una prova cronometra o scrive.",
        note="3-5 min. Il collega, se presente, mostra le due prove."))
    S.append(attivita("La stessa prova, tre cronometri",
        ["Un volontario fa una prova di equilibrio",
         "Tre compagni la cronometrano, ognuno con il suo cronometro, senza guardarsi",
         "Dicono il tempo solo alla fine",
         "In R1: i tre tempi e lo scarto = tempo più grande − tempo più piccolo"],
        "tutti", "R1", "4 minuti", [(240, "R1")], rumore="spento",
        esempio="tempi 23,4 · 24,1 · 23,8 secondi → scarto = 24,1 − 23,4 = 0,7 secondi",
        note="5-9 min. I tempi di solito differiscono di qualche decimo: ognuno preme il pulsante in un momento un po' diverso."))
    S.append(spiega("Due tipi di errore", occhiello="Misurare non è mai perfetto",
        carte=[("Errore casuale", ["Misure ripetute danno valori un po' diversi: a volte di più, a volte di meno.", "Rimedio: ripetere e fare la media."], "#2C8BC9"),
               ("Errore sistematico", ["Tutte le misure sono spostate nello stesso verso.", "Esempio: un cronometrista che parte sempre in ritardo; la linea di lancio messa a 1,5 metri invece che a 2."], "#DB6A1C")],
        dopo=["In R2: un errore sistematico che potrebbe capitare nelle nostre prove, e come si evita (1 minuto)."],
        timer=[(60, "R2")], rumore="discussione", fase="gruppo",
        note="9-11 min. Rimedi possibili: chi dà il via è anche chi cronometra; linea misurata con il metro e segnata col nastro; regola precisa su quando si ferma il tempo."))
    S.append(spiega("Il protocollo: decidere prima di misurare", occhiello="Perché tutti misurino allo stesso modo",
        punti=["<b>Che cosa</b> si misura", "<b>Come</b> si misura", "Con quale <b>unità</b>", "<b>Quante prove</b> per persona"], ordinati=True,
        esempio=["1 secondi in equilibrio su un piede · 2 mani sui fianchi, occhi aperti; il tempo parte al «via» e si ferma quando l'altro piede tocca terra o le mani si staccano dai fianchi · 3 secondi interi, al massimo 60 · 4 due prove, si scrivono entrambe"],
        note="11-12 min."))
    S.append(attivita("Scrivete un protocollo",
        ["Gruppi 1, 2, 3: protocollo dei <b>lanci</b>. Gruppi 4, 5, 6: protocollo dell'<b>equilibrio</b>, migliorando l'esempio",
         "Scrivetelo in R3 in quattro righe",
         "Rileggete: un altro gruppo potrebbe eseguirlo senza farvi domande?"],
        "gruppo", "R3", "3 minuti", [(180, "R3")],
        esempio="lanci: 1 centri nel cestino · 2 da dietro la linea a 2 metri, una pallina alla volta, con una mano · 3 numero di centri · 4 dieci lanci",
        note="12-15 min. Raccogliere un protocollo per prova: si appendono alle postazioni dell'ora 2."))
    S.append(spiega("Privacy: un codice al posto del nome", occhiello="Dati di persone",
        punti=["ognuno pesca un <b>codice</b> dall'urna, lo scrive sul diario e lo usa al posto del nome",
               "sui fogli solo codici e misure, <b>mai nomi</b>",
               "si mostrano solo risultati della classe intera, <b>nessuna classifica</b>"],
        tabella=(["Colonna", "Che cosa contiene", "Valori ammessi"],
                 [["codice", "il codice pescato", "uno per persona"], ["mano", "mano usata per lanciare", "destra, sinistra"],
                  ["equilibrio_1, equilibrio_2", "le due prove di equilibrio", "secondi interi da 0 a 60"], ["lanci_10", "centri su 10 lanci", "da 0 a 10"]], True),
        dopo=["La tabella è il <b>contratto dei dati</b>: le regole che i dati devono rispettare."],
        note="15-17 min. Estrarre i codici."))
    S.append(spiega("Imparare per tentativi", occhiello="Apprendimento per rinforzo",
        carte=[("Agente", "chi impara"), ("Azione", "quello che l'agente fa"), ("Ricompensa", "il punteggio che riceve dopo l'azione"), ("Strategia", "la regola con cui sceglie l'azione")],
        testo=["L'agente non sa qual è l'azione giusta: lo scopre provando e guardando la ricompensa. Così si addestrano anche robot e programmi che giocano."],
        note="17-18 min. Esempio quotidiano: imparare ad andare in bicicletta."))
    S.append(attivita("Il bersaglio nascosto",
        ["Scrivete in R4 una strategia «se… allora…»",
         "Un componente del gruppo, bendato, fa 6 lanci di pallina verso il bersaglio sul pavimento",
         "Dopo ogni lancio sente solo il punteggio: 3 nel cerchio piccolo, 1 nel cerchio grande, 0 fuori",
         "Segue la strategia del gruppo; gli altri non danno indicazioni. In R4: i 6 punteggi"],
        "gruppo", "R4", "3 + 10 minuti", [(180, "Strategia"), (600, "Lanci")], materiale="benda, palline di carta",
        esempio="«se il punteggio sale, ripeti lo stesso lancio; se scende, cambia di poco la forza»",
        note="18-31 min. Il docente dice solo il punteggio. Se il tempo è poco: 4 lanci per volontario."))
    S.append(spiega("Il punteggio totale", occhiello="La ricompensa cumulata",
        formula="R = r₁ + r₂ + … + rₙ",
        esempio="punteggi 0, 1, 1, 3, 3, 3 → R = 11",
        testo=["Calcolate R in R4. Chi ha imparato più in fretta? Quale strategia ha funzionato meglio, e perché?"],
        note="31-33 min. Una strategia che non cambia mai non impara; una che cambia sempre troppo non si ferma sul bersaglio."))
    S.append(controllo(
        ["Tempi 23,4 · 24,1 · 23,8 secondi: quanto vale lo scarto?",
         "Un cronometrista parte sempre mezzo secondo in ritardo: errore casuale o sistematico?",
         "Nel bersaglio nascosto: chi è l'agente e che cos'è la ricompensa?"],
        ["0,7 secondi", "Sistematico: tutte le misure sono sbagliate nello stesso verso", "L'agente è chi lancia; la ricompensa è il punteggio 3, 1 o 0"],
        note="33-36 min."))
    S.append(riga("scarto = misura più grande − misura più piccola<br>R = r₁ + r₂ + … + rₙ",
        [("errore casuale", "misure ripetute un po' diverse: si riduce facendo la media"),
         ("errore sistematico", "tutte le misure spostate nello stesso verso: si corregge il modo di misurare"),
         ("R", "somma delle ricompense di tutti i tentativi")],
        note="36-40 min. Preparare le postazioni per l'ora 2."))

    # ================================================================ ORA 2
    R = [("R1", "Equilibrio", "Tabella: codice · prova 1 (s) · prova 2 (s) · note.", 2),
         ("R2", "Lanci", "Tabella: codice · mano · centri su 10 · note.", 1),
         ("R3", "Controllo", "Le tre risposte del controllo finale.", 3)]
    foglio_ora(R); F.append((2, "La raccolta", R))
    S.append(ora(2, "In aula", "La raccolta", "Sei postazioni, due turni, un foglio per gruppo",
        "raccogliere dati di cui ci si può fidare.",
        note="Sei postazioni: tre di equilibrio (spazio libero di un metro) e tre di lanci (cestino e linea a 2 metri). Protocolli dell'ora 1 appesi."))
    S.append(obiettivi([
        "<b>eseguire</b> una prova seguendo il protocollo",
        "<b>misurare</b> seguendo il protocollo",
        "<b>scrivere</b> le misure con le regole di un buon foglio dati",
        "<b>annotare</b> una misura dubbia invece di correggerla a memoria",
        "<b>controllare</b> che ogni codice abbia tutte le misure"]))
    S.append(spiega("Come si scrive un buon foglio dati", occhiello="Esempio",
        tabella=(["codice", "prova 1 (s)", "prova 2 (s)", "note"],
                 [["K7", "23", "31", ""], ["B3", "60", "", "seconda prova non fatta: caviglia"], ["R1", "12", "6", "seconda prova disturbata da un rumore"]]),
        punti=["una riga per persona", "numeri senza unità: l'unità è nell'intestazione", "casella vuota se la prova manca", "un dubbio va nelle note, non si corregge a memoria"],
        note="3-5 min."))
    S.append(spiega("Uno studente non fa la seconda prova", occhiello="Domanda", testo=["Che cosa si scrive nella casella?"],
        risposta=["Niente: la casella resta vuota.", "0 vorrebbe dire «è stato in equilibrio zero secondi», che è un valore vero e diverso."],
        note="5-6 min."))
    S.append(spiega("A turno, dentro il gruppo", occhiello="Chi fa che cosa",
        testo=["Nel gruppo, a turno: uno fa la prova, uno misura (cronometra o conta i centri), uno scrive sul foglio. Poi si cambia, finché tutti hanno fatto la prova."],
        tabella=(["Turno", "Minuti", "Equilibrio", "Lanci"], [["1", "7-19", "gruppi 1, 2, 3", "gruppi 4, 5, 6"], ["2", "20-32", "gruppi 4, 5, 6", "gruppi 1, 2, 3"]]),
        note="6-7 min. Il foglio dell'ora viaggia con il gruppo."))
    S.append(attivita("Turno 1",
        ["Andate alla vostra postazione con il foglio del gruppo",
         "Ognuno scrive il proprio codice su una riga",
         "Equilibrio: due prove a testa, in R1. Lanci: 10 lanci a testa, in R2",
         "Un dubbio? Nelle note"],
        "gruppo", "R1 o R2, secondo la postazione", "12 minuti", [(720, "Turno 1")],
        esempio="K7 · 23 · 31 · (note vuote)",
        note="7-19 min. Girare tra le postazioni e controllare che si segua il protocollo."))
    S.append(attivita("Turno 2",
        ["Scambio: chi era all'equilibrio va ai lanci, e viceversa",
         "Stesse regole",
         "Alla fine controllate: ogni codice ha tutte le misure?"],
        "gruppo", "R1 o R2, secondo la postazione", "12 minuti", [(720, "Turno 2")],
        note="20-32 min."))
    S.append(spiega("Prima di consegnare", occhiello="Il controllo finale",
        punti=["ogni codice ha due prove di equilibrio e i lanci?", "le caselle vuote sono spiegate nelle note?", "ci sono nomi sul foglio? (non devono esserci)"],
        note="32-33 min. Le prove mancanti si recuperano nei minuti finali."))
    S.append(controllo(
        ["Se uno studente non fa i lanci, che cosa si scrive?", "Perché non si scrive 0?", "Perché sul foglio c'è il codice e non il nome?"],
        ["Niente: la casella resta vuota", "Perché 0 è un valore vero: zero centri", "Per la privacy: i dati non devono far riconoscere le persone"],
        note="33-36 min."))
    S.append(riga("una riga per persona, una colonna per misura<br>dato mancante = casella vuota",
        [("vuoto", "la prova non è stata fatta"), ("0", "la prova è stata fatta, e il risultato è zero")],
        dopo="I fogli dei gruppi vanno subito al laboratorio.",
        note="36-40 min. Riordinare l'aula."))

    # ================================================================ ORA 3
    R = [("R1", "Il rifiuto", "Che cosa ha fatto il foglio con il valore 600? Quale regola lo blocca?", 1),
         ("R2", "Errori e decisioni", "Errore trovato · decisione (correggo, svuoto, tengo) · motivo.", 1),
         ("R3", "Quanto sbagliamo copiando", "Caselle diverse ÷ caselle confrontate = ___%.", 1),
         ("R4", "Controllo", "Le tre risposte del controllo finale.", 3)]
    foglio_ora(R); F.append((3, "Dal foglio di carta all'archivio", R))
    S.append(ora(3, "In laboratorio", "Dal foglio di carta all'archivio", "Inserimento controllato, pulizia, registro",
        "trasformare i fogli della raccolta in dati di cui ci si può fidare.",
        note="Preparare: foglio condiviso «Prove 1P» (colonne A codice, B mano, C equilibrio_1, D equilibrio_2, E lanci_10) con la convalida su ogni colonna; foglio «Parallelo» con le stesse colonne; foglio «Registro» (chi, riga, colonna, prima, dopo, motivo)."))
    S.append(obiettivi([
        "inserire dati in un foglio con la <b>convalida</b>",
        "dire quale <b>regola</b> blocca un valore sbagliato",
        "trovare caselle vuote, codici ripetuti e valori impossibili con le <b>formule</b>",
        "decidere che cosa fare di un errore e scriverlo nel <b>registro</b>",
        "misurare quanti errori si fanno <b>copiando</b>",
        "scrivere una regola con <b>E</b> e il suo contrario con <b>O</b>"]))
    S.append(spiega("La convalida: un controllo all'ingresso", occhiello="Il foglio accetta solo valori previsti",
        testo=["Il foglio conosce il contratto dei dati: se scrivete un valore fuori dalle regole, lo rifiuta."],
        esempio="Dati › Convalida dei dati › colonne C e D: numero tra 0 e 60 › se non è valido: rifiuta",
        note="3-4 min. La convalida è già impostata: qui si mostra dove si trova."))
    S.append(attivita("Inserite i vostri dati",
        ["Un componente inserisce il foglio del gruppo in «Prove 1P», nelle righe del gruppo",
         "Un altro componente, senza guardare, inserisce le stesse prove di equilibrio nel foglio «Parallelo»",
         "Poi scrivete <b>600</b> in una casella di prova: che cosa succede? Rispondete in R1, poi cancellate",
         "Un valore rifiutato davvero? Controllate il foglio di carta"],
        "gruppo", "sul computer; poi R1", "10 minuti", [(600, "Inserire")],
        esempio="K7 · destra · 23 · 31 · 6",
        note="4-14 min. Risposta R1: il foglio rifiuta 600 perché l'equilibrio deve essere tra 0 e 60 secondi."))
    S.append(spiega("Errori che la convalida non vede", occhiello="Perché serve anche pulire",
        punti=["un valore possibile ma sbagliato: 32 scritto 23", "lo stesso codice inserito due volte", "una prova dimenticata: la casella vuota è ammessa"],
        tabella=(["Che cosa cerco", "Formula", "Risultato"],
                 [["caselle vuote", "=CONTA.VUOTE(C2:E30)", "quante sono"], ["codici ripetuti", "=CONTA.SE(A$2:A$30;A2)>1", "VERO se il codice è doppio"],
                  ["valore impossibile", "=O(C2&lt;0;C2>60)", "VERO se fuori dal contratto"], ["testo al posto del numero", "=VAL.NUMERO(C2)", "FALSO se non è un numero"]], True),
        note="14-16 min. Le formule di riga vanno in colonne nuove a destra e si trascinano fino alla riga 30."))
    S.append(spiega("E e O", occhiello="Condizioni logiche",
        formula="valido: E(C2>=0; C2&lt;=60)<br>non valido: O(C2&lt;0; C2>60)",
        testo=["<b>E</b> è vero se tutte le condizioni sono vere. <b>O</b> è vero se almeno una è vera. Il contrario di «tutte e due vere» è «almeno una falsa»."],
        note="16-17 min. È la legge di De Morgan."))
    S.append(spiega("Che cosa fare di un errore", occhiello="Tre decisioni, sempre scritte",
        carte=[("Correggere", "se il foglio di carta dice con certezza il valore giusto", "#3A8A3E"), ("Svuotare", "se il valore è sbagliato e non si può ricontrollare", "#DB6A1C"),
               ("Tenere", "se il valore è strano ma vero: un valore anomalo non è un errore", "#2C8BC9")],
        tabella=(["chi", "riga", "colonna", "prima", "dopo", "motivo"], [["gruppo 3", "14", "equilibrio_2", "23", "32", "foglio di carta: cifre invertite"]]),
        dopo=["Ogni modifica va nel foglio «Registro». Mai inventare un valore."],
        note="17-19 min."))
    S.append(attivita("Pulite e registrate",
        ["Applicate le quattro formule di controllo alle vostre righe",
         "Per ogni VERO sospetto controllate il foglio di carta",
         "Decidete: correggere, svuotare o tenere. Scrivetelo in R2 e nel foglio «Registro»"],
        "gruppo", "R2 e foglio «Registro»", "7 minuti", [(420, "Pulire")],
        esempio="riga 14: 23 al posto di 32 · correggo · il foglio di carta dice 32",
        note="19-26 min. Caso da discutere: un equilibrio di 60 secondi. È il massimo previsto: si tiene."))
    S.append(spiega("Quanto sbagliamo copiando?", occhiello="Il confronto tra i due inserimenti",
        codice="=SE(\'Prove 1P\'!C2=Parallelo!C2;0;1)",
        testo=["La formula vale 1 se le due caselle sono diverse. Si sommano gli 1 e si divide per il numero di caselle confrontate."],
        esempio="2 caselle diverse su 58 (29 persone × 2 prove) → 2 ÷ 58 ≈ 3,4%",
        dopo=["Scrivete in R3 la percentuale della classe."],
        note="26-29 min. Lavoro alla LIM. È una stima della qualità dei nostri dati: un numero da mettere nel cruscotto dell'installazione."))
    S.append(spiega("Il file finale", occhiello="Esportazione",
        punti=["File › Scarica › CSV", "Nome: <b>prove_1p.csv</b>", "Apritelo con un editor di testo: 30 righe, i nomi delle colonne e 29 persone"],
        note="29-33 min."))
    S.append(controllo(
        ["Scrivi la regola del <b>non valido</b> per l'equilibrio, con O.", "Che differenza c'è tra una casella vuota e uno 0?", "Un valore è sbagliato e non puoi ricontrollarlo: correggi o svuoti?"],
        ["O(equilibrio &lt; 0; equilibrio > 60)", "Vuota: la prova manca. 0: la prova c'è e il risultato è zero", "Svuoti, e lo scrivi nel registro"],
        note="33-36 min."))
    S.append(riga("valido ⇔ (x ≥ 0) E (x ≤ 60)<br>non valido ⇔ (x &lt; 0) O (x > 60)",
        [("E", "vero se tutte le condizioni sono vere"), ("O", "vero se almeno una condizione è vera")],
        dopo="Pezzi per l'installazione: prove_1p.csv, il registro e la percentuale di errori di copiatura.",
        note="36-40 min. Conservare i fogli di carta fino alla giornata 4."))
    return "IA e dati 1P · Giornata 3 · Il corpo come fonte di dati", S, F
