# api/__app.py__

from flask import Flask, render_template, Response, url_for, redirect, request
from flask_restful import Api
from .middlewares.conecction import initialize_db
from .routes.routehome import initialize_routes
import os


# Clases Opencv
from .services.opencvservice_reconocimiento import reconocimientofc, Recursos
from .services.opencvservice_recopilacion import recopilacion


# Security
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
    JWTManager)

app = Flask(__name__)
api = Api(app)

# Secret JWT
SECRET_KEY = os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = ['cookies', 'headers']
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/'

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


try:
    # creation of MongoClient
    app.config['MONGODB_SETTINGS'] = {
        "host": "mongodb://localhost/eduvi_nsql_test"
    }
    initialize_db(app)
except Exception as error:
    print("ERROR - Cannot connect to db")
    print(error)

# Template


# def gen(camera):
#     while True:
#         data = camera.get_frame()
#         frame = data[0]
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# @app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')

@jwt_required
@app.route('/video_feed/<int:cod>/<string:nom>')
def video_feed(cod, nom):
    return Response(Recursos(cod, nom), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_recono/<int:tiempo>/')
def video_recono(tiempo):
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(reconocimientofc(tiempo), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/guardar_rostro/<int:cod>/<string:nom>', methods=['GET'])
def guardar_rostro(cod, nom):
    return Response(recopilacion(cod, nom), mimetype='multipart/x-mixed-replace; boundary=frame')


#  implementacion
@app.route('/recopilar_rostro')
def Imple_recopilar_rostro():
    return render_template('recopilacion.html')


@app.route('/reconocer_rostros')
def Imple_reconocer_rostro():
    return render_template('reconocimiento.html')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template("about.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")


@app.route('/app', methods=['POST', 'GET'])
@jwt_required
def template_app():
    return "/main", 200


@app.route("/main", methods=['GET'])
def main():
    return render_template("app.html")

# Validacion de es


@app.route("/tiempo", methods=['POST'])
def tiempo_a():
    body = request.get_json()
    tiempo = body['tiempo']
    return tiempo


@app.route("/datos", methods=['POST'])
def datos_a():
    body = request.get_json()
    print(body)
    return body


# Routes - directions
initialize_routes(api)
