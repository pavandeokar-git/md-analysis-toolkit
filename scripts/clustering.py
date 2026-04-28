from sklearn.cluster import KMeans

def run_clustering(df, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["Cluster"] = kmeans.fit_predict(df[["PC1", "PC2"]])
    return df
