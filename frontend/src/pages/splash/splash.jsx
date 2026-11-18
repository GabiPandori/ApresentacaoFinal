import { useEffect } from "react";
import Tela from "../../componentes/tela/tela";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

function Splash({ onNavegar }) {
  useEffect(() => {
    const t = setTimeout(() => onNavegar("inicio"), 2600);
    return () => clearTimeout(t);
  }, [onNavegar]);
  return (
    <Tela fundo={FUNDOS.arcoiris} centro>
      <h1 className={s.splash}>Triad</h1>
    </Tela>
  );
}
export default Splash;
