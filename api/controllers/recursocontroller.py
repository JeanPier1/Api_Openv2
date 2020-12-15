from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Response, request

from models.recurso import Recurso


class RecursosApi(Resource):

    def get(self):
        recurso = Recurso.objects().to_json()
        return Response(recurso, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        recurso = Recurso(**body).save()
        id = recurso.id
        return {'id': str(id)}, 200


class RecursoApi(Resource):
    def get(self, id):
        recurso = Recurso.objects.get(id=id).to_json()
        return Response(curso, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Recurso.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Recurso.objects.get(id=id).delete()
        return '', 200
