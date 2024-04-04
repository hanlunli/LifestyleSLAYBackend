import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required
import pdb

from model.loans import Loan #imports titanic data

loan_api = Blueprint('loan_api', __name__,
                   url_prefix='/api/loan')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(loan_api)
class LoanAPI:        
    class Predict(Resource): 
        def get(self):
            Loan.initialize()
            return { 'message': "training complete" }
        def post(self):
            body = request.get_json()
            print(body)
            # Initializing all parameters
            no_of_dependents = body.get(' no_of_dependents')
            if no_of_dependents is None:
                return {'message': f'no_of_dependents is missing'}, 400

            education = body.get(' education')
            if education is None:
                return {'message': f'education is missing'}, 400

            self_employed = body.get(' self_employed')
            if self_employed is None:
                return {'message': f'self_employed is missing'}, 400

            income_annum = body.get(' income_annum')
            if income_annum is None:
                return {'message': f'income_annum is missing'}, 400

            loan_amount = body.get(' loan_amount')
            if loan_amount is None:
                return {'message': f'loan_amount is missing'}, 400

            loan_term = body.get(' loan_term')
            if loan_term is None:
                return {'message': f'loan_term is missing'}, 400

            cibil_score = body.get(' cibil_score')
            if cibil_score is None:
                return {'message': f'cibil_score is missing'}, 400

            residential_assets_value = body.get(' residential_assets_value')
            if residential_assets_value is None:
                return {'message': f'residential_assets_value is missing'}, 400

            commercial_assets_value = body.get(' commercial_assets_value')
            if commercial_assets_value is None:
                return {'message': f'commercial_assets_value is missing'}, 400

            luxury_assets_value = body.get(' luxury_assets_value')
            if luxury_assets_value is None:
                return {'message': f'luxury_assets_value is missing'}, 400

            bank_asset_value = body.get(' bank_asset_value')
            if bank_asset_value is None:
                return {'message': f'bank_asset_value is missing'}, 400

            result = Loan.predict(body)
            
            return { 'message': result }
        
    api.add_resource(Predict, '/predict')