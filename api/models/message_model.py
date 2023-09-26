from api.database import DatabaseConnection

class Message:
    def __init__(self, message_id=None, content=None, creation_date=None, channel_id=None, user_id=None):
        self.message_id = message_id
        self.content = content
        self.creation_date = creation_date
        self.channel_id = channel_id
        self.user_id = user_id

    def __str__(self):
        return f"Message sent: {self.content}"
    
    @classmethod
    def send_message(cls, message):
        """Send a message and save it in the database"""
        sql = """INSERT INTO discord_app.messages (content, channels_channel_id, users_user_id)
                VALUES (%(content)s, %(channel_id)s, %(user_id)s);
            """
        params = message.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Servidor Registrado con exito!"}, 201