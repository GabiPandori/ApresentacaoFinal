from repository.evento_repository import EventoRepository


class EventoService:
    def __init__(self):
        self.repo = EventoRepository()

    def listar(self, pag, por_pagina):
        return self.repo.listar(pag, por_pagina)
