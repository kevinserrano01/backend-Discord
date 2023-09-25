from flask import Blueprint
from ..controllers.messageController import MessageController

message_bp = Blueprint('message_bp', __name__)

@message_bp.route('/all', methods=['GET'])
def obtener_mensajes():
    return MessageController.get_messages()

@message_bp.route('/get/<string:channel_name>', methods=['GET'])
def obtener_canal_asiociado_a_servidor(channel_name):
    return MessageController.get_messages_attached_channel(channel_name)