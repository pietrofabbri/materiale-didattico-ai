from g import *

def build():
    S, F = [], []
    S.append(titolo_giornata(4, "Dai dati alle scoperte",
        "Che cosa ci dicono i nostri dati, e come impara una macchina dagli esempi?",
        [("Ora 1 · Laboratorio", "L'analisi dei nostri dati"),
         ("Ora 2 · Laboratorio", "Macchine che imparano dagli esempi"),
         ("Ora 3 · Laboratorio", "Prepariamo «Dentro la macchina»")],
        note="Preparare: prove_1p.csv e i calcolatori della giornata 2 nella cartella della classe; computer con webcam; oggetti (penna, gomma, temperino) o fogli e pennarelli per i disegni. Alla fine della giornata la classe ha preparato le stazioni dell'installazione «Dentro la macchina»."))

    # ================================================================ ORA 1
    R = [("R1", "La nostra stima", "La stima del gruppo della media dell'equilibrio; poi il valore vero.", 1),
         ("R2", "Due persone", "Media e variabilità delle due prove per due codici.", 1),
         ("R3", "Tabella pivot", "Media dei centri per mano, con il numero di persone.", 1),
         ("R4", "Previsione di r", "Segno previsto, poi valore calcolato.", 1),
         ("R5", "La nostra scoperta", "Un numero · un grafico (descritto) · un limite.", 1),
         ("R6", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((1, "L'analisi dei nostri dati", R))
    S.append(ora(1, "Laboratorio di informatica", "L'analisi dei nostri dati", "Il calcolatore al lavoro sulle nostre prove",
        "trovare una cosa vera sui nostri dati e saperla difendere."))
    S.append(obiettivi([
        "confrontare una <b>stima</b> con il valore calcolato",
        "calcolare per ogni persona <b>media</b> e <b>variabilità</b> delle due prove",
        "usare il <b>calcolatore</b> della giornata 2 su dati nuovi",
        "costruire una <b>tabella pivot</b> e un <b>grafico di dispersione</b>",
        "<b>prevedere</b> il segno di una correlazione prima di calcolarla",
        "scrivere una scoperta con <b>un numero, un grafico e un limite</b>"]))
    S.append(sorteggio("Gruppi nuovi anche oggi: sono i gruppi di tutta la giornata, anche dell'installazione.", note="Inserire gli assenti e premere Sorteggia."))
    S.append(attivita("Prima stima, poi calcola",
        ["Senza guardare i dati: quanti secondi è durata, in media, la prima prova di equilibrio della classe?",
         "Scrivete la stima del gruppo in R1",
         "Poi la calcoliamo insieme: <span class=\"mono\">=MEDIA(C2:C30)</span>"],
        "gruppo", "R1", "2 minuti", [(120, "R1")],
        esempio="«Secondo noi 35 secondi»",
        note="3-6 min. Scrivere alla lavagna le sei stime e la loro media, poi il valore vero. Spesso la media delle stime è più vicina al vero della maggior parte delle stime singole: si chiama saggezza della folla. Funziona meglio se le stime sono indipendenti."))
    S.append(spiega("Una persona, due prove", occhiello="Media e variabilità",
        codice="F2: =MEDIA(C2:D2)\nG2: =DEV.ST.POP(C2:D2)",
        punti=["F: la media delle due prove della persona", "G: quanto sono diverse le sue due prove (σ, giornata 2)"],
        testo=["Si scrivono nella riga 2 e si trascinano fino alla riga 30. Le caselle vuote non vengono contate."],
        dopo=["In R2: media e variabilità per due codici a scelta."],
        timer=[(180, "R2")], rumore="discussione", fase="gruppo",
        note="6-9 min."))
    S.append(spiega("Chi ha le prove più diverse?", occhiello="Domanda",
        formula="30 e 50 secondi &nbsp;&nbsp; oppure &nbsp;&nbsp; 39 e 41 secondi",
        testo=["Stessa media: 40 secondi."],
        risposta=["La prima: σ = 10 secondi. La seconda: σ = 1 secondo.", "La variabilità delle prove di una persona dipende dall'errore di misura e da quanto cambia la prestazione da una volta all'altra."],
        note="9-10 min."))
    S.append(attivita("Il calcolatore sui nostri dati",
        ["Copiate la colonna F (media dell'equilibrio) nella colonna A del foglio «Dati» del vostro calcolatore: Incolla speciale › Solo valori",
         "Leggete media, mediana, deviazione standard",
         "Guardate i punteggi z: c'è qualche valore oltre 3 o sotto −3? Se sì, controllate il foglio di carta"],
        "gruppo", "sul computer, calcolatore della giornata 2", "5 minuti", [(300, "Calcolatore")],
        esempio="z = 3 vuol dire: tre deviazioni standard sopra la media, molto lontano dagli altri",
        note="10-15 min. Aggiornare gli intervalli del calcolatore da A2:A41 ad A2:A30. Un valore molto lontano può essere un errore rimasto o una prova davvero eccezionale: se è vero, si tiene."))
    S.append(spiega("Confrontare gruppi: la tabella pivot", occhiello="Mano destra e mano sinistra",
        punti=["Inserisci › Tabella pivot", "Righe: <b>mano</b>", "Valori: <b>lanci_10</b>, riepilogo MEDIA; poi ancora <b>lanci_10</b>, riepilogo CONTA"], ordinati=True,
        attenzione="Se chi lancia con la sinistra sono 3 persone, la loro media dipende da 3 persone: basta una prova storta per cambiarla. Guardate sempre la colonna CONTA.",
        dopo=["In R3: le due medie e il numero di persone."],
        timer=[(240, "R3")], rumore="discussione", fase="gruppo",
        note="15-19 min."))
    S.append(spiega("Due misure insieme", occhiello="Grafico di dispersione e correlazione",
        punti=["Selezionate le colonne F (equilibrio medio) ed E (centri)", "Inserisci › Grafico › Grafico a dispersione",
               "Titolo, nome degli assi con l'unità, fonte: «prove della 1P in aula»"], ordinati=True,
        testo=["Prima di calcolare: secondo voi r sarà positivo, negativo o vicino a 0? Scrivetelo in R4. Poi: <span class=\"mono\">=CORRELAZIONE(F2:F30;E2:E30)</span>"],
        timer=[(300, "R4")], rumore="discussione", fase="gruppo",
        note="19-24 min. Il valore dipende dai dati della classe: non c'è una risposta prestabilita. Anche una correlazione forte non dice che una cosa causa l'altra."))
    S.append(spiega("Il formato di una scoperta", occhiello="Un numero, un grafico, un limite",
        esempio=["«Chi lancia con la destra fa in media 5,8 centri su 10, chi lancia con la sinistra 4,1 (tabella pivot).",
                 "Limite: chi lancia con la sinistra sono solo 4 persone, di una sola classe, in un solo giorno.»"],
        attenzione="I numeri dell'esempio sono inventati: usate i vostri.",
        note="24-25 min."))
    S.append(attivita("Scrivete la vostra scoperta",
        ["Scegliete un risultato dei vostri dati",
         "Scrivete in R5: un numero, il grafico o la tabella da cui viene, un limite",
         "Salvate grafico e frase nella cartella della classe: andranno nel cruscotto dell'installazione"],
        "gruppo", "R5", "8 minuti", [(480, "R5")],
        esempio="numero: r = 0,3 · grafico: dispersione equilibrio e centri · limite: 29 persone, due prove a testa",
        note="25-33 min."))
    S.append(controllo(
        ["Prove 30 e 50, prove 39 e 41: quali hanno la variabilità più alta?",
         "r = 0,4 tra equilibrio e centri: stare in equilibrio fa lanciare meglio?",
         "Quale limite ha una media calcolata su 3 persone?"],
        ["30 e 50 (σ = 10 contro σ = 1)", "No: la correlazione non dice quale causa l'altra; può esserci una causa comune, come l'abitudine allo sport",
         "Dipende da pochissime persone: può cambiare molto per caso"],
        note="33-36 min."))
    S.append(riga("una scoperta = un numero + un grafico + un limite",
        [("numero", "che cosa abbiamo misurato o calcolato"), ("grafico", "da dove viene il numero"), ("limite", "che cosa il numero non può dire")],
        note="36-40 min."))

    # ================================================================ ORA 2
    R = [("R1", "Esempio ed etichetta", "Nel nostro progetto: che cos'è x? che cos'è y?", 1),
         ("R2", "Le nostre classi", "Le tre classi e quanti esempi per ciascuna.", 1),
         ("R3", "Il test", "Tabella: prova · risposta giusta · risposta del modello (10 righe).", 1),
         ("R4", "Accuratezza", "Risposte giuste ÷ 10 = ___", 1),
         ("R5", "L'inganno", "L'esempio ingannevole e perché, scritto prima di provarlo.", 1),
         ("R6", "Controllo", "Le tre risposte del controllo finale.", 1)]
    foglio_ora(R); F.append((2, "Macchine che imparano dagli esempi", R))
    S.append(ora(2, "Laboratorio di informatica", "Macchine che imparano dagli esempi", "Addestrare, provare, ingannare",
        "insegnare a una macchina con gli esempi, e poi provare a ingannarla.",
        note="Provare prima che teachablemachine.withgoogle.com funzioni dalla rete della scuola. Se il collega di educazione fisica è presente può fare una dimostrazione con le pose, davanti alla webcam."))
    S.append(obiettivi([
        "dire che cosa sono l'<b>esempio</b> e l'<b>etichetta</b> in un problema",
        "<b>addestrare</b> un modello con 3 classi e almeno 20 esempi per classe",
        "preparare un <b>test</b> con 10 esempi nuovi",
        "calcolare l'<b>accuratezza</b>",
        "progettare un esempio che <b>inganna</b> il modello e spiegare perché",
        "distinguere i <b>tre modi di imparare</b> visti nel percorso"]))
    S.append(spiega("Imparare da esempi con la risposta", occhiello="Apprendimento supervisionato",
        carte=[("Esempio (x)", "quello che il modello vede: qui un'immagine dalla webcam", "#2C8BC9"),
               ("Etichetta (y)", "la risposta giusta: qui il nome della classe", "#3A8A3E"),
               ("Modello", "dopo l'addestramento, vede un esempio nuovo e dice l'etichetta", "#6B3FA0")],
        testo=["<b>Addestrare</b> vuol dire dare al modello tanti esempi con l'etichetta, perché impari. Scrivete in R1 che cosa sono x e y nel vostro progetto."],
        timer=[(60, "R1")], rumore="discussione", fase="gruppo",
        note="3-6 min. È lo stesso tipo di apprendimento del pappagallo: impara dagli esempi."))
    S.append(spiega("Come si addestra con Teachable Machine", occhiello="Passo per passo",
        punti=["teachablemachine.withgoogle.com › Get Started › Image Project › Standard image model",
               "Rinominate Class 1 e Class 2, aggiungete Class 3 (Add a class)",
               "Webcam › tenete premuto «Hold to Record»: almeno 20 esempi per classe, in posizioni diverse",
               "Train Model; poi provate nell'anteprima (Preview)"], ordinati=True,
        attenzione="Solo oggetti o disegni su carta: niente volti né corpi nell'inquadratura.",
        note="6-8 min. Dimostrazione al proiettore. L'interfaccia è in inglese: i nomi dei pulsanti sono quelli scritti nella slide."))
    S.append(attivita("Addestrate il vostro modello",
        ["Scegliete 3 classi di oggetti o di disegni e scrivetele in R2",
         "Registrate almeno 20 esempi per classe",
         "Cambiate angolo, distanza, luce",
         "Train Model"],
        "gruppo", "computer con webcam; R2", "10 minuti", [(600, "Addestrare")],
        esempio="classi: penna, gomma, temperino · 25 esempi ciascuna",
        note="8-18 min. Se l'addestramento è lento, 15 esempi per classe."))
    S.append(spiega("Addestramento e test", occhiello="Come si valuta un modello",
        carte=[("Esempi di addestramento", "quelli da cui il modello impara", "#2C8BC9"), ("Esempi di test", ["esempi nuovi, mai visti dal modello", "dicono se ha imparato o solo memorizzato"], "#DB6A1C")],
        formula="accuratezza = risposte giuste ÷ risposte totali",
        esempio="8 giuste su 10 → 8 ÷ 10 = 0,8 = 80%",
        note="18-19 min. Come una verifica: se le domande sono gli stessi esercizi già fatti, non si capisce se lo studente ha capito."))
    S.append(attivita("Il vostro test",
        ["Preparate 10 prove nuove: oggetti in posizioni diverse, disegni rifatti",
         "Scrivete in R3 la risposta giusta di ogni prova, <b>prima</b> di mostrarla",
         "Mostratele al modello e scrivete la sua risposta",
         "In R4: l'accuratezza"],
        "gruppo", "R3 e R4", "6 minuti", [(360, "Test")],
        esempio="prova 1 · gomma · il modello dice gomma (giusta)",
        note="19-25 min."))
    S.append(attivita("Batti la macchina",
        ["Progettate l'esempio più ingannevole che vi viene in mente",
         "Scrivete in R5 perché dovrebbe ingannare il modello, <b>prima</b> di provarlo",
         "Provatelo: che cosa risponde, e con quale percentuale?"],
        "gruppo", "R5", "4 minuti", [(240, "R5")],
        esempio="«la penna davanti a uno sfondo diverso: forse il modello ha imparato lo sfondo»",
        note="25-29 min. Tre punti se il modello sbaglia con più dell'80% e la spiegazione era scritta prima."))
    S.append(spiega("Perché il modello si inganna", occhiello="Esempi non rappresentativi",
        punti=["ha imparato lo <b>sfondo</b> invece dell'oggetto", "ha visto gli oggetti sempre con la stessa <b>luce</b> o lo stesso <b>angolo</b>",
               "davanti a un oggetto <b>nuovo</b> deve comunque scegliere una delle sue classi"],
        attenzione="Una percentuale alta non vuol dire «giusto»: il modello può sbagliare con il 99% di sicurezza.",
        note="29-31 min."))
    S.append(spiega("Tre modi di imparare", occhiello="Riepilogo del percorso",
        tabella=(["Modo", "Da che cosa impara", "Dove l'abbiamo visto"],
                 [["supervisionato", "esempi con la risposta giusta", "Teachable Machine"], ["per rinforzo", "tentativi e punteggi", "il bersaglio nascosto"],
                  ["non supervisionato", "esempi senza risposta: cerca da solo dei gruppi", "raggruppare oggetti simili senza sapere che cosa sono"]]),
        testo=["Un chatbot li usa tutti: prima impara a prevedere la parola successiva su moltissimi testi, poi da esempi di buone risposte e dai giudizi delle persone."],
        note="31-33 min."))
    S.append(controllo(
        ["7 risposte giuste su 10: quanto vale l'accuratezza?", "Perché il test si fa con esempi nuovi?",
         "Bersaglio nascosto e Teachable Machine: quale modo di imparare è ciascuno?"],
        ["7 ÷ 10 = 0,7 = 70%", "Per vedere se il modello ha imparato e non solo memorizzato", "Rinforzo; supervisionato"],
        note="33-36 min."))
    S.append(riga("accuratezza = risposte giuste ÷ risposte totali",
        [("risposte", "su esempi che il modello non ha mai visto"), ("addestramento", "gli esempi da cui il modello impara")],
        dopo="Salvate il modello (Export Model › Upload): servirà alla stazione «Batti la macchina».",
        note="36-40 min. Salvare il modello migliore per l'installazione."))

    # ================================================================ ORA 3
    R = [("R1", "Il titolo per il visitatore", "Il nome della stazione e un invito di una riga.", 1),
         ("R2", "Istruzioni", "Al massimo 3 passi per il visitatore.", 1),
         ("R3", "Che cosa dice la guida", "Tre frasi: che cosa succede dentro la macchina.", 1),
         ("R4", "Un numero e un limite", "Un dato della classe e che cosa non può dire.", 1),
         ("R5", "La domanda", "Una domanda da fare al visitatore alla fine.", 1),
         ("R6", "Prova incrociata", "L'osservazione del gruppo che ha provato la stazione.", 1)]
    foglio_ora(R); F.append((3, "Prepariamo «Dentro la macchina»", R))
    S.append(ora(3, "Laboratorio di informatica", "Prepariamo «Dentro la macchina»", "L'installazione in cui i visitatori diventano i dati",
        "preparare e provare le stazioni dell'installazione della classe.",
        note="Il foglio di quest'ora è la scheda della stazione. La pagina web dell'installazione (cruscotto e stazioni) la prepara il docente con i pezzi salvati dalla classe."))
    S.append(obiettivi([
        "scegliere, tra i pezzi della classe, quelli utili alla <b>propria stazione</b>",
        "scrivere <b>istruzioni</b> chiare per un visitatore",
        "spiegare in tre frasi che cosa succede <b>dentro la macchina</b>",
        "dare <b>un numero</b> della classe con il suo <b>limite</b>",
        "fare da <b>guida</b> per un minuto e rispondere a una domanda",
        "distinguere <b>stima</b> e <b>verità</b> con un esempio del percorso"]))
    S.append(spiega("«Dentro la macchina»", occhiello="Il prodotto della classe",
        testo=["Un'installazione in cui i <b>visitatori diventano i dati</b>. Su uno schermo grande un cruscotto cambia mentre i visitatori partecipano. Voi fate da guide."],
        carte=[("1 Il pappagallo", "il visitatore scrive una frase; il pappagallo impara le sue parole", "#C8372D"),
               ("2 Vero o verosimile?", "il visitatore giudica frasi della classe; quante volte viene ingannato?", "#DB6A1C"),
               ("3 La moneta", "il visitatore lancia; la frequenza di tutti i lanci si avvicina a 0,5", "#3A8A3E"),
               ("4 Batti la macchina", "il visitatore prova a ingannare il modello della classe", "#0E7C7B"),
               ("5 Le nostre prove", "il cruscotto con le scoperte della classe, ciascuna con il suo limite", "#2C8BC9"),
               ("6 Accoglienza", "accoglie, spiega le regole sui dati, guida il giro, chiude con stima e verità", "#6B3FA0")],
        note="3-6 min. Il gruppo n segue la stazione n. Si presenta ad altre classi, alle famiglie o all'open day."))
    S.append(spiega("La scheda della stazione: un esempio", occhiello="Stazione 3, la moneta",
        tabella=(["Riquadro", "Esempio"],
                 [["R1 Titolo", "«Testa o croce: vince il caso?» · Lancia e guarda che cosa fa la classe intera"],
                  ["R2 Istruzioni", "1 lancia la moneta 10 volte · 2 scrivi le teste · 3 guarda la curva sullo schermo"],
                  ["R3 La guida dice", "Ogni lancio è imprevedibile. Tanti lanci insieme no: la frequenza si avvicina a 0,5. Si chiama legge dei grandi numeri."],
                  ["R4 Numero e limite", "La 1P ha fatto 290 lanci: 52% teste. Limite: anche con 290 lanci non è esattamente 50%."],
                  ["R5 Domanda", "Dopo 5 teste di fila, la croce è più probabile?"]], True),
        dopo=["I numeri dell'esempio sono inventati: usate quelli veri della classe, che trovate nella cartella."],
        note="6-8 min."))
    S.append(attivita("Preparate la vostra stazione",
        ["Aprite la cartella della classe e cercate i pezzi della vostra stazione",
         "Compilate la scheda: R1, R2, R3, R4, R5",
         "Frasi brevi: un visitatore di 11 anni deve capire",
         "Solo dati della classe intera, nessun nome"],
        "gruppo", "R1-R5", "14 minuti", [(840, "Preparare")],
        esempio="R2: «1 scrivi una frase di 4-8 parole · 2 premi Insegna · 3 leggi la frase che inventa il pappagallo»",
        note="8-22 min. Pezzi: stazione 1 corpus e pappagallo (giornata 1); 2 frasi etichettate e ingredienti del verosimile (giornata 1); 3 lanci, albero, grafico (giornata 2); 4 modello di Teachable Machine (ora 2 di oggi); 5 scoperte, percentuale di errori di copiatura (giornate 3 e 4); 6 regole sui dati, stima e verità (tutte)."))
    S.append(attivita("Prova incrociata",
        ["Il gruppo 1 prova la stazione del gruppo 2, il 2 quella del 3, … il 6 quella dell'1",
         "Fate i visitatori: seguite le istruzioni e rispondete alla domanda",
         "Scrivete in R6 del gruppo che vi ospita un'osservazione precisa: un passo poco chiaro, un numero senza limite, una parola difficile"],
        "gruppo", "R6 della scheda dell'altro gruppo", "6 minuti", [(360, "Prova")],
        esempio="«Al passo 2 non si capisce dove scrivere le teste»",
        note="22-28 min. «Non mi piace» non vale: l'osservazione deve indicare un punto preciso."))
    S.append(attivita("La guida in un minuto",
        ["Un componente per gruppo presenta la stazione: titolo, che cosa fa il visitatore, che cosa succede dentro la macchina",
         "Un minuto a testa",
         "Il gruppo che ha fatto la prova incrociata fa una domanda: si risponde con un dato, o dicendo che cosa non sappiamo"],
        "tutti", "davanti alla classe", "6 minuti", [(60, "Gruppo 1"), (60, "Gruppo 2"), (60, "Gruppo 3"), (60, "Gruppo 4"), (60, "Gruppo 5"), (60, "Gruppo 6")], rumore="spento",
        note="28-34 min. Spazio per passare da un gruppo al successivo."))
    S.append(spiega("Stima e verità", occhiello="Il filo di tutto il percorso",
        carte=[("La 1Z", ["stima: 9,92 − 0,51 · schermo", "verità: 9,6 − 0,45 · schermo"], "#2C8BC9"),
               ("La moneta", ["dopo 4 teste: P(truccata) ≈ 0,94", "ma può essere la moneta normale"], "#DB6A1C"),
               ("Il modello", ["accuratezza sul nostro test", "non è l'accuratezza su tutti gli oggetti del mondo"], "#3A8A3E")],
        testo=["Dai dati si ottengono stime. Con più dati migliorano, ma non diventano la verità."],
        note="34-35 min."))
    S.append(spiega("Il biglietto finale", occhiello="Da soli, su un foglietto, con il codice e senza nome",
        formula="Scrivi la differenza tra stima e verità, con un esempio del percorso.",
        timer=[(180, "Biglietto")], rumore="silenzio", fase="solo",
        note="35-38 min. Risposta corretta: un esempio a scelta (1Z, moneta, equilibrio, accuratezza) con la distinzione tra ciò che si calcola dai dati e ciò che è vero ma non si osserva direttamente."))
    S.append(spiega("Che cosa abbiamo costruito", occhiello="Quattro giornate",
        tabella=(["Giornata", "Pezzo per l'installazione"],
                 [["1 La lingua come dati", "il corpus della classe e il pappagallo"], ["2 Incertezza e misura", "i lanci, la moneta, il calcolatore"],
                  ["3 Il corpo come fonte di dati", "le prove in aula, pulite e con l'errore misurato"], ["4 Dai dati alle scoperte", "le scoperte, il modello, le stazioni"]]),
        dopo=["Prossimo passo: la presentazione di «Dentro la macchina»."],
        note="38-40 min. Raccogliere le schede delle stazioni e i biglietti."))
    return "IA e dati 1P · Giornata 4 · Dai dati alle scoperte", S, F
