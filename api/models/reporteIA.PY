from api.middlewares.conecction import db


class ReporteIA(db.Document):
    nombre = db.StringField(required=True)
    descripcion = db.StringField(required=True)
    link = db.StringField(required=True)
