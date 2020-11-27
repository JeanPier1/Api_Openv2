from middlewares.conecction import db


class User(db.Document):
    correo = db.StringField(required=True, unique=True)
    celular = db.IntField(required=True)
    constrasena = db.StringField(required=True)
    roles = db.ListField(StringField(required=True))
