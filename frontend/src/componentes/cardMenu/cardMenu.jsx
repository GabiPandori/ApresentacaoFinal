import styles from "./cardMenu.module.css";

function CardMenu({ icone, label, onClick, cor = "#ffb3b3" }) {
  return (
    <button className={styles["card-menu"]} style={{ boxShadow: `6px 6px 0 ${cor}` }} onClick={onClick}>
      {icone && <span className={styles["card-menu-icone"]}>{icone}</span>}
      <span className={styles["card-menu-label"]}>{label}</span>
    </button>
  );
}
export default CardMenu;
