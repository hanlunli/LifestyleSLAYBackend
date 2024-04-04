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

class Loan():
    #Loading, pre-proccessing, and splitting of data
    def initialize():
        data_train = pd.read_csv('train.csv')
        data_train[' education'] = data_train[' education'].map({' Graduate': 1, ' Not Graduate': 0})
        data_train[' self_employed'] = data_train[' self_employed'].map({' Yes': 1, ' No': 0})
        data_train[" loan_status"]= data_train[" loan_status"].map({" Approved": 1, " Rejected": 0})
        X = data_train[[' no_of_dependents', ' education', ' self_employed', ' income_annum', ' loan_amount', ' loan_term',' cibil_score',' residential_assets_value',' commercial_assets_value',' luxury_assets_value',' bank_asset_value']]
        y = data_train[' loan_status']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        #Training Model (skipped b/c model already trained in file.)
        log_reg = LogisticRegression(solver='liblinear')
        log_reg.fit(X_train, y_train)
        save_path = "logistic_regression_model_loan.pkl"
        with open(save_path, 'wb') as model_file:
            pickle.dump(log_reg, model_file)

    #userInput=[pclass, sex, age, sibsp,fare]
    def predict(userInput):
        save_path = "logistic_regression_model_loan.pkl"
        userInput = pd.DataFrame.from_dict([userInput])
        with open(save_path, 'rb') as model_file:
            loaded_model = pickle.load(model_file)
        loan = loaded_model.predict_proba(userInput)[0]
        print(loan)
        return loan[1]
    
