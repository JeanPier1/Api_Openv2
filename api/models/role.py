from middllewares.conecction import db


class Role(db.Document):
    nombre = db.StringField(required=True, unique=True)
    estado = db.StringField(required=True)
    addid_by = db.ReferenceField('User')
