from middlewares.conecction import db


class Examen(db.Document):
    preguntas = db.StringField(required=True)
    respuestas = db.StringField(required=True)
    estado = db.StringField(required=True)
    codigo_esudiante = db.IntField(required=True)
    fecha = db.StringField(required=True)
