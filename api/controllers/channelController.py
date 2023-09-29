from flask import request, jsonify, session
from api.database import *
from ..models.channel_model import Channel

class ChannelController:

    @classmethod
    def register_channel(cls):
        """Add channel to database."""
        # channel_name = request.args.get('channel_name')
        # server_id = request.args.get('server_id')
        # channel = Channel(channel_name=channel_name, server_id=server_id)

        data = request.json
        channel_name = data.get('channel_name')
        server_id = data.get('server_id')
        channel = Channel(channel_name=channel_name, server_id=server_id)

        print(f"\033[92m{channel}\033[0m")
        return Channel.create_channel(channel)

        # Si el canal ya esta creado mostar un mensaje de que ya fue creado, caso contario deberia crearlo
        # if Channel.is_registered(channel):
        #     print(f"\033[91m{channel}\033[0m")
        #     return {"message": "Este canal ya fue creado..."}, 401
        # else:
        #     print(f"\033[92m{channel}\033[0m")
        #     return Channel.create_channel(channel)

    @classmethod
    def get_channels(self):
        """Funcion que retorna todos los canales de la base de datos en formato JSON"""
        sql = """
                SELECT channels.channel_id, channels.channel_name, servers.server_name
                FROM servers INNER JOIN channels
                ON servers.server_id = channels.server_id;
            """
        resultado = DatabaseConnection.fetch_all(sql)
        canales = []
        if resultado is not None:
            for canal in resultado:
                canales.append({
                    'channel_id': canal[0],
                    'channel_name': canal[1],
                    'server_name': canal[2]
                })
        return jsonify(canales), 200
    
    @classmethod
    def get_channel_attached_server(self, server_name):
        """Funcion que retorna los canales asosiados a un sevidor especifico"""
        nombre_servidor = server_name
        sql = """
                SELECT channels.channel_id, channels.channel_name, servers.server_name
                FROM servers INNER JOIN channels
                ON servers.server_id = channels.server_id
                WHERE servers.server_name = %s;
            """
        params = (nombre_servidor,)
        resultado = DatabaseConnection.fetch_all(sql, params=params)
        canales = []
        if resultado is not None:
            for canal in resultado:
                canales.append({
                    'channel_id': canal[0],
                    'channel_name': canal[1],
                    'server_name': canal[2]
                })
        return jsonify(canales), 200