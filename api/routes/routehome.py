# Services

from api.services.opencvservice import CapturandoRostros, reconocimientoFacial

# Controller
from api.controllers.cursocontroller import CursoApi, CursosApi
from api.controllers.authcontroller import SignupApi, LoginApi, RoleApi, RolesApi
from api.controllers.examencontroller import ExamenApi, ExamenesApi
from api.controllers.institucioncontroller import InstitucionApi, InstitucionesApi
from api.controllers.modulecontroller import ModuleApi, ModulesApi
from api.controllers.personacontroller import PersonaApi, PersonasApi
from api.controllers.recursocontroller import RecursoApi, RecursosApi


def initialize_routes(api):
    # Solo ia

    api.add_resource(CapturandoRostros, '/api/cv')
    api.add_resource(reconocimientoFacial, '/api/cv/reconocimiento')

    # Curso
    api.add_resource(CursosApi, '/api/cursos')
    api.add_resource(CursoApi, '/api/cursos/<id>')

    # Salida de user
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    # Salida de roles
    api.add_resource(RolesApi, '/api/role')
    api.add_resource(RoleApi, '/api/role/<id>')

    # Salida de examen

    api.add_resource(ExamenesApi, '/api/examen')
    api.add_resource(ExamenApi, '/api/exammen/<id>')

    # Salida del institucion
    api.add_resource(InstitucionesApi, '/api/institucion')
    api.add_resource(InstitucionApi, '/api/institucion/<id>')

    # salida del module

    api.add_resource(ModulesApi, '/api/module')
    api.add_resource(ModuleApi, '/api/module/<id>')

    # salida de persona

    api.add_resource(PersonasApi, '/api/module')
    api.add_resource(PersonaApi, '/api/module/<id>')

    # salida de recurso
    api.add_resource(RecursosApi, '/api/module')
    api.add_resource(RecursoApi, '/api/module/<id>')
