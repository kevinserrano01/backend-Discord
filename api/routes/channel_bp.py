from flask import Blueprint
from ..controllers.channelController import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

@channel_bp.route('/all', methods=['GET'])
def obtener_canales():
    return ChannelController.get_channels()

@channel_bp.route('/get/<string:server_name>', methods=['GET'])
def obtener_canal_asiociado_a_servidor(server_name):
    return ChannelController.get_channel_attached_server(server_name)

# @channel_bp.route('/add', methods=['GET','POST'])
# def crear_servidor():
#     return ChannelController.register_channel()