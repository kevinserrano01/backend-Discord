from flask import Blueprint
from ..controllers.messageController import MessageController

message_bp = Blueprint('message_bp', __name__)

@message_bp.route('/all', methods=['GET'])
def obtener_mensajes():
    return MessageController.get_messages()

@message_bp.route('/get/<string:channel_name>', methods=['GET'])
def obtener_mensaje_asiociado_a_canal(channel_name):
    return MessageController.get_messages_attached_channel(channel_name)

@message_bp.route('/add', methods=['GET', 'POST'])
def crear_mensaje():
    return MessageController.add_message()

@message_bp.route('/delete', methods=['GET', 'POST'])
def borrar_mensaje():
    return MessageController.remove_message()

@message_bp.route('/edit', methods=['GET', 'POST'])
def editar_mensaje():
    return MessageController.edit_message()