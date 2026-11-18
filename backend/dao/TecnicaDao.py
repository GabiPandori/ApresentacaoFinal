from sqlalchemy import select
from service.db_service import db
from model.entities import Tecnica
from dao.paginacao import paginar


class TecnicaDao:
    @staticmethod
    def listar(pag, por_pagina):
        return paginar(select(Tecnica).order_by(Tecnica.idTecnica), pag, por_pagina)

    @staticmethod
    def obter(idTecnica):
        return db.session.get(Tecnica, idTecnica)
