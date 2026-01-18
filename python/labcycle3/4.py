import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from scipy.stats import mode

# 1. Load the Iris Dataset
iris = load_iris()
X = iris.data  # Features
y_true = iris.target  # Actual Labels (0, 1, 2)

# 2. Apply K-Means
# We know there are 3 species, so we set n_clusters=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
clusters = kmeans.fit_predict(X)

# 3. Fix the Labels (Mapping)
# K-Means labels might not match Iris target labels (e.g., Cluster 0 might be Target 2)
labels = np.zeros_like(clusters)
for i in range(3):
    # Find which true species is most common in this cluster
    mask = (clusters == i)
    labels[mask] = mode(y_true[mask], keepdims=True).mode[0]

# 4. Calculate Accuracy
accuracy = accuracy_score(y_true, labels)

print(f"K-Means Accuracy for Iris: {accuracy * 100:.2f}%")