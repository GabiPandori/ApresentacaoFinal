import Tela from "../../componentes/tela/tela";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

function Inicio({ onNavegar }) {
  return (
    <Tela fundo={FUNDOS.suave} centro>
      <div className={s.icone}>👤</div>
      <button className={s.botao} onClick={() => onNavegar("login")}>Login</button>
      <button className={s.botao} onClick={() => onNavegar("escolha")}>Cadastro</button>
    </Tela>
  );
}
export default Inicio;
