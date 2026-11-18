from service.erros import ErroValidacao, ErroProibido, ErroNaoEncontrado
from repository.paciente_tecnica_repository import PacienteTecnicaRepository
from repository.tecnica_repository import TecnicaRepository
from repository.paciente_repository import PacienteRepository
from repository.serializers import serializar


class PacienteTecnicaService:
    def __init__(self):
        self.repo = PacienteTecnicaRepository()
        self.tecnicas = TecnicaRepository()
        self.pacientes = PacienteRepository()

    def registrar(self, usuario, dados):
        if usuario["tipo"] != "paciente":
            raise ErroProibido("Apenas pacientes podem registrar técnicas.")
        idTecnica = (dados or {}).get("idTecnica")
        if not isinstance(idTecnica, int):
            raise ErroValidacao("Informe o idTecnica.")
        if not self.tecnicas.obter(idTecnica):
            raise ErroNaoEncontrado("Técnica não encontrada.")
        return serializar(self.repo.criar(usuario["id"], idTecnica))

    def listar(self, usuario, pag, por_pagina, idPaciente=None):
        if usuario["tipo"] == "paciente":
            idPaciente = usuario["id"]
        elif not idPaciente:
            raise ErroValidacao("Informe idPaciente na URL.")
        elif not self.pacientes.obter(idPaciente):
            raise ErroNaoEncontrado("Paciente não encontrado.")
        return self.repo.listar_por_paciente(idPaciente, pag, por_pagina)

    def excluir(self, usuario, idPacienteTecnica):
        item = self.repo.obter(idPacienteTecnica)
        if not item:
            raise ErroNaoEncontrado("Registro não encontrado.")
        if usuario["tipo"] != "paciente" or item.idPaciente != usuario["id"]:
            raise ErroProibido("Acesso negado.")
        self.repo.excluir(item)
