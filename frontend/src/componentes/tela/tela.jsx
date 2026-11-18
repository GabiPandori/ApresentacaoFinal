import s from "../../estilos/comum.module.css";

function Tela({ fundo, titulo, voltar, onNavegar, centro, children }) {
  return (
    <div className={s.tela} style={{ background: fundo }}>
      <div className={`${s.col} ${centro ? s.centro : ""}`}>
        {voltar && <button className={s.voltar} onClick={() => onNavegar(voltar)}>← voltar</button>}
        {titulo && <h1 className={s.titulo}>{titulo}</h1>}
        {children}
      </div>
    </div>
  );
}
export default Tela;
