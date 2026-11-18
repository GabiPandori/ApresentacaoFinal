from sqlalchemy import select, desc, func
from sqlalchemy.orm import selectinload
from service.db_service import db
from model.entities import Diario
from dao.paginacao import paginar


class DiarioDao:
    @staticmethod
    def criar(idPaciente, texto, data, enviado=False):
        item = Diario(idPaciente=idPaciente, texto=texto, data=data, enviado=enviado)
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def obter(idDiario):
        return db.session.get(Diario, idDiario)

    @staticmethod
    def listar(pag, por_pagina, idPaciente=None, enviado=None):
        # selectinload carrega paciente e profissional (relacionamentos 1:N) sem N+1 consultas
        q = (select(Diario)
             .options(selectinload(Diario.paciente), selectinload(Diario.profissional))
             .order_by(desc(Diario.data), desc(Diario.idDiario)))
        if idPaciente is not None:
            q = q.where(Diario.idPaciente == idPaciente)
        if enviado is not None:
            q = q.where(Diario.enviado == enviado)
        return paginar(q, pag, por_pagina)

    @staticmethod
    def contar_por_paciente(idPaciente):
        return db.session.scalar(select(func.count()).select_from(Diario).where(Diario.idPaciente == idPaciente)) or 0

    @staticmethod
    def atualizar(item, **campos):
        for chave, valor in campos.items():
            setattr(item, chave, valor)
        db.session.commit()
        return item

    @staticmethod
    def excluir(item):
        db.session.delete(item)
        db.session.commit()
