from dao.ProfissionalDao import ProfissionalDao


class ProfissionalRepository:
    def criar(self, **dados): return ProfissionalDao.criar(**dados)
    def obter(self, idProfissional): return ProfissionalDao.obter(idProfissional)
    def obter_por_login(self, login): return ProfissionalDao.obter_por_login(login)
    def existe(self, email, telefone, documentoCip): return ProfissionalDao.existe(email, telefone, documentoCip)
