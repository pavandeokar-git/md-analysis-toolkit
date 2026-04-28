# MD Analysis Toolkit

A Python-based toolkit for automated analysis of molecular dynamics (MD) simulations, designed for computational drug design (CADD) workflows.

This toolkit enables fast, reproducible, and publication-ready analysis of MD trajectories using MDAnalysis.
---
## Features
RMSD – Structural stability over time
RMSF – Residue-wise flexibility
Radius of Gyration (Rg) – Protein compactness
Hydrogen Bond Analysis – Interaction stability
PCA (Essential Dynamics) – Dominant motions
K-means Clustering – Conformational states

git clone https://github.com/YOUR_USERNAME/md-analysis-toolkit.git
cd md-analysis-toolkit

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
---
## Usage
Run all analyses (default)
md_ana_toolkit.py

### Run specific analyses
python main.py --rmsd --pca 

### Available options
  Flag	  Description
--rmsd	  RMSD analysis
--rmsf	  RMSF analysis
--rg	  Radius of Gyration
--hbonds  Hydrogen bonds
--pca	  PCA + clustering
---
## Output
outputs/
Includes:
.csv → numerical data
.png → high-quality plots

### Example Outputs
#### RMSD Plot
![RMSD Plot](images/rmsd.png)

#### PCA Clustering
![PCA Clustering](images/pca_clusters.png)
---
## Test Dataset
Uses sample trajectory from:
MDAnalysis test dataset (Adenylate Kinase)
---
## Use Cases
Protein stability analysis
Binding site dynamics
Post-docking MD validation
Conformational clustering
Drug design workflows
---
##Author
Pavan Deokar
Computational Drug Discovery Researcher
M.S. (Pharm.) Pharmacoinformatics
NIPER Mohali
