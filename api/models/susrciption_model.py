from api.database import DatabaseConnection
from flask import request

class Suscription:

    def __init__(self, user_id=None, server_id=None):
        self.user_id = user_id
        self.server_id = server_id

    def __str__(self):
        return f"Usuario: {self.user_id} - Servidor: {self.server_id}"
    
    @classmethod
    def get_server(cls, server):
        pass