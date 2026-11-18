from datetime import datetime, timezone
from service.db_service import db


def agora_utc():
    return datetime.now(timezone.utc).replace(tzinfo=None)


class Paciente(db.Model):
    __tablename__ = "Paciente"
    idPaciente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(30), unique=True, nullable=False)
    dataNasc = db.Column(db.Date, nullable=True)
    genero = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    # 1:N  Paciente -> Diario
    diarios = db.relationship("Diario", back_populates="paciente", cascade="all, delete-orphan", passive_deletes=True)
    # N:N  Paciente <-> Tecnica (via PacienteTecnica)
    tecnicas = db.relationship("PacienteTecnica", back_populates="paciente", cascade="all, delete-orphan", passive_deletes=True)


class Profissional(db.Model):
    __tablename__ = "Profissional"
    idProfissional = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(30), unique=True, nullable=False)
    dataNasc = db.Column(db.Date, nullable=True)
    genero = db.Column(db.String(40), nullable=False)
    documentoCip = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    # 1:N  Profissional -> Diario (respostas)
    respostas = db.relationship("Diario", back_populates="profissional")


class Diario(db.Model):
    __tablename__ = "Diario"
    idDiario = db.Column(db.Integer, primary_key=True)
    idPaciente = db.Column(db.Integer, db.ForeignKey("Paciente.idPaciente", ondelete="CASCADE"), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    data = db.Column(db.Date, nullable=False)
    enviado = db.Column(db.Boolean, default=False, nullable=False)
    resposta = db.Column(db.Text)
    idProfissionalResposta = db.Column(db.Integer, db.ForeignKey("Profissional.idProfissional", ondelete="SET NULL"), nullable=True)
    dataResposta = db.Column(db.DateTime)
    paciente = db.relationship("Paciente", back_populates="diarios")
    profissional = db.relationship("Profissional", back_populates="respostas")


class Tecnica(db.Model):
    __tablename__ = "Tecnica"
    idTecnica = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    pacientes = db.relationship("PacienteTecnica", back_populates="tecnica", cascade="all, delete-orphan", passive_deletes=True)


class PacienteTecnica(db.Model):
    """Tabela associativa do N:N Paciente <-> Tecnica (guarda cada vez que o paciente usou a técnica)."""
    __tablename__ = "PacienteTecnica"
    idPacienteTecnica = db.Column(db.Integer, primary_key=True)
    idPaciente = db.Column(db.Integer, db.ForeignKey("Paciente.idPaciente", ondelete="CASCADE"), nullable=False)
    idTecnica = db.Column(db.Integer, db.ForeignKey("Tecnica.idTecnica", ondelete="CASCADE"), nullable=False)
    dataUtilizacao = db.Column(db.DateTime, default=agora_utc)
    paciente = db.relationship("Paciente", back_populates="tecnicas")
    tecnica = db.relationship("Tecnica", back_populates="pacientes")


class Evento(db.Model):
    __tablename__ = "Evento"
    idEvento = db.Column(db.Integer, primary_key=True)
    tema = db.Column(db.String(180), nullable=False)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.Text)


class Livro(db.Model):
    __tablename__ = "Livro"
    idLivro = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(180), nullable=False)
    mes = db.Column(db.String(20), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    autor = db.Column(db.String(120), nullable=False)


class FraseDiaria(db.Model):
    __tablename__ = "FraseDiaria"
    idFrase = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, unique=True, nullable=False)
    frase = db.Column(db.String(500), nullable=False)
