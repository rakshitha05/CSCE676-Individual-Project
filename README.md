# CSCE676 — Individual Project  
## Graph Mining & Embeddings Project

**Author:** Rakshitha Gurudatt Kagal  
**UIN:** 337002110  
**Course:** CSCE 676 — Data Mining & Analysis  
**Checkpoint:** Dataset Selection, Dataset Comparison, & Exploratory Data Analysis

---

## 📌 Project Overview

This project analyzes a real-world social network graph using classical data
mining techniques and modern representation learning methods. The objective is
to explore structural properties of graph data, identify meaningful patterns,
and evaluate how embeddings capture network behavior.

The selected dataset is the **SNAP Facebook Combined Graph**, a widely used
benchmark dataset for graph mining research.

---

## 📊 Dataset

**Source:** Stanford Network Analysis Project (SNAP)  
**Dataset:** Facebook Combined Graph  

- **Nodes:** 4039  
- **Edges:** 88,234  
- **Graph Type:** Undirected  
- **Node Attributes:** None (structural analysis)

Dataset link:  
https://snap.stanford.edu/data/facebook_combined.html

---

## 🎯 Objectives

This checkpoint focuses on:

✔ Dataset selection and justification  
✔ Data cleaning and preprocessing  
✔ Exploratory Data Analysis (EDA)  
✔ Bias and ethical considerations  
✔ Establishing a foundation for advanced techniques  

---

## 🔎 Techniques Applied

### Course-Aligned Methods

- Graph Construction & Cleaning  
- Graph Summary Statistics  
- Degree Distribution Analysis  
- Centrality Measures  
- Community Detection  

### Beyond-Core Exploration

- Spectral Graph Embeddings  
- PCA Visualization of Embeddings  

---

## 🧹 Data Cleaning Decisions

The following preprocessing steps were applied:

- Removed self-loops  
- Removed duplicate edges  
- Canonicalized undirected edges  
- Loaded node IDs as strings  

**Why this matters:**  
Graph metrics are highly sensitive to structural artifacts. Proper cleaning
ensures correctness and prevents distortion of degree, centrality, and
clustering measures.

---

## 📈 Key Findings

- The network is sparse but fully connected  
- Degree distribution is highly skewed  
- Hub nodes dominate centrality rankings  
- Community sizes are uneven  
- Embeddings capture structural variation  

---

## ⚠ Bias & Limitations

This dataset reflects sampling decisions during collection. Observed structural
patterns may not fully generalize to all social networks. Additionally, the
absence of node attributes limits semantic interpretation.

---

## 🧭 Future Directions

Potential extensions include:

- Similarity search via LSH  
- Link prediction experiments  
- Node classification (if attributes available)  
- Graph neural network methods  

---

## ▶ Reproducibility

The notebook automatically downloads the dataset from SNAP when needed.

To run locally:

```bash
pip install pandas numpy networkx matplotlib scipy scikit-learn
jupyter notebook


