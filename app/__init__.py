import logging
from flask import Flask, jsonify
from dotenv import load_dotenv
from .config import Config
from .extensions import db, migrate, jwt

def create_app(config_object=Config):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config_object)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import models so Alembic can discover metadata.
    from . import models  # noqa: F401
    from .routes import register_blueprints
    register_blueprints(app)
    from .middleware import register_request_logging
    register_request_logging(app)

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"error": {"code": "NOT_FOUND", "message": "Resource not found"}}), 404

    @app.errorhandler(500)
    def internal_error(_error):
        app.logger.exception("Unhandled server error")
        return jsonify({"error": {"code": "INTERNAL_SERVER_ERROR", "message": "An unexpected error occurred"}}), 500

    @jwt.unauthorized_loader
    def missing_token(reason):
        return jsonify({"error": {"code": "UNAUTHORIZED", "message": reason}}), 401

    @jwt.invalid_token_loader
    def invalid_token(reason):
        return jsonify({"error": {"code": "INVALID_TOKEN", "message": reason}}), 401

    @jwt.expired_token_loader
    def expired_token(_header, _payload):
        return jsonify({"error": {"code": "TOKEN_EXPIRED", "message": "Access token has expired"}}), 401

    return app
