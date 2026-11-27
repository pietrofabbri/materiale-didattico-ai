(function(){
const D=__DATI__, LIV=__LIV__;
const $=s=>document.querySelector(s);
let mat="tutti"; try{mat=localStorage.getItem("materia")||"tutti"}catch(e){}
const LNOME={1:"Che cosa fare",2:"Perché è fatta così",3:"Che cosa dice la ricerca",4:"Il concetto a fondo"};
const LGEN={1:"Livello base",2:"Più a fondo",3:"Ancora più a fondo",4:"Il fondo"};
function nomeLiv(p,l){return D[p].scala?LNOME[l]:LGEN[l]}
function radice(id){let r=id;while(D[r].su&&D[D[r].su].capitolo===D[id].capitolo&&D[r].livello>1)r=D[r].su;return r}
function scalaDi(id){const up=[id];let r=id;while(D[r].su&&D[D[r].su].capitolo===D[id].capitolo&&D[r].livello>1){r=D[r].su;up.unshift(r)}let d=id;while(D[d].giu&&D[D[d].giu].livello>D[d].livello){d=D[d].giu;up.push(d)}return up}
function mia(p){return mat!=="tutti"&&D[p].ruoli.includes(mat)}
function vai(){
  let id=decodeURIComponent(location.hash.slice(1))||"home";
  if(!D[id]){const el=document.getElementById(id);if(el){const s=el.closest(".pag");if(s)id=s.dataset.id}else id="home"}
  document.querySelectorAll(".pag").forEach(s=>s.classList.toggle("on",s.dataset.id===id));
  const p=D[id];
  $(".titolo").textContent=p.titolo;
  $(".capitolo").innerHTML=(p.capitolo||"")+(p.livello>1||D[id].giu?` <span class="lv lv${p.livello}">${p.livello} · ${nomeLiv(id,p.livello)}</span>`:"");
  // briciole
  const sc=scalaDi(id);let b=`<a href="#home">Inizio</a>`;
  if(p.capitolo)b+=`<span class="sep">›</span>${p.capitolo}`;
  if(id!=="home"){sc.slice(0,sc.indexOf(id)+1).forEach((q,i)=>{b+=`<span class="sep">›</span>`+(q===id?`<b>${i?nomeLiv(q,D[q].livello):D[q].titolo}</b>`:`<a href="#${q}">${i?nomeLiv(q,D[q].livello):D[q].titolo}</a>`)})}
  $(".briciole").innerHTML=b;
  // profondità
  const pr=$(".profondita");
  if(sc.length>1){const k=sc.indexOf(id);pr.innerHTML=sc.map((q,i)=>`<a class="pz l${D[q].livello} ${q===id?"on":i<k?"pass":""}" href="#${q}"><b>Livello ${D[q].livello}</b>${nomeLiv(q,D[q].livello)}</a>`).join("")}else pr.innerHTML="";
  // scendi/risali
  let g="";
  if(p.giu){const q=D[p.giu];g+=`<a class="scendi" href="#${p.giu}"><small>Scendi · livello ${q.livello} &nbsp;↓</small><span>${D[id].scala?nomeLiv(p.giu,q.livello):q.titolo}</span></a>`}
  if(p.su&&p.livello>1){g+=`<a class="risali" href="#${p.su}"><small>Risali · livello ${D[p.su].livello} &nbsp;↑</small>${D[id].scala?nomeLiv(p.su,D[p.su].livello):D[p.su].titolo}</a>`}
  $(".giu").innerHTML=g;
  const ls=$(".lato");
  ls.innerHTML=(p.prec?`<a class="prec" href="#${p.prec}"><small>← Precedente</small>${D[p.prec].titolo}</a>`:"")+(p.succ?`<a class="succ" href="#${p.succ}"><small>Successiva →</small>${D[p.succ].titolo}</a>`:"");
  indice(id); materia(); window.scrollTo(0,0);
  document.title=p.titolo+" · Guida per i docenti";
}
function indice(cur){
  const caps={};Object.keys(D).forEach(k=>{const p=D[k];if(p.livello===1&&k!=="home"){(caps[p.capitolo]=caps[p.capitolo]||[]).push(k)}});
  if(D.principi)(caps["Principi didattici"]=caps["Principi didattici"]||[]);
  let h=`<a href="#home" class="${cur==="home"?"on":""}">Inizio</a>`;
  for(const c in caps){h+=`<h4>${c}</h4>`+caps[c].map(k=>`<a href="#${k}" class="${radice(cur)===k?"on":""} ${mia(k)?"mia":""}">${D[k].titolo}</a>`).join("")}
  $(".indice-l").innerHTML=h;
}
function materia(){
  const s=$("#materia");if(s)s.value=mat;
  document.querySelectorAll(".ore-home li").forEach(li=>li.classList.toggle("mia",mat!=="tutti"&&li.dataset.ruoli.split(" ").includes(mat)));
}
document.addEventListener("change",e=>{if(e.target.id==="materia"){mat=e.target.value;try{localStorage.setItem("materia",mat)}catch(x){}materia();indice(decodeURIComponent(location.hash.slice(1))||"home")}});
const ov=$(".indice");
$(".apri-indice").onclick=()=>{ov.hidden=false};
$(".chiudi").onclick=()=>{ov.hidden=true};
ov.addEventListener("click",e=>{if(e.target===ov||e.target.closest(".indice-l a"))ov.hidden=true});
document.addEventListener("input",e=>{if(e.target.classList.contains("cerca")){const t=e.target.value.toLowerCase();document.querySelectorAll(".glossario .voce").forEach(v=>v.style.display=v.textContent.toLowerCase().includes(t)?"":"none")}});
document.addEventListener("keydown",e=>{
  if(e.target.matches("input,select,textarea"))return;
  const id=decodeURIComponent(location.hash.slice(1))||"home",p=D[id]||D.home;
  if(e.key==="Escape")ov.hidden=true;
  else if(e.key==="ArrowRight"&&p.succ)location.hash=p.succ;
  else if(e.key==="ArrowLeft"&&p.prec)location.hash=p.prec;
  else if(e.key==="ArrowDown"&&e.altKey&&p.giu)location.hash=p.giu;
  else if(e.key==="ArrowUp"&&e.altKey&&p.su)location.hash=p.su;
  else if(e.key==="i"||e.key==="I")ov.hidden=!ov.hidden;
});
addEventListener("hashchange",vai);vai();
})();
