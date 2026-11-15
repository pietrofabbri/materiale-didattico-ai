"""Dalle slide del generatore (g.py + giornataN.py) a un deck del tipo Slides di Claude.

Uso: python3 artefatto.py 1   -> scrive ../../artefatti/g1/project/{deck.json,deck.css,slides/*.html}

Le impostazioni che il deck non sa rappresentare (barattolo, fase, timer, sorteggio) vanno nella
PRIMA RIGA delle note della slide, in questa forma (si può modificare a mano nell'editor):
  IMPOSTAZIONI: rumore=discussione | fase=gruppo | timer=300 Contare; 180 R2 | logica=sorteggio
Il convertitore inverso (da_artefatto.py) legge quella riga e ricostruisce la slide HTML.
"""
import datetime, html, importlib, json, os, re, sys

QUI = os.path.dirname(os.path.abspath(__file__))
FONT = "https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap"

CSS = r"""
:root{--carta:#F5F6F8;--bianco:#FFFFFF;--inchiostro:#1B2130;--grigio:#5B6475;--linea:#D5DAE2;--notte:#0D1322;
--rosso:#C8372D;--arancio:#DB6A1C;--verde:#3A8A3E;--petrolio:#0E7C7B;--azzurro:#2C8BC9;--blu:#2E4A9B;--viola:#6B3FA0;--giallo:#FFF4D6}
section{background:var(--carta);color:var(--inchiostro);font-family:'Atkinson Hyperlegible',Arial,sans-serif;padding:88px 128px 150px 112px;box-sizing:border-box;display:flex;flex-direction:column;gap:26px}
section.scena{background:var(--notte);color:var(--carta)}
section.centro{justify-content:center}
h1{font-size:88px;line-height:1.05;font-weight:700;margin:0}
h2{font-size:60px;line-height:1.1;font-weight:700;margin:0;padding-right:260px}
p{font-size:36px;line-height:1.35;margin:0}
li{font-size:36px;line-height:1.35}
ol,ul{margin:0;padding-left:56px;display:flex;flex-direction:column;gap:10px}
.occhiello{font-size:24px;letter-spacing:3px;text-transform:uppercase;color:var(--grigio);font-weight:700}
.scena .occhiello{color:#9AA3B2}
.scena p{color:#C9CFDA}
.grande{font-size:50px;line-height:1.3;font-weight:700}
.piccolo{font-size:28px;color:var(--grigio);line-height:1.4}
.spazio{flex:1}
.acc{color:var(--blu)}
.box{background:var(--bianco);border-left:10px solid var(--azzurro);border-radius:8px;padding:22px 36px;display:flex;flex-direction:column;gap:10px}
.box.esempio{border-left-color:var(--verde)}
.box.attenzione{border-left-color:var(--arancio)}
.box.risposta{border-left-color:var(--blu)}
.scena .box{background:#1C2538}
.scena .box p{color:var(--carta)}
.etichetta{font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:var(--grigio)}
.cols{display:flex;flex-direction:row;gap:48px;align-items:flex-start}
.cols>div{flex:1}
.carte{display:flex;flex-direction:row;flex-wrap:wrap;gap:24px}
.carta{flex:1 1 30%;background:var(--bianco);border-radius:10px;padding:22px 28px;border-top:8px solid var(--azzurro);display:flex;flex-direction:column;gap:8px}
.carta .tit{font-size:36px;font-weight:700}
.carta p{font-size:32px}
.scena .carta{background:#1C2538}
.scena .carta .tit{color:var(--carta)}
.formula{font-size:56px;font-weight:700;line-height:1.35;background:var(--bianco);border:3px solid var(--linea);border-radius:12px;padding:24px 40px}
.legenda{display:grid;grid-template-columns:260px 1fr;gap:8px 28px}
.legenda .s{font-size:38px;font-weight:700}
.codice{font-family:'Courier New',monospace;font-size:34px;line-height:1.5;background:var(--bianco);border:2px solid var(--linea);border-radius:8px;padding:18px 28px}
table.t{font-size:34px;color:var(--inchiostro)}
table.t.compatta{font-size:28px}
.attivita{display:grid;grid-template-columns:1.25fr 1fr;gap:48px;align-items:start}
.dettagli{display:flex;flex-direction:column;gap:14px}
.det{display:grid;grid-template-columns:170px 1fr;gap:16px;align-items:baseline}
.det .k{font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:var(--grigio)}
.det p{font-size:32px}
.foglio{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;background:var(--bianco);border:3px solid var(--inchiostro);border-radius:8px;padding:10px;width:560px}
.foglio .r{border:2px solid var(--linea);border-radius:6px;padding:6px 8px;color:var(--grigio)}
.foglio .r p{font-size:24px;line-height:1.15}
.foglio .r.qui{background:var(--giallo);border:4px solid var(--arancio);color:var(--inchiostro)}
.foglio .testa{grid-column:span 3}
.foglio .testa p{font-size:24px;color:var(--grigio)}
.segnaposto{background:var(--bianco);border:3px dashed var(--linea);border-radius:10px;padding:28px 36px}
.foot{position:absolute;left:112px;bottom:56px;width:1600px;font-size:24px;color:var(--grigio)}
.scena .foot{color:#9AA3B2}
"""

def impostazioni(attr):
    parti = []
    if attr.get("rumore") and attr["rumore"] != "spento":
        parti.append("rumore=" + attr["rumore"])
    if attr.get("fase"):
        parti.append("fase=" + attr["fase"])
    if attr.get("timer"):
        sec = attr["timer"].split(",")
        nomi = (attr.get("timer-nomi") or "").split("|")
        parti.append("timer=" + "; ".join(f"{s} {nomi[k] if k < len(nomi) else ''}".strip() for k, s in enumerate(sec)))
    if attr.get("logica"):
        parti.append("logica=" + attr["logica"])
    return "IMPOSTAZIONI: " + (" | ".join(parti) if parti else "nessuna")

def converti(sez, ident, piede):
    m = re.match(r"<section ([^>]*)>", sez)
    attr = dict(re.findall(r'data-([a-z-]+)="([^"]*)"', m.group(1)))
    classi = re.search(r'class="([^"]*)"', m.group(1)).group(1).split()
    classi = [c for c in classi if c != "slide"]
    corpo = sez[m.end():].rsplit("</section>", 1)[0]
    nota = ""
    a = re.search(r'<aside class="note">(.*?)</aside>', corpo, re.S)
    if a:
        nota = html.unescape(a.group(1)).strip()
        corpo = corpo[:a.start()] + corpo[a.end():]
    corpo = re.sub(r'\bpasso\b', "fragment", corpo)
    corpo = corpo.replace('<div class="sorteggio"></div>',
        '<div class="segnaposto"><p>Qui compare il sorteggio dei gruppi: si scrivono gli assenti (numeri del registro) e si preme «Sorteggia». Funziona nella versione HTML.</p></div>')
    # testo nudo dentro i div della miniatura del foglio e dei dettagli: in un deck il testo va in un <p>
    corpo = re.sub(r'(<div class="r(?: qui)?"[^>]*>)(.*?)(</div>)', lambda x: x.group(1) + "<p>" + x.group(2) + "</p>" + x.group(3), corpo)
    corpo = re.sub(r'(<div class="testa">)(.*?)(</div>)', lambda x: x.group(1) + "<p>" + x.group(2) + "</p>" + x.group(3), corpo)
    corpo = re.sub(r'<div class="(occhiello|etichetta|tit)">(.*?)</div>', r'<p class="\1">\2</p>', corpo)
    corpo = re.sub(r'<span class="k">(.*?)</span>', r'<p class="k">\1</p>', corpo)
    corpo = re.sub(r'<div class="s">(.*?)</div>', r'<p class="s">\1</p>', corpo)
    corpo = re.sub(r'<div class="formula">(.*?)</div>', r'<p class="formula">\1</p>', corpo, flags=re.S)
    corpo = re.sub(r'<div class="codice">(.*?)</div>', lambda x: '<p class="codice">' + x.group(1).replace("\n", "<br>") + "</p>", corpo, flags=re.S)
    corpo = re.sub(r'style="grid-template-columns:repeat\(3,1fr\)"', "", corpo)
    corpo = re.sub(r'style="--c:(#[0-9A-Fa-f]{6})"', r'style="border-top-color:\1"', corpo)
    corpo = re.sub(r'style="--c:var\(--p16-g-([a-z]+)\)"', r'style="border-top-color:var(--\1)"', corpo)
    testo_nota = impostazioni(attr) + ("\n" + nota if nota else "")
    cls = f' class="{" ".join(classi)}"' if classi else ""
    return (f'<section id="{ident}"{cls}>\n{corpo.strip()}\n<p class="foot">{piede}</p>\n'
            f"<aside>{html.escape(testo_nota, quote=False)}</aside>\n</section>\n")

def main(n):
    mod = importlib.import_module(f"giornata{n}")
    titolo, S, _F = mod.build()
    out = os.path.join(os.path.dirname(QUI), "artefatti", f"g{n}", "project")
    os.makedirs(os.path.join(out, "slides"), exist_ok=True)
    ordine, sezioni, ora = [], {}, 0
    for k, s in enumerate(S):
        ident = f"g{n}-{k + 1:03d}"
        if 'class="slide scena"' in s:
            ora += 1
            tit = re.search(r"<h1>(.*?)</h1>", s).group(1)
            sezioni[f"s{len(sezioni) + 1}"] = {"description": f"Ora {ora}: {html.unescape(tit)}", "start": ident}
        if k == 0:
            sezioni["s0"] = {"description": "Copertina della giornata", "start": ident}
        piede = f"IA e dati · 1P · Giornata {n}" + (f" · Ora {ora}" if ora else "")
        with open(os.path.join(out, "slides", ident + ".html"), "w") as f:
            f.write(converti(s, ident, piede))
        ordine.append(ident)
    sez = {"s0": sezioni.pop("s0")}
    sez.update(sezioni)
    deck = {"v": 5, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
            "lists": "css", "format": {"v": 1, "shared": ["project/deck.css"]}, "title": html.unescape(titolo),
            "order": ordine, "cover": ordine[0], "sections": sez,
            "faces": {"atkinson-hyperlegible": {"family": "Atkinson Hyperlegible", "href": FONT}}, "designSystems": []}
    with open(os.path.join(out, "deck.json"), "w") as f:
        json.dump(deck, f, ensure_ascii=False, indent=1)
    with open(os.path.join(out, "deck.css"), "w") as f:
        f.write(CSS)
    print(f"giornata {n}: {len(ordine)} slide in {out}")

if __name__ == "__main__":
    sys.path.insert(0, QUI)
    for n in sys.argv[1:]:
        main(n)
