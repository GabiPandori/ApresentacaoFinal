// Armazenamento local (localStorage). Para ligar ao banco, troque estas funções por chamadas a uma API.
export function ler(chave, padrao) {
  try { return JSON.parse(localStorage.getItem(chave)) ?? padrao; } catch { return padrao; }
}
export function salvar(chave, valor) {
  localStorage.setItem(chave, JSON.stringify(valor));
}
export function cadastrar(usuario) {
  const lista = ler("triad_usuarios", []);
  if (lista.some((u) => u.email === usuario.email || u.telefone === usuario.telefone)) return null;
  salvar("triad_usuarios", [...lista, usuario]);
  return usuario;
}
export function entrar(login, senha) {
  return ler("triad_usuarios", []).find((u) => (u.email === login || u.telefone === login) && u.senha === senha) || null;
}
