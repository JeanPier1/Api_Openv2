from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Response, request


from models.examen import Examen


class ExamenesApi(Resource):

    def get(self):
        examen = Examen.objects().to_json()
        return Response(examen, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        examen = Examen(**body).save()
        id = examen.id
        return {'id': str(id)}, 200


class ExamenApi(Resource):
    def get(self, id):
        examen = Examen.objects.get(id=id).to_json()
        return Response(curso, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Examen.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Examen.objects.get(id=id).delete()
        return '', 200
