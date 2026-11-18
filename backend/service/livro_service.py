from repository.livro_repository import LivroRepository


class LivroService:
    def __init__(self):
        self.repo = LivroRepository()

    def listar(self, pag, por_pagina, mes=None, ano=None):
        return self.repo.listar(pag, por_pagina, mes, ano)
