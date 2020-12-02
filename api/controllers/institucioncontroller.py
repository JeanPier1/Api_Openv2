from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Response, request

from api.models.institucion import Institucion


class InstitucionesApi(Resource):

    def get(self):
        instituto = Institucion.objects().to_json()
        return Response(instituto, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        instituto = Institucion(**body).save()
        id = instituto.id
        return {'id': str(id)}, 200


class InstitucionApi(Resource):
    def get(self, id):
        instituto = Institucion.objects.get(id=id).to_json()
        return Response(curso, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Institucion.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Institucion.objects.get(id=id).delete()
        return '', 200
