
import os
import re
from deepsig import aso
import numpy as np
import pandas as pd

mt_results = pd.read_csv('results/rethinking_result.csv')["bleu"].tolist()
ts_results = pd.read_csv('results/text-simplification/search.csv')["BLEU"].tolist()




print(f'Mean: {np.mean(mt_results):.2f}, Median {np.median(mt_results):.2f}, Std: {np.std(mt_results):.2f},        Min: {np.min(mt_results):.2f}, Max: {np.max(mt_results):.2f}')

print(f'Mean: {np.mean(ts_results):.2f}, Median {np.median(ts_results):.2f}, Std: {np.std(ts_results):.2f},        Min: {np.min(ts_results):.2f}, Max: {np.max(ts_results):.2f}')

# Mean: 36.18, Median 36.19, Std: 0.20,        Min: 34.76, Max: 36.46
# Mean: 87.90, Median 88.11, Std: 1.16,        Min: 84.47, Max: 89.59


mt_results = sorted(mt_results, reverse=True)
ts_results = sorted(ts_results, reverse=True)

top_half = mt_results[:len(mt_results) // 2]
bottom_half = mt_results[len(mt_results) // 2:]



# shuffled_result = np.random.permutation(sorted_file_name_result_list)
seed = 0
min_eps = aso(top_half, bottom_half, seed=seed)
print("\nmt min_eps: ", min_eps)

top_half = ts_results[:len(ts_results) // 2]
bottom_half = ts_results[len(ts_results) // 2:]

min_eps = aso(top_half, bottom_half, seed=seed)
print("\nts min_eps: ", min_eps)
