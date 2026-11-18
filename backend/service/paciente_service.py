from service.erros import ErroNaoEncontrado, ErroProibido
from repository.paciente_repository import PacienteRepository


class PacienteService:
    def __init__(self):
        self.repo = PacienteRepository()

    def resumo(self, usuario, idPaciente):
        if not (usuario["tipo"] == "profissional" or usuario["id"] == idPaciente):
            raise ErroProibido("Acesso negado.")
        paciente = self.repo.obter(idPaciente)
        if not paciente:
            raise ErroNaoEncontrado("Paciente não encontrado.")
        return self.repo.resumo(paciente)
