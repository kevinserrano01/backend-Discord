from flask import request, jsonify, session
from api.database import *
from ..models.server_model import Server

class ServerController:
    
    @classmethod
    def register_server(cls):
        """Add server to database."""
        # server_name = request.args.get('server_name')
        # server = Server(server_name=server_name)

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
    
    # @classmethod
    # def get_server(cls, username):
    #     """Retrieves a user from the database, by means of an id"""
    #     user = User.get(User(username = username))
    #     if user is not None:
    #         return {
    #             "user_id": user.user_id,
    #             "username": user.username,
    #             "email": user.email,
    #             "first_name": user.first_name,
    #             "last_name": user.last_name,
    #             "date_of_birth": user.date_of_birth,
    #             "phone_number": user.phone_number,
    #             "creation_date": user.creation_date,
    #             "last_login": user.last_login,
    #             "status_id": user.status_id,
    #             "role_id": user.role_id
    #         }, 200
    #     else:
    #         return {"message": "Usuario no encontrado"}, 404