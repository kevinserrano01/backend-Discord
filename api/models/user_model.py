from api.database import DatabaseConnection
from flask import request

class User:

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.date_of_birth = kwargs.get('date_of_birth')
        self.phone_number = kwargs.get('phone_number')
        self.creation_date = kwargs.get('creation_date')
        self.last_login = kwargs.get('last_login')
        self.status_id = kwargs.get('status_id')
        self.role_id = kwargs.get('role_id')

    def __str__(self) -> str:
        return f"Username: {self.username} - Password: {self.password}"

    @classmethod
    def is_registered(cls, user):
        """Verifica si el usuario esta registrado en la Base de datos."""
        query = """SELECT user_id FROM discord_app.users
        WHERE username = %(username)s and password = %(password)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        query = """SELECT * FROM discord_app.users 
        WHERE username = %(username)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                user_id = result[0],
                username = result[1],
                email = result[3],
                first_name = result[4],
                last_name = result[5],
                date_of_birth = result[6],
                phone_number = result[7],
                creation_date = result[8],
                last_login = result[9],
                status_id = result[10],
                role_id = result[11]
            )
        return None
    
    @classmethod
    def create_user(cls, user):
        """Create a user from the database"""
        sql = """INSERT INTO discord_app.users (username, password, email, first_name, last_name, date_of_birth, phone_number, user_status_status_id, user_roles_role_id)
                VALUES (%(username)s, %(password)s, %(email)s, %(first_name)s, %(last_name)s, %(date_of_birth)s, %(phone_number)s, %(status_id)s, %(role_id)s);
            """
        params = user.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Usuario Registrado"}, 201
    
    @classmethod
    def get_servers(cls, user):
        """Obtener todos los servidores creados o suscriptos por el usuario logeado"""
        query = """
                SELECT users.username, servers.server_name
                FROM ((suscription 
                INNER JOIN users
                ON suscription.suscription_user_id = users.user_id) 
                INNER JOIN servers
                ON suscription.suscription_server_id = servers.server_id)
                WHERE users.username = %(username)s
            """
        params = user.__dict__
        result = DatabaseConnection.fetch_all(query, params=params)
        list_servers = []

        if result is not None:
            for suscription in result:
                list_servers.append(suscription[1])
            return list_servers
        return None

    @classmethod
    def update_user(cls, user):
        """Update a user from the database"""
        sql = """UPDATE discord_app.users SET username=%(username)s, email=%(email)s, first_name=%(first_name)s, last_name=%(last_name)s WHERE user_id = %(user_id)s;"""
        params = user.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Usuario Actualizado con exito"}, 200
    


    # def serialize(self):
    #     return {
    #         "user_id": self.user_id,
    #         "username": self.username,
    #         "password": self.password,
    #         "email": self.email,
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #         "date_of_birth": self.date_of_birth,
    #         "phone_number": self.phone_number,
    #         "creation_date": self.creation_date,
    #         "last_login": self.last_login,
    #         "status": UserStatusModel.get(UserStatusModel(status_id = self.status_id)).serialize(),
    #         "role": UserRoleModel.get(UserRoleModel(role_id = self.role_id)).serialize()
    #     }