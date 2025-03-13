from flask import Blueprint, jsonify, request
from models import Envio, db

envio_bp = Blueprint('envio', __name__)

@envio_bp.route('/envios', methods=['GET'])
def get_envios():
    envios = Envio.query.all()
    return jsonify([e.to_dict() for e in envios])

@envio_bp.route('/envios/<int:id>', methods=['GET'])
def get_envio(id):
    envio = Envio.query.get_or_404(id)
    return jsonify(envio.to_dict())

@envio_bp.route('/envios', methods=['POST'])
def create_envio():
    data = request.get_json()
    nuevo_envio = Envio(
        equipo_id=data.get('equipo_id'),
        toner_tambor_id=data.get('toner_tambor_id'),
        sucursal_origen_id=data['sucursal_origen_id'],
        sucursal_destino_id=data['sucursal_destino_id'],
        cantidad=data.get('cantidad', 1),
        usuario_id=data['usuario_id']
    )
    db.session.add(nuevo_envio)
    db.session.commit()
    return jsonify(nuevo_envio.to_dict()), 201

@envio_bp.route('/envios/<int:id>', methods=['PUT'])
def update_envio(id):
    envio = Envio.query.get_or_404(id)
    data = request.get_json()
    envio.equipo_id = data.get('equipo_id', envio.equipo_id)
    envio.toner_tambor_id = data.get('toner_tambor_id', envio.toner_tambor_id)
    envio.sucursal_origen_id = data.get('sucursal_origen_id', envio.sucursal_origen_id)
    envio.sucursal_destino_id = data.get('sucursal_destino_id', envio.sucursal_destino_id)
    envio.cantidad = data.get('cantidad', envio.cantidad)
    envio.usuario_id = data.get('usuario_id', envio.usuario_id)
    db.session.commit()
    return jsonify(envio.to_dict())

@envio_bp.route('/envios/<int:id>', methods=['DELETE'])
def delete_envio(id):
    envio = Envio.query.get_or_404(id)
    db.session.delete(envio)
    db.session.commit()
    return jsonify({'message': 'Envío eliminado correctamente'}), 200