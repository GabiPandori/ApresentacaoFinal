from sqlalchemy import select, desc, func
from sqlalchemy.orm import selectinload
from service.db_service import db
from model.entities import PacienteTecnica, Tecnica
from dao.paginacao import paginar


class PacienteTecnicaDao:
    @staticmethod
    def criar(idPaciente, idTecnica):
        item = PacienteTecnica(idPaciente=idPaciente, idTecnica=idTecnica)
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def obter(idPacienteTecnica):
        return db.session.get(PacienteTecnica, idPacienteTecnica)

    @staticmethod
    def listar_por_paciente(idPaciente, pag, por_pagina):
        q = (select(PacienteTecnica)
             .options(selectinload(PacienteTecnica.tecnica))
             .where(PacienteTecnica.idPaciente == idPaciente)
             .order_by(desc(PacienteTecnica.dataUtilizacao), desc(PacienteTecnica.idPacienteTecnica)))
        return paginar(q, pag, por_pagina)

    @staticmethod
    def resumo_por_paciente(idPaciente):
        """Quantas vezes o paciente usou cada técnica (JOIN N:N)."""
        q = (select(Tecnica, func.count(PacienteTecnica.idPacienteTecnica), func.max(PacienteTecnica.dataUtilizacao))
             .join(PacienteTecnica, PacienteTecnica.idTecnica == Tecnica.idTecnica)
             .where(PacienteTecnica.idPaciente == idPaciente)
             .group_by(Tecnica.idTecnica)
             .order_by(Tecnica.idTecnica))
        return db.session.execute(q).all()

    @staticmethod
    def excluir(item):
        db.session.delete(item)
        db.session.commit()
