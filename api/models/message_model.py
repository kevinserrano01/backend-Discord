from api.database import DatabaseConnection
from flask import request, session

class Message:
    def __init__(self, message_id=None, content=None, creation_date=None, channels_channel_id=None, users_user_id=None):
        self.message_id = message_id
        self.content = content
        self.creation_date = creation_date
        self.channels_channel_id = channels_channel_id
        self.users_user_id = users_user_id

    def __str__(self):
        return f"Message: {self.content}"