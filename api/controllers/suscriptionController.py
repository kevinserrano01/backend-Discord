from flask import request, jsonify, session
from api.database import *
from ..models.susrciption_model import Suscription

class SuscriptionController:

    @classmethod
    def get_suscription(self):

        pass

    @classmethod
    def get_suscriptions(self):
        sql = """
                SELECT users.username, servers.server_name
                FROM ((suscription 
                INNER JOIN users
                ON suscription.suscription_user_id = users.user_id) 
                INNER JOIN servers
                ON suscription.suscription_server_id = servers.server_id)
            """
        resultado = DatabaseConnection.fetch_all(sql)
        suscriptions = []
        if resultado is not None:
            for suscription in resultado:
                suscriptions.append({
                    'Username': suscription[0],
                    'server_name': suscription[1]
                })
        return jsonify(suscriptions), 200