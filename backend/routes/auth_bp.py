from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from routes.helpers import usuario_atual
from service.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)
service = AuthService()


@auth_bp.post("/register")
def register():
    usuario = service.registrar(request.get_json(silent=True))
    return jsonify({"message": "Cadastro realizado com sucesso.", "usuario": usuario}), 201


@auth_bp.post("/login")
def login():
    return jsonify(service.login(request.get_json(silent=True))), 200


@auth_bp.get("/me")
@jwt_required()
def me():
    return jsonify({"usuario": service.me(usuario_atual())}), 200
