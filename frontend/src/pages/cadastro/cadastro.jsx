import {useState} from "react";
import Tela from "../../componentes/tela/tela";
import CampoTexto from "../../componentes/campoTexto/campoTexto";
import {cadastrar} from "../../servicos/api";
import {FUNDOS} from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";
const GENEROS=["Feminino","Masculino","Não binário","Prefiro não informar"];
const CAMPOS={paciente:[["nome","Nome:"],["telefone","Telefone:","tel"],["dataNasc","Data de nascimento:","date"],["email","Email:","email"],["genero","Gênero:","select"],["senha","Senha:","password"]],profissional:[["nome","Nome:"],["telefone","Telefone:","tel"],["dataNasc","Data de nascimento:","date"],["email","Email:","email"],["genero","Gênero:","select"],["documentoCip","Documento CIP:"],["senha","Senha:","password"]]};
function Cadastro({tipo,onNavegar,onEntrar}){
 const campos=CAMPOS[tipo], [form,setForm]=useState(Object.fromEntries(campos.map(([k])=>[k,""]))),[erro,setErro]=useState(""),[busy,setBusy]=useState(false);
 async function enviar(){setErro("");if(Object.values(form).some(v=>!String(v).trim())){setErro("Preencha todos os campos.");return;}setBusy(true);try{await cadastrar({...form,tipo});onNavegar("login");}catch(e){setErro(e.message);}finally{setBusy(false);}}
 return <Tela fundo={FUNDOS.arcoiris} voltar="escolha" onNavegar={onNavegar} titulo="Cadastro">
 {campos.map(([k,label,type])=><CampoTexto key={k} label={label} type={type==="select"?"text":type} opcoes={type==="select"?GENEROS:undefined} value={form[k]} onChange={e=>setForm({...form,[k]:e.target.value})}/> )}
 {erro&&<p role="alert" className={s.vazio}>{erro}</p>}
 <button disabled={busy} className={`${s.botao} ${s.botaoAuto}`} onClick={enviar}>{busy?"cadastrando...":"cadastrar"}</button>
 <button className={s.link} onClick={()=>onNavegar("login")}>já tenho conta</button>
 </Tela>;
}
export default Cadastro;
