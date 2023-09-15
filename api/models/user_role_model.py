from api.database import DatabaseConnection

class UserRoleModel:

    def __init__(self, **kwargs):
        self.role_id = kwargs.get('role_id')
        self.role_name = kwargs.get('role_name')

    def serialize(self):
        return {
            "role_id": self.role_id,
            "role_name": self.role_name
        }
    
    @classmethod
    def get(cls, role):
        query = """SELECT role_id, role_name FROM authentication_db.user_roles WHERE role_id = %(role_id)s"""
        params = role.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserRoleModel(
                role_id = result[0],
                role_name = result[1]
            )
        return None