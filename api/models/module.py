from api.middlewares.conecction import db


class Module(db.Document):
    nombre = db.StringField(required=True, unique=True)
    descripcion = db.StringField(required=True)
    url = db.StringField(required=True)
