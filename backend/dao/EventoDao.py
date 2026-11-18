from sqlalchemy import select
from model.entities import Evento
from dao.paginacao import paginar


class EventoDao:
    @staticmethod
    def listar(pag, por_pagina):
        return paginar(select(Evento).order_by(Evento.data), pag, por_pagina)
