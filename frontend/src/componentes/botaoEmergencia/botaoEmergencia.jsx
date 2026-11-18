import s from "../../estilos/comum.module.css";

function BotaoEmergencia({ onNavegar }) {
  return (
    <button className={s.botao} style={{ color: "#e02b2b", fontWeight: 600 }} onClick={() => onNavegar("emergencia")}>
      Contato de Emergência
    </button>
  );
}
export default BotaoEmergencia;
