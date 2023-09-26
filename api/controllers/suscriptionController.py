from flask import request, jsonify, session
from api.database import *
from ..models.susrciption_model import Suscription

class SuscriptionController:

    @classmethod
    def suscription(self):
        data = request.json
        server_id = data.get('server_id')
        user_id = data.get('user_id')
        suscription = Suscription(user_id=user_id, server_id=server_id)

        print(f"\033[92m{suscription}\033[0m")
        return Suscription.create_suscription(suscription)

        # Si el usuario ya esta suscrito al servidor, mostar un mensaje de que ya fue suscrito, caso contario deberia unirse
        # if Suscription.is_registered(suscription):
        #     print(f"\033[91m{suscription}\033[0m")
        #     return {"message": "Usted ya esta suscrito en este servidor..."}, 401
        # else:
        #     print(f"\033[92m{suscription}\033[0m")
        #     return Suscription.create_suscription(suscription)

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