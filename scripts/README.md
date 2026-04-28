# Scripts

This folder contains supporting scripts used in the project to keep the main notebook clean and organized.

## Contents

- **download_data.py**  
  Handles downloading and extracting the SNAP Facebook Combined Graph dataset.  
  This ensures the project is reproducible without manually adding data files.

- **utils.py** *(optional)*  
  Contains reusable helper functions such as:
  - Precision@k for role consistency  
  - Cluster role purity  
  These functions are used during evaluation to measure how well embeddings preserve structural roles.

- **visualization.py** *(optional)*  
  Contains helper functions for plotting embeddings and visualizing results in a consistent format.

## Purpose

The goal of this folder is to separate reusable logic from the main notebook, improving:
- Code readability  
- Modularity  
- Maintainability  

Instead of cluttering the notebook with repeated logic, common functions are stored here and imported when needed.

## Notes

- The main project workflow is in `main_notebook.ipynb`  
- Scripts are lightweight and optional — the notebook can still run independently  
- These files are included to reflect good software engineering practices