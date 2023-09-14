from api.database import DatabaseConnection

class User:
    # def __init__(self, user_id = None, username = None, password = None, email = None, first_name = None, last_name = None, date_of_birth = None, phone_number = None, creation_date = None, last_login = None, status_id = None, role_id = None):
    #     self.user_id = user_id
    #     self.username = username
    #     self.password = password
    #     self.email = email
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.date_of_birth = date_of_birth
    #     self.phone_number = phone_number
    #     self.creation_date = creation_date
    #     self.last_login = last_login
    #     self.status_id = status_id
    #     self.role_id = role_id

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
                password = result[2],
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