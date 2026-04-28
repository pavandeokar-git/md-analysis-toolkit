import pandas as pd
from MDAnalysis.analysis import rms

def calculate_rmsf(universe, selection="protein and name CA"):
    atoms = universe.select_atoms(selection)

    R = rms.RMSF(atoms)
    R.run()

    return pd.DataFrame({
        "Residue": atoms.resnums,
        "RMSF (Å)": R.results.rmsf
    })
