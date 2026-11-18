from datetime import date
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from service.db_service import db
from service.erros import ErroValidacao, ErroNaoAutenticado, ErroConflito, ErroNaoEncontrado
from repository.paciente_repository import PacienteRepository
from repository.profissional_repository import ProfissionalRepository
from repository.serializers import serializar


bcrypt = Bcrypt()


class AuthService:
    def __init__(self):
        self.pacientes = PacienteRepository()
        self.profissionais = ProfissionalRepository()

    def registrar(self, dados):
        dados = dados or {}
        tipo = dados.get("tipo", "paciente")
        if tipo not in ("paciente", "profissional"):
            raise ErroValidacao("Tipo de usuário inválido.")
        if any(not str(dados.get(c, "")).strip() for c in ("nome", "telefone", "genero", "email", "senha")):
            raise ErroValidacao("Preencha todos os campos obrigatórios.")
        if tipo == "profissional" and not str(dados.get("documentoCip", "")).strip():
            raise ErroValidacao("Informe o documento CIP.")
        email = dados["email"].strip().lower()
        if "@" not in email:
            raise ErroValidacao("E-mail inválido.")
        if len(dados["senha"]) < 6:
            raise ErroValidacao("A senha deve ter pelo menos 6 caracteres.")
        try:
            nasc = date.fromisoformat(dados["dataNasc"]) if dados.get("dataNasc") else None
        except ValueError:
            raise ErroValidacao("Data de nascimento inválida.")

        telefone = dados["telefone"].strip()
        base = dict(nome=dados["nome"].strip(), telefone=telefone, dataNasc=nasc,
                    genero=dados["genero"], email=email,
                    senha=bcrypt.generate_password_hash(dados["senha"]).decode("utf-8"))  # hash bcrypt
        try:
            if tipo == "profissional":
                cip = dados["documentoCip"].strip()
                if self.profissionais.existe(email, telefone, cip):
                    raise ErroConflito("E-mail, telefone ou documento já cadastrado.")
                usuario = self.profissionais.criar(documentoCip=cip, **base)
            else:
                if self.pacientes.existe(email, telefone):
                    raise ErroConflito("E-mail ou telefone já cadastrado.")
                usuario = self.pacientes.criar(**base)
        except IntegrityError:
            db.session.rollback()
            raise ErroConflito("E-mail, telefone ou documento já cadastrado.")
        return serializar(usuario)

    def login(self, dados):
        dados = dados or {}
        login = str(dados.get("login", "")).strip().lower()
        senha = dados.get("senha", "")
        if not login or not senha:
            raise ErroValidacao("Informe telefone/e-mail e senha.")
        for tipo, repo, campo in (("paciente", self.pacientes, "idPaciente"),
                                  ("profissional", self.profissionais, "idProfissional")):
            usuario = repo.obter_por_login(login)
            if usuario and bcrypt.check_password_hash(usuario.senha, senha):
                token = create_access_token(identity=usuario.email,
                                            additional_claims={"tipo": tipo, "id": getattr(usuario, campo), "nome": usuario.nome})
                return {"access_token": token, "usuario": serializar(usuario)}
        raise ErroNaoAutenticado("Telefone/e-mail ou senha incorretos.")

    def me(self, usuario):
        repo = self.profissionais if usuario["tipo"] == "profissional" else self.pacientes
        obj = repo.obter(usuario["id"])
        if not obj:
            raise ErroNaoEncontrado("Usuário não encontrado.")
        return serializar(obj)
