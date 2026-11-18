import {useEffect,useState} from "react";
import Tela from "../../componentes/tela/tela";
import {api} from "../../servicos/api";
import {FUNDOS} from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";
const MESES=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"];
function Livro({onNavegar,voltar}){
 const [mes,setMes]=useState(1),[livros,setLivros]=useState([]),[erro,setErro]=useState("");
 useEffect(()=>{api("/livro").then(r=>setLivros(r.livros||[])).catch(e=>setErro(e.message));},[]);
 const livro=livros.find(x=>x.mes.toLowerCase()===MESES[mes].toLowerCase());
 const seta={background:"#3f5a35",color:"white",border:0,borderRadius:"50%",width:44,height:44,fontSize:22,cursor:"pointer"};
 return <Tela fundo={FUNDOS.verde} voltar={voltar} onNavegar={onNavegar}>
 <div style={{display:"flex",gap:12,alignItems:"center",width:"100%"}}><button style={seta} onClick={()=>setMes((mes+11)%12)}>‹</button><h1 className={s.card} style={{margin:0,padding:14,fontSize:28}}>{MESES[mes]}</h1><button style={seta} onClick={()=>setMes((mes+1)%12)}>›</button></div>
 <div className={s.card} style={{marginTop:24,minHeight:420,display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",gap:20,fontSize:20}}>
 {erro?<p>{erro}</p>:livro?<><p>{livro.titulo}<br/>por<br/>{livro.autor}</p><div style={{width:160,height:240,background:"linear-gradient(160deg,#003a7a,#001c3d)",color:"white",display:"flex",flexDirection:"column",justifyContent:"center",padding:12,fontWeight:600,fontSize:26,lineHeight:1.1}}>{livro.titulo.toUpperCase()}</div></>:<p className={s.vazio}>O livro de {MESES[mes]} ainda não foi definido.</p>}
 </div></Tela>;
}
export default Livro;
