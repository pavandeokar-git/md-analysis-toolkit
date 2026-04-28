import matplotlib.pyplot as plt
import seaborn as sns

# Modern clean style
sns.set(style="whitegrid", context="talk")

# ---------------- GENERIC LINE PLOT ---------------- #
def plot_line(df, x, y, title, outfile):
    plt.figure(figsize=(8, 5))

    # Main plot (NO average line)
    plt.plot(df[x], df[y], linewidth=2)

    # Labels and title
    plt.xlabel(x, fontsize=12)
    plt.ylabel(y, fontsize=12)
    plt.title(title, fontsize=14, weight="bold")

    # Clean layout
    plt.tight_layout()

    # Save high quality image
    plt.savefig(outfile, dpi=300)
    plt.close()


# ---------------- PCA CLUSTER PLOT ---------------- #
def plot_clusters(df, outfile):
    plt.figure(figsize=(6, 5))

    for c in df["Cluster"].unique():
        subset = df[df["Cluster"] == c]
        plt.scatter(
            subset["PC1"],
            subset["PC2"],
            label=f"Cluster {c}",
            s=25
        )

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("PCA Clustering", weight="bold")
    plt.legend()

    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()
