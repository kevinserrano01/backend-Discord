from flask import Flask
from api.routes.user_bp import user_bp

app = Flask(__name__)

# Rutas
app.register_blueprint(user_bp, url_prefix = '/auth')