from flask import request
from flask_jwt_extended import get_jwt
from service.erros import ErroValidacao


def pagina_params(max_por_pagina=50):
    pag = request.args.get("pag", 1, type=int)
    por_pagina = request.args.get("por_pagina", 10, type=int)
    if pag < 1 or por_pagina < 1 or por_pagina > max_por_pagina:
        raise ErroValidacao(f"Use pag >= 1 e por_pagina entre 1 e {max_por_pagina}.")
    return pag, por_pagina


def usuario_atual():
    """Dados do usuário autenticado, lidos do token JWT."""
    claims = get_jwt()
    return {"tipo": claims["tipo"], "id": claims["id"], "nome": claims.get("nome")}
