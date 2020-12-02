# api/__app.py__

from flask import Flask
from flask_restful import Api
from .middlewares.conecction import initialize_db
from .routes.routehome import initialize_routes

app = Flask(__name__)
api = Api(app)

try:
    # creation of MongoClient
    app.config['MONGODB_SETTINGS'] = {
        "host": "mongodb://localhost/eduvi_nsql_test"
    }
    initialize_db(app)
except Exception as error:
    print("ERROR - Cannot connect to db")
    print(error)

# Routes - directions
initialize_routes(api)
