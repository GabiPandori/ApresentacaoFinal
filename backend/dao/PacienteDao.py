from sqlalchemy import select, or_, func
from service.db_service import db
from model.entities import Paciente


class PacienteDao:
    @staticmethod
    def criar(**dados):
        paciente = Paciente(**dados)
        db.session.add(paciente)
        db.session.commit()
        return paciente

    @staticmethod
    def obter(idPaciente):
        return db.session.get(Paciente, idPaciente)

    @staticmethod
    def obter_por_login(login):
        return db.session.scalar(select(Paciente).where(or_(Paciente.email == login, Paciente.telefone == login)))

    @staticmethod
    def existe(email, telefone):
        return db.session.scalar(select(func.count()).select_from(Paciente).where(or_(Paciente.email == email, Paciente.telefone == telefone))) > 0
