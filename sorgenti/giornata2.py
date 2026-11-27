from g import *

def build():
    S, F = [], []
    S.append(titolo_giornata(2, "Incertezza e misura",
        "Quanto possiamo essere sicuri di qualcosa che ricaviamo dai dati?",
        [("Ora 1 · In aula", "Probabile non vuol dire certo"),
         ("Ora 2 · In aula", "Tanti numeri, pochi numeri"),
         ("Ora 3 · In laboratorio", "Il calcolatore statistico e i dati della 1Z")],
        note="Materiale: una moneta per coppia; una moneta normale e una con due teste in un sacchetto; 10 gettoni per gruppo (o fagioli); calcolatrici. Nei fogli dei lanci, metà con il biglietto «inventa» e metà «lancia». Pezzi per l'installazione: la tabella della moneta truccata, i lanci della classe, il calcolatore."))

    # ================================================================ ORA 1
    R = [("R1", "La scala da 0 a 1", "I sei eventi in ordine, ciascuno con il suo numero.", 1),
         ("R2", "I nostri 20 lanci", "T o C per 20 volte; numero di teste; frequenza = teste ÷ 20.", 1),
         ("R3", "La serie più lunga", "Quanti risultati uguali di fila, al massimo? Lanciata o inventata?", 1),
         ("R4", "I gettoni", "Dopo ogni lancio: gettoni su «normale» e su «truccata».", 1),
         ("R5", "L'albero", "L'albero della moneta e P(truccata | testa).", 1),
         ("R6", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((1, "Probabile non vuol dire certo", R))
    S.append(ora(1, "In aula", "Probabile non vuol dire certo", "Probabilità con monete e gettoni",
        "capire quanto possiamo fidarci di ciò che osserviamo."))
    S.append(obiettivi([
        "dare a un evento un numero tra <b>0</b> (impossibile) e <b>1</b> (certo)",
        "calcolare la probabilità che un evento <b>non</b> succeda",
        "calcolare la <b>frequenza</b> dei risultati di un esperimento",
        "spiegare perché con <b>più prove</b> la frequenza si avvicina alla probabilità",
        "usare un <b>albero</b> per cambiare una probabilità dopo un'osservazione",
        "spiegare perché tante prove non danno la <b>certezza</b>, ma una sola smentita sì"]))
    S.append(sorteggio("Gruppi nuovi anche oggi. Andate all'isola del colore del vostro gruppo.",
        note="Inserire gli assenti e premere Sorteggia."))
    S.append(spiega("La probabilità: un numero da 0 a 1", occhiello="Che cosa vuol dire probabile",
        carte=[("0", ["impossibile", "non succede mai"], "#C8372D"), ("1/2 = 0,5 = 50%", ["come testa o croce", "una volta su due"], "#E2B007"), ("1", ["certo", "succede sempre"], "#3A8A3E")],
        testo=["La <b>probabilità</b> di un evento dice quanto è facile che succeda. Si scrive P(evento)."],
        note="3-5 min. Disegnare alla lavagna una lunga riga con 0 a sinistra e 1 a destra."))
    S.append(attivita("La scala della probabilità",
        ["Mettete in ordine i sei eventi, dal meno probabile al più probabile",
         "Scrivete accanto a ognuno un numero tra 0 e 1",
         "Eventi: <b>un dado fa 7</b> · <b>7 × 8 = 56</b> · <b>esce testa</b> · <b>un dado fa 6</b> · <b>domani sorge il sole</b> · <b>vincere al Superenalotto</b>"],
        "gruppo", "R1", "3 minuti", [(180, "R1")],
        esempio="«Domani a Ferrara c'è nebbia, a novembre» → molto probabile, vicino a 1 ma non 1",
        note="5-8 min. Soluzione nella slide successiva."))
    S.append(spiega("Soluzione", occhiello="La scala",
        tabella=(["Evento", "Probabilità", "Perché"],
                 [["un dado fa 7", "0", "nessuna faccia ha il 7"], ["vincere al Superenalotto", "quasi 0", "1 caso su più di 600 milioni"],
                  ["un dado fa 6", "1/6 ≈ 0,17", "1 faccia su 6"], ["esce testa", "1/2 = 0,5", "1 faccia su 2"],
                  ["domani sorge il sole", "quasi 1", "è sempre successo e lo spiega la fisica"], ["7 × 8 = 56", "1", "è un calcolo: è certo"]], True),
        note="8-9 min. Differenza tra certo (7 × 8, dimostrabile) e quasi certo (il sole, basato su esperienza e fisica). Superenalotto: 1 su 622.614.630 per il 6 con una colonna."))
    S.append(spiega("Due regole", occhiello="Contare i casi",
        formula="P(non E) = 1 − P(E)<br>P(E) = casi favorevoli ÷ casi possibili",
        testo=["«non E» vuol dire «l'evento E non succede». La seconda regola vale se tutti i casi sono ugualmente probabili."],
        esempio=["P(il dado fa 6) = 1/6, quindi P(il dado non fa 6) = 1 − 1/6 = 5/6.", "P(il dado fa un numero pari) = 3 casi su 6 = 3/6 = 1/2."],
        note="9-11 min."))
    S.append(attivita("Testa o croce",
        ["Leggete in segreto il biglietto nel vostro foglio: c'è scritto <b>lanciate</b> oppure <b>inventate</b>",
         "Scrivete in R2 20 risultati: T per testa, C per croce (lanciando davvero, oppure inventando)",
         "Contate le teste",
         "Calcolate la frequenza: teste ÷ 20"],
        "coppia", "R2", "5 minuti", [(300, "Lanci")], materiale="una moneta",
        esempio="12 teste su 20 lanci → frequenza = 12 ÷ 20 = 0,6",
        note="11-16 min. Non dire a voce chi inventa. I fogli si conservano: servono nell'ora 3."))
    S.append(spiega("Più prove, più vicini a 0,5", occhiello="La legge dei grandi numeri",
        testo=["Chi ha fatto esattamente 10 teste? Pochi: succede circa 18 volte su 100.",
               "Sommiamo i lanci di tutta la classe: la frequenza è molto più vicina a 0,5."],
        formula="frequenza = successi ÷ prove",
        attenzione="Con molte prove la frequenza si avvicina alla probabilità, ma la moneta non «recupera»: dopo 5 teste di fila la croce non diventa più probabile.",
        note="16-18 min. Raccogliere alla lavagna le teste di ogni coppia e calcolare la frequenza di classe."))
    S.append(attivita("Dati lanciati o inventati?",
        ["Il prof guarda i fogli e dice per ognuno: «lanciata» o «inventata»",
         "Poi, in R3: trovate la serie più lunga di risultati uguali di fila nella vostra sequenza",
         "Secondo voi, come ha fatto il prof?"],
        "coppia", "R3", "3 minuti", [(180, "R3")],
        esempio="T C C T <b>T T T T</b> C T … → serie più lunga: 4 teste di fila",
        note="18-21 min. Il trucco: chi inventa alterna troppo (T C T C…). In 20 lanci veri c'è una serie di almeno 4 risultati uguali circa 77 volte su 100, e di almeno 5 circa 46 volte su 100. Ritirare tutti i fogli dei lanci."))
    S.append(spiega("La moneta del prof", occhiello="Due monete in un sacchetto",
        carte=[("Moneta normale", ["una faccia testa, una croce", "P(testa) = 1/2"], "#2C8BC9"), ("Moneta truccata", ["due facce testa", "P(testa) = 1"], "#DB6A1C")],
        testo=["Il prof ne prende una a caso, senza guardare, e la lancia. Esce testa. Quale moneta ha in mano?"],
        note="21-22 min. Mostrare le due monete, metterle nel sacchetto, estrarne una e tenerla nel pugno."))
    S.append(attivita("Puntate i gettoni",
        ["Ogni gruppo ha 10 gettoni: dividili tra «normale» e «truccata»",
         "Dopo ogni lancio potete spostarli",
         "Scrivete in R4 come li avete messi dopo ogni lancio",
         "I gettoni dicono quanto siete sicuri"],
        "gruppo", "R4", "6 minuti", [(360, "Gettoni")], materiale="10 gettoni",
        esempio="Prima del lancio: 5 e 5. Dopo una testa: 7 su truccata e 3 su normale.",
        note="22-28 min. Dopo il primo lancio mostrare l'albero (slide successiva), poi continuare. Se la moneta è normale, prima o poi esce croce: allora tutti i gettoni su normale."))
    S.append(spiega("L'albero delle probabilità", occhiello="Il calcolo dopo una testa",
        tabella=(["Moneta (1/2 ciascuna)", "Faccia", "Probabilità del ramo"],
                 [["normale", "testa", "1/2 × 1/2 = 1/4"], ["normale", "croce", "1/2 × 1/2 = 1/4"], ["truccata", "testa", "1/2 × 1 = 1/2"]]),
        testo=["È uscita testa: restano i rami con testa, 1/4 + 1/2 = 3/4. La parte della truccata è 1/2 su 3/4."],
        formula="P(truccata | testa) = (1/2) ÷ (3/4) = 2/3",
        dopo=["La barra | si legge «sapendo che». Copiate l'albero in R5."],
        note="Durante il gioco, dopo il primo lancio. Disegnare l'albero alla lavagna: radice, due rami per la moneta, poi i rami per la faccia."))
    S.append(spiega("Più teste, più sicuri. Mai certi", occhiello="Dopo n teste di fila",
        tabella=(["Teste di fila", "1", "2", "3", "4", "10"], [["P(truccata)", "2/3 ≈ 0,67", "4/5 = 0,8", "8/9 ≈ 0,89", "16/17 ≈ 0,94", "≈ 0,999"]]),
        formula="P(truccata | n teste) = 1 ÷ (1 + (1/2)ⁿ)",
        carte=[("Tante teste", "la probabilità sale ma non arriva mai a 1: resta la moneta normale fortunata", "#2C8BC9"),
               ("Una croce", "la truccata non ha croci: P(truccata) = 0. Una smentita basta", "#DB6A1C")],
        note="28-31 min. (1/2) elevato alla n è la probabilità che una moneta normale faccia n teste di fila. È lo stesso modo di ragionare della scienza: molte conferme rendono un'idea credibile, una smentita la fa cadere."))
    S.append(spiega("Il pappagallo è come un dado truccato", occhiello="Collegamento con l'intelligenza artificiale",
        testo=["Il pappagallo della giornata 1 sceglie la parola <b>probabile</b>, non quella <b>vera</b>.",
               "E di solito parla sempre con lo stesso tono sicuro: non dice quanto è sicuro."],
        note="31-33 min."))
    S.append(controllo(
        ["P(pioggia) = 0,3. Quanto vale P(non pioggia)?",
         "Dopo 4 teste di fila, quanto vale P(truccata)?",
         "Al quinto lancio esce croce. Quanto vale ora P(truccata)?"],
        ["1 − 0,3 = 0,7", "1 ÷ (1 + 1/16) = 16/17 ≈ 0,94", "0: la moneta truccata non ha croci"],
        note="33-36 min."))
    S.append(riga("P(non E) = 1 − P(E)<br>frequenza = successi ÷ prove",
        [("P(E)", "probabilità dell'evento E, un numero da 0 a 1"),
         ("frequenza", "con tante prove si avvicina alla probabilità"),
         ("P(A | B)", "probabilità di A sapendo che è successo B")],
        dopo="I fogli dei lanci vanno al laboratorio dell'ora 3.",
        note="36-40 min."))

    # ================================================================ ORA 2
    R = [("R1", "Media e valore estremo", "Media e mediana; quale descrive meglio la stanza.", 1),
         ("R2", "La scommessa", "Quale insieme è più disperso: A, B o C?", 1),
         ("R3", "Deviazione standard", "I 5 passi per B oppure per C.", 1),
         ("R4", "z e min-max", "I due calcoli richiesti.", 1),
         ("R5", "Stimare r", "Sei stime di r, una per grafico.", 1),
         ("R6", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((2, "Tanti numeri, pochi numeri", R))
    S.append(ora(2, "In aula", "Tanti numeri, pochi numeri", "Media, mediana, dispersione, correlazione",
        "riassumere tanti numeri con pochi numeri, senza farsi ingannare."))
    S.append(obiettivi([
        "calcolare <b>media</b> e <b>mediana</b> e scegliere la più adatta",
        "leggere la scrittura con il simbolo <b>Σ</b>",
        "calcolare a mano la <b>deviazione standard</b> di pochi numeri",
        "confrontare valori con il <b>punteggio z</b> e la <b>normalizzazione</b>",
        "stimare la <b>correlazione r</b> da un grafico",
        "spiegare che <b>correlazione non vuol dire causa</b>"]))
    S.append(attivita("Media e valore estremo",
        ["Nove persone guadagnano 1.000 € al mese. Entra un miliardario: 1.000.000.000 €",
         "Calcolate la <b>media</b>: somma di tutti i valori diviso quanti sono",
         "Calcolate la <b>mediana</b>: mettete i valori in ordine e prendete quello in mezzo (con un numero pari di valori, la media dei due in mezzo)",
         "Quale dei due numeri descrive meglio le persone nella stanza?"],
        "gruppo", "R1", "3 minuti", [(180, "R1")],
        esempio="Valori 2, 3, 10: media = 15 ÷ 3 = 5; mediana = 3",
        note="3-6 min. Soluzione: media = (9 × 1.000 + 1.000.000.000) ÷ 10 = 100.000.900 €; mediana = 1.000 €. Con un valore estremo la media inganna, la mediana no."))
    S.append(spiega("La media con il simbolo Σ", occhiello="Come si scrive una somma",
        formula="x̄ = (1/n) · Σ xᵢ",
        punti=["<b>x̄</b> (x segnato): la media", "<b>Σ</b> (sigma): «somma tutti»", "<b>xᵢ</b>: il valore numero i", "<b>n</b>: quanti valori ci sono"],
        esempio="A = {4, 6, 8, 10, 12}: Σ xᵢ = 40, n = 5, x̄ = 40 ÷ 5 = 8",
        note="6-8 min. Far leggere la formula ad alta voce a due studenti."))
    S.append(spiega("Chi è più disperso?", occhiello="Scommessa",
        tabella=(["Insieme", "Valori", "Media"], [["A", "4, 6, 8, 10, 12", "8"], ["B", "7, 8, 8, 8, 9", "8"], ["C", "2, 8, 8, 8, 14", "8"]]),
        testo=["Stessa media. In quale insieme i valori sono più sparpagliati intorno alla media? Scrivetelo in R2."],
        timer=[(60, "R2")], rumore="discussione", fase="gruppo",
        note="8-9 min. Molti scelgono A perché i valori sono tutti diversi."))
    S.append(spiega("La deviazione standard in 5 passi", occhiello="Esempio svolto su A",
        tabella=(["x", "scarto (x − 8)", "scarto al quadrato"], [["4", "−4", "16"], ["6", "−2", "4"], ["8", "0", "0"], ["10", "2", "4"], ["12", "4", "16"], ["", "somma", "40"]], True),
        punti=["media = 8", "scarti", "quadrati", "media dei quadrati: 40 ÷ 5 = 8", "radice: σ = √8 ≈ 2,83"], ordinati=True,
        note="9-12 min. Svolgere alla lavagna. σ si legge sigma minuscola."))
    S.append(attivita("Calcolate σ di B oppure di C",
        ["Gruppi 1, 3, 5: insieme B. Gruppi 2, 4, 6: insieme C",
         "Seguite i 5 passi e scrivete la tabella in R3",
         "Arrotondate a due decimali",
         "Confrontate con la vostra scommessa"],
        "gruppo", "R3", "6 minuti", [(360, "R3")], materiale="calcolatrice",
        esempio="A: 16 + 4 + 0 + 4 + 16 = 40 → 40 ÷ 5 = 8 → √8 ≈ 2,83",
        note="12-18 min. Errore tipico: dividere per 4 invece che per 5, o dimenticare la radice."))
    S.append(spiega("C è il più disperso", occhiello="Soluzione",
        tabella=(["Insieme", "Quadrati degli scarti", "Media dei quadrati", "σ"],
                 [["A", "16, 4, 0, 4, 16", "8", "≈ 2,83"], ["B", "1, 0, 0, 0, 1", "0,4", "≈ 0,63"], ["C", "36, 0, 0, 0, 36", "14,4", "≈ 3,79"]]),
        formula="σ = √( (1/n) · Σ (xᵢ − x̄)² )",
        testo=["Il quadrato rende positivi tutti gli scarti e dà più peso a quelli grandi; la radice riporta il risultato all'unità di misura dei dati."],
        note="18-21 min. Senza quadrato la somma degli scarti farebbe sempre 0."))
    S.append(attivita("Confrontare valori diversi",
        ["<b>Punteggio z</b> = (x − media) ÷ σ: di quante σ un valore sta sopra o sotto la media",
         "<b>Min-max</b> = (x − minimo) ÷ (massimo − minimo): porta i valori tra 0 e 1",
         "In R4 calcolate, per l'insieme A: lo z di x = 10 e il min-max di x = 6"],
        "gruppo", "R4", "3 minuti", [(180, "R4")],
        esempio="A, x = 12: z = (12 − 8) ÷ 2,83 ≈ 1,41; min-max = (12 − 4) ÷ (12 − 4) = 1",
        note="21-24 min. Soluzioni: z = 2 ÷ 2,83 ≈ 0,71; min-max = 2 ÷ 8 = 0,25. Servono a confrontare grandezze con unità diverse (secondi e centri nel cestino, giornata 3)."))
    S.append(spiega("Due grandezze insieme: la correlazione r", occhiello="Grafico di dispersione",
        testo=["Ogni punto è una persona: la sua posizione dice due valori, uno in orizzontale e uno in verticale."],
        carte=[("r vicino a 1", "quando una cresce, cresce anche l'altra", "#3A8A3E"), ("r vicino a −1", "quando una cresce, l'altra cala", "#C8372D"), ("r vicino a 0", "nessuna relazione a forma di retta", "#5B6475")],
        formula="−1 ≤ r ≤ 1",
        note="24-25 min. Disegnare a mano tre nuvole di punti."))
    S.append(immagini("Stimare r: grafici 1, 2, 3", [("img/indovina_r_1.png", "Grafico 1", "1"), ("img/indovina_r_2.png", "Grafico 2", "2"), ("img/indovina_r_3.png", "Grafico 3", "3")],
        occhiello="Scrivete in R5 una stima di r per ogni grafico", timer=[(120, "R5")], fase="gruppo", rumore="discussione",
        note="25-27 min. 40 secondi per grafico."))
    S.append(immagini("Stimare r: grafici 4, 5, 6", [("img/indovina_r_4.png", "Grafico 4", "4"), ("img/indovina_r_5.png", "Grafico 5", "5"), ("img/indovina_r_6.png", "Grafico 6", "6")],
        occhiello="Scrivete in R5 una stima di r per ogni grafico", timer=[(120, "R5")], fase="gruppo", rumore="discussione",
        note="27-29 min."))
    S.append(spiega("I valori veri", occhiello="Soluzione",
        tabella=(["Grafico", "1", "2", "3", "4", "5", "6"], [["r", "0,93", "−0,84", "−0,09", "−0,17", "0,48", "−0,10"]]),
        testo=["Il grafico 2 è ore di schermo contro ore di sonno della classe 1Z: lo ritroviamo nell'ora 3."],
        note="29-30 min. Un punto a chi indovina il segno, un altro a chi sbaglia di meno di 0,2."))
    S.append(spiega("Correlazione non vuol dire causa", occhiello="Attenzione",
        carte=[("Gelati e annegamenti", ["Nei mesi in cui si vendono più gelati ci sono più annegamenti.", "Causa comune: il caldo."], "#2C8BC9"),
               ("Schermo e sonno", ["Più schermo, meno sonno.", "Lo schermo toglie sonno, o chi dorme poco usa più lo schermo?"], "#DB6A1C")],
        formula="retta: y = a + b · x",
        testo=["<b>b</b> (pendenza): di quanto cambia y quando x aumenta di 1. <b>a</b> (intercetta): y quando x = 0."],
        note="30-33 min. Esempio di retta: y = 10 − 0,5 · x; se x = 4, y = 8."))
    S.append(controllo(
        ["Punteggio z di x = 8 nell'insieme A (media 8, σ ≈ 2,83)?",
         "Min-max di x = 10 nell'insieme A?",
         "y = 10 − 0,5 · x: quanto vale y per x = 6?"],
        ["z = 0", "(10 − 4) ÷ (12 − 4) = 0,75", "10 − 3 = 7"],
        note="33-36 min."))
    S.append(riga("σ = √( (1/n) · Σ (xᵢ − x̄)² )<br>z = (x − x̄) ÷ σ",
        [("σ", "deviazione standard: la distanza tipica dei valori dalla media"),
         ("z", "di quante σ un valore sta sopra (+) o sotto (−) la media"),
         ("min-max", "(x − min) ÷ (max − min), tra 0 e 1"), ("r", "correlazione, tra −1 e 1")],
        note="36-40 min."))

    # ================================================================ ORA 3
    R = [("R1", "La curva dei lanci", "Che cosa fa la curva all'inizio e alla fine?", 1),
         ("R2", "Collaudo", "I cinque valori del vostro calcolatore sulla 1Z.", 1),
         ("R3", "Stima e verità", "Le due rette e una ragione per cui non coincidono.", 1),
         ("R4", "Controllo", "Le tre risposte del controllo finale.", 3)]
    foglio_ora(R); F.append((3, "Il calcolatore statistico", R))
    S.append(ora(3, "In laboratorio", "Il calcolatore statistico", "E i dati della classe 1Z",
        "trasformare le formule in un foglio che calcola da solo.",
        note="Preparare: foglio condiviso «Lanci» (colonne n ed esito, 20 righe per coppia); modello «Calcolatore» per gruppo con i fogli Dati (colonna A ore di schermo, B ore di sonno della 1Z, righe 2-41) e Statistiche."))
    S.append(obiettivi([
        "inserire i lanci e calcolare la <b>frequenza</b> lancio dopo lancio",
        "usare il simbolo <b>$</b> in una formula da trascinare",
        "leggere un <b>grafico</b> della legge dei grandi numeri",
        "scrivere le formule di media, mediana, σ, z, min-max, correlazione e retta",
        "controllare che il foglio <b>si aggiorni da solo</b>",
        "distinguere la <b>stima</b> ricavata dai dati dalla <b>verità</b>"]))
    S.append(attivita("I lanci nel foglio",
        ["Aprite il foglio «Lanci»: nelle vostre 20 righe, colonna B, scrivete 1 per testa e 0 per croce",
         "In C2 scrivete <span class=\"mono\">=SOMMA($B$2:B2)</span>: le teste fino a quel lancio",
         "In D2 scrivete <span class=\"mono\">=C2/A2</span>: la frequenza fino a quel lancio",
         "Trascinate C2 e D2 fino all'ultima riga"],
        "coppia", "sul computer, foglio «Lanci»", "6 minuti", [(360, "Lanci")],
        esempio="lanci T, C, T → colonna B: 1, 0, 1 → colonna C: 1, 1, 2 → colonna D: 1, 0,5, 0,67",
        note="3-9 min. Anche chi aveva inventato la sequenza la inserisce."))
    S.append(spiega("A che cosa serve il dollaro", occhiello="Riferimento fisso e riferimento che scorre",
        tabella=(["Riga", "Formula dopo il trascinamento", "Che cosa somma"],
                 [["2", "=SOMMA($B$2:B2)", "solo B2"], ["3", "=SOMMA($B$2:B3)", "da B2 a B3"], ["10", "=SOMMA($B$2:B10)", "da B2 a B10"]]),
        testo=["<b>$B$2</b> resta fermo; <b>B2</b> scorre quando si trascina. Senza il dollaro anche l'inizio scorrerebbe e la somma sarebbe sbagliata."],
        note="9-10 min. Far togliere il $ in una cella e trascinare: l'errore si vede subito."))
    S.append(attivita("Il grafico dei lanci",
        ["Selezionate le colonne A e D",
         "Inserisci › Grafico › Grafico a linee",
         "Scrivete in R1: che cosa fa la curva all'inizio? E alla fine?"],
        "coppia", "R1", "3 minuti", [(180, "R1")],
        esempio="asse orizzontale: numero del lancio; asse verticale: frequenza delle teste",
        note="10-13 min. Risposta attesa: all'inizio salta molto, poi si avvicina a 0,5. È la legge dei grandi numeri con i nostri lanci."))
    S.append(spiega("Il calcolatore: il foglio «Statistiche»", occhiello="Un foglio che si riusa con altri dati",
        tabella=(["Cella", "Che cosa", "Formula"],
                 [["B2", "media", "=MEDIA(Dati!A2:A41)"], ["B3", "mediana", "=MEDIANA(Dati!A2:A41)"], ["B4", "minimo", "=MIN(Dati!A2:A41)"],
                  ["B5", "massimo", "=MAX(Dati!A2:A41)"], ["B6", "deviazione standard", "=DEV.ST.POP(Dati!A2:A41)"]], True),
        testo=["<span class=\"mono\">Dati!A2:A41</span> vuol dire: le celle da A2 ad A41 del foglio Dati. Lì ci sono le ore di schermo di 40 studenti della classe 1Z."],
        note="13-14 min. Distribuire il modello."))
    S.append(attivita("Scrivete le formule",
        ["Nel foglio Statistiche: le 5 formule della slide precedente",
         "Nel foglio Dati, colonna C, il punteggio z: <span class=\"mono\">=(A2-Statistiche!$B$2)/Statistiche!$B$6</span>",
         "Colonna D, il min-max: <span class=\"mono\">=(A2-Statistiche!$B$4)/(Statistiche!$B$5-Statistiche!$B$4)</span>",
         "Trascinate C2 e D2 fino alla riga 41"],
        "gruppo", "sul computer, modello «Calcolatore»", "8 minuti", [(480, "Formule")],
        esempio="la colonna D deve andare da 0 (chi ha il minimo) a 1 (chi ha il massimo)",
        note="14-22 min. Nei fogli in italiano gli argomenti si separano con il punto e virgola. Media, σ, minimo e massimo hanno il $ perché devono restare fermi."))
    S.append(spiega("Correlazione e retta", occhiello="Due colonne insieme",
        codice="B8:  =CORRELAZIONE(Dati!A2:A41;Dati!B2:B41)\nB9:  =PENDENZA(Dati!B2:B41;Dati!A2:A41)\nB10: =INTERCETTA(Dati!B2:B41;Dati!A2:A41)",
        attenzione="In PENDENZA e INTERCETTA si scrive prima la colonna da prevedere (il sonno), poi l'altra (lo schermo).",
        tabella=(["Media schermo", "σ schermo", "r", "Pendenza", "Intercetta"], [["4,10", "1,497", "−0,84", "−0,51", "9,92"]]),
        dopo=["Collaudo: il vostro calcolatore deve dare questi valori. Scriveteli in R2. Poi cambiate un numero nei Dati: i risultati cambiano da soli?"],
        timer=[(240, "R2")], rumore="discussione", fase="gruppo",
        note="22-26 min. Se un valore non torna: controllare l'intervallo (A2:A41) e l'ordine degli argomenti di PENDENZA."))
    S.append(spiega("La classe 1Z non esiste", occhiello="Da dove vengono i dati",
        testo=["I dati della 1Z li ha inventati un programma. Ecco la riga che calcola il sonno:"],
        codice="sonno = round((9.6 - 0.45 * schermo + random.gauss(0, 0.45)) * 2) / 2",
        punti=["9,6 − 0,45 · schermo: la relazione vera", "random.gauss: un piccolo errore casuale diverso per ogni studente (il <b>rumore</b>)", "round(… · 2) / 2: arrotonda alla mezz'ora"],
        note="26-28 min."))
    S.append(spiega("Il calcolatore ha trovato la formula?", occhiello="Stima e verità",
        tabella=(["", "Intercetta", "Pendenza"], [["Verità (il programma)", "9,6", "−0,45"], ["Stima (il nostro calcolatore)", "9,92", "−0,51"]]),
        testo=["Vicine, ma non uguali. Perché? Scrivetelo in R3."],
        risposta=["il <b>rumore</b>: ogni studente ha un errore casuale", "i dati sono <b>pochi</b>: 40 studenti", "l'<b>arrotondamento</b> alla mezz'ora",
                  "Nella realtà la formula vera non si vede mai: abbiamo solo i dati e le stime. Con più dati, la stima si avvicina alla verità."],
        timer=[(180, "R3")], rumore="discussione", fase="gruppo",
        note="28-33 min. È la stessa situazione di un modello di intelligenza artificiale: impara dai dati una stima, mai la verità."))
    S.append(controllo(
        ["A che cosa serve il $ in $B$2?",
         "Con il vostro calcolatore: quante ore di sonno prevedete per 6 ore di schermo?",
         "Perché la stima non coincide con la formula vera?"],
        ["Tiene ferma la cella quando si trascina la formula", "9,92 − 0,51 · 6 ≈ 6,86 ore", "Rumore, pochi dati, arrotondamento"],
        note="33-36 min."))
    S.append(riga("stima dai dati: sonno ≈ 9,92 − 0,51 · schermo<br>verità: sonno = 9,6 − 0,45 · schermo + rumore",
        [("stima", "quello che calcoliamo dai dati"), ("verità", "quello che vorremmo sapere e che di solito non si vede"),
         ("più dati", "stima più vicina alla verità")],
        dopo="Pezzi per l'installazione, nella cartella della classe: il foglio «Lanci» con il grafico e i calcolatori.",
        note="36-40 min. Salvare il calcolatore: si usa nella giornata 4."))
    return "IA e dati 1P · Giornata 2 · Incertezza e misura", S, F
