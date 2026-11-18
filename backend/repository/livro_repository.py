from dao.LivroDao import LivroDao
from repository.serializers import montar_pagina


class LivroRepository:
    def listar(self, pag, por_pagina, mes=None, ano=None):
        return montar_pagina(LivroDao.listar(pag, por_pagina, mes, ano), pag, por_pagina)
