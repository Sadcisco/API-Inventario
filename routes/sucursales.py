from flask import Blueprint, jsonify, request
from models import Sucursal, db

sucursal_bp = Blueprint('sucursal', __name__)

@sucursal_bp.route('/sucursales', methods=['GET'])
def get_sucursales():
    sucursales = Sucursal.query.all()
    return jsonify([s.to_dict() for s in sucursales])

@sucursal_bp.route('/sucursales/<int:id>', methods=['GET'])
def get_sucursal(id):
    sucursal = Sucursal.query.get_or_404(id)
    return jsonify(sucursal.to_dict())

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

@sucursal_bp.route('/sucursales/<int:id>', methods=['PUT'])
def update_sucursal(id):
    sucursal = Sucursal.query.get_or_404(id)
    data = request.get_json()
    sucursal.nombre = data.get('nombre', sucursal.nombre)
    sucursal.direccion = data.get('direccion', sucursal.direccion)
    sucursal.telefono = data.get('telefono', sucursal.telefono)
    db.session.commit()
    return jsonify(sucursal.to_dict())

@sucursal_bp.route('/sucursales/<int:id>', methods=['DELETE'])
def delete_sucursal(id):
    sucursal = Sucursal.query.get_or_404(id)
    db.session.delete(sucursal)
    db.session.commit()
    return jsonify({'message': 'Sucursal eliminada correctamente'}), 200