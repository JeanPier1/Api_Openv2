from api.controllers.cursocontroller import CursoApi, CursosApi
from api.services.opencvservice import CapturandoRostros, reconocimientoFacial


def initialize_routes(api):
    api.add_resource(CursosApi, '/api/cursos')
    api.add_resource(CursoApi, '/api/cursos/<id>')

    # Solo ia

    api.add_resource(CapturandoRostros, '/api/cv')
    api.add_resource(reconocimientoFacial, '/api/cv/reconocimiento')
