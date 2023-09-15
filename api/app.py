from flask import Flask
from flask_cors import CORS
from api.routes.user_bp import user_bp

app = Flask(__name__)

# Registrar Rutas
app.register_blueprint(user_bp, url_prefix = '/auth')

# API: permitir el acceso desde dominios específicos. Permite solicitudes desde el dominio de tu página web.
CORS(app, supports_credentials=True)