import { useState } from "react";
import styles from "./campoTexto.module.css";

// Com `opcoes` vira um select; type="date" mostra o rótulo até receber foco.
function CampoTexto({ label, type = "text", value, onChange, opcoes }) {
  const [foco, setFoco] = useState(false);
  if (opcoes) {
    return (
      <select className={styles["campo-texto"]} value={value} onChange={onChange} style={{ color: value ? "#161616" : "#757575" }}>
        <option value="">{label}</option>
        {opcoes.map((o) => <option key={o} value={o}>{o}</option>)}
      </select>
    );
  }
  const tipo = type === "date" && !foco && !value ? "text" : type;
  return (
    <input
      className={styles["campo-texto"]}
      type={tipo}
      placeholder={label}
      aria-label={label}
      value={value}
      onChange={onChange}
      onFocus={() => setFoco(true)}
      onBlur={() => setFoco(false)}
    />
  );
}
export default CampoTexto;
