from api.database import DatabaseConnection

class Message:
    def __init__(self, message_id=None, content=None, creation_date=None, channel_id=None, user_id=None):
        self.message_id = message_id
        self.content = content
        self.creation_date = creation_date
        self.channel_id = channel_id
        self.user_id = user_id

    def __str__(self):
        return f"Message: {self.content}"
    
    @classmethod
    def send_message(cls, message):
        """Send a message and save it in the database"""
        sql = """INSERT INTO discord_app.messages (content, channels_channel_id, users_user_id)
                VALUES (%(content)s, %(channel_id)s, %(user_id)s);
            """
        params = message.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Servidor Registrado con exito!"}, 201
    
    @classmethod
    def verify_id(cls, message):
        """Verifica si el mensaje esta registrado con el id del usuario logeado Base de datos."""
        query = """SELECT users_user_id FROM discord_app.messages WHERE messages_id = %(message_id)s"""
        params = message.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            id_user_database = result[0]
            id_user_logeado = message.user_id

            if id_user_database == int(id_user_logeado):
                return True
            else:
                return False
        return False
    
    @classmethod
    def delete_message(cls, message):
        """Delete a message from the database"""
        sql = """DELETE FROM discord_app.messages WHERE messages_id = %(message_id)s and users_user_id = %(user_id)s;"""
        params = message.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Mensaje Eliminado con exito"}, 200

    @classmethod
    def update_message(cls, message):
        """Update a message from the database"""
        sql = """UPDATE discord_app.messages SET content = %(content)s WHERE messages_id = %(message_id)s and users_user_id = %(user_id)s;"""
        params = message.__dict__
        DatabaseConnection.execute_query(sql, params=params)
        return {"message": "Mensaje Editado con exito"}, 200