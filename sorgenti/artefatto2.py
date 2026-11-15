"""Giornate scritte con g2.py -> deck del tipo Slides di Claude.
Uso: python3 artefatto2.py 1  -> ../artefatti/g1/project/{deck.json,deck.css,slides/*.html}
"""
import datetime, html, importlib, json, os, re, shutil, sys
QUI = os.path.dirname(os.path.abspath(__file__))
FONT = "https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap"

def main(n):
    titolo, S, _F = importlib.import_module(f"giornata{n}").build()
    out = os.path.join(os.path.dirname(QUI), "artefatti", f"g{n}", "project")
    if os.path.isdir(os.path.join(out, "slides")):
        shutil.rmtree(os.path.join(out, "slides"))
    os.makedirs(os.path.join(out, "slides"))
    ordine, sez = [], {}
    for ident, s in S:
        if "copertina" in s.split(">")[0]:
            sez["s0"] = {"description": "Copertina della giornata", "start": ident}
        elif 'class="scena' in s.split(">")[0]:
            tit = html.unescape(re.sub("<[^>]+>", "", re.search(r"<h1>(.*?)</h1>", s).group(1)))
            sez[f"s{len(sez)}"] = {"description": f"Ora {len(sez)}: {tit}", "start": ident}
        open(os.path.join(out, "slides", ident + ".html"), "w").write(s)
        ordine.append(ident)
    deck = {"v": 5, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
            "lists": "css", "format": {"v": 1, "shared": ["project/deck.css"]}, "title": titolo,
            "order": ordine, "cover": ordine[0], "sections": sez,
            "faces": {"atkinson-hyperlegible": {"family": "Atkinson Hyperlegible", "href": FONT}}, "designSystems": []}
    json.dump(deck, open(os.path.join(out, "deck.json"), "w"), ensure_ascii=False, indent=1)
    shutil.copy(os.path.join(QUI, "stile_deck.css"), os.path.join(out, "deck.css"))
    print(f"giornata {n}: {len(ordine)} slide; sezioni: {[v['description'] for v in sez.values()]}")

if __name__ == "__main__":
    sys.path.insert(0, QUI)
    for n in sys.argv[1:]:
        main(n)
