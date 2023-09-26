from flask import Blueprint
from ..controllers.suscriptionController import SuscriptionController

suscriptcion_bp = Blueprint('suscriptcion_bp', __name__)

@suscriptcion_bp.route('/all', methods=['GET'])
def listar_suscripciones():
    return SuscriptionController.get_suscriptions()

@suscriptcion_bp.route('/add', methods=['GET', 'POST'])
def crear_suscripcion():
    return SuscriptionController.suscription()