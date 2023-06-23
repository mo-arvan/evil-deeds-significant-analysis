import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd

ts_results = pd.read_csv('results/text-simplification/search.csv')
mt_results = pd.read_csv('results/rethinking_result.csv')



ax = sns.violinplot(x=mt_results["bleu"].tolist(), inner="quart")

ax.legend()

plt.savefig('mt_violin_plot.svg')

plt.close()


ax = sns.violinplot(x=ts_results["BLEU"].tolist(), inner="quart")

ax.legend()

plt.savefig('ts_violin_plot.svg')

plt.close()

import numpy as np

# Assuming the data is associated with random seed values
random_seeds = np.arange(len(ts_results["BLEU"].tolist()))

plt.scatter(random_seeds, ts_results["BLEU"].tolist())
plt.xlabel('Random Seed')
plt.ylabel('Result')
plt.title('Machine Learning Model Results')


plt.savefig('ts_scatter_plot.svg')
