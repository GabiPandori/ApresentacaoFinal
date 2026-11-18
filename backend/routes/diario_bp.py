from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from routes.helpers import pagina_params, usuario_atual
from service.diario_service import DiarioService

diario_bp = Blueprint("diario", __name__)
service = DiarioService()


@diario_bp.post("")
@jwt_required()
def criar():
    relato = service.criar(usuario_atual(), request.get_json(silent=True))
    return jsonify({"message": "Relato salvo.", "relato": relato}), 201


@diario_bp.get("")
@jwt_required()
def listar():
    pag, por_pagina = pagina_params()
    enviado_arg = request.args.get("enviado")
    enviado = None if enviado_arg is None else enviado_arg.lower() in ("true", "1", "sim")
    id_paciente = request.args.get("idPaciente", type=int)
    return jsonify(service.listar(usuario_atual(), pag, por_pagina, id_paciente, enviado)), 200


@diario_bp.get("/<int:id_diario>")
@jwt_required()
def obter(id_diario):
    return jsonify({"relato": service.obter(usuario_atual(), id_diario)}), 200


@diario_bp.put("/<int:id_diario>")
@jwt_required()
def atualizar(id_diario):
    relato = service.atualizar(usuario_atual(), id_diario, request.get_json(silent=True))
    return jsonify({"message": "Atualizado.", "relato": relato}), 200


@diario_bp.delete("/<int:id_diario>")
@jwt_required()
def excluir(id_diario):
    service.excluir(usuario_atual(), id_diario)
    return jsonify({"message": "Relato excluído."}), 200
