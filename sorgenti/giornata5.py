from g import *

def build():
    S, F = [], []
    S.append(titolo_giornata(5, "Recupero, oppure il primo modello",
        "Che cosa resta da sistemare? Se niente: costruiamo un classificatore che funziona davvero.",
        [("Ora 1 · In laboratorio", "Distanze e vicini: che frutto è W?"),
         ("Ora 2 · In laboratorio", "Progettare il modello e scommettere"),
         ("Ora 3 · In laboratorio", "Il torneo dei classificatori")],
        note="Giornata condotta dal docente di informatica. Il percorso si è già concluso in 4 giornate. Se qualcosa è rimasto indietro, questa giornata serve a recuperarlo con i file delle giornate precedenti (slide successiva). Se la classe è in pari, si fa il primo modello. Dati: dati/frutti.csv (24 frutti) e dati/frutti_segreti.csv (7 frutti)."))
    S.append(spiega("Prima di cominciare: c'è qualcosa da recuperare?", occhiello="Per il docente",
        punti=["Corpus o pappagallo incompleti → giornata-1.html, ora 3",
               "Calcolatore non collaudato → giornata-2.html, ora 3",
               "Dati delle prove non puliti → giornata-3.html, ora 3",
               "Stazioni dell'installazione da finire → giornata-4.html, ora 3"],
        testo=["Si aprono quei file e si riprende dalla slide indicata. Se tutto è a posto, si va avanti con questo file."],
        note="Usare il tasto Home nei file delle altre giornate per tornare all'inizio; il numero della slide si può scrivere nell'indirizzo dopo il simbolo #."))

    # ================================================================ ORA 1
    R = [("R1", "Una distanza", "Il calcolo della distanza tra due frutti, passo per passo.", 1),
         ("R2", "La scommessa su W", "Che cosa dirà il modello? Gettoni puntati.", 1),
         ("R3", "I 3 vicini, senza normalizzare", "I tre frutti più vicini a W e il loro tipo.", 1),
         ("R4", "I 3 vicini, normalizzando", "I tre frutti più vicini a W e il loro tipo.", 1),
         ("R5", "Perché è cambiato?", "La spiegazione del gruppo.", 1),
         ("R6", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((1, "Distanze e vicini", R))
    S.append(ora(1, "In laboratorio", "Distanze e vicini", "Il classificatore dei vicini sul foglio di calcolo",
        "far decidere al foglio di calcolo che frutto è W."))
    S.append(obiettivi([
        "calcolare la <b>distanza</b> tra due esempi con più misure",
        "trovare i <b>3 vicini</b> di un frutto nuovo con il foglio di calcolo",
        "decidere il tipo con il <b>voto di maggioranza</b>",
        "spiegare perché la <b>normalizzazione</b> cambia la risposta"]))
    S.append(sorteggio("Gruppi nuovi anche oggi.", note="Inserire gli assenti e premere Sorteggia."))
    S.append(spiega("Dimmi a chi somigli e ti dirò che cosa sei", occhiello="L'idea",
        testo=["Abbiamo 24 frutti misurati e già etichettati: mandarino, arancia, limone. Arriva un frutto nuovo, W.",
               "Cerchiamo i 3 frutti più <b>simili</b>, cioè più <b>vicini</b>, e guardiamo il loro tipo: vince il tipo più frequente."],
        attenzione="Si chiama classificatore dei k vicini (in inglese k-NN): qui k = 3. È apprendimento supervisionato, come Teachable Machine, con un metodo molto più semplice.",
        note="3-5 min."))
    S.append(spiega("Quanto sono vicini due frutti?", occhiello="La distanza",
        formula="d = √( (a₁ − b₁)² + (a₂ − b₂)² + (a₃ − b₃)² )",
        testo=["a₁, a₂, a₃ sono peso, larghezza e altezza del primo frutto; b₁, b₂, b₃ quelli del secondo."],
        esempio=["Con due misure è il teorema di Pitagora: tra (0, 0) e (3, 4) la distanza è √(9 + 16) = √25 = 5.",
                 "Frutto 1 (116 g; 5,8 cm; 5,3 cm) e frutto 2 (62 g; 6,7 cm; 4,4 cm): √(54² + 0,9² + 0,9²) ≈ 54,0"],
        dopo=["In R1: la distanza tra il frutto 1 e il frutto W (125 g; 6,2 cm; 5,4 cm)."],
        timer=[(180, "R1")], rumore="discussione", fase="gruppo",
        note="5-9 min. Soluzione R1: √(9² + 0,4² + 0,1²) ≈ 9,0."))
    S.append(spiega("La scommessa sul frutto W", occhiello="125 g · larghezza 6,2 cm · altezza 5,4 cm",
        testo=["Non che cosa è secondo voi: che cosa dirà il modello? Mandarino, arancia o limone?",
               "Scrivetelo in R2 e puntate da 0 a 5 gettoni."],
        timer=[(60, "R2")], rumore="discussione", fase="gruppo",
        note="9-10 min. Per il buon senso W è un mandarino grande, piccolo e schiacciato. Chi prevede limone ha capito il modello meglio del buon senso."))
    S.append(attivita("I 3 vicini di W",
        ["Aprite frutti.csv: A id, B peso, C larghezza, D altezza, E tipo. Scrivete W in K2, L2, M2",
         "In F2: <span class=\"mono\">=RADQ((B2-$K$2)^2+(C2-$L$2)^2+(D2-$M$2)^2)</span> e trascinate fino alla riga 25",
         "Ordinate <b>tutta la tabella</b> per la colonna F, dalla più piccola",
         "In R3: i primi 3 frutti e il loro tipo. Che cosa dice il modello?"],
        "gruppo", "R3", "7 minuti", [(420, "R3")],
        esempio="se i 3 vicini sono arancia, arancia, limone → il modello dice arancia",
        note="10-17 min. Ordinare tutta la tabella, non solo la colonna F. Soluzione: limone 24 (4,54), limone 11 (5,94), limone 20 (6,54): il modello dice limone."))
    S.append(spiega("Perché limone?", occhiello="Il problema delle unità",
        punti=["il peso è in grammi: differenze di decine (125 contro 100 fa 25)", "larghezza e altezza sono in centimetri: differenze di pochi centimetri",
               "al quadrato: 25 grammi pesano 625, 3 centimetri pesano 9"],
        testo=["W pesa quanto un limone: nella distanza conta quasi solo il peso."],
        note="17-19 min."))
    S.append(attivita("Normalizziamo, poi rifacciamo",
        ["Rivincita: nuova scommessa in R2",
         "Colonne G, H, I: min-max di peso, larghezza, altezza. G2: <span class=\"mono\">=(B2-MIN(B$2:B$25))/(MAX(B$2:B$25)-MIN(B$2:B$25))</span>",
         "W normalizzato con gli stessi minimi e massimi in K3, L3, M3; nuova distanza in J sulle colonne G, H, I",
         "In R4: i 3 vicini nuovi"],
        "gruppo", "R4", "9 minuti", [(540, "R4")],
        esempio="peso di W normalizzato: (125 − 62) ÷ (235 − 62) ≈ 0,36",
        note="19-28 min. Minimi e massimi: peso 62-235 g, larghezza 5,1-8,8 cm, altezza 3,5-9,5 cm. Distanza: J2 =RADQ((G2-$K$3)^2+(H2-$L$3)^2+(I2-$M$3)^2). Soluzione: mandarino 1 (0,121), mandarino 18 (0,144), mandarino 12 (0,155)."))
    S.append(spiega("Normalizzando: mandarino", occhiello="Soluzione",
        tabella=(["", "1° vicino", "2° vicino", "3° vicino", "Verdetto"],
                 [["senza normalizzare", "limone 24", "limone 11", "limone 20", "limone"], ["normalizzando", "mandarino 1", "mandarino 18", "mandarino 12", "mandarino"]]),
        testo=["Ora tutte e tre le misure contano allo stesso modo. Scrivete in R5 perché il verdetto è cambiato."],
        timer=[(120, "R5")], rumore="discussione", fase="gruppo",
        note="28-33 min. W è stato scelto apposta: gli altri frutti di prova danno lo stesso verdetto nei due modi."))
    S.append(controllo(
        ["Quanto vale la distanza tra (0, 0) e (3, 4)?", "Che cosa fa la normalizzazione alla distanza?", "Che cosa succede con k = 1?"],
        ["5", "Fa contare allo stesso modo tutte le misure, anche con unità diverse", "Decide un solo vicino: basta un esempio sbagliato nei dati per sbagliare"],
        note="33-36 min."))
    S.append(riga("d = √( (a₁ − b₁)² + (a₂ − b₂)² + (a₃ − b₃)² )",
        [("d", "distanza tra due esempi"), ("k vicini", "vince il tipo più frequente tra i k esempi più vicini"),
         ("normalizzare", "senza, conta la misura con i numeri più grandi")],
        note="36-40 min."))

    # ================================================================ ORA 2
    R = [("R1", "Che tipo di problema?", "Classificazione o regressione, per ogni esempio.", 1),
         ("R2", "Le nostre scelte", "k · normalizzazione sì/no · misure usate.", 1),
         ("R3", "Perché", "Una motivazione per ogni scelta.", 1),
         ("R4", "Prove su X, Y, Z", "Il verdetto del nostro modello su tre frutti di prova.", 1),
         ("R5", "La scommessa", "Quanti frutti segreti su 7 indovineremo? Gettoni puntati.", 1),
         ("R6", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((2, "Progettare il modello", R))
    S.append(ora(2, "In laboratorio", "Progettare il modello", "Scelte di progetto e valutazione",
        "decidere come è fatto il nostro modello e scommettere su quanto funziona."))
    S.append(obiettivi([
        "distinguere <b>classificazione</b> e <b>regressione</b>",
        "distinguere le <b>misure</b> che il modello guarda dalla <b>risposta</b> da prevedere",
        "spiegare perché si valuta su esempi <b>mai visti</b>",
        "scegliere e motivare le <b>scelte di progetto</b>",
        "fare una <b>previsione</b> sull'accuratezza"]))
    S.append(spiega("Due tipi di problema", occhiello="Che cosa prevede il modello",
        tabella=(["", "Che cosa prevede", "Esempio"],
                 [["Classificazione", "una categoria", "tipo di frutto; messaggio pubblicitario o no"], ["Regressione", "un numero", "ore di sonno dalle ore di schermo (la retta della giornata 2)"]]),
        testo=["Le <b>misure</b> che il modello guarda (peso, larghezza, altezza) si chiamano in inglese <i>feature</i>; la risposta da prevedere (il tipo) si chiama <i>target</i>."],
        dopo=["In R1: domani piove? · quanti millimetri di pioggia? · il prezzo di una bici usata · un messaggio è pubblicità o no?"],
        timer=[(120, "R1")], rumore="discussione", fase="gruppo",
        note="3-7 min. Soluzioni: classificazione, regressione, regressione, classificazione."))
    S.append(spiega("Lo studente che impara a memoria", occhiello="Una storia",
        testo=["Uno studente impara a memoria le risposte della verifica dell'anno scorso. A quella verifica prende 10. A una verifica nuova?"],
        attenzione="Un modello si valuta su esempi che non ha mai visto. Se va bene sugli esempi visti e male su quelli nuovi, ha imparato a memoria: in inglese overfitting.",
        note="7-11 min."))
    S.append(spiega("Le scelte di chi progetta", occhiello="Tre decisioni",
        carte=[("k", ["quanti vicini votano: 1, 3 o 5"], "#2C8BC9"), ("Normalizzazione", ["sì o no"], "#3A8A3E"),
               ("Misure", ["tutte e tre, solo alcune, o una nuova: la forma = altezza ÷ larghezza"], "#DB6A1C")],
        testo=["Queste scelte non le impara il modello: le decide chi lo progetta, e le deve motivare."],
        esempio="la forma: un limone è allungato (forma maggiore di 1,2), un mandarino è schiacciato (forma minore di 1)",
        note="11-14 min."))
    S.append(attivita("Progettate il vostro modello",
        ["Scrivete in R2 le vostre tre scelte e in R3 una motivazione per ciascuna",
         "Preparate il foglio di calcolo con le vostre scelte",
         "Provatelo su X (6,3 cm; 8,0 cm), Y (6,1 cm; 5,3 cm), Z (7,6 cm; 7,4 cm) usando solo larghezza e altezza, oppure anche il peso se lo chiedete al docente",
         "Scrivete i verdetti in R4"],
        "gruppo", "R2, R3, R4", "14 minuti", [(840, "Progetto")],
        esempio="k = 3, normalizzazione sì, misure: peso e forma · perché: la forma distingue il limone",
        note="14-28 min. Verdetti attesi sui frutti di prova: X limone, Y mandarino, Z arancia. X, Y e Z hanno solo larghezza e altezza: il peso si può tralasciare oppure stimare."))
    S.append(spiega("La scommessa", occhiello="Quanti frutti segreti indovinerà il vostro modello?",
        testo=["Scrivete in R5 un numero da 0 a 7 e puntate da 0 a 10 gettoni. Nell'ora 3 il modello non si può più cambiare."],
        timer=[(120, "R5")], rumore="discussione", fase="gruppo",
        note="28-33 min. Raccogliere le scommesse per iscritto."))
    S.append(controllo(
        ["Prevedere il prezzo di una casa: classificazione o regressione?", "Perché non si valuta un modello sugli esempi da cui ha imparato?", "Che cos'è k?"],
        ["Regressione: prevede un numero", "Perché li ha già visti: si misurerebbe la memoria, non quanto ha imparato", "Il numero di vicini che votano"],
        note="33-36 min."))
    S.append(riga("classificazione: una categoria · regressione: un numero",
        [("scelte di progetto", "k, normalizzazione, misure: le decide chi progetta"), ("valutazione", "sempre su esempi mai visti")],
        note="36-40 min."))

    # ================================================================ ORA 3
    R = [("R1", "I verdetti", "Per i 7 frutti segreti: i vicini e il verdetto del modello.", 2),
         ("R2", "Accuratezza", "Verdetti giusti ÷ 7, confrontata con la scommessa.", 1),
         ("R3", "Il frutto impossibile", "Perché S7 è difficile per tutti? Che cosa servirebbe?", 2),
         ("R4", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((3, "Il torneo dei classificatori", R))
    S.append(ora(3, "In laboratorio", "Il torneo dei classificatori", "Sette frutti che il modello non ha mai visto",
        "mettere alla prova il modello su frutti mai visti."))
    S.append(obiettivi([
        "applicare il proprio modello a dati nuovi <b>senza cambiarlo</b>",
        "calcolare l'<b>accuratezza</b> e confrontarla con la scommessa",
        "riconoscere un caso che <b>nessun modello</b> può risolvere con questi dati"]))
    S.append(spiega("I frutti segreti", occhiello="Classificateli con il vostro modello",
        tabella=(["Frutto", "Peso (g)", "Larghezza (cm)", "Altezza (cm)"],
                 [["S1", "210", "8,1", "7,9"], ["S2", "78", "5,6", "4,6"], ["S3", "122", "6,1", "8,4"], ["S4", "128", "6,3", "5,6"],
                  ["S5", "172", "7,3", "8,9"], ["S6", "140", "5,9", "7,8"], ["S7", "170", "6,6", "8,9"]], True),
        note="3-4 min. Il file è dati/frutti_segreti.csv."))
    S.append(attivita("I verdetti",
        ["Per ogni frutto: misure in K2, L2, M2",
         "Leggete i vicini e scrivete in R1 il verdetto",
         "Il modello non si cambia: le scelte sono quelle dell'ora 2",
         "Consegnate i 7 verdetti prima della rivelazione"],
        "gruppo", "R1", "11 minuti", [(660, "Verdetti")],
        esempio="S1 · vicini arancia, arancia, arancia · verdetto arancia",
        note="4-15 min."))
    S.append(spiega("I tipi veri", occhiello="Rivelazione",
        tabella=(["S1", "S2", "S3", "S4", "S5", "S6", "S7"], [["arancia", "mandarino", "limone", "mandarino", "arancia", "limone", "arancia"]]),
        formula="accuratezza = verdetti giusti ÷ 7",
        testo=["Scrivetela in R2 e confrontatela con la vostra scommessa."],
        timer=[(180, "R2")], rumore="discussione", fase="gruppo",
        note="15-19 min. Chi ha previsto esattamente la propria accuratezza vince il doppio dei gettoni."))
    S.append(spiega("Stessa accuratezza, errori diversi", occhiello="Due modelli a confronto",
        tabella=(["Modello", "Accuratezza", "Sbaglia", "Perché"],
                 [["senza normalizzazione", "6 su 7", "S4", "mandarino pesante scambiato per limone"], ["con normalizzazione", "6 su 7", "S7", "arancia piccola e allungata scambiata per limone"]]),
        testo=["Vale per k = 1, 3 e 5. Due modelli con lo stesso numero possono sbagliare cose diverse: l'accuratezza da sola non dice tutto."],
        note="19-25 min."))
    S.append(spiega("S7 è impossibile con questi dati", occhiello="Il limite dei dati",
        testo=["Con peso, larghezza, altezza e anche la forma, S7 assomiglia davvero a un limone. Nessuna scelta di k o di normalizzazione lo salva.",
               "Che cosa servirebbe? Scrivetelo in R3."],
        risposta=["Un'altra misura che nei dati non c'è: il <b>colore</b> della buccia.", "Il limite di un modello spesso non sta nel metodo, ma nei dati che gli diamo."],
        timer=[(180, "R3")], rumore="discussione", fase="gruppo",
        note="25-33 min."))
    S.append(controllo(
        ["Due modelli con 6 su 7: sono uguali?", "Che cosa serve per indovinare S7?", "A che cosa serviva la scommessa?"],
        ["No: sbagliano frutti diversi", "Una misura nuova, per esempio il colore", "A confrontare quanto pensavamo che funzionasse con quanto funziona davvero"],
        note="33-36 min."))
    S.append(riga("un modello non può usare un'informazione che non è nei dati",
        [("accuratezza", "si misura su dati nuovi, e può essere diversa da quella sperata")],
        dopo="Se volete: aggiungete la stazione «Che frutto è?» all'installazione.",
        note="36-40 min."))
    return "IA e dati 1P · Giornata 5 · Recupero, oppure il primo modello", S, F
