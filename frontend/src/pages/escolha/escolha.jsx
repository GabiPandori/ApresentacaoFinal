import Tela from "../../componentes/tela/tela";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

function Escolha({ onNavegar }) {
  return (
    <Tela fundo={FUNDOS.suave} voltar="inicio" onNavegar={onNavegar} centro>
      <div className={s.icone}>👤</div>
      <button className={s.botao} onClick={() => onNavegar("cadastroPaciente")}>Paciente</button>
      <button className={s.botao} onClick={() => onNavegar("cadastroProfissional")}>Profissional</button>
    </Tela>
  );
}
export default Escolha;
