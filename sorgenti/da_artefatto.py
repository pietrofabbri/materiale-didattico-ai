"""Da un deck del tipo Slides di Claude alle slide HTML del motore (timer, barattolo, note, sorteggio).

Il deck va scaricato in artefatti/gN/project/ (deck.json, deck.css, slides/*.html).
Ogni slide del deck viene disegnata sulla sua tela di 1920×1080 px, scalata per riempire lo schermo.
La prima riga delle note della slide contiene le impostazioni per il motore:
  IMPOSTAZIONI: rumore=discussione | fase=gruppo | timer=300 Contare; 180 R2 | logica=sorteggio
Le altre righe diventano le note del docente (tasto N).
Funzioni usate da unico.py: sezioni(n) -> lista di <section class="slide">, css(n) -> CSS del deck.
"""
import html, json, os, re

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.join(os.path.dirname(QUI), "artefatti")

def cartella(n):
    return os.path.join(RADICE, f"g{n}", "project")

def disponibile(n):
    return os.path.exists(os.path.join(cartella(n), "deck.json"))

def leggi_impostazioni(nota):
    righe = nota.strip().split("\n")
    attr, resto = {}, righe
    if righe and righe[0].strip().upper().startswith("IMPOSTAZIONI"):
        resto = righe[1:]
        testo = righe[0].split(":", 1)[1] if ":" in righe[0] else ""
        for parte in testo.split("|"):
            if "=" not in parte:
                continue
            k, v = [x.strip() for x in parte.split("=", 1)]
            attr[k.lower()] = v
    return attr, "\n".join(resto).strip()

def timer_attr(v):
    sec, nomi = [], []
    for pezzo in v.split(";"):
        pezzo = pezzo.strip()
        m = re.match(r"(\d+)\s*(.*)", pezzo)
        if m:
            sec.append(m.group(1)); nomi.append(m.group(2).strip())
    return ",".join(sec), "|".join(nomi)

def css(n):
    """CSS del deck riscritto per la tela: 'section' diventa '.tela'."""
    c = open(os.path.join(cartella(n), "deck.css")).read()
    c = re.sub(r"/\*.*?\*/", "", c, flags=re.S)
    kf = re.findall(r"@keyframes[^{]*\{(?:[^{}]*\{[^{}]*\})*\s*\}", c)
    for x in kf:
        c = c.replace(x, "")
    out = list(kf)
    for sel, corpo in re.findall(r"([^{}]+)\{([^{}]*)\}", c):
        nuovi = []
        for x in sel.split(","):
            x = x.strip()
            if not x:
                continue
            prima = x.split()[0]
            if prima.startswith(".") and prima.split(":")[0].split(".")[1] in ("scena", "centro", "copertina", "imp-e", "imp-c", "imp-f"):
                nuovi.append(".tela" + x)
                continue
            if x == ":root" or x == "section":
                nuovi.append(".tela")
            elif x.startswith("section"):
                nuovi.append(".tela" + x[len("section"):])
            else:
                nuovi.append(".tela " + x)
        out.append(",".join(nuovi) + "{" + corpo + "}")
    return "\n".join(out)

def sezioni(n):
    d = json.load(open(os.path.join(cartella(n), "deck.json")))
    out = []
    for k, ident in enumerate(d["order"]):
        p = os.path.join(cartella(n), "slides", ident + ".html")
        if not os.path.exists(p):
            continue
        s = open(p).read().strip()
        m = re.match(r"<section([^>]*)>", s)
        aperture = m.group(1)
        if 'hidden' in re.sub(r'"[^"]*"', "", aperture):
            continue                                      # slide nascosta nell'editor
        classi = re.search(r'class="([^"]*)"', aperture)
        classi = classi.group(1) if classi else ""
        stile = re.search(r'style="([^"]*)"', aperture)
        corpo = s[m.end():].rsplit("</section>", 1)[0]
        nota = ""
        a = re.search(r"<aside[^>]*>(.*?)</aside>", corpo, re.S)
        if a:
            nota = html.unescape(re.sub(r"<[^>]+>", "", a.group(1)))
            corpo = corpo[:a.start()] + corpo[a.end():]
        attr, nota = leggi_impostazioni(nota)
        corpo = re.sub(r'\bfragment\b', "passo", corpo)
        if attr.get("logica") == "sorteggio":
            corpo = re.sub(r'<div class="segnaposto">.*?</div>', '<div class="sorteggio sorteggio-tela"></div>', corpo, count=1, flags=re.S)
        a_html = [f'class="slide"', f'data-rumore="{attr.get("rumore", "spento")}"']
        if attr.get("fase"):
            a_html.append(f'data-fase="{attr["fase"]}"')
        if attr.get("timer"):
            sec, nomi = timer_attr(attr["timer"])
            a_html.append(f'data-timer="{sec}"'); a_html.append(f'data-timer-nomi="{html.escape(nomi)}"')
        if attr.get("logica"):
            a_html.append(f'data-logica="{attr["logica"]}"')
        a_html.append(f'data-importanza="{attr.get("importanza", "essenziale")}"')
        if k == 0:
            a_html.append('data-inizio-ora="Apertura"')
        elif "scena" in classi.split():
            mo = re.search(r"Ora (\d+) di", corpo)
            a_html.append(f'data-inizio-ora="Ora {mo.group(1) if mo else ""}"')
        idsez = f' id="giornata-{n}"' if k == 0 else ""
        st = f' style="{stile.group(1)}"' if stile else ""
        nota_html = f'<aside class="note">{html.escape(nota).replace(chr(10), "<br>")}</aside>' if nota else ""
        out.append(f'<section{idsez} {" ".join(a_html)}><div class="tela {classi}"{st}>{corpo}</div>{nota_html}</section>\n')
    return out

CSS_TELA = """
/* slide prese da un deck: tela di 1920×1080 scalata */
section.slide:has(> .tela){padding:0 150px 0 0;align-items:center;justify-content:center;background:#E9ECF1}
section.slide:has(> .tela.scena){background:#0D1322}
.tela{position:relative;width:1920px;height:1080px;flex:none;transform-origin:center center;transform:scale(var(--scala,0.5));overflow:hidden}
.tela .passo{opacity:0;transition:opacity .35s ease;animation:none}
.tela .passo.visto{opacity:1;animation:sali .45s ease both}
.tela .striscia{display:none}
.tela p,.tela ol,.tela ul,.tela h2,.tela h1{max-width:none}
.tela .box,.tela .formula,.tela .legenda,.tela .codice,.tela table.t{max-width:none}
.tela table.t{border-collapse:collapse;background:#fff}
.tela table.t th,.tela table.t td{padding:10px 18px;border-bottom:1px solid #D5DAE2;text-align:left}
.tela table.t th{background:#E7EAF0}
.tela .carta{min-width:0;box-shadow:none}
.tela .foglio{aspect-ratio:auto}
.tela .foglio .r{font-size:24px}
.sorteggio-tela .sort-comandi label,.sorteggio-tela .sort-comandi input,.sorteggio-tela .bottone{font-size:28px}
.sorteggio-tela .gtit{font-size:30px}.sorteggio-tela .gnum{font-size:44px}
"""

JS_TELA = """<script>(function(){function s(){var k=Math.min((innerWidth-150)/1920,innerHeight/1080);document.documentElement.style.setProperty('--scala',k)}addEventListener('resize',s);s()})();</script>"""
