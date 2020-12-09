# api/__app.py__

from flask import Flask, render_template, Response
from flask_restful import Api
from .middlewares.conecction import initialize_db
from .routes.routehome import initialize_routes
import os


# Clases Opencv
from .services.opencvservice_reconocimiento import reconocimientofc, Recursos
from .services.opencvservice_recopilacion import recopilacion


# Security
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

# Secret JWT
SECRET_KEY = os.urandom(24)
app.config['SECRET_KEY'] = SECRET_KEY
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


# Routes - directions
initialize_routes(api)
