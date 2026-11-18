import {useEffect,useState} from "react";
import Tela from "../../componentes/tela/tela";
import {api} from "../../servicos/api";
import {FUNDOS} from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";
const fmt=d=>d.toLocaleDateString("pt-BR",{day:"2-digit",month:"2-digit",year:"numeric"});
function Frase({onNavegar}){
 const [data,setData]=useState(new Date()),[frase,setFrase]=useState(""),[erro,setErro]=useState("");
 useEffect(()=>{api(`/frase?data=${data.toISOString().slice(0,10)}`).then(r=>setFrase(r.frase?.frase||"Uma pequena atitude de cuidado também importa.")).catch(e=>setErro(e.message));},[data]);
 const mover=n=>setData(d=>new Date(d.getTime()+n*86400000));
 const seta={background:"#6b6262",color:"white",border:0,borderRadius:"50%",width:44,height:44,fontSize:22,cursor:"pointer"};
 return <Tela fundo={FUNDOS.rosa} voltar="home" onNavegar={onNavegar} titulo={fmt(data)}>
 <div style={{display:"flex",justifyContent:"space-between",width:"100%",alignItems:"center"}}><span><button style={seta} onClick={()=>mover(-1)}>‹</button><br/>{fmt(new Date(data.getTime()-86400000))}</span><span><button style={seta} onClick={()=>mover(1)}>›</button><br/>{fmt(new Date(data.getTime()+86400000))}</span></div>
 <div className={s.card} style={{marginTop:24,minHeight:260,display:"flex",alignItems:"center",justifyContent:"center",fontSize:24}}>{erro||frase}</div>
 </Tela>;
}
export default Frase;
