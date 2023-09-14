from flask import Blueprint
from ..controllers.userController import UserController

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['GET', 'POST'])
def iniciar_sesion():
    return UserController.login()

@user_bp.route('/profile', methods=['GET'])
def ver_perfil():
    return UserController.show_profile()

@user_bp.route('/usuario<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    """Endpoint para mostrar mostar un usuario la base de datos"""    
    return UserController.get_user(usuario_id)

@user_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """Endpoint para mostrar todos los usuarios de la base de datos"""
    return UserController.get_users()

@user_bp.route('/crear_usuario')
def crear_usuario():
    """Endpoint para crear un usuario"""
    return UserController.create_user()

@user_bp.route('/actualizar_usuario/<int:user_id>')
def actualizar_usuario(user_id):
    """Endpoint para actualizar un usuario  travez de su ID"""
    return UserController.update_user(user_id)

@user_bp.route('/deleteUser/<int:user_id>')
def eliminar_usuario(user_id):
    """Endpoint para eliminar un usuario"""
    return UserController.delete_user(user_id)