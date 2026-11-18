import { useEffect, useState } from "react";
import Tela from "../../componentes/tela/tela";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

const FASES = [["Inspire", 4], ["Segure", 7], ["Expire", 8]]; // respiração 4-7-8

function Respiracao({ onNavegar }) {
  const [rodando, setRodando] = useState(false);
  const [i, setI] = useState(0);

  useEffect(() => {
    if (!rodando) return;
    const t = setTimeout(() => setI((i + 1) % FASES.length), FASES[i][1] * 1000);
    return () => clearTimeout(t);
  }, [rodando, i]);

  const cheio = rodando && i < 2;
  return (
    <Tela fundo={FUNDOS.amarelo} voltar="tecnicas" onNavegar={onNavegar} titulo="Respiração 4-7-8">
      <p className={s.texto} style={{ marginBottom: 24 }}>Inspire pelo nariz por 4 segundos, segure por 7 e expire devagar pela boca por 8. Repita por alguns ciclos, no seu ritmo.</p>
      <div style={{ width: 220, height: 220, borderRadius: "50%", background: "white", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 24, margin: "16px 0 32px",
        transform: `scale(${cheio ? 1 : 0.6})`, transition: `transform ${rodando ? FASES[i][1] : 0.5}s ease-in-out` }}>
        {rodando ? FASES[i][0] : "Pronto?"}
      </div>
      <button className={`${s.botao} ${s.botaoAuto}`} onClick={() => { setRodando(!rodando); setI(0); }}>{rodando ? "parar" : "começar"}</button>
    </Tela>
  );
}
export default Respiracao;
