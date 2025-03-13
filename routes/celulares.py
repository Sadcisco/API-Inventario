from flask import Blueprint, jsonify, request
from models import Celular, db

celular_bp = Blueprint('celular', __name__)

@celular_bp.route('/celulares', methods=['GET'])
def get_celulares():
    celulares = Celular.query.all()
    return jsonify([c.to_dict() for c in celulares])

@celular_bp.route('/celulares/<int:id>', methods=['GET'])
def get_celular(id):
    celular = Celular.query.get_or_404(id)
    return jsonify(celular.to_dict())

@celular_bp.route('/celulares', methods=['POST'])
def create_celular():
    data = request.get_json()
    nuevo_celular = Celular(
        equipo_id=data['equipo_id'],
        ram=data['ram'],
        almacenamiento=data['almacenamiento'],
        sistema_operativo=data['sistema_operativo']
    )
    db.session.add(nuevo_celular)
    db.session.commit()
    return jsonify(nuevo_celular.to_dict()), 201

@celular_bp.route('/celulares/<int:id>', methods=['PUT'])
def update_celular(id):
    celular = Celular.query.get_or_404(id)
    data = request.get_json()
    celular.ram = data.get('ram', celular.ram)
    celular.almacenamiento = data.get('almacenamiento', celular.almacenamiento)
    celular.sistema_operativo = data.get('sistema_operativo', celular.sistema_operativo)
    db.session.commit()
    return jsonify(celular.to_dict())

@celular_bp.route('/celulares/<int:id>', methods=['DELETE'])
def delete_celular(id):
    celular = Celular.query.get_or_404(id)
    db.session.delete(celular)
    db.session.commit()
    return jsonify({'message': 'Celular eliminado correctamente'}), 200