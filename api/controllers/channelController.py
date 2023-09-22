from flask import request, jsonify, session
from api.database import *
# from ..models.

class ChannelController:

    @classmethod
    def register_channel(cls):
        """Add channel to database."""
        # server_name = request.args.get('server_name')
        # server = Server(server_name=server_name)

        # data = request.json
        # server = Server(server_name=data.get('server_name'))
        
        # if Server.is_registered(server):
        #     print(f"\033[91m{server}\033[0m")
        #     return {"message": "Este servidor ya fue creado..."}, 401
        # else:
        #     print(f"\033[92m{server}\033[0m")
        #     return Server.create_server(server)
        pass

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