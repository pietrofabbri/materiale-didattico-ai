"""Costruisce index.html: tutte le giornate in un solo file autosufficiente.

Dentro il file ci sono stile, font, immagini, barattolo, motore e i fogli dell'ora da stampare
(bottone nel menu iniziale). Funziona offline aprendo il file, e online da GitHub Pages.
Uso: python3 unico.py [cartella di uscita]   (predefinita: la cartella sopra sorgenti/)
"""
import base64, importlib, os, re, sys
from g import T, FOGLI_TESTA, pagina_foglio
import da_artefatto as DA

QUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(QUI)
OUT = sys.argv[1] if len(sys.argv) > 1 else BASE

def leggi(p, binario=False):
    with open(os.path.join(BASE, p), "rb" if binario else "r") as f:
        return f.read()

def data_uri(p, mime):
    return f"data:{mime};base64," + base64.b64encode(leggi(p, True)).decode()

FONT_R = data_uri("comune/fonts/AtkinsonHyperlegible-Regular.ttf", "font/ttf")
FONT_B = data_uri("comune/fonts/AtkinsonHyperlegible-Bold.ttf", "font/ttf")

def css_con_font(css):
    css = css.replace('url("fonts/AtkinsonHyperlegible-Regular.ttf")', f'url("{FONT_R}")')
    return css.replace('url("fonts/AtkinsonHyperlegible-Bold.ttf")', f'url("{FONT_B}")')

def js_sicuro(js):
    """Un </script> dentro i commenti chiuderebbe il tag in anticipo."""
    return re.sub(r"</(script)", r"<\\/\1", js, flags=re.I)

def immagini_inline(html):
    return re.sub(r'src="(img/[^"]+\.png)"', lambda m: f'src="{data_uri(m.group(1), "image/png")}"', html)

GIORNATE = [
    (1, "La lingua come dati", "Parole, fatti e opinioni, il pappagallo della classe"),
    (2, "Incertezza e misura", "Probabilità, dispersione, il calcolatore"),
    (3, "Il corpo come fonte di dati", "Prove motorie in aula, misure, dataset pulito"),
    (4, "Dai dati alle scoperte", "Analisi, modelli che imparano, presentazione finale"),
    (5, "Recupero, oppure il primo modello", "Vicini e distanze, il torneo dei frutti"),
]

def main():
    sezioni, templ, css_deck, fonti = [], [], [], []
    palette = leggi("comune/palette.css")
    for n, _tit, _sotto in GIORNATE:
        _titolo, S, F = importlib.import_module(f"giornata{n}").build()
        if DA.disponibile(n):            # la giornata è stata rivista nel deck: si usano le slide del deck
            sezioni += DA.sezioni(n)
            css_deck.append(DA.css(n))
            fonti.append(f"giornata {n}: deck")
        else:
            S = list(S)
            S[0] = S[0].replace("<section ", f'<section id="giornata-{n}" ', 1)
            sezioni += S
            fonti.append(f"giornata {n}: generatore")
        fogli = "".join(pagina_foglio(n, h, t, r) for h, t, r in F)
        templ.append(f'<template id="fogli-{n}">{fogli}</template>')
    testa = (FOGLI_TESTA.format(titolo=T("Fogli dell'ora"))
             .replace('<link rel="stylesheet" href="comune/palette.css">', f"<style>{palette}</style>")
             .replace('url("comune/fonts/AtkinsonHyperlegible-Regular.ttf")', f'url("{FONT_R}")')
             .replace('url("comune/fonts/AtkinsonHyperlegible-Bold.ttf")', f'url("{FONT_B}")'))
    templ.append(f'<template id="fogli-testa">{testa}</template>')

    righe = "".join(
        f'<div class="carta" style="--c:var(--p16-g-{c})"><div class="tit">Giornata {n} · {T(t)}</div><p class="piccolo">{T(s)}</p>'
        f'<div class="menu-bottoni"><button class="bottone pieno" type="button" data-vai="giornata-{n}">Apri le slide</button>'
        f'<button class="bottone" type="button" data-stampa="fogli-{n}">Stampa i fogli dell’ora</button></div></div>'
        for (n, t, s), c in zip(GIORNATE, ["azzurro", "verde", "arancio", "viola", "petrolio"]))
    menu = ('<section class="slide" id="menu" data-rumore="spento">\n'
            '<div class="occhiello">Percorso «Intelligenza artificiale e dati» · Classe 1P</div>'
            '<h2>Come impara una macchina</h2>'
            f'<p>{T("Quattro giornate, più una di recupero o di approfondimento. Scegli la giornata.")}</p>'
            f'<div class="carte menu">{righe}</div>'
            '<aside class="note">Prima della lezione: premere B e fare la taratura del barattolo (silenzio, poi discussione). Tasti: frecce avanti e indietro, spazio timer, N note, H aiuto, Home torna al menu. Nessun dato degli studenti viene salvato o trasmesso. Stampare i fogli dell’ora della giornata, in A3 orizzontale, una copia per gruppo: il bottone apre una finestra di stampa (consentire i popup).</aside>\n'
            "</section>\n")

    stile = css_con_font(leggi("comune/stile.css")) + "\n".join(css_deck) + (DA.CSS_TELA if css_deck else "") + """
.carte.menu{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4vw}
.carte.menu .carta{min-width:0}\n.carte.menu .tit{font-size:clamp(16px,1.8vw,34px)}
.menu-bottoni{display:flex;gap:.8vw;flex-wrap:wrap;margin-top:.6vh}
.menu-bottoni .bottone{font-size:clamp(14px,1.15vw,22px);padding:6px 12px}
"""
    corpo = menu + "".join(sezioni)
    html = ("<!doctype html>\n<html lang=\"it\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>IA e dati · 1P · Slide delle cinque giornate</title>"
            f"<style>{palette}</style><style>{stile}</style></head><body>\n"
            + immagini_inline(corpo) + "".join(templ)
            + "<script>" + js_sicuro(leggi('comune/barattolo.js')) + "</script>\n"
            + "<script>" + js_sicuro(leggi('comune/motore.js')) + "</script>\n" + (DA.JS_TELA if css_deck else "") + "<script>Motore.avvia();</script>\n</body></html>\n")
    assert not re.search("[\\u2013\\u2014]", html), "trattino lungo"
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(html)
    print(", ".join(fonti))
    print("index.html:", len(re.findall(r'<section class="slide', corpo)), "slide,", round(len(html) / 1024), "KB")

if __name__ == "__main__":
    main()
