from flask import Blueprint, jsonify, request
from models import Usuario, db

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict())

@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        contrasena=data['contrasena'],
        rol=data.get('rol', 'user'),
        sucursal_id=data.get('sucursal_id')
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.to_dict()), 201

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.email = data.get('email', usuario.email)
    usuario.contrasena = data.get('contrasena', usuario.contrasena)
    usuario.rol = data.get('rol', usuario.rol)
    usuario.sucursal_id = data.get('sucursal_id', usuario.sucursal_id)
    db.session.commit()
    return jsonify(usuario.to_dict())

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado correctamente'}), 200