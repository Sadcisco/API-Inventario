from flask import Blueprint, jsonify, request
from models import Impresora, db

impresora_bp = Blueprint('impresora', __name__)

@impresora_bp.route('/impresoras', methods=['GET'])
def get_impresoras():
    impresoras = Impresora.query.all()
    return jsonify([i.to_dict() for i in impresoras])

@impresora_bp.route('/impresoras/<int:id>', methods=['GET'])
def get_impresora(id):
    impresora = Impresora.query.get_or_404(id)
    return jsonify(impresora.to_dict())

@impresora_bp.route('/impresoras', methods=['POST'])
def create_impresora():
    data = request.get_json()
    nueva_impresora = Impresora(
        equipo_id=data['equipo_id'],
        tipo_toner=data['tipo_toner'],
        capacidad_toner=data['capacidad_toner'],
        velocidad_impresion=data['velocidad_impresion']
    )
    db.session.add(nueva_impresora)
    db.session.commit()
    return jsonify(nueva_impresora.to_dict()), 201

@impresora_bp.route('/impresoras/<int:id>', methods=['PUT'])
def update_impresora(id):
    impresora = Impresora.query.get_or_404(id)
    data = request.get_json()
    impresora.tipo_toner = data.get('tipo_toner', impresora.tipo_toner)
    impresora.capacidad_toner = data.get('capacidad_toner', impresora.capacidad_toner)
    impresora.velocidad_impresion = data.get('velocidad_impresion', impresora.velocidad_impresion)
    db.session.commit()
    return jsonify(impresora.to_dict())

@impresora_bp.route('/impresoras/<int:id>', methods=['DELETE'])
def delete_impresora(id):
    impresora = Impresora.query.get_or_404(id)
    db.session.delete(impresora)
    db.session.commit()
    return jsonify({'message': 'Impresora eliminada correctamente'}), 200