from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
import pandas as pd
from xgboost import XGBClassifier

app = Flask(__name__)
CORS(app)

water_api = Blueprint('water_api', __name__)  # Define a Flask Blueprint named 'water_api'

class WaterPotabilityModel:
    def __init__(self, data_file):
        self.data = pd.read_csv(data_file)
        self.X = self.data.drop(columns=['Potability'])
        self.y = self.data['Potability']
        self.model = XGBClassifier()
        self.model.fit(self.X, self.y)

    def predict_potability(self, user_data):
        user_data = pd.DataFrame(user_data, index=[0])  # Convert user input to DataFrame
        prediction = self.model.predict(user_data)
        return "potable" if prediction[0] == 1 else "not potable"

water_model = WaterPotabilityModel("water_potability.csv")

@water_api.route('/water/predict', methods=['POST'])  # Use the water_api Blueprint for the route
def predict_water_potability():
    print('aslkdfj')
    try:
        user_data = request.get_json()  # Get user input from request
        prediction = water_model.predict_potability(pd.DataFrame(user_data, index=[0]))
        print(user_data)
        return jsonify({"prediction": prediction}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

app.register_blueprint(water_api, url_prefix='/water')  # Register the water_api Blueprint with the Flask application

if __name__ == '__main__':
    app.run(port=8086)  # Adjust port as needed
