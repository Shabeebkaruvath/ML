import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    'age': [25, 45, 35, 50, 22, 38, 40], 
    'gender': [1, 1, 1, 0, 1, 0, 1], #Age, Gender (0:F, 1:M) 
    'edu': [0, 1, 0, 1, 0, 1, 0],#Education (0:Diploma, 1:Degree) 
    'industry': [0, 1, 0, 1, 0, 1, 0],#Industry:Manufacturing 0, 1:IT 
    'residence': [1, 1, 1, 1, 0, 0, 1],# Residence (0:Non-Metro, 1:Metro) 
    'income_bucket': [1, 3, 2, 3, 1, 2, 2] # 1: <4L, 2: 4-15L, 3: >15L
}

df = pd.DataFrame(data)

X = df.drop('income_bucket', axis=1)
y = df['income_bucket']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict
one = [35, 1, 0, 0, 0]
person = pd.DataFrame([one], columns=X.columns)

prediction = model.predict(person)
if prediction[0] == 1:
    print("Predicted Income : <4L")
elif prediction[0] == 2:
    print("Predicted Income : 4-15L")
else:  
    print("Predicted Income : >15L")

