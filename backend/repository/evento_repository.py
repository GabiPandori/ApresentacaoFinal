from dao.EventoDao import EventoDao
from repository.serializers import montar_pagina


class EventoRepository:
    def listar(self, pag, por_pagina):
        return montar_pagina(EventoDao.listar(pag, por_pagina), pag, por_pagina)
