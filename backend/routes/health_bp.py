from flask import Blueprint, jsonify
from sqlalchemy import text
from service.db_service import db

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    return jsonify({"status": "ok", "app": "Triad"}), 200


@health_bp.get("/health/db")
def health_db():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"conexao": "ok"}), 200
    except Exception:
        return jsonify({"message": "Banco de dados indisponível."}), 503
