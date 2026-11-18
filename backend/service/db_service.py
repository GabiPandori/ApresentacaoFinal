import os
import ssl
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def _opcoes_engine(uri):
    opcoes = {"pool_pre_ping": True, "pool_recycle": 280}
    if uri.startswith("mysql") and "ssl_ca" not in uri and os.getenv("DB_SSL", "true").lower() != "false":
        # Bancos na nuvem (Aiven etc.) exigem conexão criptografada (SSL).
        # Se DB_SSL_CA apontar para o certificado (ca.pem), ele é verificado;
        # sem ele, a conexão é criptografada mas sem verificar o certificado.
        ca = os.getenv("DB_SSL_CA")
        ctx = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
        if not ca:
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        opcoes["connect_args"] = {"ssl": ctx}
    return opcoes


def configurar_banco(app):
    uri = os.getenv("DATABASE_URL", "sqlite:///triad_dev.db")
    if uri.startswith("mysql://"):
        uri = uri.replace("mysql://", "mysql+pymysql://", 1)
    app.config.update(
        SQLALCHEMY_DATABASE_URI=uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ENGINE_OPTIONS=_opcoes_engine(uri),
    )
    db.init_app(app)
