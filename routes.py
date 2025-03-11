from flask import Blueprint, request, jsonify
from models import db, Usuario

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario or usuario.contrasena != password:
        return jsonify({'message': 'Credenciales inválidas'}), 401

    return jsonify({
        'id': usuario.id,
        'nombre': usuario.nombre,
        'email': usuario.email,
        'rol': usuario.rol,
        'sucursal_id': usuario.sucursal_id
    })
