from .customer_routes import customer_bp
from .credit_routes import credit_bp
from .risk_routes import risk_bp
from .health_routes import health_bp

def register_blueprints(app):
    app.register_blueprint(customer_bp, url_prefix="/api/customers")
    app.register_blueprint(credit_bp, url_prefix="/api")
    app.register_blueprint(risk_bp, url_prefix="/api")
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)

from .auth_routes import auth_bp
