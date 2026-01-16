import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import precision_score, recall_score, f1_score

# 1. Setup the Dataset
data = {
    'VAR1': [1.713, 0.180, 0.353, 0.940, 1.486, 1.540, 0.773, 1.106, 1.799],
    'VAR2': [1.586, 1.786, 1.240, 1.566, 1.266, 0.459, 0.759, 0.419, 0.186],
    'True_Class': [0, 1, 1, 0, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
X = df[['VAR1', 'VAR2']]
y_true = df['True_Class']

# 2. Apply K-Means with 3 Centroids
# n_init='auto' handles initial centroid placement automatically
kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
df['Cluster'] = kmeans.fit_predict(X)

# 3. Predict for the specific case: VAR1=0.906, VAR2=0.606
new_case = np.array([[0.906, 0.606]])
predicted_cluster = kmeans.predict(new_case)[0]

# 4. Map Clusters to True Classes
# Since K-means labels (0,1,2) are arbitrary, we map each cluster 
# to the most frequent 'True_Class' found within that cluster.
cluster_map = {}
for i in range(3):
    # Find the most common true class in this cluster
    mode_result = df[df['Cluster'] == i]['True_Class'].mode()
    cluster_map[i] = mode_result[0] if not mode_result.empty else 0

# Apply the mapping to get predicted classes
y_pred = df['Cluster'].map(cluster_map)
final_prediction = cluster_map[predicted_cluster]

# 5. Calculate Metrics
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Output Results
print(f"Predicted Class for (0.906, 0.606): {final_prediction}")
print("-" * 30)
print(f"Precision: {precision:.3f}")
print(f"Recall:    {recall:.3f}")
print(f"F1 Score:  {f1:.3f}")