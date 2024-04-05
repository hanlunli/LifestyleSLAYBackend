#Importating Packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pdb
import pickle
from sklearn.metrics import accuracy_score

class Stroke():
    def initialize():
        data_train = pd.read_csv('trainStroke.csv')
        data_train['age'].fillna(data_train['age'].mean(), inplace=True)
        data_train['bmi'].fillna(data_train['bmi'].mean(), inplace=True)
        # Encode 'gender' and 'ever_married' column
        data_train['gender'] = data_train['gender'].map({'Male': 1, 'Female': 0})
        data_train['ever_married'] = data_train['ever_married'].map({'Yes': 1, 'No': 0})
        # Select features and target variable
        X = data_train[['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'avg_glucose_level','bmi']]
        y = data_train['stroke']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        #Training Model
        log_reg = LogisticRegression(solver='liblinear')
        log_reg.fit(X_train, y_train)
        save_path = "logistic_regression_model_stroke.pkl"
        with open(save_path, 'wb') as model_file:
            pickle.dump(log_reg, model_file)
    #userInput=[pclass, sex, age, sibsp,fare]
    def predict(userInput):
        save_path = "logistic_regression_model_stroke.pkl"
        userInput = pd.DataFrame.from_dict([userInput])
        with open(save_path, 'rb') as model_file:
            loaded_model = pickle.load(model_file)
        stroke = loaded_model.predict_proba(userInput)[0]
        print(stroke)
        return stroke[1]
    
