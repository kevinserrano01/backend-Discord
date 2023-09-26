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