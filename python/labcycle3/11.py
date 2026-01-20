import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load and prepare data
data = pd.read_csv("11.csv")
fraud_pct = data['is_fraud'].mean()*100

data = data.drop(columns=["user_id", "device_id", "ip_address"], errors="ignore")

# Feature engineering
data['signup_time'] = pd.to_datetime(data['signup_time'])
data['purchase_time'] = pd.to_datetime(data['purchase_time'])
data['time_to_purchase'] = (data['purchase_time'] - data['signup_time']).dt.total_seconds() / 3600
data['purchase_hour'] = data['purchase_time'].dt.hour
data = data.drop(columns=['signup_time', 'purchase_time'])

# Encode categorical
for col in ['source', 'browser', 'sex']:
    data[col] = LabelEncoder().fit_transform(data[col].fillna('Unknown'))

# Train-test split
X = data.drop("is_fraud", axis=1)
y = data["is_fraud"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale
X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

# Models (optimized SVM)
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42, class_weight='balanced', max_depth=10),
    "Random Forest": RandomForestClassifier(n_estimators=50, random_state=42, class_weight='balanced', n_jobs=-1),
    "SVM": SVC(kernel="rbf", random_state=42, class_weight='balanced', cache_size=500, max_iter=1000)
}

# Train and evaluate
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results[name] = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, zero_division=0),
        "Recall": recall_score(y_test, y_pred, zero_division=0),
        "F1-Score": f1_score(y_test, y_pred, zero_division=0)
    }

# Results
results_df = pd.DataFrame(results).T
print("Model Performance:")
print(results_df.round(4))
print(f"Best: {results_df['F1-Score'].idxmax()} (F1: {results_df['F1-Score'].max():.4f})    \n Fraud: {fraud_pct:.2f}%")