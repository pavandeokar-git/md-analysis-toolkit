import argparse
import os

# Core modules
from utils.loader import load_trajectory
from scripts.rmsd import calculate_rmsd
from scripts.rmsf import calculate_rmsf
from scripts.rg import calculate_rg
from scripts.hbonds import calculate_hbonds
from scripts.pca import run_pca
from scripts.clustering import run_clustering

# Plotting
from utils.plotting import plot_line, plot_clusters

# Sample data (for testing)
from MDAnalysisTests.datafiles import TPR, XTC


# ARGUMENT PARSER 
parser = argparse.ArgumentParser(description="MD Analysis Toolkit")

parser.add_argument("--rmsd", action="store_true", help="Run RMSD analysis")
parser.add_argument("--rmsf", action="store_true", help="Run RMSF analysis")
parser.add_argument("--rg", action="store_true", help="Run Radius of Gyration")
parser.add_argument("--hbonds", action="store_true", help="Run H-bond analysis")
parser.add_argument("--pca", action="store_true", help="Run PCA + clustering")

args = parser.parse_args()

# If no arguments → run all
if not any(vars(args).values()):
    args.rmsd = True
    args.rmsf = True
    args.rg = True
    args.hbonds = True
    args.pca = True


# LOAD DATA 
topology = TPR
trajectory = XTC

os.makedirs("outputs", exist_ok=True)

print("\nReading trajectory...")
u = load_trajectory(topology, trajectory)


# ANALYSIS 
results_done = []

# RMSD
if args.rmsd:
    print("Calculating RMSD...")
    rmsd_df = calculate_rmsd(u)
    rmsd_df.to_csv("outputs/rmsd.csv", index=False)

    plot_line(
        rmsd_df,
        "Time (ps)",
        "RMSD (Å)",
        "RMSD vs Time",
        "outputs/rmsd.png"
    )

    results_done.append("RMSD")


# RMSF
if args.rmsf:
    print("Calculating RMSF...")
    rmsf_df = calculate_rmsf(u)
    rmsf_df.to_csv("outputs/rmsf.csv", index=False)

    plot_line(
        rmsf_df,
        "Residue",
        "RMSF (Å)",
        "RMSF per Residue",
        "outputs/rmsf.png"
    )

    results_done.append("RMSF")


# Radius of Gyration
if args.rg:
    print("Calculating Radius of Gyration...")
    rg_df = calculate_rg(u)
    rg_df.to_csv("outputs/rg.csv", index=False)

    plot_line(
        rg_df,
        "Time (ps)",
        "Rg (Å)",
        "Radius of Gyration",
        "outputs/rg.png"
    )

    results_done.append("Rg")


# Hydrogen Bonds
if args.hbonds:
    print("Calculating hydrogen bonds...")
    hb_df = calculate_hbonds(u)
    hb_df.to_csv("outputs/hbonds.csv", index=False)

    plot_line(
        hb_df,
        "Time (ps)",
        "H-bonds",
        "Hydrogen Bonds vs Time",
        "outputs/hbonds.png"
    )

    results_done.append("H-bonds")


# PCA + Clustering
if args.pca:
    print("Calculating PCA...")
    pca_df = run_pca(u)

    print("Performing clustering...")
    cluster_df = run_clustering(pca_df)

    cluster_df.to_csv("outputs/pca_clusters.csv", index=False)
    plot_clusters(cluster_df, "outputs/pca_clusters.png")

    results_done.append("PCA + Clustering")


# FINAL OUTPUT
print("\nFinished.")

if results_done:
    print("Analyses performed:")
    for r in results_done:
        print(f" - {r}")
else:
    print("No analysis selected.")

print("\nResults written to: outputs/\n")
