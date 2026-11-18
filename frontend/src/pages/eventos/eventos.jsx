import {useEffect,useState} from "react";
import Tela from "../../componentes/tela/tela";
import {api} from "../../servicos/api";
import {FUNDOS} from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";
function Eventos({onNavegar,voltar}){
 const [eventos,setEventos]=useState([]),[aberto,setAberto]=useState(null),[erro,setErro]=useState("");
 useEffect(()=>{api("/evento?pag=1&por_pagina=30").then(r=>setEventos(r.itens||[])).catch(e=>setErro(e.message));},[]);
 return <Tela fundo={FUNDOS.roxo} voltar={voltar} onNavegar={onNavegar} titulo="Eventos">
 {erro&&<p>{erro}</p>}{eventos.map(ev=><button key={ev.idEvento} className={s.card} style={{border:0,cursor:"pointer",font:"inherit",fontSize:18}} aria-expanded={aberto===ev.idEvento} onClick={()=>setAberto(aberto===ev.idEvento?null:ev.idEvento)}>
 {ev.tema} - {new Date(`${ev.data}T12:00:00`).toLocaleDateString("pt-BR")} <span style={{color:"#666"}}>{aberto===ev.idEvento?"⌃":"⌄"}</span>
 {aberto===ev.idEvento&&<p className={s.texto} style={{marginTop:10,color:"#444",fontSize:15}}>{ev.descricao}</p>}</button>)}
 {!eventos.length&&!erro&&<p className={s.vazio}>Nenhum evento cadastrado.</p>}
 </Tela>;
}
export default Eventos;
