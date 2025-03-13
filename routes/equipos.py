from flask import Blueprint, jsonify, request
from models import Equipo, db

equipo_bp = Blueprint('equipo', __name__)

@equipo_bp.route('/equipos', methods=['GET'])
def get_equipos():
    equipos = Equipo.query.all()
    return jsonify([e.to_dict() for e in equipos])

@equipo_bp.route('/equipos/<int:id>', methods=['GET'])
def get_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    return jsonify(equipo.to_dict())

@equipo_bp.route('/equipos', methods=['POST'])
def create_equipo():
    data = request.get_json()
    nuevo_equipo = Equipo(
        tipo=data['tipo'],
        marca=data['marca'],
        modelo=data['modelo'],
        serial=data['serial'],
        responsable_id=data['responsable_id'],
        cargo=data['cargo'],
        sucursal_id=data['sucursal_id'],
        fecha_revision=data.get('fecha_revision'),
        entregado=data.get('entregado', False),
        comentario=data.get('comentario')
    )
    db.session.add(nuevo_equipo)
    db.session.commit()
    return jsonify(nuevo_equipo.to_dict()), 201

@equipo_bp.route('/equipos/<int:id>', methods=['PUT'])
def update_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    data = request.get_json()
    equipo.tipo = data.get('tipo', equipo.tipo)
    equipo.marca = data.get('marca', equipo.marca)
    equipo.modelo = data.get('modelo', equipo.modelo)
    equipo.serial = data.get('serial', equipo.serial)
    equipo.responsable_id = data.get('responsable_id', equipo.responsable_id)
    equipo.cargo = data.get('cargo', equipo.cargo)
    equipo.sucursal_id = data.get('sucursal_id', equipo.sucursal_id)
    equipo.fecha_revision = data.get('fecha_revision', equipo.fecha_revision)
    equipo.entregado = data.get('entregado', equipo.entregado)
    equipo.comentario = data.get('comentario', equipo.comentario)
    db.session.commit()
    return jsonify(equipo.to_dict())

@equipo_bp.route('/equipos/<int:id>', methods=['DELETE'])
def delete_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return jsonify({'message': 'Equipo eliminado correctamente'}), 200