import mysql.connector
from config import Config

class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host = Config.DATABASE_HOST,
                user = Config.DATABASE_USERNAME,
                port = Config.DATABASE_PORT,
                password = Config.DATABASE_PASSWORD,
                database = Config.DATABASE_NAME
            )
        return cls._connection
    
    # @classmethod
    # def set_config(cls, config):
    #     cls._config = config
    
    @classmethod
    def execute_query(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor
    
    @classmethod
    def fetch_one(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    
    @classmethod
    def fetch_all(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None