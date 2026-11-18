import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from service.db_service import db, configurar_banco
from service.erros import ErroServico
from service.seed_service import inicializar_banco
import model.entities 
from routes.health_bp import health_bp
from routes.auth_bp import auth_bp
from routes.diario_bp import diario_bp
from routes.paciente_bp import paciente_bp
from routes.tecnica_bp import tecnica_bp
from routes.paciente_tecnica_bp import paciente_tecnica_bp
from routes.evento_bp import evento_bp
from routes.livro_bp import livro_bp
from routes.frase_bp import frase_bp


def criar_app():
    app = Flask(__name__)
    configurar_banco(app)

    chave = os.getenv("JWT_SECRET_KEY")
    if not chave:
        if os.getenv("DATABASE_URL"): 
            raise RuntimeError("Defina a variável de ambiente JWT_SECRET_KEY.")
        chave = "chave-somente-para-desenvolvimento-local-0123456789"
    app.config["JWT_SECRET_KEY"] = chave
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=8)

    origens = [o.strip() for o in os.getenv("FRONTEND_ORIGIN", "*").split(",") if o.strip()]
    CORS(app, resources={r"/api/*": {"origins": origens if origens != ["*"] else "*"}})

    jwt = JWTManager(app)

    @jwt.unauthorized_loader
    def sem_token(motivo):
        return jsonify({"message": "Faça login para acessar este recurso."}), 401

    @jwt.invalid_token_loader
    def token_invalido(motivo):
        return jsonify({"message": "Token inválido."}), 401

    @jwt.expired_token_loader
    def token_expirado(header, payload):
        return jsonify({"message": "Sessão expirada. Faça login novamente."}), 401

    # Blueprints (camada routes)
    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(diario_bp, url_prefix="/api/diario")
    app.register_blueprint(paciente_bp, url_prefix="/api/paciente")
    app.register_blueprint(tecnica_bp, url_prefix="/api/tecnica")
    app.register_blueprint(paciente_tecnica_bp, url_prefix="/api/paciente-tecnica")
    app.register_blueprint(evento_bp, url_prefix="/api/evento")
    app.register_blueprint(livro_bp, url_prefix="/api/livro")
    app.register_blueprint(frase_bp, url_prefix="/api/frase")

    @app.errorhandler(ErroServico)
    def erro_servico(e):
        return jsonify({"message": e.mensagem}), e.status

    @app.errorhandler(404)
    def nao_encontrado(_):
        return jsonify({"message": "Rota não encontrada."}), 404

    @app.errorhandler(405)
    def metodo_nao_permitido(_):
        return jsonify({"message": "Método não permitido."}), 405

    @app.errorhandler(500)
    def erro_interno(_):
        db.session.rollback()
        return jsonify({"message": "Erro interno do servidor."}), 500


    if os.getenv("AUTO_CREATE_TABLES", "true").lower() != "false":
        with app.app_context():
            try:
                inicializar_banco()
            except Exception as e: 
                db.session.rollback()
                app.logger.error("Falha ao inicializar o banco: %s", e)
    return app


app = criar_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
