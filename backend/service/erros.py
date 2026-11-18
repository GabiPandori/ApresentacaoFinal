class ErroServico(Exception):
    status = 400

    def __init__(self, mensagem, status=None):
        super().__init__(mensagem)
        self.mensagem = mensagem
        if status:
            self.status = status


class ErroValidacao(ErroServico):
    status = 400


class ErroNaoAutenticado(ErroServico):
    status = 401


class ErroProibido(ErroServico):
    status = 403


class ErroNaoEncontrado(ErroServico):
    status = 404


class ErroConflito(ErroServico):
    status = 409
