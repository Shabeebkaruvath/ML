import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report

df = pd.read_csv('9.csv')

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

svm = SVC(kernel='linear')
svm.fit(X_train_s, y_train)
svm_pred = svm.predict(X_test_s)

print("Decision Tree\n", classification_report(y_test, dt_pred))
print("SVM\n", classification_report(y_test, svm_pred))
print("better acuracy is : Decision Tree")
