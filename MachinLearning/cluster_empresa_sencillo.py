import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import random
# Generate random company data
# num_companies = 400
# sectors = ['Technology', 'Retail', 'Financial Services', 'Healthcare', 'Manufacturing']
# sizes = ['Small Business', 'Medium Business', 'Large Enterprise']

# random_data = {
#     'Sector': [random.choice(sectors) for _ in range(num_companies)],
#     'Size': [random.choice(sizes) for _ in range(num_companies)],
#     'Purchase_Frequency': [random.randint(1, 50) for _ in range(num_companies)],  # Purchases per year
#     'Average_Ticket': [random.randint(500, 50000) for _ in range(num_companies)],  # Average purchase value
#     'Customer_Lifetime': [random.randint(1, 20) for _ in range(num_companies)],  # Years as a customer
#     'Satisfaction': [random.randint(1, 5) for _ in range(num_companies)]  # Satisfaction score
# }

# # Create a DataFrame and save it to a CSV file
# random_df = pd.DataFrame(random_data)
# random_df.to_csv('c:/Users/carlo/Desktop/python/Proyecto-Esail-Python/MachinLearning/client_data.csv', index=False)
# Load the dataset
file_path = 'c:/Users/carlo/Desktop/python/Proyecto-Esail-Python/MachinLearning/client_data.csv'
data = pd.read_csv(file_path)

# Preprocess the data
# Convert categorical variables to numerical using one-hot encoding
data_encoded = pd.get_dummies(data, columns=['Sector', 'Size'], drop_first=True)

# Standardize the numerical features
scaler = StandardScaler()
numerical_features = ['Purchase_Frequency', 'Average_Ticket', 'Customer_Lifetime', 'Satisfaction']
data_encoded[numerical_features] = scaler.fit_transform(data_encoded[numerical_features])

# Elbow method to determine the optimal number of clusters
inertia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_encoded)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.xticks(k_range)
plt.grid()
plt.show()

# Calculate inertia (how far groups from centre of the cluster) and silhouette (how far are the clusters from each other) score for different numbers of clusters
silhouette_scores = []

for k in range(2, 11):  # Silhouette score is not defined for k=1
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_encoded)
    cluster_labels = kmeans.labels_
    
    # Calculate silhouette score
    silhouette_avg = silhouette_score(data_encoded, cluster_labels)
    silhouette_scores.append(silhouette_avg)
    print(f'For k={k}, Inertia={kmeans.inertia_:.2f}, Silhouette Score={silhouette_avg:.2f}')

# Perform KMeans clustering with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(data_encoded)
data_encoded['Cluster'] = kmeans.labels_

# Get the centroids
centroids = kmeans.cluster_centers_

# Visualize the clusters and centroids
plt.figure(figsize=(10, 7))
sns.scatterplot(
    x=data_encoded['Purchase_Frequency'],
    y=data_encoded['Average_Ticket'],
    hue=data_encoded['Cluster'],
    palette='viridis',
    s=100
)

# Plot the centroids with labels
for i, (x, y) in enumerate(zip(
    centroids[:, numerical_features.index('Purchase_Frequency')],
    centroids[:, numerical_features.index('Average_Ticket')]
)):
    plt.scatter(x, y, c='red', s=200, marker='X', label=f'Centroid {i}')
    plt.text(x, y, f'Cluster {i}', color='black', fontsize=10, ha='center', va='center')

plt.title('Clusters of Clients with Centroids')
plt.xlabel('Purchase Frequency (Standardized)')
plt.ylabel('Average Ticket (Standardized)')
plt.legend(title='Cluster')
plt.grid()
plt.show()
