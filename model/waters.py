import pandas as pd
from xgboost import XGBClassifier

class WaterPotabilityModel:
    def __init__(self, data_file):
        self.data = pd.read_csv(data_file)
        self.X = self.data.drop(columns=['Potability'])
        self.y = self.data['Potability']
        self.model = XGBClassifier()

    def train_model(self):
        self.model.fit(self.X, self.y)

    def get_user_inputs(self, value):
        user_inputs = {}
        print("Enter values for the following water parameters:")
        for column in self.X.columns:
        #     value = float(input(f"{column}: "))
            user_inputs[column] = [value]
        return pd.DataFrame(user_inputs)

    def predict_potability(self, user_data):
        prediction = self.model.predict(user_data)
        return prediction[0]

water_model = WaterPotabilityModel("water_potability.csv")
water_model.train_model()
# user_data = water_model.get_user_inputs()
# prediction = water_model.predict_potability(user_data)

# if prediction == 1:
#     print("The water is potable.")
# else:
#     print("The water is not potable.")
