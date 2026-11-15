/*!
 * Percorso «IA e dati» 1P. Motore delle slide.
 * Derivato dal motore del Progetto 16 (stessa logica, stesso barattolo), con tre aggiunte:
 * timer in sequenza, note per il docente, sorteggio dei gruppi.
 *
 * Una lezione è un file HTML con tante <section class="slide">. Attributi:
 *   data-rumore="silenzio|discussione|spento"   modalità del barattolo (predefinita: spento)
 *   data-fase="solo|gruppo|tutti"               icona della fase in alto a destra
 *   data-timer="180,300"                        uno o più timer in secondi, in sequenza
 *   data-timer-nomi="Da soli|Nel gruppo"        nome di ciascun timer (facoltativo)
 *   data-logica="sorteggio"                     slide con il sorteggio dei gruppi
 * Gli elementi con classe .passo compaiono uno alla volta con la freccia avanti.
 * Le note per il docente stanno in <aside class="note"> dentro la slide (tasto N).
 *
 * Tasti: freccia destra / pagina giù = avanti; freccia sinistra / pagina su = indietro;
 *   spazio = avvia o ferma il timer; quando un timer è finito, spazio avvia il successivo;
 *   R = riavvia il timer corrente; N = note del docente; H = aiuto; Home = prima slide;
 *   B, T, U, M, K = barattolo (vedi barattolo.js).
 * Nessun dato degli studenti viene salvato o trasmesso.
 */
(function () {
  "use strict";
  const slides = [...document.querySelectorAll("section.slide")];
  let i = -1, passi = 0;

  const ICONE = {
    solo: { testo: "Da soli", svg: '<circle cx="12" cy="7" r="4"/><path d="M4 22c0-5 3.6-8 8-8s8 3 8 8z"/>' },
    gruppo: { testo: "Nel gruppo", svg: '<circle cx="6" cy="8" r="3"/><circle cx="12" cy="6" r="3.3"/><circle cx="18" cy="8" r="3"/><path d="M0 21c0-4 2.6-7 6-7s6 3 6 7zM6 21c0-4.4 2.7-7.5 6-7.5s6 3.1 6 7.5zM12 21c0-4 2.6-7 6-7s6 3 6 7z"/>' },
    tutti: { testo: "Tutti insieme", svg: '<rect x="2" y="3" width="20" height="13" rx="2"/><path d="M8 21h8M12 16v5" stroke="currentColor" stroke-width="2"/>' },
  };

  // ---------- interfaccia comune
  const testata = document.createElement("div"); testata.className = "m-testata";
  const fase = document.createElement("div"); fase.className = "m-fase"; fase.hidden = true;
  const timer = document.createElement("div"); timer.className = "m-timer"; timer.hidden = true;
  timer.innerHTML = '<div class="anello"><svg viewBox="0 0 100 100"><circle class="fondo" cx="50" cy="50" r="44"/><circle class="arco" cx="50" cy="50" r="44" pathLength="100" stroke-dasharray="100 100"/></svg><div class="cifre"></div></div><div class="nome"></div>';
  testata.append(fase, timer);
  const barra = document.createElement("div"); barra.className = "m-barra";
  const numero = document.createElement("div"); numero.className = "m-numero";
  const aiuto = document.createElement("div"); aiuto.className = "m-aiuto"; aiuto.hidden = true;
  aiuto.innerHTML = "<kbd>→</kbd> avanti · <kbd>←</kbd> indietro · <kbd>spazio</kbd> avvia o ferma il timer (finito: passa al successivo) · <kbd>R</kbd> riavvia il timer<br><kbd>N</kbd> note del docente · <kbd>B</kbd> barattolo · <kbd>T</kbd> taratura · <kbd>U</kbd> sblocca · <kbd>M</kbd> modalità solo per questa slide · <kbd>K</kbd> blocco sì/no · <kbd>H</kbd> aiuto";
  const note = document.createElement("div"); note.className = "m-note"; note.hidden = true;
  document.body.append(testata, barra, numero, aiuto, note);

  // ---------- timer in sequenza
  const T = { lista: [], nomi: [], k: 0, durata: 0, resto: 0, va: false, ultimo: 0, inPausaPerBlocco: false };
  const arco = timer.querySelector(".arco"), cifre = timer.querySelector(".cifre"), nomeT = timer.querySelector(".nome");
  function mostraTimer() {
    const s = Math.max(0, Math.ceil(T.resto));
    cifre.textContent = Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0");
    arco.setAttribute("stroke-dasharray", (T.durata ? (T.resto / T.durata) * 100 : 0) + " 100");
    const fine = T.durata > 0 && T.resto <= 0;
    timer.classList.toggle("fine", fine);
    timer.classList.toggle("pausa", !T.va && T.resto > 0);
    const n = T.lista.length;
    let testo = T.nomi[T.k] || "";
    if (n > 1) testo = (testo ? testo + " · " : "") + (T.k + 1) + " di " + n;
    if (fine && T.k < n - 1) testo += " · spazio: prossimo";
    nomeT.textContent = testo;
  }
  function caricaTimer(k) {
    T.k = k; T.durata = T.lista[k] || 0; T.resto = T.durata; T.va = false; mostraTimer();
  }
  function impostaTimer(lista, nomi) {
    T.lista = lista; T.nomi = nomi; timer.hidden = !lista.length; caricaTimer(0);
  }
  function avviaTimer() { if (!T.durata) return; if (T.resto <= 0) T.resto = T.durata; T.va = true; T.ultimo = performance.now(); mostraTimer(); }
  function fermaTimer() { T.va = false; mostraTimer(); }
  function spazio() {
    if (!T.lista.length) return;
    if (T.va) return fermaTimer();
    if (T.resto <= 0 && T.k < T.lista.length - 1) { caricaTimer(T.k + 1); return avviaTimer(); }
    avviaTimer();
  }
  function giro(now) {
    if (T.va) {
      T.resto -= (now - T.ultimo) / 1000; T.ultimo = now;
      if (T.resto <= 0) { T.resto = 0; T.va = false; campanella(); }
      mostraTimer();
    }
    requestAnimationFrame(giro);
  }
  requestAnimationFrame(giro);
  document.addEventListener("barattolo:blocco", () => { if (T.va) { T.inPausaPerBlocco = true; fermaTimer(); } });
  document.addEventListener("barattolo:sblocco", () => { if (T.inPausaPerBlocco) { T.inPausaPerBlocco = false; avviaTimer(); } });

  let actx = null;
  function campanella() {
    try {
      actx = actx || new (window.AudioContext || window.webkitAudioContext)();
      const t0 = actx.currentTime, g = actx.createGain(); g.connect(actx.destination);
      [[880, 0.18], [1320, 0.08]].forEach(([f, a]) => {
        const o = actx.createOscillator(), gg = actx.createGain(); o.frequency.value = f;
        gg.gain.setValueAtTime(a, t0); gg.gain.exponentialRampToValueAtTime(0.0001, t0 + 1.2);
        o.connect(gg).connect(g); o.start(t0); o.stop(t0 + 1.3);
      });
    } catch (e) {}
  }

  // ---------- sorteggio dei gruppi (solo numeri del registro, nulla viene salvato)
  const COLORI = [["Rosso", "#C8372D"], ["Arancio", "#DB6A1C"], ["Verde", "#3A8A3E"], ["Petrolio", "#0E7C7B"], ["Azzurro", "#2C8BC9"], ["Viola", "#6B3FA0"]];
  function preparaSorteggio(s) {
    const box = s.querySelector(".sorteggio"); if (!box || box.dataset.pronto) return;
    box.dataset.pronto = "1";
    box.innerHTML = '<div class="sort-comandi"><label>Studenti in elenco <input type="number" class="s-tot" min="6" max="40" value="29"></label>' +
      '<label>Assenti (numeri del registro) <input type="text" class="s-ass" placeholder="es. 4, 17"></label>' +
      '<label>Gruppi <input type="number" class="s-n" min="2" max="6" value="6"></label>' +
      '<button class="bottone pieno s-via" type="button">Sorteggia</button></div><div class="sort-gruppi"></div>';
    box.querySelector(".s-via").addEventListener("click", () => {
      const tot = +box.querySelector(".s-tot").value || 29, n = Math.min(6, Math.max(2, +box.querySelector(".s-n").value || 6));
      const ass = new Set(box.querySelector(".s-ass").value.split(/[^0-9]+/).filter(Boolean).map(Number));
      const num = []; for (let k = 1; k <= tot; k++) if (!ass.has(k)) num.push(k);
      for (let k = num.length - 1; k > 0; k--) { const j = Math.floor(Math.random() * (k + 1)); [num[k], num[j]] = [num[j], num[k]]; }
      const gr = Array.from({ length: n }, () => []); num.forEach((x, k) => gr[k % n].push(x));
      box.querySelector(".sort-gruppi").innerHTML = gr.map((g, k) =>
        `<div class="gruppo" style="--g:${COLORI[k][1]}"><div class="gtit">Gruppo ${k + 1} · ${COLORI[k][0]}</div><div class="gnum">${g.sort((a, b) => a - b).join(" · ")}</div></div>`).join("");
    });
  }

  // ---------- navigazione
  function vai(k, daDietro) {
    if (k < 0 || k >= slides.length) return;
    if (i >= 0) slides[i].classList.remove("attiva");
    i = k;
    const s = slides[i];
    s.classList.add("attiva");
    const tutti = [...s.querySelectorAll(".passo")];
    passi = daDietro ? tutti.length : 0;
    tutti.forEach((el, n) => el.classList.toggle("visto", n < passi));
    const f = s.dataset.fase;
    fase.hidden = !ICONE[f];
    if (ICONE[f]) fase.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor">' + ICONE[f].svg + "</svg>" + ICONE[f].testo;
    const lista = (s.dataset.timer || "").split(",").map(Number).filter(x => x > 0);
    impostaTimer(lista, (s.dataset.timerNomi || "").split("|"));
    if (window.Barattolo) Barattolo.modalita(s.dataset.rumore || "spento");
    if (s.dataset.logica === "sorteggio") preparaSorteggio(s);
    barra.style.width = ((i + 1) / slides.length * 100) + "%";
    numero.textContent = (i + 1) + " / " + slides.length;
    const a = s.querySelector("aside.note");
    note.innerHTML = a ? '<b>Note per il docente</b><br>' + a.innerHTML : "<b>Nessuna nota per questa slide.</b>";
    try { history.replaceState(null, "", "#" + (i + 1)); } catch (e) {}
  }
  function avanti() {
    const tutti = [...slides[i].querySelectorAll(".passo")];
    if (passi < tutti.length) { tutti[passi].classList.add("visto"); passi++; return; }
    vai(i + 1);
  }
  function indietro() {
    const tutti = [...slides[i].querySelectorAll(".passo")];
    if (passi > 0) { passi--; tutti[passi].classList.remove("visto"); return; }
    vai(i - 1, true);
  }

  // ---------- tastiera
  document.addEventListener("keydown", e => {
    if (e.target && /input|textarea|select/i.test(e.target.tagName)) return;
    if (document.querySelector(".p16b-pann")) return;
    if (document.querySelector(".p16b-velo.on")) return;
    const k = e.key;
    if (k === "ArrowRight" || k === "PageDown") avanti();
    else if (k === "ArrowLeft" || k === "PageUp") indietro();
    else if (k === " ") spazio();
    else if (k === "r" || k === "R") { T.resto = T.durata; T.va = false; mostraTimer(); }
    else if (k === "n" || k === "N") note.hidden = !note.hidden;
    else if (k === "h" || k === "H") aiuto.hidden = !aiuto.hidden;
    else if (k === "Home") vai(0);
    else return;
    e.preventDefault();
  });

  // ---------- menu delle giornate e stampa dei fogli (versione in un solo file)
  document.addEventListener("click", e => {
    const v = e.target.closest("[data-vai]");
    if (v) { const k = slides.findIndex(s => s.id === v.dataset.vai); if (k >= 0) vai(k); return; }
    const st = e.target.closest("[data-stampa]");
    if (st) {
      const tpl = document.getElementById(st.dataset.stampa); if (!tpl) return;
      const w = window.open("", "_blank");
      if (!w) { alert("Il browser ha bloccato la finestra: consenti i popup per questa pagina."); return; }
      const testa = document.getElementById("fogli-testa");
      w.document.open(); w.document.write((testa ? testa.innerHTML : "") + tpl.innerHTML + "</body></html>"); w.document.close();
      setTimeout(() => { try { w.focus(); w.print(); } catch (err) {} }, 600);
    }
  });

  window.Motore = {
    vai: n => vai(n), avanti, indietro,
    avvia() {
      if (window.Barattolo) Barattolo.monta({ modalita: "spento" });
      const h = parseInt((location.hash || "").slice(1), 10);
      vai(h > 0 && h <= slides.length ? h - 1 : 0);
    },
  };
})();
