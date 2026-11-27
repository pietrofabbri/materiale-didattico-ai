(function () {
  const ORDINE = __ORDINE__;
  const RUOLI = { it: "Italiano", ma: "Matematica", ef: "Ed. fisica", in: "Informatica", tutti: "Tutto" };
  const pagine = {}; document.querySelectorAll(".pag").forEach(p => pagine[p.dataset.id] = p);
  const link = [...document.querySelectorAll(".menu nav a")];
  const riemp = document.querySelector(".riemp"), pos = document.querySelector(".pos");
  const area = document.querySelector(".pagine");
  let i = 0;

  function mostra(id, ancora) {
    const k = ORDINE.indexOf(id); if (k < 0) return;
    i = k;
    Object.values(pagine).forEach(p => p.classList.remove("on"));
    pagine[id].classList.add("on");
    link.forEach(a => a.classList.toggle("qui", a.getAttribute("href") === "#" + id));
    riemp.style.width = ((i + 1) / ORDINE.length * 100) + "%";
    pos.textContent = (i + 1) + " / " + ORDINE.length;
    if (ancora) {
      const d = document.getElementById(ancora);
      if (d) { d.open = true; setTimeout(() => d.scrollIntoView({ block: "center" }), 60); }
    } else area.scrollTop = 0;
    try { if (location.hash.slice(1) !== (ancora || id)) history.replaceState(null, "", "#" + (ancora || id)); } catch (e) {}
  }
  function daHash() {
    const h = location.hash.slice(1);
    if (!h) return mostra(ORDINE[0]);
    if (pagine[h]) return mostra(h);
    const m = h.match(/^(.*)-(\d+)$/);
    if (m && pagine[m[1]]) return mostra(m[1], h);
    mostra(ORDINE[0]);
  }
  window.addEventListener("hashchange", daHash);
  document.addEventListener("click", e => {
    const a = e.target.closest("a[href^='#']"); if (!a) return;
    e.preventDefault(); const h = a.getAttribute("href").slice(1);
    const m = h.match(/^(.*)-(\d+)$/);
    if (pagine[h]) mostra(h); else if (m && pagine[m[1]]) mostra(m[1], h);
  });
  document.querySelector(".prec").onclick = () => i > 0 && mostra(ORDINE[i - 1]);
  document.querySelector(".succ").onclick = () => i < ORDINE.length - 1 && mostra(ORDINE[i + 1]);
  document.addEventListener("keydown", e => {
    if (e.target.matches("input")) return;
    if (e.key === "ArrowRight") document.querySelector(".succ").click();
    if (e.key === "ArrowLeft") document.querySelector(".prec").click();
  });

  // filtro per materia
  const filtro = document.querySelector(".filtro");
  Object.entries(RUOLI).forEach(([k, v]) => {
    const b = document.createElement("button"); b.textContent = v; b.dataset.ruolo = k; filtro.appendChild(b);
  });
  function scegli(r) {
    document.body.dataset.ruolo = r;
    document.querySelectorAll("[data-ruolo]").forEach(b => { if (b.tagName === "BUTTON") b.classList.toggle("on", b.dataset.ruolo === r); });
    link.forEach(a => {
      const rr = a.dataset.ruoli.split(" ");
      const mia = r !== "tutti" && rr.includes(r);
      a.classList.toggle("mia", mia);
      a.classList.toggle("altrui", r !== "tutti" && !rr.includes(r) && !rr.includes("tutti"));
    });
    try { localStorage.setItem("guida-ruolo", r); } catch (e) {}
  }
  document.addEventListener("click", e => {
    const b = e.target.closest("button[data-ruolo]"); if (!b) return;
    scegli(b.dataset.ruolo);
    if (b.closest(".scelta")) mostra(ORDINE[1]);
  });
  try { const r = localStorage.getItem("guida-ruolo"); if (r) scegli(r); } catch (e) {}

  // scaletta: clic su un segmento apre l'attività
  document.querySelectorAll(".scaletta .seg").forEach(s => s.addEventListener("mouseenter", () => s.classList.add("on")));
  document.querySelectorAll(".scaletta .seg").forEach(s => s.addEventListener("mouseleave", () => s.classList.remove("on")));

  // glossario
  const cerca = document.querySelector(".cerca");
  if (cerca) cerca.addEventListener("input", () => {
    const q = cerca.value.trim().toLowerCase();
    document.querySelectorAll(".voce").forEach(v => v.style.display = v.textContent.toLowerCase().includes(q) ? "" : "none");
  });
  daHash();
})();
