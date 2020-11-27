from middlewares.conecction import db


class Institucion(db.Document):
    nombre = db.StringField(required=True, unique=True)
    direccion = db.StringField(required=True)
    descripcion = db.StringField(required=True)
    estado = db.StringField(required=True)
