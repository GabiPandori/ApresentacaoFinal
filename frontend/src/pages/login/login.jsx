import { useState } from "react";
import Tela from "../../componentes/tela/tela";
import CampoTexto from "../../componentes/campoTexto/campoTexto";
import { entrar } from "../../servicos/api";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";
function Login({onNavegar,onEntrar}) {
 const [form,setForm]=useState({login:"",senha:""}); const [erro,setErro]=useState(""); const [busy,setBusy]=useState(false);
 async function enviar(){setErro("");if(!form.login||!form.senha){setErro("Preencha todos os campos.");return;}setBusy(true);try{onEntrar(await entrar(form.login.trim(),form.senha));}catch(e){setErro(e.message);}finally{setBusy(false);}}
 return <Tela fundo={FUNDOS.arcoiris} voltar="inicio" onNavegar={onNavegar} titulo="Login">
  <div className={s.icone}>👤</div>
  <CampoTexto label="Telefone/Email:" value={form.login} onChange={e=>setForm({...form,login:e.target.value})}/>
  <CampoTexto label="Senha:" type="password" value={form.senha} onChange={e=>setForm({...form,senha:e.target.value})}/>
  {erro&&<p role="alert" className={s.vazio}>{erro}</p>}
  <button disabled={busy} className={`${s.botao} ${s.botaoAuto}`} onClick={enviar}>{busy?"entrando...":"entrar"}</button>
  <button className={s.link} onClick={()=>onNavegar("escolha")}>cadastrar-se</button>
 </Tela>;
}
export default Login;
