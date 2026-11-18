const BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:5000/api";
export const token = () => localStorage.getItem("triad_token");
export function sairApi(){ localStorage.removeItem("triad_token"); localStorage.removeItem("triad_usuario"); }

export async function api(path, options = {}) {
  const headers = {
    "Content-Type": "application/json",
    ...(token() ? {Authorization: `Bearer ${token()}`} : {}),
    ...(options.headers || {})
  };
  const res = await fetch(`${BASE}${path}`, {...options, headers});
  const corpo = await res.text();
  let data = {};
  if (corpo) {
    try {
      data = JSON.parse(corpo);
    } catch {
      const detalhe = corpo.replace(/\s+/g, " ").slice(0, 180);
      throw new Error(`O servidor respondeu em formato inesperado (HTTP ${res.status}). ${detalhe}`);
    }
  }
  if (!res.ok) throw new Error(data.message || `Não foi possível concluir a operação (HTTP ${res.status}).`);
  return data;
}

export async function cadastrar(dados){return api("/auth/register",{method:"POST",body:JSON.stringify(dados)});}
export async function entrar(login,senha){
 const r=await api("/auth/login",{method:"POST",body:JSON.stringify({login,senha})});
 localStorage.setItem("triad_token",r.access_token);localStorage.setItem("triad_usuario",JSON.stringify(r.usuario));return r.usuario;
}
