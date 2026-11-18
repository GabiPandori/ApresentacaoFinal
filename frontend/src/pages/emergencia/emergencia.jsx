import { useState } from "react";
import Tela from "../../componentes/tela/tela";
import CampoTexto from "../../componentes/campoTexto/campoTexto";
import { ler, salvar } from "../../servicos/armazenamento";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

function Emergencia({ onNavegar, voltar }) {
  const [contato, setContato] = useState(() => ler("triad_emergencia", { nome: "", telefone: "" }));
  const tel = contato.telefone.replace(/[^\d+]/g, "");

  return (
    <Tela fundo={FUNDOS.rosa} voltar={voltar} onNavegar={onNavegar} titulo="Contato de emergência">
      <CampoTexto label="Nome:" value={contato.nome} onChange={(e) => setContato({ ...contato, nome: e.target.value })} />
      <CampoTexto label="Telefone:" type="tel" value={contato.telefone} onChange={(e) => setContato({ ...contato, telefone: e.target.value })} />
      <button className={`${s.botao} ${s.botaoAuto}`} onClick={() => { salvar("triad_emergencia", contato); alert("Contato salvo."); }}>salvar</button>
      {tel && <a className={s.botao} style={{ textAlign: "center", textDecoration: "none", color: "#e02b2b", fontWeight: 600 }} href={`tel:${tel}`}>Ligar para {contato.nome || tel}</a>}
      <div className={s.card} style={{ marginTop: 24 }}>
        Precisa de ajuda agora? O CVV atende 24 horas, de graça, pelo <a href="tel:188">188</a>. Em risco imediato, ligue para o SAMU: <a href="tel:192">192</a>.
      </div>
    </Tela>
  );
}
export default Emergencia;
