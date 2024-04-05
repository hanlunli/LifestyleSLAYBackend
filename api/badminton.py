import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.badmintons import Badminton

badminton_api = Blueprint('badminton_api', __name__,
                   url_prefix='/badminton')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(badminton_api)

class BadmintonAPI:        
    class _CRUD(Resource):  # User API operation for Create, Read.  THe Update, Delete methods need to be implemeented
        def post(self): # Create method            
            data = request.get_json()
            badminton = Badminton(data.get('outlook'), data.get('temperature'), data.get('humidity'), data.get('wind'))
            return badminton.predict()

            
    # building RESTapi endpoint
    api.add_resource(_CRUD, '/')