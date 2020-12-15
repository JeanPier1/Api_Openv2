from middllewares.conecction import db


class Persona(db.Document):
    nombre = db.StringField(required=True, unique=True)
    apellidos = db.StringField(required=True)
    DNI = db.StringField(required=True, unique=True)
    codigo_universitario = db.StringField(required=True)
    user_id = db.StringField(required=True)
