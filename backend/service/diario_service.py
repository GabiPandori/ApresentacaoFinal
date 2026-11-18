from datetime import date, datetime, timezone
from service.erros import ErroValidacao, ErroProibido, ErroNaoEncontrado
from repository.diario_repository import DiarioRepository
from repository.serializers import serializar


class DiarioService:
    def __init__(self):
        self.repo = DiarioRepository()

    def _obter_visivel(self, usuario, idDiario):
        item = self.repo.obter(idDiario)
        if not item:
            raise ErroNaoEncontrado("Relato não encontrado.")
        if usuario["tipo"] == "paciente" and item.idPaciente != usuario["id"]:
            raise ErroProibido("Acesso negado.")
        # rascunhos (não enviados) são privados do paciente
        if usuario["tipo"] == "profissional" and not item.enviado:
            raise ErroProibido("Este relato ainda não foi enviado ao profissional.")
        return item

    def criar(self, usuario, dados):
        dados = dados or {}
        if usuario["tipo"] != "paciente":
            raise ErroProibido("Apenas pacientes podem criar relatos.")
        texto = str(dados.get("texto", "")).strip()
        if not texto:
            raise ErroValidacao("Escreva seu relato.")
        try:
            data = date.fromisoformat(dados.get("data") or date.today().isoformat())
        except ValueError:
            raise ErroValidacao("Data inválida (use AAAA-MM-DD).")
        item = self.repo.criar(usuario["id"], texto, data, bool(dados.get("enviado", False)))
        return serializar(item)

    def listar(self, usuario, pag, por_pagina, idPaciente=None, enviado=None):
        if usuario["tipo"] == "paciente":
            idPaciente = usuario["id"]
        else:
            enviado = True  # profissional só enxerga o que foi enviado
        return self.repo.listar(pag, por_pagina, idPaciente, enviado)

    def obter(self, usuario, idDiario):
        return serializar(self._obter_visivel(usuario, idDiario))

    def atualizar(self, usuario, idDiario, dados):
        dados = dados or {}
        item = self._obter_visivel(usuario, idDiario)
        if usuario["tipo"] == "paciente":
            campos = {}
            if "texto" in dados:
                texto = str(dados["texto"]).strip()
                if not texto:
                    raise ErroValidacao("O texto do relato não pode ficar vazio.")
                campos["texto"] = texto
            if "enviado" in dados:
                campos["enviado"] = bool(dados["enviado"])
            if not campos:
                raise ErroValidacao("Nada para atualizar.")
        else:
            resposta = str(dados.get("resposta", "")).strip()
            if not resposta:
                raise ErroValidacao("Escreva uma resposta.")
            campos = {"resposta": resposta, "idProfissionalResposta": usuario["id"],
                      "dataResposta": datetime.now(timezone.utc).replace(tzinfo=None)}
        return serializar(self.repo.atualizar(item, **campos))

    def excluir(self, usuario, idDiario):
        if usuario["tipo"] != "paciente":
            raise ErroProibido("Apenas o paciente pode excluir o próprio relato.")
        self.repo.excluir(self._obter_visivel(usuario, idDiario))
