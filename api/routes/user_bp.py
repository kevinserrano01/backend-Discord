from flask import Blueprint
from ..controllers.userController import UserController

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['GET', 'POST'])
def iniciar_sesion():
    return UserController.login()

@user_bp.route('/profile', methods=['GET'])
def ver_perfil():
    return UserController.show_profile()

@user_bp.route('/logout', methods=['GET'])
def cerrar_sesion():
    return UserController.logout()

@user_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """Endpoint para mostrar todos los usuarios de la base de datos"""
    return UserController.get_users()

@user_bp.route('/usuarios/<string:username>', methods=['GET', 'POST'])
def get_usuario(username):
    """Endpoint para mostrar mostar un usuario la base de datos"""    
    return UserController.get_user(username)

@user_bp.route('/register', methods=['GET', 'POST'])
def registrar_usuario():
    """Endpoint para registrar un usuario en la base de datos"""
    return UserController.register()

@user_bp.route('/edit', methods=['GET', 'POST'])
def actualizar_usuario():
    """Endpoint para actualizar un usuario con su id"""
    return UserController.edit_user()

@user_bp.route('/deleteUser/<int:user_id>')
def eliminar_usuario(user_id):
    """Endpoint para eliminar un usuario"""
    return UserController.delete_user(user_id)