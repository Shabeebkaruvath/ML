import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

 
df = pd.read_csv('9.csv')
print("Dataset loaded!")
print(df.head())

 
df = df.drop_duplicates()
df = df.dropna()
print(f"\nTotal samples: {len(df)}")

 
X = df.iloc[:, :-1]  
y = df.iloc[:, -1]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

 
print("\nSamples per species:")
print(y.value_counts())

 
plt.figure(figsize=(12, 8))

 
plt.subplot(2, 2, 1)
plt.hist(df.iloc[:, 0], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Sepal Length Distribution')
 
plt.subplot(2, 2, 2)
plt.hist(df.iloc[:, 2], bins=20, color='lightcoral', edgecolor='black')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.title('Petal Length Distribution')

 
plt.subplot(2, 2, 3)
y.value_counts().plot(kind='bar', color=['red', 'green', 'blue'])
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Species Distribution')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()