import Tela from "../../componentes/tela/tela";
import CardMenu from "../../componentes/cardMenu/cardMenu";
import { FUNDOS } from "../../estilos/fundos";

const itens = [
  { icone: "💡", label: "Frase do Dia", tela: "frase", cor: "#ffb3b3" },
  { icone: "🧘", label: "Técnicas de aterramento", tela: "tecnicas", cor: "#ffe066" },
  { icone: "📚", label: "Livro do Mês", tela: "livro", cor: "#c4ff6b" },
  { icone: "📔", label: "Diário", tela: "diario", cor: "#38b6ff" },
  { icone: "📅", label: "Eventos", tela: "eventos", cor: "#c86bea" },
];

function Home({ onNavegar, usuario, onSair }) {
  return (
    <Tela fundo={FUNDOS.arcoiris} titulo={`Olá, ${usuario?.nome?.split(" ")[0] ?? ""}`}>
      {itens.map((i) => <CardMenu key={i.tela} {...i} onClick={() => onNavegar(i.tela)} />)}
      <button style={{ background: "none", border: "none", textDecoration: "underline", cursor: "pointer" }} onClick={onSair}>sair</button>
    </Tela>
  );
}
export default Home;
