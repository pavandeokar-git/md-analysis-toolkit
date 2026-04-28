import pandas as pd
from MDAnalysis.analysis import rms

def calculate_rmsd(universe, selection="protein"):
    R = rms.RMSD(universe, universe, select=selection, ref_frame=0)
    R.run()

    rmsd = R.results.rmsd[:, 2]
    time = R.results.rmsd[:, 1]

    return pd.DataFrame({
        "Time (ps)": time,
        "RMSD (Å)": rmsd
    })
