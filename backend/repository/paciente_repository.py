from dao.PacienteDao import PacienteDao
from dao.DiarioDao import DiarioDao
from dao.PacienteTecnicaDao import PacienteTecnicaDao
from repository.serializers import serializar


class PacienteRepository:
    def criar(self, **dados): return PacienteDao.criar(**dados)
    def obter(self, idPaciente): return PacienteDao.obter(idPaciente)
    def obter_por_login(self, login): return PacienteDao.obter_por_login(login)
    def existe(self, email, telefone): return PacienteDao.existe(email, telefone)

    def resumo(self, paciente):
        """Paciente + dados relacionados: total de relatos (1:N) e técnicas usadas (N:N)."""
        tecnicas = [{**serializar(t), "vezes_utilizada": qtd, "ultima_utilizacao": ultima.isoformat() if ultima else None}
                    for t, qtd, ultima in PacienteTecnicaDao.resumo_por_paciente(paciente.idPaciente)]
        return {"paciente": serializar(paciente),
                "total_relatos": DiarioDao.contar_por_paciente(paciente.idPaciente),
                "tecnicas_utilizadas": tecnicas}
