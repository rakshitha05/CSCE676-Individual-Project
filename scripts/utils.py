import numpy as np
from sklearn.metrics import silhouette_score

def precision_at_k_same_role(embedding, nodes, role_map, k=5):
    from sklearn.neighbors import NearestNeighbors

    nbrs = NearestNeighbors(n_neighbors=k+1).fit(embedding)
    _, indices = nbrs.kneighbors(embedding)

    scores = []
    for i, node in enumerate(nodes):
        true_role = role_map[node]
        neighbors = [nodes[j] for j in indices[i][1:]]
        same_role = [1 if role_map[n] == true_role else 0 for n in neighbors]
        scores.append(np.mean(same_role))

    return float(np.mean(scores))


def cluster_role_purity(labels, nodes, role_map):
    import pandas as pd

    df = pd.DataFrame({"node": nodes, "cluster": labels})
    df["role"] = df["node"].map(role_map)

    purity = []
    for cluster in df["cluster"].unique():
        sub = df[df["cluster"] == cluster]
        purity.append(sub["role"].value_counts(normalize=True).max())

    return float(np.mean(purity))