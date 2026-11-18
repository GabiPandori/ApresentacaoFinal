from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from routes.helpers import usuario_atual
from service.paciente_service import PacienteService

paciente_bp = Blueprint("paciente", __name__)
service = PacienteService()


@paciente_bp.get("/<int:id_paciente>/resumo")
@jwt_required()
def resumo(id_paciente):
    """Paciente com dados relacionados: total de relatos (1:N) e técnicas usadas (N:N)."""
    return jsonify(service.resumo(usuario_atual(), id_paciente)), 200
