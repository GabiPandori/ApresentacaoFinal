from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from routes.helpers import pagina_params, usuario_atual
from service.paciente_tecnica_service import PacienteTecnicaService

paciente_tecnica_bp = Blueprint("paciente_tecnica", __name__)
service = PacienteTecnicaService()


@paciente_tecnica_bp.post("")
@jwt_required()
def registrar():
    item = service.registrar(usuario_atual(), request.get_json(silent=True))
    return jsonify({"message": "Técnica registrada.", "id": item["idPacienteTecnica"], "registro": item}), 201


@paciente_tecnica_bp.get("")
@jwt_required()
def listar():
    pag, por_pagina = pagina_params()
    id_paciente = request.args.get("idPaciente", type=int)
    return jsonify(service.listar(usuario_atual(), pag, por_pagina, id_paciente)), 200


@paciente_tecnica_bp.delete("/<int:id_registro>")
@jwt_required()
def excluir(id_registro):
    service.excluir(usuario_atual(), id_registro)
    return jsonify({"message": "Registro removido."}), 200
