import random

import numpy as np
import pandas as pd
from deepsig import aso
from tqdm import tqdm

random.seed(0)
np.random.seed(0)

mt_results = pd.read_csv('results/rethinking/rethinking_result.csv')["bleu"].tolist()
ts_results = pd.read_csv('results/text-simplification/search.csv')["BLEU"].tolist()

print(
    f'Mean: {np.mean(mt_results):.2f}, Median {np.median(mt_results):.2f}, Std: {np.std(mt_results):.2f},        Min: {np.min(mt_results):.2f}, Max: {np.max(mt_results):.2f}')

print(
    f'Mean: {np.mean(ts_results):.2f}, Median {np.median(ts_results):.2f}, Std: {np.std(ts_results):.2f},        Min: {np.min(ts_results):.2f}, Max: {np.max(ts_results):.2f}')


def perform_aso(results_array, file_tag):
    result_len = len(results_array)
    range_indices = np.arange(result_len)
    range_indices = np.random.permutation(range_indices)

    eps_list = []

    for _ in tqdm(range(10 ** 4)):
        c = random.sample(range(result_len), result_len // 2)
        dist_a = [results_array[i] for i in c]
        dist_b = [results_array[i] for i in range_indices if i not in c]
        seed = 0
        min_eps = aso(dist_a, dist_b, seed=seed, show_progress=False, num_jobs=16)

        eps_list.append(min_eps)

    # combination_list = list(combination_list)
    # print(len(combination_list))
    less_than_05 = [i for i in eps_list if i < 0.05]
    print(len(less_than_05))

    print(np.mean(eps_list))
    print(np.median(eps_list))
    print(np.std(eps_list))
    print(np.min(eps_list))
    print(np.max(eps_list))

    # saving eps list to file as csv in pd
    pd.DataFrame(eps_list).to_csv(f"results/aso_eps_{file_tag}.csv", index=False)


perform_aso(mt_results, "mt")
perform_aso(ts_results, "ts")
