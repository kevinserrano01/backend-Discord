from flask import Flask
from flask_cors import CORS
from api.routes.user_bp import user_bp
from api.routes.server_bp import server_bp
from api.routes.suscription_bp import suscriptcion_bp

app = Flask(__name__)

# API: permitir el acceso desde dominios específicos. Permite solicitudes desde el dominio de tu página web.
CORS(app, supports_credentials=True, origins="http://127.0.0.1:5500")

# Registrar Rutas despues de CORS
app.register_blueprint(user_bp, url_prefix = '/auth')
app.register_blueprint(server_bp, url_prefix = '/server')
app.register_blueprint(suscriptcion_bp, url_prefix = '/suscription')