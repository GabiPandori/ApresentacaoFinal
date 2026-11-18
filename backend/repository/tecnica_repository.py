from dao.TecnicaDao import TecnicaDao
from repository.serializers import montar_pagina


class TecnicaRepository:
    def obter(self, idTecnica): return TecnicaDao.obter(idTecnica)

    def listar(self, pag, por_pagina):
        return montar_pagina(TecnicaDao.listar(pag, por_pagina), pag, por_pagina)
