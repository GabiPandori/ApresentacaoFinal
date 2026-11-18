import { useEffect, useState } from "react";
import Tela from "../../componentes/tela/tela";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

const mmss = (t) => `${String(Math.floor(t / 60)).padStart(2, "0")}:${String(t % 60).padStart(2, "0")}`;

function Meditacao({ onNavegar }) {
  const [min, setMin] = useState(5);
  const [resta, setResta] = useState(300);
  const [rodando, setRodando] = useState(false);

  useEffect(() => {
    if (!rodando) return;
    if (resta <= 0) { setRodando(false); return; }
    const t = setTimeout(() => setResta(resta - 1), 1000);
    return () => clearTimeout(t);
  }, [rodando, resta]);

  function escolher(m) { setMin(m); setResta(m * 60); setRodando(false); }

  return (
    <Tela fundo={FUNDOS.amarelo} voltar="tecnicas" onNavegar={onNavegar} titulo="Meditação">
      <p className={s.texto} style={{ marginBottom: 20 }}>Sente-se com a coluna confortável, feche os olhos e leve a atenção para a respiração. Quando a mente divagar, volte com gentileza.</p>
      <div style={{ display: "flex", gap: 10, marginBottom: 20 }}>
        {[3, 5, 10].map((m) => <button key={m} className={s.botao} style={{ width: "auto", padding: "10px 18px", outline: m === min ? "2px solid #161616" : "none" }} onClick={() => escolher(m)}>{m} min</button>)}
      </div>
      <div style={{ fontSize: 64, margin: "12px 0 24px" }} aria-live="off">{mmss(resta)}</div>
      <button className={`${s.botao} ${s.botaoAuto}`} onClick={() => (resta <= 0 ? escolher(min) : setRodando(!rodando))}>{resta <= 0 ? "reiniciar" : rodando ? "pausar" : "iniciar"}</button>
    </Tela>
  );
}
export default Meditacao;
