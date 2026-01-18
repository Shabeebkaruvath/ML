import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# -------------------------------
# 1. Create the dataset
# Features: glucose, BMI, age, blood pressure
# Target: diabetes (0 = No, 1 = Yes)
# -------------------------------
df = pd.DataFrame({
    'glucose': [85, 190, 150, 90, 170, 110, 200, 95],
    'bmi': [22, 35, 30, 24, 33, 26, 40, 21],
    'age': [25, 50, 45, 30, 60, 22, 55, 33],
    'bp': [80, 95, 90, 82, 100, 85, 110, 78],
    'diabetes': [0, 1, 1, 0, 1, 0, 1, 0]
})

# Separate input features (X) and output label (y)
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# -------------------------------
# 2. Feature Scaling
# ANN works better when input data is normalized
# -------------------------------
scaler = StandardScaler()
X = scaler.fit_transform(X)

# -------------------------------
# 3. Build the ANN model
# Input layer → Hidden layer → Output layer
# -------------------------------
model = Sequential([
    Input(shape=(4,)),              # Input layer with 4 features
    Dense(8, activation='relu'),    # Hidden layer with ReLU activation
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy'
)

# -------------------------------
# 4. Train the model
# -------------------------------
model.fit(X, y, epochs=50, verbose=0)

# -------------------------------
# 5. Predict and evaluate (YES / NO)
# -------------------------------
pred = (model.predict(X) > 0.5).astype(int)

# Display result for each patient
for i, p in enumerate(pred):
    if p[0] == 1:
        print(f"Patient {i+1}: YES (Diabetic)")
    else:
        print(f"Patient {i+1}: NO (Not Diabetic)")
