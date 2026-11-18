from sqlalchemy import select, desc
from model.entities import Livro
from dao.paginacao import paginar


class LivroDao:
    @staticmethod
    def listar(pag, por_pagina, mes=None, ano=None):
        q = select(Livro).order_by(desc(Livro.ano), Livro.idLivro)
        if mes:
            q = q.where(Livro.mes == mes)
        if ano:
            q = q.where(Livro.ano == ano)
        return paginar(q, pag, por_pagina)
