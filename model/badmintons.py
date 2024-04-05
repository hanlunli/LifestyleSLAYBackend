from random import randrange
from datetime import date
import os
import base64
import json
from flask import Blueprint, request, jsonify, current_app, Response
from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

df = pd.read_csv('badminton_dataset.csv')
dataList = ['Outlook', 'Temperature', 'Humidity', 'Wind', 'Play_Badminton']
labelencoder = LabelEncoder()
X = df.drop(columns=['Play_Badminton'])
y = df['Play_Badminton']
regressor = RandomForestRegressor(n_estimators=10, random_state=42)
regressor.fit(X, y)

def stringToInt(var):
    if var == 'yes':
        var = 1
    elif var == 'no':
        var = 0
    else:
        var = int(var)
    return var

class Badminton():
    def __init__(self, outlook, temperature, humidity, wind):
        self._outlook = outlook
        self._temperature = temperature
        self._humidity = humidity
        self._wind = wind

    @property
    def outlook(self):
        return self._outlook

    @outlook.setter
    def outlook(self, value):
        self._outlook = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value

    @property
    def wind(self):
        return self._wind

    @wind.setter
    def wind(self, value):
        self._wind = value

    # @property
    # def play_badminton(self):
    #     return self._play_badminton

    # @play_badminton.setter
    # def play_badminton(self, value):
    #     self._play_badminton = value

    def predict(self):
        # Ensure all features are properly converted
        self._outlook = stringToInt(self._outlook)
        self._temperature = stringToInt(self._temperature)
        self._humidity = stringToInt(self._humidity)
        self._wind = stringToInt(self._wind)

        varList = [self._outlook, self._temperature, self._humidity, self._wind]

        # Ensure the same number of features as the model expects

        # Predicting the price
        predicted_badminton = regressor.predict([varList])[0]
        if predicted_badminton == 0:
            string = 'no'
        else:
            string = 'yes'
        return string


"""Database Creation and Testing """
