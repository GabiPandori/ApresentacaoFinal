from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from routes.helpers import pagina_params
from service.livro_service import LivroService

livro_bp = Blueprint("livro", __name__)
service = LivroService()


@livro_bp.get("")
@jwt_required()
def listar():
    pag, por_pagina = pagina_params()
    resposta = service.listar(pag, por_pagina, request.args.get("mes"), request.args.get("ano", type=int))
    resposta["livros"] = resposta["itens"]
    return jsonify(resposta), 200
