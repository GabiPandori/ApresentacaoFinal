from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from routes.helpers import pagina_params
from service.evento_service import EventoService

evento_bp = Blueprint("evento", __name__)
service = EventoService()


@evento_bp.get("")
@jwt_required()
def listar():
    pag, por_pagina = pagina_params()
    return jsonify(service.listar(pag, por_pagina)), 200
