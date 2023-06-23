
import os
import re
from deepsig import aso
import numpy as np
import pandas as pd

mt_results = pd.read_csv('results/rethinking_result.csv')["bleu"].tolist()
ts_results = pd.read_csv('results/text-simplification/search.csv')["BLEU"].tolist()


mt_results = sorted(mt_results)
ts_results = sorted(ts_results)

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
