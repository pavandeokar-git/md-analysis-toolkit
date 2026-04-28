import pandas as pd
from MDAnalysis.analysis import pca

def run_pca(universe, selection="protein and name CA"):
    pc = pca.PCA(universe, select=selection)
    pc.run()

    atoms = universe.select_atoms(selection)
    transformed = pc.transform(atoms, n_components=2)

    return pd.DataFrame({
        "PC1": transformed[:, 0],
        "PC2": transformed[:, 1]
    })
