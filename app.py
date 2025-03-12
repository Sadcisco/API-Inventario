from flask import Flask, jsonify, request
from flask_cors import CORS
from extensions import db
from models import Equipo
from dotenv import load_dotenv
import os

# Importa las rutas
from routes import routes_bp

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuración de conexión MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos
db.init_app(app)

with app.app_context():
    db.create_all()

# Registrar rutas adicionales
app.register_blueprint(routes_bp)

@app.before_request
def handle_preflight():
    if request.method == 'OPTIONS':
        return '', 200

@app.route('/')
def index():
    return jsonify({"message": "API de Inventario funcionando correctamente"})

@app.route('/equipos', methods=['GET'])
def get_equipos():
    equipos = Equipo.query.all()
    return jsonify([{
        'id': e.id,
        'tipo': e.tipo,
        'modelo': e.modelo,
        'serial': e.serial,
        'sucursal_id': e.sucursal_id,
        'usuario_id': e.usuario_id,
        'fecha_registro': e.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')
    } for e in equipos])

@app.route('/equipos', methods=['POST'])
def add_equipo():
    data = request.json
    nuevo_equipo = Equipo(
        tipo=data['tipo'],
        modelo=data['modelo'],
        serial=data['serial'],
        sucursal_id=data['sucursal_id'],
        usuario_id=data['usuario_id']
    )
    db.session.add(nuevo_equipo)
    db.session.commit()
    return jsonify({'message': 'Equipo agregado correctamente'}), 201

@app.route('/equipos/<int:id>', methods=['DELETE'])
def eliminar_equipo(id):
    equipo = Equipo.query.get(id)
    if not equipo:
        return jsonify({'mensaje': 'Equipo no encontrado'}), 404

    db.session.delete(equipo)
    db.session.commit()
    return jsonify({'mensaje': 'Equipo eliminado correctamente'}), 200

@app.route('/equipos/<int:id>', methods=['PUT'])
def editar_equipo(id):
    data = request.json
    equipo = Equipo.query.get(id)
    if not equipo:
        return jsonify({'mensaje': 'Equipo no encontrado'}), 404

    equipo.tipo = data.get('tipo', equipo.tipo)
    equipo.modelo = data.get('modelo', equipo.modelo)
    equipo.serial = data.get('serial', equipo.serial)
    equipo.sucursal_id = data.get('sucursal_id', equipo.sucursal_id)
    equipo.usuario_id = data.get('usuario_id', equipo.usuario_id)

    db.session.commit()
    return jsonify({'mensaje': 'Equipo actualizado correctamente'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
