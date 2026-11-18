import Tela from "../../componentes/tela/tela";
import CardMenu from "../../componentes/cardMenu/cardMenu";
import { FUNDOS } from "../../estilos/fundos";

const itens = [
  { label: "Analisar relatos", tela: "relatos", cor: "#ffb3b3" },
  { label: "Livro do mês", tela: "livro", cor: "#c4ff6b" },
  { label: "Eventos", tela: "eventos", cor: "#c86bea" },
];

function HomePro({ onNavegar, onSair }) {
  return (
    <Tela fundo={FUNDOS.suave} titulo="Funcionalidades">
      {itens.map((i) => <CardMenu key={i.tela} {...i} onClick={() => onNavegar(i.tela)} />)}
      <button style={{ background: "none", border: "none", textDecoration: "underline", cursor: "pointer" }} onClick={onSair}>sair</button>
    </Tela>
  );
}
export default HomePro;
