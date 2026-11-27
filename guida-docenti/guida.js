(function () {
  const ORDINE = __ORDINE__;
  const pagine = {}; document.querySelectorAll(".pag").forEach(p => pagine[p.dataset.id] = p);
  const link = [...document.querySelectorAll(".indice a")];
  const pos = document.querySelector(".pos"), area = document.querySelector(".pagine");
  let i = 0;

  function mostra(id, ancora) {
    const k = ORDINE.indexOf(id); if (k < 0) return;
    i = k;
    Object.values(pagine).forEach(p => p.classList.remove("on"));
    pagine[id].classList.add("on");
    link.forEach(a => a.classList.toggle("qui", a.getAttribute("href") === "#" + id));
    pos.textContent = (i + 1) + " di " + ORDINE.length;
    if (ancora) {
      const d = document.getElementById(ancora);
      if (d) { d.open = true; setTimeout(() => d.scrollIntoView({ block: "center" }), 50); }
    } else area.scrollTop = 0;
    try { history.replaceState(null, "", "#" + (ancora || id)); } catch (e) {}
  }
  function vai(h) {
    if (pagine[h]) return mostra(h);
    const m = h.match(/^(.*)-(\d+)$/);
    if (m && pagine[m[1]]) return mostra(m[1], h);
    mostra(ORDINE[0]);
  }
  window.addEventListener("hashchange", () => vai(location.hash.slice(1)));
  document.addEventListener("click", e => {
    const a = e.target.closest("a[href^='#']"); if (!a) return;
    e.preventDefault(); vai(a.getAttribute("href").slice(1));
  });
  const prec = document.querySelector(".prec"), succ = document.querySelector(".succ");
  prec.onclick = () => i > 0 && mostra(ORDINE[i - 1]);
  succ.onclick = () => i < ORDINE.length - 1 && mostra(ORDINE[i + 1]);
  document.addEventListener("keydown", e => {
    if (e.target.matches("input,select")) return;
    if (e.key === "ArrowRight") succ.click();
    if (e.key === "ArrowLeft") prec.click();
  });

  const sel = document.getElementById("materia");
  function scegli(r) {
    document.body.dataset.ruolo = r; if (sel) sel.value = r;
    link.forEach(a => {
      const rr = a.dataset.ruoli.split(" ");
      a.classList.toggle("mia", r !== "tutti" && rr.includes(r));
      a.classList.toggle("altrui", r !== "tutti" && !rr.includes(r) && !rr.includes("tutti"));
    });
    try { localStorage.setItem("guida-ruolo", r); } catch (e) {}
  }
  if (sel) sel.addEventListener("change", () => scegli(sel.value));
  try { const r = localStorage.getItem("guida-ruolo"); if (r) scegli(r); } catch (e) {}

  const cerca = document.querySelector(".cerca");
  if (cerca) cerca.addEventListener("input", () => {
    const q = cerca.value.trim().toLowerCase();
    document.querySelectorAll(".voce").forEach(v => v.style.display = v.textContent.toLowerCase().includes(q) ? "" : "none");
  });
  vai(location.hash.slice(1));
})();
