from api.database import DatabaseConnection
from flask import request, session

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
    

    def guardar_en_tabla_intermedia():
        user_name = session.get('username')
        query = "SELECT user_id FROM discord_app.users WHERE username = %s"
        parametro = (user_name,)
        id_usuario_db = DatabaseConnection.fetch_one(query, params=parametro)
        id_user_login = id_usuario_db[0] # Id del usuario logeado

        # TOMAR EL TOTAL DE SEVIDORES QUE HAY EN LA BASE DE DATOS PARA COLOCARLO COMO PARAMETRO AQUI ABAJO..
        consulta = "SELECT server_name FROM discord_app.servers;"
        total_servers_db = DatabaseConnection.fetch_all(consulta)
        total_servers = len(total_servers_db)

        sql = """INSERT INTO discord_app.suscription (suscription_user_id, suscription_server_id)
                VALUES (%s, %s);
            """
        params = (id_user_login, total_servers)
        DatabaseConnection.execute_query(sql, params=params)

        print('Usuario y servidor registrados con exito!')
        return {"message": "Usuario y servidor registrados con exito!"}, 201
    

    @classmethod
    def create_server(cls, server):
        """Create a server from the database"""
        sql = """INSERT INTO discord_app.servers (server_name)
                VALUES (%(server_name)s);
            """
        params = server.__dict__
        DatabaseConnection.execute_query(sql, params=params)

        cls.guardar_en_tabla_intermedia()

        return {"message": "Servidor Registrado con exito!"}, 201
    

    @classmethod
    def get(cls, server):
        query = """SELECT * FROM discord_app.servers 
                    WHERE server_name = %(server_name)s"""
        params = server.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                server_id = result[0],
                server_name = result[1]
            )
        return None
    
