"""Generatore v2: scrive direttamente le slide di un deck del tipo Slides di Claude.

Ogni slide è una <section> per la tela di 1920×1080 px. Le impostazioni per il motore HTML
(barattolo, fase, timer, sorteggio, importanza) vanno nella prima riga delle note:
  IMPOSTAZIONI: importanza=essenziale | rumore=discussione | fase=gruppo | timer=300 Contare; 180 R2
Importanza: essenziale (non saltare), consigliata, facoltativa (si può saltare se manca tempo).
Il deck si converte nell'HTML finale con da_artefatto.py (chiamato da unico.py).
"""
import html as _h

def T(s):
    return s.replace("'", "’")

STATO = {"foglio": [], "giornata": 0, "ora": 0, "n": 0}
IMP = {"e": "essenziale", "c": "consigliata", "f": "facoltativa"}

def foglio_ora(riquadri):
    STATO["foglio"] = riquadri

# ------------------------------------------------------------------ blocchi
def P(t, cls=None):
    c = f' class="{cls}"' if cls else ""
    return f"<p{c}>{T(t)}</p>"

def Lista(items, ordinata=False, frammento=False):
    tag = "ol" if ordinata else "ul"
    f = ' class="fragment"' if frammento else ""
    return f"<{tag}{f}>" + "".join(f"<li>{T(i)}</li>" for i in items) + f"</{tag}>"

def Box(tipo, etichetta, contenuto, frammento=False):
    if isinstance(contenuto, str):
        contenuto = [contenuto]
    corpo = "".join(c if c.startswith(("<p", "<ul", "<ol", "<table", "<div")) else P(c) for c in contenuto)
    fr = " fragment" if frammento else ""
    return f'<div class="box {tipo}{fr}"><p class="etichetta">{T(etichetta)}</p>{corpo}</div>'

def Esempio(c, fr=False): return Box("esempio", "Esempio", c, fr)
def Ricorda(c, fr=False): return Box("ricorda", "Ricorda", c, fr)
def Attenzione(c, fr=False): return Box("attenzione", "Attenzione", c, fr)
def Risposta(c, fr=True): return Box("risposta", "Risposta", c, fr)

def Formula(t, piccola=False):
    return f'<p class="formula{" piccola" if piccola else ""}">{T(t)}</p>'

def Codice(t):
    return '<p class="codice">' + _h.escape(t, quote=False).replace("\n", "<br>") + "</p>"

def Tabella(testa, righe, compatta=False):
    th = "".join(f"<th>{T(x)}</th>" for x in testa)
    tr = "".join("<tr>" + "".join(f"<td>{T(str(c))}</td>" for c in r) + "</tr>" for r in righe)
    return f'<table class="t{" compatta" if compatta else ""}"><tr>{th}</tr>{tr}</table>'

COLORI_CARTA = {"indaco": "#3B4BA0", "corallo": "#E0603C", "ambra": "#E8A21C", "salvia": "#4F9A73", "cielo": "#3E8EC4", "prugna": "#7A4E9C"}

def Carte(carte, frammento=False):
    out = []
    for c in carte:
        tit, testo = c[0], c[1]
        col = COLORI_CARTA.get(c[2], c[2]) if len(c) > 2 else None
        st = f' style="border-top-color:{col}"' if col else ""
        corpo = "".join(P(x) for x in (testo if isinstance(testo, list) else [testo]))
        out.append(f'<div class="carta"{st}><p class="tit">{T(tit)}</p>{corpo}</div>')
    return f'<div class="carte{" fragment" if frammento else ""}">' + "".join(out) + "</div>"

def Tasselli(parole, colori=None, frammento=False):
    """Parole come tasselli; le parole uguali hanno lo stesso colore (colori: parola -> nome colore)."""
    colori = colori or {}
    out = []
    for k, w in enumerate(parole):
        col = colori.get(w)
        cls = f"tassello t-{col}" if col else "tassello"
        out.append(f'<p class="{cls}">{T(w)}</p>')
    return f'<div class="tasselli{" fragment" if frammento else ""}">' + "".join(out) + "</div>"

def Catena(parole, frammento=False):
    """Parole collegate da frecce: la catena delle coppie."""
    out = []
    for k, w in enumerate(parole):
        if k:
            out.append('<p class="freccia">→</p>')
        out.append(f'<p class="tassello">{T(w)}</p>')
    return f'<div class="tasselli catena{" fragment" if frammento else ""}">' + "".join(out) + "</div>"

def Barre(voci, frammento=False):
    """voci: (etichetta, valore 0-1, testo del valore)."""
    righe = "".join(
        f'<div class="barra"><p class="b-et">{T(et)}</p><div class="b-fondo"><div class="b-riemp" style="width:{round(v * 100)}%"></div></div><p class="b-val">{T(tx)}</p></div>'
        for et, v, tx in voci)
    return f'<div class="barre{" fragment" if frammento else ""}">' + righe + "</div>"

def Colonne(*blocchi):
    return '<div class="cols">' + "".join(f"<div>{b}</div>" for b in blocchi) + "</div>"

def Mappa(qui):
    r = STATO["foglio"]
    celle = [f'<div class="testa"><p>Foglio dell’ora · Giornata {STATO["giornata"]} · Ora {STATO["ora"]}</p></div>']
    for cod, tit, _i, span in r:
        cls = "r qui" if cod == qui else "r"
        celle.append(f'<div class="{cls}" style="grid-column:span {span}"><p><b>{cod}</b> {T(tit)}</p></div>')
    return '<div class="foglio">' + "".join(celle) + "</div>"

# ------------------------------------------------------------------ slide
def _imp(attr):
    p = []
    for k in ("importanza", "rumore", "fase", "timer", "logica"):
        v = attr.get(k)
        if v:
            p.append(f"{k}={v}")
    return "IMPOSTAZIONI: " + " | ".join(p)

def _slide(corpo, imp="e", note="", rumore=None, fase=None, timer=None, logica=None, cls=""):
    STATO["n"] += 1
    ident = f"g{STATO['giornata']}-{STATO['n']:03d}"
    attr = {"importanza": IMP[imp], "rumore": rumore if rumore and rumore != "spento" else None, "fase": fase,
            "timer": "; ".join(f"{s} {n}".strip() for s, n in timer) if timer else None, "logica": logica}
    classi = " ".join(x for x in [cls, "imp-" + imp] if x)
    piede = f"IA e dati · 1P · Giornata {STATO['giornata']}" + (f" · Ora {STATO['ora']}" if STATO["ora"] else "")
    testo_nota = _imp(attr) + ("\n" + T(note) if note else "")
    return (ident, f'<section id="{ident}" class="{classi}">\n{corpo}\n<div class="striscia"></div>\n'
            f'<p class="foot">{piede}</p>\n<aside>{_h.escape(testo_nota, quote=False)}</aside>\n</section>\n')

def _testa(titolo, occhiello=""):
    o = f'<p class="occhiello">{T(occhiello)}</p>' if occhiello else ""
    return o + f"<h2>{T(titolo)}</h2>" + '<div class="linea"></div>'

def copertina(n, titolo, domanda, ore, note=""):
    STATO.update(giornata=n, ora=0, n=0)
    carte = Carte([(o, d, c) for (o, d), c in zip(ore, ["indaco", "corallo", "salvia"])])
    corpo = (f'<p class="occhiello">Percorso «Intelligenza artificiale e dati» · Classe 1P · Giornata {n}</p>'
             f"<h1>{T(titolo)}</h1>" + P(domanda, "grande") + '<div class="spazio"></div>' + carte)
    return _slide(corpo, "e", note, cls="copertina")

def ora(h, disciplina, titolo, sotto, missione, note=""):
    STATO["ora"] = h
    corpo = (f'<p class="occhiello">Giornata {STATO["giornata"]} · Ora {h} di 3 · {T(disciplina)} · 40 minuti</p>'
             f"<h1>{T(titolo)}</h1>" + P(sotto, "grande") + '<div class="spazio"></div>'
             + Box("missione", "Missione dell'ora", missione))
    return _slide(corpo, "e", note, cls="scena")

def obiettivi(items, note=""):
    corpo = _testa("Alla fine di quest'ora sai…", "Obiettivi") + Lista(items, True) + P(
        "Alla fine, tre domande controllano questi obiettivi.", "piccolo")
    return _slide(corpo, "e", note)

def sorteggio(testo, note=""):
    corpo = (_testa("Formiamo i gruppi", "Oggi lavoriamo in gruppi nuovi") + P(testo)
             + '<div class="segnaposto"><p>Qui compare il sorteggio dei gruppi: si scrivono gli assenti (numeri del registro) e si preme «Sorteggia».</p></div>')
    return _slide(corpo, "e", note, fase="tutti", logica="sorteggio")

def slide(titolo, *blocchi, occhiello="", imp="e", note="", rumore=None, fase=None, timer=None):
    return _slide(_testa(titolo, occhiello) + "".join(blocchi), imp, note, rumore, fase, timer)

CHI = {"solo": "Da soli", "coppia": "In coppia", "gruppo": "Nel gruppo", "tutti": "Tutti insieme"}

def attivita(titolo, consegna, chi, dove, tempo, timer, esempio=None, imp="e", note="", rumore=None, materiale=None):
    fase = "gruppo" if chi in ("gruppo", "coppia") else ("solo" if chi == "solo" else "tutti")
    if rumore is None:
        rumore = "discussione" if chi in ("gruppo", "coppia") else "silenzio"
    det = [("Con chi", CHI.get(chi, chi))]
    mini = ""
    if dove.startswith("R"):
        cod = dove.split()[0]
        tit = next((t for k, t, _i, _s in STATO["foglio"] if k == cod), "")
        det.append(("Dove", f"riquadro <b>{cod}</b>: {tit}"))
        mini = Mappa(cod)
    else:
        det.append(("Dove", dove))
    det.append(("Tempo", tempo))
    if materiale:
        det.append(("Materiale", materiale))
    dett = "".join(f'<div class="det"><p class="k">{T(k)}</p><p>{T(v)}</p></div>' for k, v in det)
    sinistra = "<div>" + Lista(consegna, True) + (Esempio(esempio) if esempio else "") + "</div>"
    corpo = _testa(titolo, "Attività") + f'<div class="attivita">{sinistra}<div class="dettagli">{dett}{mini}</div></div>'
    return _slide(corpo, imp, note, rumore, fase, timer)

def controllo(domande, risposte, note=""):
    cod = STATO["foglio"][-1][0] if STATO["foglio"] else ""
    corpo = (_testa("Tre domande", "Controllo degli obiettivi · 3 minuti")
             + P(f"Da soli, nel riquadro <b>{cod}</b>. Poi si confronta nel gruppo.", "piccolo")
             + Colonne(Lista(domande, True), Box("risposta", "Risposte", [Lista(risposte, True)], True)))
    return _slide(corpo, "e", note, "silenzio", "solo", [(180, "Da soli")])

def riga(formula, legenda, dopo="", note=""):
    leg = "".join(f'<p class="s">{T(s)}</p><p>{T(v)}</p>' for s, v in legenda)
    corpo = (_testa("Da copiare nel formulario", "Formulario della classe") + Formula(formula)
             + (f'<div class="legenda">{leg}</div>' if leg else "") + (P(dopo, "piccolo") if dopo else ""))
    return _slide(corpo, "c", note)
