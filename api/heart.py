import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required
import pdb

from model.heart import Heart

heart_api = Blueprint('heart_api', __name__,
                   url_prefix='/api/heart')

api = Api(heart_api)

class HeartAPI:
    class Predict(Resource):
        def get(self):
            Heart.initialize()
            return { 'message': "training complete" }
        
        def post(self):
            body = request.get_json()
            print(body)
            # Initializing all parameters
            age = body.get('age')
            if age is None:
                return {'message': f'age is missing'}, 400
            
            sex = body.get('sex')
            if sex is None:
                return {'message': f'Sex is missing'}, 400
            
            cp = body.get('cp')
            if cp is None:
                return {'message': f'CP is missing'}, 400
            
            trtbps = body.get('trtbps')
            if trtbps is None:
                return {'message': f'Trtbps is missing'}, 400
            
            chol = body.get('chol')
            if chol is None:
                return {'message': f'Chol is missing'}, 400
            
            fbs = body.get('fbs')
            if fbs is None:
                return {'message': f'Fbs is missing'}, 400
            
            restecg = body.get('restecg')
            if restecg is None:
                return {'message': f'Restecg is missing'}, 400
            
            thalachh = body.get('thalachh')
            if thalachh is None:
                return {'message': f'Thalachh is missing'}, 400
            
            exng = body.get('exng')
            if exng is None:
                return {'message': f'Exng is missing'}, 400
            
            oldpeak = body.get('oldpeak')
            if oldpeak is None:
                return {'message': f'Oldpeak is missing'}, 400
            
            slp = body.get('slp')
            if slp is None:
                return {'message': f'Slp is missing'}, 400
            
            caa = body.get('caa')
            if caa is None:
                return {'message': f'Caa is missing'}, 400
            
            thall = body.get('thall')
            if thall is None:
                return {'message': f'Thall is missing'}, 400
                        
            result = Heart.predict(body)
            
            return {'message': result}
        
    api.add_resource(Predict, '/predict')       

            
            