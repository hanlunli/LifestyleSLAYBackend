import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required
import pdb

from model.stroke import Stroke

stroke_api = Blueprint('stroke_api', __name__,
                   url_prefix='/api/stroke')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(stroke_api)
class StrokeAPI:        
    class Predict(Resource): 
        def get(self):
            Stroke.initialize()
            return { 'message': "training complete" }

        def post(self):
            body = request.get_json()
            print(body)
            # Initializing all parameters
            gender = body.get('gender')
            if gender is None:
                return {'message': f'gender is missing'}, 400
            age = body.get('age')
            if age is None:
                return {'message': f'age is missing'}, 400
            hypertension = body.get('hypertension')
            if hypertension is None:
                return {'message': f'hypertension is missing'}, 400
            heart_disease = body.get('heart_disease')
            if heart_disease is None:
                return {'message': f'heart_disease is missing'}, 400
            ever_married = body.get('ever_married')
            if ever_married is None:
                return {'message': f'ever_married is missing'}, 400
            avg_glucose_level = body.get('avg_glucose_level')
            if avg_glucose_level is None:
                return {'message': f'avg_glucose_level is missing'}, 400
            bmi = body.get('bmi')
            if bmi is None:
                return {'message': f'bmi is missing'}, 400
            
            result = Stroke.predict(body)
            
            return { 'message': result }
        
    api.add_resource(Predict, '/predict')