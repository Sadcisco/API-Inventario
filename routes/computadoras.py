from flask import Blueprint, jsonify, request
from models import Computadora, db

computadora_bp = Blueprint('computadora', __name__)

@computadora_bp.route('/computadoras', methods=['GET'])
def get_computadoras():
    computadoras = Computadora.query.all()
    return jsonify([c.to_dict() for c in computadoras])

@computadora_bp.route('/computadoras/<int:id>', methods=['GET'])
def get_computadora(id):
    computadora = Computadora.query.get_or_404(id)
    return jsonify(computadora.to_dict())

@computadora_bp.route('/computadoras', methods=['POST'])
def create_computadora():
    data = request.get_json()
    nueva_computadora = Computadora(
        equipo_id=data['equipo_id'],
        tipo=data['tipo'],
        procesador=data['procesador'],
        ram=data['ram'],
        disco=data['disco'],
        office=data['office'],
        antivirus=data['antivirus'],
        drive=data['drive'],
        nombre_maquina=data['nombre_maquina']
    )
    db.session.add(nueva_computadora)
    db.session.commit()
    return jsonify(nueva_computadora.to_dict()), 201

@computadora_bp.route('/computadoras/<int:id>', methods=['PUT'])
def update_computadora(id):
    computadora = Computadora.query.get_or_404(id)
    data = request.get_json()
    computadora.tipo = data.get('tipo', computadora.tipo)
    computadora.procesador = data.get('procesador', computadora.procesador)
    computadora.ram = data.get('ram', computadora.ram)
    computadora.disco = data.get('disco', computadora.disco)
    computadora.office = data.get('office', computadora.office)
    computadora.antivirus = data.get('antivirus', computadora.antivirus)
    computadora.drive = data.get('drive', computadora.drive)
    computadora.nombre_maquina = data.get('nombre_maquina', computadora.nombre_maquina)
    db.session.commit()
    return jsonify(computadora.to_dict())

@computadora_bp.route('/computadoras/<int:id>', methods=['DELETE'])
def delete_computadora(id):
    computadora = Computadora.query.get_or_404(id)
    db.session.delete(computadora)
    db.session.commit()
    return jsonify({'message': 'Computadora eliminada correctamente'}), 200