# TRIAD — API Flask + React

Projeto de inteligência emocional (IFSP Bragança Paulista — Amanda e Gabriela, 3º info).
Bim 4 — Autenticação, relacionamentos, paginação e implantação na nuvem.

## Estrutura
- `frontend/`: React + Vite.
- `backend/`: Flask + SQLAlchemy em camadas: `routes` → `service` → `repository` → `dao` → `model`.
- `backend/schema.sql`: estrutura equivalente em MySQL (opcional; o app também cria as tabelas sozinho).
- `backend/testes.http`: coleção de testes (extensão REST Client do VS Code).

## Relacionamentos (MySQL)
- **1:N** `Paciente → Diario` (cria, lista, edita e exclui relatos do paciente)
- **1:N** `Profissional → Diario` (profissional responde relatos; a resposta guarda a FK e o nome aparece na listagem)
- **N:N** `Paciente ↔ Tecnica` pela tabela `PacienteTecnica` (registrar uso, listar com dados da técnica, remover, e `GET /api/paciente/<id>/resumo`)

## Autenticação e segurança
- `POST /api/auth/register` e `POST /api/auth/login` (JWT, validade de 8 h).
- Senhas gravadas com **hash bcrypt**.
- Todas as rotas, exceto cadastro, login e health, exigem `Authorization: Bearer <token>`.
- Paciente só acessa os próprios dados; rascunhos do diário são privados; profissional só vê relatos enviados.

## Paginação
`?pag=1&por_pagina=10` (máx. 50) em diário, eventos, livros, técnicas e técnicas do paciente. Resposta:
```json
{ "itens": [...], "paginacao": { "total": 25, "pag": 1, "por_pagina": 10, "total_paginas": 3 } }
```

## Endpoints
| Método | Rota | Observação |
|---|---|---|
| GET | `/api/health`, `/api/health/db` | públicas |
| POST | `/api/auth/register`, `/api/auth/login` | públicas |
| GET | `/api/auth/me` | JWT |
| GET/POST | `/api/diario` | lista paginada / cria relato |
| GET/PUT/DELETE | `/api/diario/<id>` | PUT: paciente edita, profissional responde |
| GET | `/api/paciente/<id>/resumo` | relatos (1:N) + técnicas (N:N) |
| GET | `/api/tecnica` | paginado |
| GET/POST | `/api/paciente-tecnica` | N:N: lista / registra |
| DELETE | `/api/paciente-tecnica/<id>` | remove registro |
| GET | `/api/evento`, `/api/livro` | paginados |
| GET | `/api/frase?data=AAAA-MM-DD` | frase do dia |

## Rodar localmente
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate        # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env        # Linux/macOS: cp .env.example .env
python app.py
```
Sem `DATABASE_URL` usa SQLite local. Front: `cd frontend && npm install && copy .env.example .env && npm run dev`.

## Deploy
1. **MySQL no Aiven**: crie o serviço, copie host, porta, usuário e senha e crie o banco `triad` (ou use o `defaultdb`).
2. **API no Render** (Web Service, *Root Directory* = `backend`):
   - Build: `pip install -r requirements.txt`  |  Start: `gunicorn app:app`
   - Variáveis: `DATABASE_URL=mysql+pymysql://USUARIO:SENHA@HOST:PORTA/NOME_BANCO`, `JWT_SECRET_KEY=<chave longa aleatória>`, `FRONTEND_ORIGIN=<URL do front>`.
   - Na primeira subida as tabelas e os dados iniciais são criados automaticamente.
3. Teste `https://SEU-APP.onrender.com/api/health` e `/api/health/db`, depois rode o `testes.http` trocando o `@base`.
4. **Front** (Vercel/Netlify): `VITE_API_URL=https://SEU-APP.onrender.com/api`.

Nunca envie o `.env` ao GitHub (já está no `.gitignore`).
