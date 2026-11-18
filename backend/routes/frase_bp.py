from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from service.frase_service import FraseService

frase_bp = Blueprint("frase", __name__)
service = FraseService()


@frase_bp.get("")
@jwt_required()
def obter():
    return jsonify({"frase": service.obter(request.args.get("data"))}), 200
