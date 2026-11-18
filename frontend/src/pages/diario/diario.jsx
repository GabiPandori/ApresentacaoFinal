import {useEffect,useState} from "react";
import Tela from "../../componentes/tela/tela";
import BotaoEmergencia from "../../componentes/botaoEmergencia/botaoEmergencia";
import {api} from "../../servicos/api";
import {FUNDOS} from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

const hoje = () => new Date().toISOString().slice(0, 10);

function Diario({onNavegar}) {
  const [data, setData] = useState(hoje());
  const [texto, setTexto] = useState("");
  const [diarioId, setDiarioId] = useState(null);
  const [msg, setMsg] = useState("");
  const [carregando, setCarregando] = useState(false);

  useEffect(() => {
    let ativo = true;
    async function carregar() {
      setCarregando(true);
      setMsg("");
      try {
        const resposta = await api("/diario?pag=1&por_pagina=50");
        const relatos = Array.isArray(resposta.itens) ? resposta.itens : [];
        const item = relatos.find((relato) => relato.data === data);
        if (!ativo) return;
        setTexto(item?.texto || "");
        setDiarioId(item?.idDiario ?? null);
      } catch (erro) {
        if (ativo) {
          setTexto("");
          setDiarioId(null);
          setMsg(erro.message);
        }
      } finally {
        if (ativo) setCarregando(false);
      }
    }
    carregar();
    return () => { ativo = false; };
  }, [data]);

  async function salvar(enviado = false) {
    setMsg("");
    if (!texto.trim()) {
      setMsg("Escreva algo antes de salvar.");
      return;
    }
    try {
      if (diarioId) {
        await api(`/diario/${diarioId}`, {
          method: "PUT",
          body: JSON.stringify({texto: texto.trim(), enviado})
        });
      } else {
        const resposta = await api("/diario", {
          method: "POST",
          body: JSON.stringify({texto: texto.trim(), data, enviado})
        });
        const novoId = resposta.relato?.idDiario ?? resposta.dados?.idDiario ?? resposta.idDiario ?? null;
        setDiarioId(novoId);
      }
      setMsg(enviado ? "Relato enviado ao profissional." : "Relato salvo com sucesso!");
    } catch (erro) {
      setMsg(erro.message);
    }
  }

  async function excluir() {
    if (!diarioId) {
      setMsg("Salve o relato antes de tentar excluí-lo.");
      return;
    }
    if (!window.confirm("Tem certeza de que deseja excluir este relato? Essa ação não poderá ser desfeita.")) return;
    setMsg("");
    try {
      await api(`/diario/${diarioId}`, {method: "DELETE"});
      setTexto("");
      setDiarioId(null);
      setMsg("Relato excluído com sucesso.");
    } catch (erro) {
      setMsg(erro.message);
    }
  }

  return (
    <Tela fundo={FUNDOS.ciano} voltar="home" onNavegar={onNavegar} titulo="Diário">
      <input
        aria-label="Data"
        type="date"
        value={data}
        max={hoje()}
        onChange={(evento) => setData(evento.target.value)}
        style={{alignSelf:"flex-start", border:0, borderRadius:14, padding:"10px 16px", fontSize:15, marginBottom:14}}
      />
      <div className={s.card} style={{padding:20}}>
        <textarea
          aria-label="Relato do dia"
          placeholder="Escreva sobre o seu dia..."
          value={texto}
          onChange={(evento) => setTexto(evento.target.value)}
          disabled={carregando}
          style={{width:"100%", minHeight:320, border:0, outline:0, resize:"vertical", fontSize:16, lineHeight:"32px", background:"repeating-linear-gradient(transparent,transparent 31px,#222 31px,#222 32px)"}}
        />
      </div>
      {msg && <p role="status">{msg}</p>}
      <div style={{display:"flex", gap:10, flexWrap:"wrap", width:"100%"}}>
        <button className={s.botao} onClick={() => salvar(false)} disabled={carregando}>salvar</button>
        <button className={s.botao} onClick={() => salvar(true)} disabled={carregando}>enviar ao profissional</button>
        {diarioId !== null && (
          <button className={s.botao} onClick={excluir} style={{color:"#a32645"}} disabled={carregando}>excluir relato</button>
        )}
      </div>
      <BotaoEmergencia onNavegar={onNavegar}/>
    </Tela>
  );
}

export default Diario;
