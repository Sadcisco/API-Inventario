from flask import Blueprint, request, jsonify
from models import db, Usuario, Sucursal

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
sucursal_bp = Blueprint('sucursal', __name__)

# Obtener todas las sucursales
@sucursal_bp.route('/sucursales', methods=['GET'])
def get_sucursales():
    sucursales = Sucursal.query.all()
    return jsonify([sucursal.to_dict() for sucursal in sucursales])

# Obtener una sucursal por su ID
@sucursal_bp.route('/sucursales/<int:id>', methods=['GET'])
def get_sucursal(id):
    sucursal = Sucursal.query.get_or_404(id)
    return jsonify(sucursal.to_dict())

# Crear una nueva sucursal
@sucursal_bp.route('/sucursales', methods=['POST'])
def create_sucursal():
    data = request.get_json()
    nueva_sucursal = Sucursal(
        nombre=data['nombre'],
        direccion=data['direccion'],
        telefono=data['telefono']
    )
    db.session.add(nueva_sucursal)
    db.session.commit()
    return jsonify(nueva_sucursal.to_dict()), 201

# Actualizar una sucursal
@sucursal_bp.route('/sucursales/<int:id>', methods=['PUT'])
def update_sucursal(id):
    sucursal = Sucursal.query.get_or_404(id)
    data = request.get_json()
    sucursal.nombre = data.get('nombre', sucursal.nombre)
    sucursal.direccion = data.get('direccion', sucursal.direccion)
    sucursal.telefono = data.get('telefono', sucursal.telefono)
    db.session.commit()
    return jsonify(sucursal.to_dict())

# Eliminar una sucursal
@sucursal_bp.route('/sucursales/<int:id>', methods=['DELETE'])
def delete_sucursal(id):
    sucursal = Sucursal.query.get_or_404(id)
    db.session.delete(sucursal)
    db.session.commit()
    return jsonify({'message': 'Sucursal eliminada correctamente'}), 200