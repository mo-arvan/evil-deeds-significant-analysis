import matplotlib.pyplot as plt
import pandas as pd

mt_results = pd.read_csv('results/rethinking_result.csv')["bleu"].tolist()
ts_results = pd.read_csv('results/text-simplification/search.csv')["BLEU"].tolist()

mt_results = sorted(mt_results, reverse=True)
ts_results = sorted(ts_results, reverse=True)


top_mt = mt_results[:len(mt_results) // 2]
bottom_mt = mt_results[len(mt_results) // 2:]


def plot_violin(d1, d2, plot_name):
    data = [d1, d2]

    fig, ax = plt.subplots()
    ax.violinplot(data, showmedians=True, positions=[1, 2])

    ax.set_xticks([1, 2])
    ax.set_xticklabels(['Best', 'Worst'])
    ax.set_xlabel('Distribution')
    ax.set_ylabel('BLEU Scores')

    plt.title('Violin Plot of best and worst Distributions')
    plt.grid(True)
    # plt.show()
    plt.savefig(plot_name)

    plt.close()

plot_violin(top_mt, bottom_mt, 'figures/mt_vs_violin_plot.svg')

top_ts = ts_results[:len(ts_results) // 2]
bottom_ts = ts_results[len(ts_results) // 2:]
plot_violin(top_ts, bottom_ts, 'figures/ts_vs_violin_plot.svg')
