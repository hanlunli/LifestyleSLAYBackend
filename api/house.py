import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
data = pd.read_csv('sleep.csv')

# Step 2: Data Preprocessing
# Drop irrelevant columns and handle missing values if any
data = data.drop(['Person ID', 'Occupation', 'BMI Category', 'Blood Pressure'], axis=1)
data = data.dropna()

# Convert categorical variables to numerical using one-hot encoding
data = pd.get_dummies(data, columns=['Gender'])

# Split the data into features and target variable
X = data.drop('Sleep Disorder', axis=1)
y = data['Sleep Disorder']

# Step 3: Feature Engineering (if required)
# You can add more feature engineering steps here

# Step 4: Model Selection and Training
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Step 5: Model Evaluation
# Predict on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 6: Prediction
# Now, you can use this trained model to predict sleep disorders for new data
# For example:
new_data = pd.DataFrame({
    'Age': [34],
    'Sleep Duration': [7.5],
    'Quality of Sleep': [9],
    'Physical Activity Level': [60],
    'Stress Level': [5],
    'Heart Rate': [70],
    'Daily Steps': [8000],
    'Gender_Female': [0],  # Adjust according to the gender
    'Gender_Male': [1]
})

prediction = clf.predict(new_data)
print("Predicted Sleep Disorder:", prediction)
