from api.database import DatabaseConnection

class UserStatusModel:

    def __init__(self, **kwargs):
        self.status_id = kwargs.get('status_id')
        self.status_name = kwargs.get('status_name')
    
    def serialize(self):
        return {
            "status_id": self.status_id,
            "status_name": self.status_name
        }

    @classmethod
    def get(cls, status):
        query = """SELECT status_id, status_name FROM authentication_db.user_status WHERE status_id = %(status_id)s"""
        params = status.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UserStatusModel(
                status_id = result[0],
                status_name = result[1]
            )
        return None