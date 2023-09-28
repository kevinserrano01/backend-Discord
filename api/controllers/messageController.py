from flask import request, jsonify, session
from api.database import *
from ..models.message_model import Message

class MessageController:

    @classmethod
    def get_messages(self):
        """Funcion que retorna todos los mensajes de la base de datos en formato JSON"""
        sql = """SELECT messages.messages_id, messages.content, messages.creation_date, channels.channel_name, users.username
                FROM ((messages
                INNER JOIN channels
                ON messages.channels_channel_id = channels.channel_id)
                INNER JOIN users
                ON messages.users_user_id = users.user_id)"""
        resultado = DatabaseConnection.fetch_all(sql)
        mensajes = []
        if resultado is not None:
            for mensaje in resultado:
                mensajes.append({
                    'message_id': mensaje[0],
                    'content': mensaje[1],
                    'creation_date': mensaje[2],
                    'channels_channel_id': mensaje[3],
                    'users_user_id': mensaje[4]
                })
        return jsonify(mensajes), 200
    
    @classmethod
    def get_messages_attached_channel(self, channel_name):
        """Funcion que retorna los mensajes asosiados a un canal en especifico"""
        nombre_canal = channel_name
        sql = """
                SELECT messages.messages_id, messages.creation_date, messages.content, channels.channel_name, users.username
                FROM ((messages
                INNER JOIN channels
                ON messages.channels_channel_id = channels.channel_id) 
                INNER JOIN users
                ON messages.users_user_id = users.user_id)
                WHERE channels.channel_name = %s;
            """
        params = (nombre_canal,)
        resultado = DatabaseConnection.fetch_all(sql, params=params)
        mensajes = []
        if resultado is not None:
            for canal in resultado:
                mensajes.append({
                    'message_id': canal[0],
                    'creation_date': canal[1],
                    'content': canal[2],
                    'channel_name': canal[3],
                    'username': canal[4]
                })
        return jsonify(mensajes), 200
    

    @classmethod
    def add_message(self):
        data = request.json
        content = data.get('content')
        channel_id = data.get('channel_id')
        user_id = data.get('user_id')
        mensaje = Message(content=content, channel_id=channel_id, user_id=user_id)

        print(f"\033[92m{mensaje}\033[0m")
        return Message.send_message(mensaje)
    
    @classmethod
    def remove_message(cls):
        data = request.json
        message_id = data.get('message_id')
        user_id = data.get('user_id')

        mensaje = Message(message_id=message_id, user_id=user_id)

        if Message.verify_id(mensaje):
            print(f"\033[92m Message deleted -> {mensaje} \033[0m")
            return Message.delete_message(mensaje)
        else:
            print(f"\033[91m Error: No puedes eliminar este mensaje porque no eres el autor. \033[0m")
            return {"message": "No puedes eliminar este mensaje porque no eres el autor."}, 401