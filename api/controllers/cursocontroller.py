from flask import Response, request
from api.models.curso import Curso
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class CursosApi(Resource):

    def get(self):
        cursos = Curso.objects().to_json()
        return Response(cursos, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        curso = Curso(**body).save()
        id = curso.id
        return {'id': str(id)}, 200


class CursoApi(Resource):
    def get(self, id):
        curso = Curso.objects.get(id=id).to_json()
        return Response(curso, mimetype="application/json", status=200)

    @jwt_required
    def put(self, id):
        body = request.get_json()
        Curso.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Curso.objects.get(id=id).delete()
        return '', 200
