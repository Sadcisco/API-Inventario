from flask import Blueprint, jsonify, request
from models import TonerTambor, db

toner_tambor_bp = Blueprint('toner_tambor', __name__)

@toner_tambor_bp.route('/toner_tambor', methods=['GET'])
def get_toner_tambor():
    toner_tambor = TonerTambor.query.all()
    return jsonify([t.to_dict() for t in toner_tambor])

@toner_tambor_bp.route('/toner_tambor/<int:id>', methods=['GET'])
def get_toner_tambor_by_id(id):
    toner_tambor = TonerTambor.query.get_or_404(id)
    return jsonify(toner_tambor.to_dict())

@toner_tambor_bp.route('/toner_tambor', methods=['POST'])
def create_toner_tambor():
    data = request.get_json()
    nuevo_toner_tambor = TonerTambor(
        tipo=data['tipo'],
        modelo=data['modelo'],
        cantidad=data['cantidad'],
        impresora_id=data.get('impresora_id'),
        sucursal_id=data.get('sucursal_id'),
        usuario_id=data.get('usuario_id')
    )
    db.session.add(nuevo_toner_tambor)
    db.session.commit()
    return jsonify(nuevo_toner_tambor.to_dict()), 201

@toner_tambor_bp.route('/toner_tambor/<int:id>', methods=['PUT'])
def update_toner_tambor(id):
    toner_tambor = TonerTambor.query.get_or_404(id)
    data = request.get_json()
    toner_tambor.tipo = data.get('tipo', toner_tambor.tipo)
    toner_tambor.modelo = data.get('modelo', toner_tambor.modelo)
    toner_tambor.cantidad = data.get('cantidad', toner_tambor.cantidad)
    toner_tambor.impresora_id = data.get('impresora_id', toner_tambor.impresora_id)
    toner_tambor.sucursal_id = data.get('sucursal_id', toner_tambor.sucursal_id)
    toner_tambor.usuario_id = data.get('usuario_id', toner_tambor.usuario_id)
    db.session.commit()
    return jsonify(toner_tambor.to_dict())

@toner_tambor_bp.route('/toner_tambor/<int:id>', methods=['DELETE'])
def delete_toner_tambor(id):
    toner_tambor = TonerTambor.query.get_or_404(id)
    db.session.delete(toner_tambor)
    db.session.commit()
    return jsonify({'message': 'Toner/Tambor eliminado correctamente'}), 200