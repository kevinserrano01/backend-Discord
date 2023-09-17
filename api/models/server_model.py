from api.database import DatabaseConnection
from flask import request

class Server:
    def __init__(self, server_id=None, server_name=None):
        self.server_id = server_id
        self.server_name = server_name

    def __str__(self):
        return f"Server: {self.server_name}"
    
    @classmethod
    def is_registered(cls, server):
        """Verifica si el servidor esta registrado en la Base de datos."""
        query = """SELECT server_id FROM discord_app.servers
                WHERE server_name = %(server_name)s"""
        params = server.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def create_server(cls, server):
        """Create a server from the database"""
        sql = """INSERT INTO discord_app.servers (server_name)
                VALUES (%(server_name)s);
            """
        params = server.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Servidor Registrado con exito!"}, 201