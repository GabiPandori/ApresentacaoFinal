import Tela from "../../componentes/tela/tela";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

const itens = [["Técnicas de Respiração", "respiracao"], ["Técnicas de Aterramento", "aterramento"], ["Meditação", "meditacao"], ["Alongamentos", "alongamentos"], ["Calistenia", "calistenia"]];

function Tecnicas({ onNavegar }) {
  return (
    <Tela fundo={FUNDOS.amarelo} voltar="home" onNavegar={onNavegar} titulo="Técnicas">
      {itens.map(([label, tela]) => <button key={tela} className={s.botao} style={{ marginBottom: 14 }} onClick={() => onNavegar(tela)}>{label}</button>)}
      <button className={s.botao} style={{ color: "#e02b2b", fontWeight: 600 }} onClick={() => onNavegar("emergencia")}>Contato de Emergência</button>
    </Tela>
  );
}
export default Tecnicas;
