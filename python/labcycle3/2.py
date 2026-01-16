import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    'age': [25, 45, 35, 50, 22, 38, 40],
    'gender': [1, 1, 1, 0, 1, 0, 1], #Age, Gender (0:F, 1:M)
    'edu': [0, 1, 0, 1, 0, 1, 0],#Education (0:Diploma, 1:Degree)
    'industry': [0, 1, 0, 1, 0, 1, 0],#Industry:Manufacturing, 1:IT
    'residence': [1, 1, 1, 1, 0, 0, 1],# Residence (0:Non-Metro, 1:Metro)
    'income_bucket': [1, 3, 2, 3, 1, 2, 2] # 1: <4L, 2: 4-15L, 3: >15L
}

df = pd.DataFrame(data)

model = RandomForestClassifier(n_estimators=100, random_state=42)

X = df.drop('income_bucket', axis=1) 
y = df['income_bucket']              
model.fit(X, y)

#Predict
person = pd.DataFrame[[35, 1, 0, 0, 1]]
prediction = model.predict(person)

print(f"The predicted Income Bucket is: {prediction[0]}")