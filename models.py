from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    sucursal_id = db.Column(db.Integer)
    fecha_registro = db.Column(db.DateTime)

class Equipo(db.Model):
    __tablename__ = 'equipos'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    serial = db.Column(db.String(50), nullable=False)
    sucursal_id = db.Column(db.Integer)
    usuario_id = db.Column(db.Integer)
    fecha_registro = db.Column(db.DateTime)
