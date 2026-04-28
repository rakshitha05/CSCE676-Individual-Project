# Data Directory

This folder is intentionally kept minimal.

## Dataset Used
- **Name:** SNAP Facebook Combined Graph  
- **Source:** Stanford Network Analysis Project (SNAP)  
- **Link:** https://snap.stanford.edu/data/facebook_combined.html  

## How Data is Handled

The dataset is **not stored in this repository** to keep it lightweight and reproducible.

Instead, the main notebook (`main_notebook.ipynb`) automatically:
1. Downloads the dataset from the SNAP website  
2. Extracts the compressed file  
3. Loads it into a graph structure for analysis  

## Why Data is Not Included

- The dataset is publicly available and easily downloadable  
- Including it would unnecessarily increase repository size  
- Automatic download ensures reproducibility across environments  

## Notes

- When you run the notebook, the dataset will be downloaded into this folder  
- No manual setup is required  

---

If needed, you can manually download the dataset:

https://snap.stanford.edu/data/facebook_combined.txt.gz