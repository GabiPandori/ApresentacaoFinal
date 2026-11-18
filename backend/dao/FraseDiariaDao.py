from sqlalchemy import select, desc
from service.db_service import db
from model.entities import FraseDiaria


class FraseDiariaDao:
    @staticmethod
    def obter_por_data(data):
        return db.session.scalar(select(FraseDiaria).where(FraseDiaria.data == data))

    @staticmethod
    def obter_mais_recente():
        return db.session.scalar(select(FraseDiaria).order_by(desc(FraseDiaria.data)))
