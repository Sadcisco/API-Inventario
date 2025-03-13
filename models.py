from extensions import db  # Cambia la importación relativa a absoluta

class Sucursal(db.Model):
    __tablename__ = 'sucursales'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    fecha_registro = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    equipos = db.relationship('Equipo', backref='sucursal', lazy=True)
    usuarios = db.relationship('Usuario', backref='sucursal', lazy=True)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum('admin', 'user'), default='user')
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'))
    fecha_registro = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    equipos = db.relationship('Equipo', backref='responsable', lazy=True)

class Equipo(db.Model):
    __tablename__ = 'equipos'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum('computadora', 'celular', 'impresora'), nullable=False)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    serial = db.Column(db.String(50), unique=True, nullable=False)
    responsable_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    cargo = db.Column(db.String(100))
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'))
    fecha_registro = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    fecha_revision = db.Column(db.TIMESTAMP)
    entregado = db.Column(db.Boolean, default=False)
    comentario = db.Column(db.Text)

    computadora = db.relationship('Computadora', backref='equipo', uselist=False, lazy=True)
    celular = db.relationship('Celular', backref='equipo', uselist=False, lazy=True)
    impresora = db.relationship('Impresora', backref='equipo', uselist=False, lazy=True)

class Computadora(db.Model):
    __tablename__ = 'computadoras'
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), unique=True)
    tipo = db.Column(db.Enum('pc', 'notebook'), nullable=False)
    procesador = db.Column(db.String(100))
    ram = db.Column(db.String(50))
    disco = db.Column(db.String(100))
    office = db.Column(db.String(100))
    antivirus = db.Column(db.String(100))
    drive = db.Column(db.String(100))
    nombre_maquina = db.Column(db.String(100))

class Celular(db.Model):
    __tablename__ = 'celulares'
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), unique=True)
    ram = db.Column(db.String(50))
    almacenamiento = db.Column(db.String(50))
    sistema_operativo = db.Column(db.String(50))

class Impresora(db.Model):
    __tablename__ = 'impresoras'
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), unique=True)
    tipo_toner = db.Column(db.String(50))
    capacidad_toner = db.Column(db.String(50))
    velocidad_impresion = db.Column(db.String(50))

class TonerTambor(db.Model):
    __tablename__ = 'toner_tambor'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum('toner', 'tambor'), nullable=False)
    modelo = db.Column(db.String(50))
    cantidad = db.Column(db.Integer, default=0)
    impresora_id = db.Column(db.Integer, db.ForeignKey('impresoras.id'))
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    fecha_registro = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Envio(db.Model):
    __tablename__ = 'envios'
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'))
    toner_tambor_id = db.Column(db.Integer, db.ForeignKey('toner_tambor.id'))
    sucursal_origen_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'))
    sucursal_destino_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'))
    cantidad = db.Column(db.Integer)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    fecha_envio = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())