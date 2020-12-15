from middllewares.conecction import db
from models.role import Role
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Document):
    correo = db.StringField(required=True, unique=True)
    celular = db.IntField(required=True)
    constrasena = db.StringField(required=True)
    roles = db.ListField(db.ReferenceField(
        'Role', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.constrasena = generate_password_hash(
            self.constrasena).decode('utf8')

    def check_password(self, constrasena):
        return check_password_hash(self.constrasena, constrasena)


User.register_delete_rule(Role, 'added_by', db.CASCADE)
