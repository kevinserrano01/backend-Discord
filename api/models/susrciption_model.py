from api.database import DatabaseConnection
from flask import request

class Suscription:

    def __init__(self, user_id=None, server_id=None):
        self.user_id = user_id
        self.server_id = server_id

    def __str__(self):
        return f"User: {self.user_id} JOINED {self.server_id} Server"
    
    @classmethod
    def create_suscription(cls, suscription):
        """Create a suscription from the database"""
        sql = """INSERT INTO discord_app.suscription (suscription_user_id, suscription_server_id)
                VALUES (%(user_id)s, %(server_id)s);
            """
        params = suscription.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Usuario suscrito al servidor con exito!"}, 201
    