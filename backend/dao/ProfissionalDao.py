from sqlalchemy import select, or_, func
from service.db_service import db
from model.entities import Profissional


class ProfissionalDao:
    @staticmethod
    def criar(**dados):
        profissional = Profissional(**dados)
        db.session.add(profissional)
        db.session.commit()
        return profissional

    @staticmethod
    def obter(idProfissional):
        return db.session.get(Profissional, idProfissional)

    @staticmethod
    def obter_por_login(login):
        return db.session.scalar(select(Profissional).where(or_(Profissional.email == login, Profissional.telefone == login)))

    @staticmethod
    def existe(email, telefone, documentoCip):
        return db.session.scalar(select(func.count()).select_from(Profissional).where(
            or_(Profissional.email == email, Profissional.telefone == telefone, Profissional.documentoCip == documentoCip))) > 0
