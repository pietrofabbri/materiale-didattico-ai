(function(){
const D=__DATI__, CAPS=__CAPS__, ORE=__ORE__;
const $=s=>document.querySelector(s);
let mat="tutti"; try{mat=localStorage.getItem("materia")||"tutti"}catch(e){}
const LORA={1:"Che cosa fare",2:"Perché è fatta così",3:"Che cosa dice la ricerca",4:"Il concetto a fondo"};
const LGEN={1:"Base",2:"Più a fondo",3:"Ancora più a fondo",4:"Il fondo"};
const nome=(q)=>D[q].scala?LORA[D[q].livello]:(D[q].livello===1?D[q].titolo:D[q].titolo);
const corto=(q)=>D[q].scala?LORA[D[q].livello]:LGEN[D[q].livello];
function scala(id){const up=[id];let r=id;while(D[r].su&&D[r].livello>1){r=D[r].su;up.unshift(r)}let d=id;while(D[d].giu&&D[D[d].giu].livello>D[d].livello&&D[D[d].giu].su===d){d=D[d].giu;up.push(d)}return up}
const cur=()=>{let id=decodeURIComponent(location.hash.slice(1))||"home";return D[id]?id:"home"};
function vai(){
  let id=decodeURIComponent(location.hash.slice(1))||"home";
  if(!D[id]){const el=document.getElementById(id);const s=el&&el.closest(".pag");id=s?s.dataset.id:"home"}
  document.querySelectorAll(".pag").forEach(s=>s.classList.toggle("on",s.dataset.id===id));
  const p=D[id], sc=scala(id), k=sc.indexOf(id), radice=sc[0];
  $(".titolo").textContent=p.titolo;
  $(".capitolo").innerHTML=sc.length>1?`<span class="lv lv${p.livello}">Livello ${p.livello} di ${sc.length} · ${corto(id)}</span>`:"";
  // dove sei: Inizio › sezione › (giornata) › pagina › livelli
  const parti=[];
  if(id!=="home")parti.push(`<a href="#home">Inizio</a>`);
  const cap=CAPS[p.capitolo];
  if(cap&&cap!==radice)parti.push(`<a href="#${cap}">${D[cap].titolo}</a>`);
  if(p.gruppo)parti.push(`<span>${p.gruppo}</span>`);
  sc.slice(0,k+1).forEach((q,i)=>{const t=i===0?D[q].titolo.replace(/^G\d · /,""):corto(q);parti.push(q===id?`<b>${t}</b>`:`<a href="#${q}">${t}</a>`)});
  $(".briciole").innerHTML=parti.join('<i class="sep">›</i>');
  // livelli
  $(".livelli").innerHTML=sc.length>1?sc.map((q,i)=>`<a href="#${q}" class="lvp l${D[q].livello} ${q===id?"on":i<k?"pass":""}" title="${corto(q)}"><span>${D[q].livello}</span><em>${corto(q)}</em></a>`).join(""):"";
  // scendi / risali
  let g="";
  if(p.giu&&D[p.giu].su===id){const q=p.giu;g+=`<a class="scendi" href="#${q}"><small>Scendi al livello ${D[q].livello} ↓</small><span>${D[id].scala?LORA[D[q].livello]:D[q].titolo}</span></a>`}
  if(p.livello>1&&p.su){g+=`<a class="risali" href="#${p.su}"><small>Risali al livello ${D[p.su].livello} ↑</small>${D[p.su].scala?LORA[D[p.su].livello]:D[p.su].titolo}</a>`;
    if(p.livello>2)g+=`<a class="risali" href="#${radice}"><small>Torna al livello 1 ⤒</small>${D[radice].titolo}</a>`}
  $(".giu").innerHTML=g;
  const fr=(q,t,c)=>q?`<a class="${c}" href="#${q}"><small>${t}</small>${D[q].titolo}</a>`:"";
  $(".lato").innerHTML=fr(p.prec,"← Precedente","prec")+fr(p.succ,"Successiva →","succ");
  indice(radice); materia(); window.scrollTo(0,0);
  document.title=p.titolo+" · Guida per i docenti";
}
function indice(r){
  const gruppi={};Object.keys(D).forEach(k=>{const p=D[k];if(p.livello===1&&p.capitolo&&CAPS[p.capitolo]!==k){(gruppi[p.capitolo]=gruppi[p.capitolo]||[]).push(k)}});
  let h=`<a href="#home" class="${r==="home"?"on":""}">Inizio</a>`;
  for(const c in CAPS){const l=CAPS[c];h+=`<h4><a href="#${l}" class="${r===l?"on":""}">${D[l].titolo}</a></h4>`;
    let g0="";(gruppi[c]||[]).forEach(k=>{if(D[k].gruppo&&D[k].gruppo!==g0){g0=D[k].gruppo;h+=`<h5>${g0}</h5>`}h+=`<a href="#${k}" class="sub ${r===k?"on":""} ${mat!=="tutti"&&D[k].ruoli.includes(mat)?"mia":""}">${D[k].titolo.replace(/^G\d · /,"")}</a>`})}
  $(".indice-l").innerHTML=h;
}
function materia(){
  const s=$("#materia");if(!s)return;s.value=mat;
  const box=$(".mie");if(!box)return;
  if(mat==="tutti"){box.innerHTML="";return}
  const ks=Object.keys(ORE).filter(k=>ORE[k].includes(mat));
  box.innerHTML=ks.length?"<ul>"+ks.map(k=>`<li><a href="#${k}">${D[k].titolo}</a></li>`).join("")+"</ul>":"";
}
document.addEventListener("change",e=>{if(e.target.id==="materia"){mat=e.target.value;try{localStorage.setItem("materia",mat)}catch(x){}materia();indice(scala(cur())[0])}});
const ov=$(".indice");
$(".apri-indice").onclick=()=>{ov.hidden=false};
$(".chiudi").onclick=()=>{ov.hidden=true};
ov.addEventListener("click",e=>{if(e.target===ov||e.target.closest(".indice-l a"))ov.hidden=true});
document.addEventListener("input",e=>{if(e.target.classList.contains("cerca")){const t=e.target.value.toLowerCase();document.querySelectorAll(".glossario .voce").forEach(v=>v.style.display=v.textContent.toLowerCase().includes(t)?"":"none")}});
document.addEventListener("keydown",e=>{
  if(e.target.matches("input,select,textarea"))return;
  const p=D[cur()];
  if(e.key==="Escape")ov.hidden=true;
  else if(e.key==="ArrowRight"&&p.succ)location.hash=p.succ;
  else if(e.key==="ArrowLeft"&&p.prec)location.hash=p.prec;
  else if(e.key==="ArrowDown"&&e.altKey&&p.giu)location.hash=p.giu;
  else if(e.key==="ArrowUp"&&e.altKey&&p.su)location.hash=p.su;
  else if(e.key==="i"||e.key==="I")ov.hidden=!ov.hidden;
});
addEventListener("hashchange",vai);vai();
})();
