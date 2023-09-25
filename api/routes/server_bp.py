from flask import Blueprint
from ..controllers.serverController import ServerController

server_bp = Blueprint('server_bp', __name__)

@server_bp.route('/all', methods=['GET'])
def obtener_servidores():
    return ServerController.get_servers()

@server_bp.route('/add', methods=['GET','POST'])
def crear_servidor():
    return ServerController.register_server()

@server_bp.route('/get/<string:server_name>', methods=['GET','POST'])
def obtener_servidor(server_name):
    return ServerController.get_server(server_name)