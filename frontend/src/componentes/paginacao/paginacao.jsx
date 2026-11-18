import s from "./paginacao.module.css";

function Paginacao({ paginacao, onMudar, desabilitado = false }) {
  if (!paginacao || paginacao.total_paginas <= 1) return null;
  const { pag, total_paginas, total } = paginacao;

  return (
    <nav className={s.nav} aria-label="Paginação">
      <button className={s.botao} onClick={() => onMudar(pag - 1)} disabled={desabilitado || pag <= 1}>
        ‹ anterior
      </button>
      <span className={s.info} aria-live="polite">
        página {pag} de {total_paginas}
        <small className={s.total}>{total} registros</small>
      </span>
      <button className={s.botao} onClick={() => onMudar(pag + 1)} disabled={desabilitado || pag >= total_paginas}>
        próxima ›
      </button>
    </nav>
  );
}

export default Paginacao;
