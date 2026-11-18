from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from routes.helpers import pagina_params
from service.tecnica_service import TecnicaService

tecnica_bp = Blueprint("tecnica", __name__)
service = TecnicaService()


@tecnica_bp.get("")
@jwt_required()
def listar():
    pag, por_pagina = pagina_params()
    resposta = service.listar(pag, por_pagina)
    resposta["tecnicas"] = resposta["itens"]
    return jsonify(resposta), 200
