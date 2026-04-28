import pandas as pd

def calculate_rg(universe, selection="protein"):
    atoms = universe.select_atoms(selection)

    times = []
    rg_values = []

    for ts in universe.trajectory:
        times.append(ts.time)
        rg_values.append(atoms.radius_of_gyration())

    return pd.DataFrame({
        "Time (ps)": times,
        "Rg (Å)": rg_values
    })
