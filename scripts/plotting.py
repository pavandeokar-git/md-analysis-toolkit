import matplotlib.pyplot as plt
import seaborn as sns

# Set global style
sns.set(style="whitegrid", palette="tab10")

def plot_line(df, x, y, title, outfile):
    plt.figure(figsize=(8,5), dpi=300)

    plt.plot(df[x], df[y], linewidth=2)

    plt.xlabel(x, fontsize=12)
    plt.ylabel(y, fontsize=12)
    plt.title(title, fontsize=14)

    plt.tight_layout()
    plt.savefig(outfile)
    plt.close()
