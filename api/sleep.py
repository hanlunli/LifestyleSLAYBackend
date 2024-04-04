import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.sleeps import Sleep

sleep_api = Blueprint('sleep_api', __name__,
                   url_prefix='/sleep')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(sleep_api)

class SleepAPI:        
    class _CRUD(Resource):  # User API operation for Create, Read.  THe Update, Delete methods need to be implemeented
        def post(self): # Create method            
            data = request.get_json()
            sleep = Sleep.predict(data)
            print(data)
            return sleep

            
    # building RESTapi endpoint
    api.add_resource(_CRUD, '/')