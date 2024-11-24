from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar rutas
    from .routes.offline import offline_bp
    app.register_blueprint(offline_bp, url_prefix="/offline")

    return app