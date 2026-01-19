import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Data
df = pd.DataFrame({
    'glucose': [85,190,150,90,170,110,200,95],
    'bmi': [22,35,30,24,33,26,40,21],
    'age': [25,50,45,30,60,22,55,33],
    'bp': [80,95,90,82,100,85,110,78],
    'diabetes': [0,1,1,0,1,0,1,0]
})

X = df[['glucose','bmi','age','bp']]
y = df['diabetes']

# Scale
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Model
model = Sequential([
    Dense(8, activation='relu', input_shape=(4,)),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X, y, epochs=50, verbose=0)


new_data = [[160, 32, 48, 92]]

new_data_scaled = scaler.transform(new_data)

prediction = model.predict(new_data_scaled)
result = "YES (Diabetic)" if prediction[0][0] > 0.5 else "NO (Not Diabetic)"

print("New Patient:", result)
