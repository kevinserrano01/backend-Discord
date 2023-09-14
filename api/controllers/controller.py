from flask import request, jsonify
from api.database import *

class UserController:

    @classmethod
    def get_user(self, id_usuario):
        sql = "SELECT * FROM usuarios W"

    @classmethod
    def get_users(self):
        sql = "SELECT * FROM usuarios"
        resultado = DatabaseConnection.fetch_all(sql)
        lista_usuarios = []
        if resultado is not None:
            for usuario in resultado:
                lista_usuarios.append({
                    "usuario_id": usuario[0],
                    "nombre": usuario[1],
                    "apellido": usuario[2],
                    "contra": usuario[3],
                    "correo": usuario[4],
                    "fecha_nacimiento": usuario[5]
                })
        return lista_tareas

    @classmethod
    def create_user(self):
        pass

    @classmethod
    def update_user(self):
        pass

    @classmethod
    def delete_user(self, user_id):
        """Delete a customer from the database."""
        sql = "DELETE FROM users WHERE user_id = %s;"
        params = user_id,
        DatabaseConnection.execute_query(sql, params)
        return {"msg": f"Usuario con id {user_id} elimnado"}, 204