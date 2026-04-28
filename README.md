# Do Graph Embeddings Preserve Structural Roles?

Graph embeddings are widely used in applications such as social networks, recommendation systems, and fraud detection. These methods compress complex graph structures into low-dimensional representations, but it is unclear whether they preserve meaningful structural information. This project investigates whether embeddings retain important node roles such as hubs, bridges, and peripheral nodes, and shows that commonly used methods may lose this information.

👉 The main deliverable is: main_notebook.ipynb

## Research Questions
- To what extent do graph embeddings preserve structurally distinct node roles?
- Do embeddings capture global structure or only local similarity?
- How do spectral embedding and node2vec compare?

🎥 Project Video: https://youtu.be/UYNXRPLKY-w

## Data
SNAP Facebook Combined Graph  
https://snap.stanford.edu/data/facebook_combined.html  

## How to Reproduce
1. git clone <repo>
2. pip install -r requirements.txt
3. Run main_notebook.ipynb

## Key Dependencies
Python 3.12.13, numpy, pandas, networkx, matplotlib, scipy, scikit-learn, node2vec, gensim

## Repo Structure
.
├── README.md
├── main_notebook.ipynb
├── requirements.txt
├── .gitignore
│
├── assets/
│   ├── README.md
│   ├── embedding_comparison.png
│   ├── spectral_embedding.png
│   ├── node2vec_embedding.png
│   ├── role_distribution.png
│   ├── results_table.png
│   └── final_presentation.pptx
│
├── data/
│   └── README.md
│
├── scripts/
│   ├── README.md
│   ├── download_data.py
│   ├── utils.py          (optional)
│   └── visualization.py  (optional)
│
├── checkpoints/
│   ├── README.md
│   ├── checkpoint_1.ipynb
│   └── checkpoint_2.ipynb

## Results Summary
Spectral embedding preserves structural roles significantly better than node2vec.  
Local similarity is not the same as structural role.
