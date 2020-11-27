from middlewares.conecction import db


class Recurso(db.Document):
    nombre = db.StringField(required=True, unique=True)
    descripcion = db.StringField(required=True)
    link = db.StringField(required=True)
