import {useEffect,useState} from "react";
import Tela from "../../componentes/tela/tela";
import Paginacao from "../../componentes/paginacao/paginacao";
import {api} from "../../servicos/api";
import {FUNDOS} from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

const POR_PAGINA = 5;

function Relatos({onNavegar}){
 const [itens,setItens]=useState([]),[meta,setMeta]=useState(null),[pagina,setPagina]=useState(1),[sel,setSel]=useState(null),[resposta,setResposta]=useState(""),[msg,setMsg]=useState("");
 // enquanto a página pedida ainda não chegou da API
 const carregando = !msg && meta?.pag !== pagina;

 async function carregar(p){
  try{
   const r=await api(`/diario?pag=${p}&por_pagina=${POR_PAGINA}&enviado=true`);
   setItens(r.itens||[]);setMeta(r.paginacao||null);
  }catch(e){setMsg(e.message);}
 }
 useEffect(()=>{carregar(pagina);},[pagina]);

 function mudarPagina(nova){setSel(null);setResposta("");setMsg("");setPagina(nova);}

 async function enviar(){
  if(!resposta.trim())return setMsg("Escreva a resposta antes de enviar.");
  try{
   await api(`/diario/${sel.idDiario}`,{method:"PUT",body:JSON.stringify({resposta})});
   setMsg("Resposta enviada.");setResposta("");setSel(null);
   carregar(pagina); // recarrega a página em que o profissional está
  }catch(e){setMsg(e.message);}
 }

 return <Tela fundo={FUNDOS.suave} voltar="homePro" onNavegar={onNavegar} titulo="Relatos">
  {itens.map(r=><button key={r.idDiario} className={`${s.card} ${sel?.idDiario===r.idDiario?s.cardSel:""}`} style={{border:0,cursor:"pointer",font:"inherit",textAlign:"left"}} onClick={()=>setSel(r)}><small>{r.data} · {r.paciente||"Paciente"}</small><p>{r.texto}</p>{r.resposta&&<small>Respondido</small>}</button>)}
  <Paginacao paginacao={meta} onMudar={mudarPagina} desabilitado={carregando}/>
  {sel&&<><p className={s.texto}>Responder relato selecionado</p><textarea className={s.card} style={{border:0,minHeight:120,font:"inherit",textAlign:"left"}} placeholder="Escreva sua resposta..." value={resposta} onChange={e=>setResposta(e.target.value)}/><button className={s.botao} onClick={enviar}>enviar resposta</button></>}
  {msg&&<p role="status">{msg}</p>}
  {!itens.length&&!msg&&!carregando&&<p className={s.vazio}>Nenhum relato enviado.</p>}
 </Tela>;
}
export default Relatos;
