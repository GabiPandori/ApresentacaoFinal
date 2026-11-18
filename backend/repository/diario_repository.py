from dao.DiarioDao import DiarioDao
from repository.serializers import montar_pagina


class DiarioRepository:
    def criar(self, idPaciente, texto, data, enviado=False): return DiarioDao.criar(idPaciente, texto, data, enviado)
    def obter(self, idDiario): return DiarioDao.obter(idDiario)
    def atualizar(self, item, **campos): return DiarioDao.atualizar(item, **campos)
    def excluir(self, item): return DiarioDao.excluir(item)

    def listar(self, pag, por_pagina, idPaciente=None, enviado=None):
        return montar_pagina(DiarioDao.listar(pag, por_pagina, idPaciente, enviado), pag, por_pagina)
