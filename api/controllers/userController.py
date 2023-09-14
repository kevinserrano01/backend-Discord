from flask import request, jsonify, session
from api.database import *
from ..models.user_model import User

class UserController:

    @classmethod
    def login(cls):
        """Iniciar sesion si esta registrado en la base de datos."""
        # data = request.json
        # user = User(
        #     username = data.get('username'),
        #     password = data.get('password')
        # )
        username = request.args.get('username')
        password = request.args.get('password')
        user = User(username=username, password=password)
        
        if User.is_registered(user):
            print(f"\033[92m{user}\033[0m")
            # Esto significa que la aplicación web recordará el nombre de usuario del usuario mientras la sesión esté activa.
            session['username'] = username
            return {"message": "Sesion iniciada"}, 200
        else:
            print(f"\033[91m{user}\033[0m")
            return {"message": "Usuario o contraseña incorrectos"}, 401
        
    @classmethod
    def show_profile(cls):
        """Ver perfil del usuario con la sesion activa en el navegador"""
        username = session.get('username')
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
    def create_user(self):
        """Create a user from the database"""
        nombre = request.args.get('nombre')
        apellido = request.args.get('apellido')
        clave = request.args.get('clave')
        email = request.args.get('email')
        fecha_nacimiento = request.args.get('fecha_nacimiento')

        sql = """INSERT INTO usuarios (nombre, apellido, clave, email, fecha_nacimiento)
                VALUES (%s, %s, %s, %s, %s);
            """

        params = nombre, apellido, clave, email, fecha_nacimiento,
        DatabaseConnection.execute_query(sql, params)

        datos = {
            "nombre": nombre,
            "apellido": apellido,
            "clave": clave,
            "email": email,
            "fecha_nacimiento": fecha_nacimiento
        }

        return datos, 201

    @classmethod
    def update_user(self, id_usuario):
        """Update a user from the database"""
        nombre = request.args.get('nombre')
        apellido = request.args.get('apellido')
        clave = request.args.get('clave')
        email = request.args.get('email')
        fecha_nacimiento = request.args.get('fecha_nacimiento')
        
        sql = "UPDATE customers SET nombre = %s, apellido = %s,clave = %s,email = %s, fecha_nacimiento = %s WHERE customer_id = %s"
        params = nombre, apellido, clave, email, fecha_nacimiento, id_usuario
        DatabaseConnection.execute_query(sql, params)

        datos = {
            "nombre": nombre,
	        "apellido": apellido,
            "clave": clave,
            "email": email,
            "fecha_nacimiento": fecha_nacimiento,
            }, 200
        
        return datos

    @classmethod
    def delete_user(self, user_id):
        """Delete a user from the database."""
        sql = "DELETE FROM users WHERE user_id = %s;"
        params = user_id,
        DatabaseConnection.execute_query(sql, params)
        return {"msg": f"Usuario con id {user_id} elimnado"}, 204