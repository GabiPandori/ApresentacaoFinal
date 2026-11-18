import Tela from "../../componentes/tela/tela";
import { FUNDOS } from "../../estilos/fundos";
import s from "../../estilos/comum.module.css";

const DADOS = {
  aterramento: { titulo: "Técnicas de Aterramento", intro: "Para voltar ao momento presente quando a ansiedade apertar. Faça a técnica 5-4-3-2-1 usando os sentidos:",
    itens: [["5 coisas que você vê", "Olhe ao redor e nomeie cinco objetos."], ["4 coisas que você toca", "Sinta a textura da roupa, da cadeira, do chão."], ["3 sons que você ouve", "Preste atenção nos sons perto e longe."], ["2 cheiros que você sente", "Ou lembre de dois cheiros de que você gosta."], ["1 gosto", "Perceba o gosto na boca ou beba um gole de água."]] },
  alongamentos: { titulo: "Alongamentos", intro: "Segure cada alongamento por 20 a 30 segundos, sem dor, respirando devagar.",
    itens: [["Pescoço", "Incline a cabeça para um lado, ouvido em direção ao ombro, e troque."], ["Ombros", "Leve um braço cruzado na frente do peito e puxe com a outra mão."], ["Costas", "Sentado, entrelace as mãos, estenda os braços à frente e arredonde as costas."], ["Pernas", "Em pé, segure o pé atrás do corpo, joelhos próximos, e troque de lado."]] },
  calistenia: { titulo: "Calistenia", intro: "Exercícios com o peso do corpo. Comece leve e respeite seus limites; pare se sentir dor.",
    itens: [["Agachamento", "3 séries de 10 repetições."], ["Flexão inclinada (mãos no sofá ou na parede)", "3 séries de 8 repetições."], ["Prancha", "3 vezes de 20 segundos."], ["Polichinelo", "3 séries de 20 repetições."]] },
};

function Lista({ tipo, onNavegar }) {
  const d = DADOS[tipo];
  return (
    <Tela fundo={FUNDOS.amarelo} voltar="tecnicas" onNavegar={onNavegar} titulo={d.titulo}>
      <p className={s.texto} style={{ marginBottom: 18 }}>{d.intro}</p>
      {d.itens.map(([t, txt]) => (
        <div key={t} className={s.card} style={{ textAlign: "left" }}><strong>{t}</strong><br />{txt}</div>
      ))}
    </Tela>
  );
}
export default Lista;
