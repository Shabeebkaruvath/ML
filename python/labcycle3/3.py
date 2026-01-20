import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import precision_score, recall_score, f1_score

# Data
data = {
    'VAR1': [1.713, 0.180, 0.353, 0.940, 1.486, 1.540, 0.773, 1.106, 1.799],
    'VAR2': [1.586, 1.786, 1.240, 1.566, 1.266, 0.459, 0.759, 0.419, 0.186],
    'True_Class': [0, 1, 1, 0, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
X = df[['VAR1', 'VAR2']]

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
df['Cluster'] = kmeans.fit_predict(X)

# Predict new case
pred_cluster = kmeans.predict([[0.906, 0.606]])[0]

# Map clusters to true classes
cluster_map = {i: df[df['Cluster'] == i]['True_Class'].mode()[0] for i in range(3)}
y_pred = df['Cluster'].map(cluster_map)

# Metrics
print(f"Predicted: {cluster_map[pred_cluster]}")
print(f"Precision: {precision_score(df['True_Class'], y_pred):.3f}")
print(f"Recall: {recall_score(df['True_Class'], y_pred):.3f}")
print(f"F1: {f1_score(df['True_Class'], y_pred):.3f}")