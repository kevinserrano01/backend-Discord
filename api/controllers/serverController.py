from flask import request, jsonify, session
from api.database import *
from ..models.server_model import Server

class ServerController:
    
    @classmethod
    def register_server(cls):
        """Add server to database."""
        data = request.json
        server = Server(server_name=data.get('server_name'))
        
        if Server.is_registered(server):
            print(f"\033[91m{server}\033[0m")
            return {"message": "Este servidor ya fue creado..."}, 401
        else:
            print(f"\033[92m{server}\033[0m")
            return Server.create_server(server)
        
        
    
    @classmethod
    def get_servers(self):
        """Funcion que retorna todos los servidores de la base de datos en formato JSON"""
        sql = "SELECT * FROM discord_app.servers"
        resultado = DatabaseConnection.fetch_all(sql)
        servidores = []
        if resultado is not None:
            for servidor in resultado:
                servidores.append({
                    'server_id': servidor[0],
                    'server_name': servidor[1]
                })
        return jsonify(servidores), 200
    
    @classmethod
    def get_server(cls, server_name):
        """Devuelve un servidor en especidifo pasandole le nombre del servidor."""
        server = Server.get(Server(server_name = server_name))
        if server is not None:
            return {
                "server_id": server.server_id,
                "server_name": server.server_name
            }, 200
        else:
            return {"message": "Servidor no encontrado"}, 404