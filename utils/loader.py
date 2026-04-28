import MDAnalysis as mda

def load_trajectory(topology, trajectory):
    print("Loading trajectory...")
    u = mda.Universe(topology, trajectory)
    return u
