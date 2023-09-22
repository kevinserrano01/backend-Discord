from api.database import DatabaseConnection
from flask import request, session, jsonify

class Channel:
    def __init__(self, channel_id=None, schannel_name=None, server_name=None):
        self.channel_id = channel_id
        self.channel_name = schannel_name
        self.server_name = server_name

    def __str__(self):
        return f"Channel: {self.channel_name}"
    

    @classmethod
    def create_channel(cls, channel):
        """Create a channel from the database"""
        sql = """INSERT INTO discord_app.channels (channel_name, server_id)
                VALUES (%(channel_name)s, %(server_id)s);
            """
        params = channel.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Canal Registrado con exito!"}, 201
    
    @classmethod
    def get_channel_attached_server(self, server):
        """Funcion que retorna los canales asosiados a un sevidor especifico"""
        sql = """
                SELECT channels.channel_id, channels.channel_name, servers.server_name
                FROM servers INNER JOIN channels
                ON servers.server_id = channels.server_id
                WHERE servers.server_name = %(server_name)s;
            """
        params = server.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        resultado = DatabaseConnection.fetch_all(sql)
        print(resultado)
        canales = []
        if resultado is not None:
            for canal in resultado:
                canales.append({
                    'channel_id': canal[0],
                    'channel_name': canal[1],
                    'server_name': canal[2]
                })
        return jsonify(canales), 200