from flask import Response, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
import datetime

from api.models.user import User
from api.models.role import Role

# class

from api.services.errors import errors, UnauthorizedError
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist


class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            return errors['SchemaValidationError']
        except NotUniqueError:
            return errors['EmailAlreadyExistsError']
        except Exception as e:
            print(e)
            return errors['InternalServerError']


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(correo=body.get('correo'))
            authorized = user.check_password(body.get('contrasena'))
            if not authorized:
                return errors['UnauthorizedError']

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(
                identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            return errors['UnauthorizedError']
        except Exception as e:
            print(e)
            return errors['InternalServerError']

# Roles Usuarios


class RolesApi(Resource):
    def get(self):
        roles = Role.objects().to_json()
        return Response(roles, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        roles = Role(**body).save()
        id = roles.id
        return {'id': str(id)}, 200


class RoleApi(Resource):
    def get(self, id):
        role = Role.objects.get(id=id).to_json()
        return Response(role, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_data()
        Role.objects.get(id=id).update(**body)
        return '', 200

    # Prueba de eleiminar
    # def delete(self, id):
    #     Role.objects.get(id=id).delete()
    #     return '',200