from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Response, request

from api.models.module import Module


class ModulesApi(Resource):

    def get(self):
        module = Module.objects().to_json()
        return Response(module, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        module = Module(**body).save()
        id = instituto.id
        return {'id': str(id)}, 200


class ModuleApi(Resource):
    def get(self, id):
        module = Module.objects.get(id=id).to_json()
        return Response(curso, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Module.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Module.objects.get(id=id).delete()
        return '', 200
