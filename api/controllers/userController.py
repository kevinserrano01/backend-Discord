from flask import request, jsonify, session
from api.database import *
from ..models.user_model import User

class UserController:

    @classmethod
    def login(cls):
        """Iniciar sesion si esta registrado en la base de datos."""
        data = request.json
        user = User(
            username = data.get('username'),
            password = data.get('password')
        ) 
        if User.is_registered(user):
            print(f"\033[92m{user}\033[0m")
            # Esto significa que la aplicación web recordará el nombre de usuario del usuario mientras la sesión esté activa.
            session['username'] = data.get('username')
            return {"message": "Sesion iniciada"}, 200
        else:
            print(f"\033[91m{user}\033[0m")
            return {"message": "Usuario o contraseña incorrectos"}, 401
        
    @classmethod
    def register(cls):
        """Registrar usuario en la base de datos."""
        data = request.json
        user = User(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            date_of_birth=data.get('date_of_birth'),
            phone_number=data.get('phone_number'),
            status_id=data.get('status_id'),
            role_id=data.get('role_id')
        )
        print(user)
        
        if User.is_registered(user):
            print(f"\033[91m{user}\033[0m")
            return {"message": "Este usuario ya fue creado, inicie sesion."}, 401
        else:
            print(f"\033[92m{user}\033[0m")
            return User.create_user(user)
        
    @classmethod
    def show_profile(cls):
        """Ver perfil del usuario con la sesion activa en el navegador"""
        username = session.get('username')
        user = User.get(User(username = username))
        servers = User.get_servers(User(username = username))        
        if user is not None:
            return {
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_of_birth": user.date_of_birth,
                "phone_number": user.phone_number,
                "creation_date": user.creation_date,
                "last_login": user.last_login,
                "status_id": user.status_id,
                "role_id": user.role_id,
                "servers": servers
            }, 200
        else:
            return {"message": "Usuario no encontrado"}, 404
        
    @classmethod
    def logout(cls):
        """Cerrar la sesion activa del navegador."""
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200

    @classmethod
    def get_user(cls, username):
        """Retrieves a user from the database, by means of an id"""
        user = User.get(User(username = username))
        if user is not None:
            return {
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_of_birth": user.date_of_birth,
                "phone_number": user.phone_number,
                "creation_date": user.creation_date,
                "last_login": user.last_login,
                "status_id": user.status_id,
                "role_id": user.role_id
            }, 200
        else:
            return {"message": "Usuario no encontrado"}, 404
        

    @classmethod
    def get_users(self):
        """Retrieves users from the database, through a user id."""
        sql = "SELECT * FROM users"
        resultado = DatabaseConnection.fetch_all(sql)
        lista_usuarios = []
        if resultado is not None:
            for usuario in resultado:
                lista_usuarios.append({
                    'user_id': usuario[0],
                    'username': usuario[1],
                    'email': usuario[3],
                    'first_name': usuario[4],
                    'last_name': usuario[5],
                    'date_of_birth': usuario[6],
                    'phone_number': usuario[7],
                    'creation_date': usuario[8],
                    'last_login': usuario[9],
                    'status_id': usuario[10],
                    'role_id': usuario[11]
                })
        return jsonify(lista_usuarios), 200

    @classmethod
    def edit_user(cls):
        """Actualizar un usuario en la base de datos."""
        data = request.json
        user = User(
            user_id = data.get('user_id'),
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
        )
        if User.is_registered(user):
            print(f"\033[91m{user}\033[0m")
            return {"message": "El nombre de usuario ya esta en uso."}, 401
        else:
            print(f"\033[92m{user}\033[0m")
            session['username'] = data.get('username') # Asignar el nuevo usuario a la Session
            return User.update_user(user)

    @classmethod
    def delete_user(self, user_id):
        """Delete a user from the database."""
        sql = "DELETE FROM users WHERE user_id = %s;"
        params = user_id,
        DatabaseConnection.execute_query(sql, params)
        return {"msg": f"Usuario con id {user_id} elimnado"}, 204