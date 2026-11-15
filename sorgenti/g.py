"""Generatore delle slide HTML del percorso «IA e dati» 1P.

Uso:  python3 genera.py            (scrive ../giornata-N.html e ../fogli-giornata-N.html)
Ogni giornata è un modulo giornataN.py che costruisce la lista GIORNATA con le funzioni qui sotto.
Regole di contenuto: file ia-1p-17-obiettivi-operativi.md del progetto Scuola.
"""
import html as _h

def T(s):
    """Testo dei contenuti: apostrofo tipografico (gli attributi HTML usano solo doppi apici)."""
    return s.replace("'", "’")

# ------------------------------------------------------------------ stato dell'ora corrente
STATO = {"foglio": [], "giornata": 0, "ora": 0, "disciplina": ""}

def foglio_ora(riquadri):
    """riquadri: lista di (codice, titolo, istruzione per il foglio stampato, colonne occupate 1-3)."""
    STATO["foglio"] = riquadri

def mappa(qui):
    """Miniatura del foglio dell'ora con il riquadro `qui` evidenziato."""
    r = STATO["foglio"]
    if not r:
        return ""
    celle = [f'<div class="testa">Giornata {STATO["giornata"]} · Ora {STATO["ora"]} · Gruppo n. ___</div>']
    for cod, tit, _istr, span in r:
        cls = "r qui" if cod == qui else "r"
        celle.append(f'<div class="{cls}" style="grid-column:span {span}"><b>{cod}</b> {T(tit)}</div>')
    return '<div class="foglio" style="grid-template-columns:repeat(3,1fr)">' + "".join(celle) + "</div>"

# ------------------------------------------------------------------ pezzi comuni
def _p(x, cls=None):
    c = f' class="{cls}"' if cls else ""
    return f"<p{c}>{T(x)}</p>"

def _lista(items, ordinata=False, cls=None):
    tag = "ol" if ordinata else "ul"
    c = f' class="{cls}"' if cls else ""
    return f"<{tag}{c}>" + "".join(f"<li>{T(i)}</li>" for i in items) + f"</{tag}>"

def _box(tipo, etichetta, contenuto, passo=False):
    extra = " passo" if passo else ""
    if isinstance(contenuto, str):
        contenuto = [contenuto]
    corpo = "".join(c if c.startswith("<") else _p(c) for c in contenuto)
    return f'<div class="box {tipo}{extra}"><div class="etichetta">{T(etichetta)}</div>{corpo}</div>'

def _tabella(testa, righe, compatta=False):
    th = "".join(f"<th>{T(x)}</th>" for x in testa)
    tr = "".join("<tr>" + "".join(f"<td>{T(str(c))}</td>" for c in r) + "</tr>" for r in righe)
    return f'<table class="t{" compatta" if compatta else ""}"><tr>{th}</tr>{tr}</table>'

def _carte(carte, passo=False):
    out = []
    for c in carte:
        tit, testo = c[0], c[1]
        col = c[2] if len(c) > 2 else None
        st = f' style="--c:{col}"' if col else ""
        corpo = "".join(_p(x) for x in (testo if isinstance(testo, list) else [testo]))
        out.append(f'<div class="carta"{st}><div class="tit">{T(tit)}</div>{corpo}</div>')
    return f'<div class="carte{" passo" if passo else ""}">' + "".join(out) + "</div>"

def _sezione(corpo, note="", rumore="spento", fase=None, timer=None, cls=None, logica=None):
    a = [f'class="slide{" " + cls if cls else ""}"', f'data-rumore="{rumore}"']
    if fase:
        a.append(f'data-fase="{fase}"')
    if timer:
        a.append('data-timer="' + ",".join(str(s) for s, _ in timer) + '"')
        a.append('data-timer-nomi="' + "|".join(T(n) for _, n in timer) + '"')
    if logica:
        a.append(f'data-logica="{logica}"')
    n = f'<aside class="note">{T(_h.escape(note, quote=False))}</aside>' if note else ""
    return f"<section {' '.join(a)}>\n{corpo}\n{n}\n</section>\n"

def _occ(x):
    return f'<div class="occhiello">{T(x)}</div>'

# ------------------------------------------------------------------ tipi di slide
def titolo_giornata(n, titolo, domanda, ore, note=""):
    STATO["giornata"] = n
    carte = _carte([(o, d) for o, d in ore])
    corpo = (_occ(f"Percorso «Intelligenza artificiale e dati» · Classe 1P · Giornata {n}")
             + f"<h1>{T(titolo)}</h1>" + _p(domanda, "grande") + '<div class="spazio"></div>' + carte)
    return _sezione(corpo, note, cls="")

def ora(h, disciplina, titolo, sotto, missione, note=""):
    STATO["ora"] = h
    STATO["disciplina"] = disciplina
    corpo = (_occ(f"Giornata {STATO['giornata']} · Ora {h} di 3 · {disciplina} · 40 minuti")
             + f"<h1>{T(titolo)}</h1>" + _p(sotto, "grande") + '<div class="spazio"></div>'
             + _box("risposta", "Missione dell'ora", missione))
    return _sezione(corpo, note, cls="scena")

def obiettivi(items, note=""):
    corpo = _occ("Obiettivi dell'ora") + "<h2>Alla fine di quest'ora sai…</h2>" + _lista(items, True, "obj") + _p(
        "Alla fine dell'ora tre domande controllano questi obiettivi.", "piccolo")
    return _sezione(corpo, note)

def sorteggio(testo, note=""):
    corpo = (_occ("Oggi lavoriamo in gruppi nuovi") + "<h2>Formiamo i gruppi</h2>" + _p(testo)
             + '<div class="sorteggio"></div>')
    return _sezione(corpo, note, logica="sorteggio", fase="tutti")

def spiega(titolo, occhiello="", testo=(), punti=(), ordinati=False, esempio=None, attenzione=None,
           risposta=None, formula=None, codice=None, tabella=None, carte=None, dopo=(), note="",
           rumore="spento", fase=None, timer=None, passo_risposta=True, colonne=None):
    c = []
    if occhiello:
        c.append(_occ(occhiello))
    c.append(f"<h2>{T(titolo)}</h2>")
    for t in testo:
        c.append(_p(t))
    if punti:
        c.append(_lista(punti, ordinati))
    if formula:
        c.append(f'<div class="formula">{T(formula)}</div>')
    if codice:
        c.append(f'<div class="codice">{_h.escape(codice, quote=False)}</div>')
    if tabella:
        c.append(_tabella(*tabella))
    if carte:
        c.append(_carte(carte))
    if colonne:
        c.append('<div class="cols">' + "".join(f"<div>{x}</div>" for x in colonne) + "</div>")
    if esempio:
        c.append(_box("esempio", "Esempio", esempio))
    if attenzione:
        c.append(_box("attenzione", "Attenzione", attenzione))
    if risposta:
        c.append(_box("risposta", "Risposta", risposta, passo=passo_risposta))
    for t in dopo:
        c.append(_p(t, "piccolo"))
    return _sezione("\n".join(c), note, rumore, fase, timer)

CHI = {"solo": "Da soli", "coppia": "In coppia", "gruppo": "Nel gruppo", "tutti": "Tutti insieme"}

def attivita(titolo, consegna, chi, dove, tempo, timer, esempio=None, materiale=None, note="", rumore=None,
             occhiello="Attività"):
    """Slide di attività: che cosa, con chi, dove si scrive (mappa del foglio), quanto tempo, esempio."""
    fase = "gruppo" if chi in ("gruppo", "coppia") else ("solo" if chi == "solo" else "tutti")
    if rumore is None:
        rumore = "discussione" if chi in ("gruppo", "coppia") else "silenzio"
    det = [("Con chi", CHI.get(chi, chi)), ("Tempo", tempo)]
    if materiale:
        det.append(("Materiale", materiale))
    if dove and dove.startswith("R"):
        cod = dove.split()[0]
        tit = next((t for k, t, _i, _s in STATO["foglio"] if k == cod), "")
        det.insert(1, ("Dove", f"foglio dell'ora, riquadro <b>{cod}</b> ({tit})" + (dove[len(cod):] or "")))
        mini = mappa(cod)
    else:
        det.insert(1, ("Dove", dove))
        mini = ""
    dett = "".join(f'<div class="det"><span class="k">{T(k)}</span>{_p(v)}</div>' for k, v in det)
    destra = f'<div class="dettagli">{dett}{mini}</div>'
    sinistra = "<div>" + _lista(consegna, True) + (_box("esempio", "Esempio", esempio) if esempio else "") + "</div>"
    corpo = _occ(occhiello) + f"<h2>{T(titolo)}</h2>" + f'<div class="attivita">{sinistra}{destra}</div>'
    return _sezione(corpo, note, rumore, fase, timer)

def controllo(domande, risposte, note=""):
    cod = STATO["foglio"][-1][0] if STATO["foglio"] else ""
    c = (_occ("Controllo degli obiettivi · 3 minuti") + "<h2>Tre domande</h2>"
         + _p(f"Da soli, nel riquadro <b>{cod}</b> del foglio. Poi si confronta nel gruppo.", "piccolo")
         + '<div class="cols">' + "<div>" + _lista(domande, True) + "</div><div>" + _box("risposta", "Risposte", [_lista(risposte, True)], passo=True) + "</div></div>")
    return _sezione(c, note, "silenzio", "solo", [(180, "Da soli")])

def riga(formula, legenda, dopo="", note=""):
    leg = "".join(f'<div class="s">{T(s)}</div>{_p(v)}' for s, v in legenda)
    c = (_occ("Per il formulario della classe") + "<h2>Da copiare nel formulario</h2>"
         + f'<div class="formula">{T(formula)}</div>' + (f'<div class="legenda">{leg}</div>' if leg else "")
         + (_p(dopo, "piccolo") if dopo else ""))
    return _sezione(c, note)

def immagini(titolo, imgs, occhiello="", testo=(), note="", timer=None, fase=None, rumore="spento"):
    figs = "".join(f'<figure><img src="{src}" alt="{T(alt)}"><figcaption>{T(cap)}</figcaption></figure>' for src, alt, cap in imgs)
    c = (_occ(occhiello) if occhiello else "") + f"<h2>{T(titolo)}</h2>" + "".join(_p(t) for t in testo) + f'<div class="imgs">{figs}</div>'
    return _sezione(c, note, rumore, fase, timer)

# ------------------------------------------------------------------ pagina completa
TESTA = """<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titolo}</title>
<link rel="stylesheet" href="comune/palette.css"><link rel="stylesheet" href="comune/stile.css">
</head><body>
"""
CODA = """<script src="comune/barattolo.js"></script>
<script src="comune/motore.js"></script>
<script>Motore.avvia();</script>
</body></html>
"""

def pagina(titolo, sezioni):
    return TESTA.format(titolo=T(titolo)) + "".join(sezioni) + CODA

# ------------------------------------------------------------------ fogli stampabili
FOGLI_TESTA = """<!doctype html><html lang="it"><head><meta charset="utf-8"><title>{titolo}</title>
<link rel="stylesheet" href="comune/palette.css">
<style>
@font-face{{font-family:"Atkinson Hyperlegible";src:url("comune/fonts/AtkinsonHyperlegible-Regular.ttf");font-weight:400}}
@font-face{{font-family:"Atkinson Hyperlegible";src:url("comune/fonts/AtkinsonHyperlegible-Bold.ttf");font-weight:700}}
@page{{size:A3 landscape;margin:10mm}}
body{{font-family:var(--p16-font);color:#1B2130;margin:0}}
.pag{{width:400mm;height:277mm;box-sizing:border-box;display:flex;flex-direction:column;gap:4mm;page-break-after:always;padding:2mm}}
.testa{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1.5pt solid #1B2130;padding-bottom:2mm}}
.testa h1{{font-size:20pt;margin:0}} .testa .g{{font-size:14pt}}
.griglia{{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;grid-auto-rows:1fr}}
.r{{border:1.2pt solid #1B2130;border-radius:3mm;padding:3mm 4mm;display:flex;flex-direction:column;gap:1mm}}
.r .c{{font-size:16pt;font-weight:700}} .r .i{{font-size:10.5pt;color:#5B6475;line-height:1.3}}
.nota{{font-size:10pt;color:#5B6475}}
@media screen{{body{{background:#ddd}} .pag{{background:#fff;margin:10mm auto;box-shadow:0 2px 10px rgba(0,0,0,.2)}}}}
</style></head><body>
"""

def pagina_foglio(g, h, titolo_ora, riquadri):
    celle = "".join(
        f'<div class="r" style="grid-column:span {span}"><div class="c">{cod} · {T(tit)}</div><div class="i">{T(istr)}</div></div>'
        for cod, tit, istr, span in riquadri)
    return (f'<div class="pag"><div class="testa"><h1>Giornata {g} · Ora {h} · {T(titolo_ora)}</h1>'
            f'<div class="g">Gruppo n. ______ &nbsp;&nbsp; Data ____________ &nbsp;&nbsp; (niente nomi)</div></div>'
            f'<div class="griglia">{celle}</div>'
            f'<div class="nota">Percorso «IA e dati» · 1P · Si scrive solo nei riquadri indicati dalle slide. Il foglio si consegna a fine ora.</div></div>')
