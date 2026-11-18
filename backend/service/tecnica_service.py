from repository.tecnica_repository import TecnicaRepository


class TecnicaService:
    def __init__(self):
        self.repo = TecnicaRepository()

    def listar(self, pag, por_pagina):
        return self.repo.listar(pag, por_pagina)
