import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_embedding(embedding, nodes, role_map, title):
    pca = PCA(n_components=2)
    emb_2d = pca.fit_transform(embedding)

    role_to_id = {"hub": 0, "bridge": 1, "peripheral": 2, "other": 3}
    colors = [role_to_id[role_map[n]] for n in nodes]

    plt.figure(figsize=(7,5))
    plt.scatter(emb_2d[:,0], emb_2d[:,1], c=colors, s=10)
    plt.title(title)
    plt.show()