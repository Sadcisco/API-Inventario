from flask import Flask
from extensions import db
from routes.sucursales import sucursal_bp
from routes.equipos import equipo_bp
from routes.usuarios import usuario_bp
from routes.computadoras import computadora_bp
from routes.celulares import celular_bp
from routes.impresoras import impresora_bp
from routes.toner_tambor import toner_tambor_bp
from routes.envios import envio_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@localhost/inventario_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registrar Blueprints
    app.register_blueprint(sucursal_bp, url_prefix='/api')
    app.register_blueprint(equipo_bp, url_prefix='/api')
    app.register_blueprint(usuario_bp, url_prefix='/api')
    app.register_blueprint(computadora_bp, url_prefix='/api')
    app.register_blueprint(celular_bp, url_prefix='/api')
    app.register_blueprint(impresora_bp, url_prefix='/api')
    app.register_blueprint(toner_tambor_bp, url_prefix='/api')
    app.register_blueprint(envio_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)