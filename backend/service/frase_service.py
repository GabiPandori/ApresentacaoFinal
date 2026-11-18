from datetime import date
from service.erros import ErroValidacao
from repository.frase_repository import FraseRepository


class FraseService:
    def __init__(self):
        self.repo = FraseRepository()

    def obter(self, data_str=None):
        try:
            dia = date.fromisoformat(data_str) if data_str else date.today()
        except ValueError:
            raise ErroValidacao("Data inválida (use AAAA-MM-DD).")
        return self.repo.obter(dia)
