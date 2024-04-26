import matplotlib.pyplot as plt
import seaborn as sns

import data


def plot_results(a, filename):
    # W = 5.8  # Figure width in inches, approximately A4-width - 2*1.25in margin
    # plt.rcParams.update({
    #     'figure.figsize': (W, W / (4 / 3)),  # 4:3 aspect ratio
    #     'font.size': 11,  # Set font size to 11pt
    #     'axes.labelsize': 11,  # -> axis labels
    #     'legend.fontsize': 11,  # -> legends
    #     'font.family': 'lmodern',
    #     # 'text.usetex': True,
    #     'text.latex.preamble': (  # LaTeX preamble
    #         r'\usepackage{lmodern}'
    #         # ... more packages if needed
    #     ),
    #     # 'text.latex.unicode': True,
    #
    # })

    # Options
    fig, ax = plt.subplots(1, 1, figsize=(4, 3))

    sns.histplot(a, ax=ax, kde=True, stat='count', color='blue')

    ax.set_title("Distribution of BLEU Scores")
    ax.set_xlabel("BLEU")
    fig.tight_layout()
    fig.savefig(f"figures/histogram_{filename}.pdf")


def main():
    mt_results = data.get_mt_results()
    ts_results = data.get_ts_results()

    sns.set_theme()
    sns.set_style("darkgrid")

    plot_results(mt_results, "mt")
    plot_results(ts_results, "ts")


if __name__ == "__main__":
    main()
