from dao.PacienteTecnicaDao import PacienteTecnicaDao
from repository.serializers import montar_pagina


class PacienteTecnicaRepository:
    def criar(self, idPaciente, idTecnica): return PacienteTecnicaDao.criar(idPaciente, idTecnica)
    def obter(self, idPacienteTecnica): return PacienteTecnicaDao.obter(idPacienteTecnica)
    def excluir(self, item): return PacienteTecnicaDao.excluir(item)

    def listar_por_paciente(self, idPaciente, pag, por_pagina):
        return montar_pagina(PacienteTecnicaDao.listar_por_paciente(idPaciente, pag, por_pagina), pag, por_pagina)
