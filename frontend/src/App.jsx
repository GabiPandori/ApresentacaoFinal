import { useEffect, useState } from "react";
import { api, sairApi, token } from "./servicos/api";
import Splash from "./pages/splash/splash";
import Inicio from "./pages/inicio/inicio";
import Login from "./pages/login/login";
import Escolha from "./pages/escolha/escolha";
import Cadastro from "./pages/cadastro/cadastro";
import Home from "./pages/home/home";
import HomePro from "./pages/homePro/homePro";
import Frase from "./pages/frase/frase";
import Tecnicas from "./pages/tecnicas/tecnicas";
import Respiracao from "./pages/tecnicas/respiracao";
import Meditacao from "./pages/tecnicas/meditacao";
import Lista from "./pages/tecnicas/lista";
import Livro from "./pages/livro/livro";
import Diario from "./pages/diario/diario";
import Eventos from "./pages/eventos/eventos";
import Emergencia from "./pages/emergencia/emergencia";
import Relatos from "./pages/relatos/relatos";

function App() {
  const [tela, setTela] = useState("splash");
  const [usuario, setUsuario] = useState(null);

  useEffect(() => { if (token()) api("/auth/me").then(r => { setUsuario(r.usuario); setTela(r.usuario.tipo === "profissional" ? "homePro" : "home"); }).catch(() => sairApi()); }, []);

  const profissional = usuario?.tipo === "profissional";
  const inicioDoUsuario = profissional ? "homePro" : "home";

  function onEntrar(u) {
    setUsuario(u);
    setTela(u.tipo === "profissional" ? "homePro" : "home");
  }
  function onSair() {
    setUsuario(null);
    setTela("inicio");
  }

  const p = { onNavegar: setTela, usuario, onEntrar, onSair };

  // Telas de uso interno: sem login, volta para o início.
  const protegidas = ["home", "homePro", "frase", "tecnicas", "respiracao", "aterramento", "meditacao", "alongamentos", "calistenia", "livro", "diario", "eventos", "emergencia", "relatos"];
  if (!usuario && protegidas.includes(tela)) return <Inicio {...p} />;

  const telas = {
    splash: <Splash {...p} />,
    inicio: <Inicio {...p} />,
    login: <Login {...p} />,
    escolha: <Escolha {...p} />,
    cadastroPaciente: <Cadastro {...p} tipo="paciente" />,
    cadastroProfissional: <Cadastro {...p} tipo="profissional" />,
    home: <Home {...p} />,
    homePro: <HomePro {...p} />,
    frase: <Frase {...p} />,
    tecnicas: <Tecnicas {...p} />,
    respiracao: <Respiracao {...p} />,
    aterramento: <Lista {...p} tipo="aterramento" />,
    meditacao: <Meditacao {...p} />,
    alongamentos: <Lista {...p} tipo="alongamentos" />,
    calistenia: <Lista {...p} tipo="calistenia" />,
    livro: <Livro {...p} voltar={inicioDoUsuario} />,
    diario: <Diario {...p} />,
    eventos: <Eventos {...p} voltar={inicioDoUsuario} />,
    emergencia: <Emergencia {...p} voltar={profissional ? "homePro" : "tecnicas"} />,
    relatos: <Relatos {...p} />,
  };
  return telas[tela] ?? <Inicio {...p} />;
}

export default App;