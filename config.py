from dotenv import load_dotenv # *pip install python-dotenv
import os

class Config:
    # Carga las variables de entorno desde el archivo .env
    load_dotenv()
    
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True

    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_NAME = os.getenv('DATABASE_NAME')

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"
    APP_NAME = "Clone Discord"