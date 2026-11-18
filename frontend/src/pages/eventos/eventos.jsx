import {useEffect,useState} from "react";
import Tela from "../../componentes/tela/tela";
import Paginacao from "../../componentes/paginacao/paginacao";
import {api} from "../../servicos/api";
import {FUNDOS} from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

const POR_PAGINA = 3;

function Eventos({onNavegar,voltar}){
 const [eventos,setEventos]=useState([]),[meta,setMeta]=useState(null),[pagina,setPagina]=useState(1),[aberto,setAberto]=useState(null),[erro,setErro]=useState("");
 // enquanto a página pedida ainda não chegou da API
 const carregando = !erro && meta?.pag !== pagina;

 useEffect(()=>{
  let ativo=true;
  api(`/evento?pag=${pagina}&por_pagina=${POR_PAGINA}`)
   .then(r=>{if(!ativo)return;setEventos(r.itens||[]);setMeta(r.paginacao||null);setErro("");})
   .catch(e=>{if(ativo)setErro(e.message);});
  return ()=>{ativo=false;};
 },[pagina]);

 function mudarPagina(nova){setAberto(null);setPagina(nova);}

 return <Tela fundo={FUNDOS.roxo} voltar={voltar} onNavegar={onNavegar} titulo="Eventos">
  {erro&&<p>{erro}</p>}
  {eventos.map(ev=><button key={ev.idEvento} className={s.card} style={{border:0,cursor:"pointer",font:"inherit",fontSize:18}} aria-expanded={aberto===ev.idEvento} onClick={()=>setAberto(aberto===ev.idEvento?null:ev.idEvento)}>
   {ev.tema} - {new Date(`${ev.data}T12:00:00`).toLocaleDateString("pt-BR")} <span style={{color:"#666"}}>{aberto===ev.idEvento?"⌃":"⌄"}</span>
   {aberto===ev.idEvento&&<p className={s.texto} style={{marginTop:10,color:"#444",fontSize:15}}>{ev.descricao}</p>}</button>)}
  {!eventos.length&&!erro&&!carregando&&<p className={s.vazio}>Nenhum evento cadastrado.</p>}
  <Paginacao paginacao={meta} onMudar={mudarPagina} desabilitado={carregando}/>
 </Tela>;
}
export default Eventos;
