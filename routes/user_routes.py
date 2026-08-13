
from flask import Blueprint
from controllers.user_controller import (
    criar_usuario, listar_usuarios, buscar_usuario,
    atualizar_usuario, deletar_usuario
)

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['POST'])(criar_usuario)
user_bp.route('/users', methods=['GET'])(listar_usuarios)
user_bp.route('/users/<int:id_usuario>', methods=['GET'])(buscar_usuario)
user_bp.route('/users/<int:id_usuario>', methods=['PUT'])(atualizar_usuario)
user_bp.route('/users/<int:id_usuario>', methods=['DELETE'])(deletar_usuario)