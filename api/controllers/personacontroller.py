from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


from api.models.persona import Persona


class PersonasApi(Resource):

    def get(self):
        persona = Persona.objects().to_json()
        return Response(persona, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        persona = Persona(**body).save()
        id = persona.id
        return {'id': str(id)}, 200


class PersonaApi(Resource):
    def get(self, id):
        persona = Persona.objects.get(id=id).to_json()
        return Response(curso, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Persona.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Persona.objects.get(id=id).delete()
        return '', 200
