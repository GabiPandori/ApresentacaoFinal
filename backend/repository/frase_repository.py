from dao.FraseDiariaDao import FraseDiariaDao
from repository.serializers import serializar


class FraseRepository:
    def obter(self, data):
        frase = FraseDiariaDao.obter_por_data(data) or FraseDiariaDao.obter_mais_recente()
        return serializar(frase) if frase else None
