import pandas as pd
from MDAnalysis.analysis.hydrogenbonds import HydrogenBondAnalysis

def calculate_hbonds(universe):
    hbond_analysis = HydrogenBondAnalysis(
        universe=universe,
        donors_sel="protein",
        hydrogens_sel="protein",
        acceptors_sel="protein",
        d_a_cutoff=3.5,
        d_h_a_angle_cutoff=150
    )

    hbond_analysis.run()

    return pd.DataFrame({
        "Time (ps)": hbond_analysis.times,
        "H-bonds": hbond_analysis.count_by_time()
    })
