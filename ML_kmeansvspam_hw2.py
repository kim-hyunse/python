import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids

# Initialize dataset with extreme outliers
data = np.array([
    [7, 6],
    [2, 6],
    [3, 8],
    [8, 5],
    [7, 4],
    [4, 7],
    [6, 2],
    [7, 3],
    [6, 4],
    [3, 4],
    [2, 30],  # moderate outlier
    [50, 60],  # extreme outlier
    [55, 65]  # extreme outlier
])

# Number of clusters
k = 2

# K-means clustering
kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
kmeans_labels = kmeans.fit_predict(data)
kmeans_distances = np.linalg.norm(data - kmeans.cluster_centers_[kmeans_labels], axis=1)

# PAM clustering
pam = KMedoids(n_clusters=k, method='pam', random_state=42)
pam_labels = pam.fit_predict(data)
pam_distances = np.linalg.norm(data - pam.cluster_centers_[pam_labels], axis=1)

# Sum of distances for K-means and PAM
kmeans_sum_distances = np.sum(kmeans_distances)
pam_sum_distances = np.sum(pam_distances)

print("Sum of distances to cluster centers for K-means:", kmeans_sum_distances)
print("Sum of distances to medoids for PAM:", pam_sum_distances)

# Visualization
plt.figure(figsize=(14, 6))

# K-means plot
plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1], c=kmeans_labels, cmap='rainbow', s=100)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='black', marker='x')
plt.title("K-means Clustering")

# PAM plot
plt.subplot(1, 2, 2)
plt.scatter(data[:, 0], data[:, 1], c=pam_labels, cmap='rainbow', s=100)
plt.scatter(pam.cluster_centers_[:, 0], pam.cluster_centers_[:, 1], s=300, c='black', marker='x')
plt.title("PAM Clustering")

plt.show()
