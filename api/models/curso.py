from middllewares.conecction import db


class Curso(db.Document):
    nombre = db.StringField(required=True, unique=True)
    descripcion = db.StringField(required=True)
