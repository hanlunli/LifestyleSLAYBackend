from flask import Blueprint, request, jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor  # Import RandomForestRegressor
import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
sleep_api = Blueprint('sleep_api', __name__,
                   url_prefix='/sleep')
# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(sleep_api)

# Load the trained model and label encoder
df = pd.read_csv('sleep.csv')
labelencoder = LabelEncoder()
df['BMI Category'] = labelencoder.fit_transform(df['BMI Category'])

X = df.drop(columns=['sleep_disorder'])
y = df['sleep_disorder']
regressor = RandomForestRegressor(n_estimators=10, random_state=42)
regressor.fit(X, y)


class Sleep():
    def __init__(self):
        self._sleep_duration = None
        self._quality_of_sleep = None
        self._physical_activity_level = None
        self._stress_level = None
        self._bmi_category = None
        self._blood_pressure = None
        self._heart_rate = None
        self._daily_steps = None

    def predict(data):
        # Get JSON data from request

        # Create a Sleep instance
        new_sleep = Sleep()

        # Set attributes using setter methods
        new_sleep.sleep_duration = data['sleep_duration']
        new_sleep.quality_of_sleep = data['quality_of_sleep']
        new_sleep.physical_activity_level = data['physical_activity_level']
        new_sleep.stress_level = data['stress_level']
        new_sleep.bmi_category = data['bmi_category']
        new_sleep.blood_pressure = data['blood_pressure']
        new_sleep.heart_rate = data['heart_rate']
        new_sleep.daily_steps = data['daily_steps']

        # Prepare input data for prediction
        input_data = pd.DataFrame({
            'Sleep Duration': [new_sleep.sleep_duration],
            'Quality of Sleep': [new_sleep.quality_of_sleep],
            'Physical Activity Level': [new_sleep.physical_activity_level],
            'Stress Level': [new_sleep.stress_level],
            'BMI Category': [new_sleep.bmi_category],
            'Blood Pressure': [new_sleep.blood_pressure],
            'Heart Rate': [new_sleep.heart_rate],
            'Daily Steps': [new_sleep.daily_steps]
        })

        # Use the trained model to make predictions
        predicted_disorder = regressor.predict(input_data)

        # Respond with the prediction
        return jsonify({'predicted_sleep_disorder': determine_closest_decimal(predicted_disorder[0])})
def determine_closest_decimal(decimal_value):
    distance_to_0 = abs(decimal_value - 0)
    distance_to_1 = abs(decimal_value - 1)
    distance_to_2 = abs(decimal_value - 2)

    if distance_to_0 < distance_to_1 and distance_to_0 < distance_to_2:
        return ("no sleep disorder")
    elif distance_to_1 < distance_to_0 and distance_to_1 < distance_to_2:
        return ("sleep apnea")
    else:
        return ("insomnia")

