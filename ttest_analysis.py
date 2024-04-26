import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from numpy import std, mean, sqrt
from scipy import stats
from statsmodels.stats.power import TTestIndPower
import random
import data


def calculate_ttest_sample_size(alpha, effect_size, power):
    # Create an instance of the FTestAnovaPower class
    power_analysis = TTestIndPower()

    # Calculate sample size
    sample_size = power_analysis.solve_power(effect_size=effect_size,
                                             alpha=alpha,
                                             power=power,
                                             alternative="two-sided",
                                             ratio=1,  # ratio of sample sizes between the two groups
                                             nobs1=None,  # sample size for group 1, None means it will be calculated
                                             )
    return sample_size


def calculate_ttest_effect_size(a, b):
    """
    cohen d is the effect size for t-test
    :param a:
    :param b:
    :return:
    """
    nx = len(a)
    ny = len(b)
    dof = nx + ny - 2

    effect_size = (mean(a) - mean(b)) / sqrt(((nx - 1) * std(a, ddof=1) ** 2 + (ny - 1) * std(b, ddof=1) ** 2) / dof)

    effect_size = abs(effect_size)
    return effect_size


def perform_ttest_simulation(a, n, file_name, effect_size_dict):
    """
    Split the data into two groups and perform t-test
    :param a:
    :param n:
    :param file_name:
    :param effect_size_dict:
    :return:
    """
    results_list = []
    for _ in range(n):
        np.random.shuffle(a)
        a1, a2 = np.split(a, 2)
        t, p = stats.ttest_ind(a1, a2)
        effect_size = calculate_ttest_effect_size(a1, a2)

        results_list.append((t, p, effect_size))

    results_df = pd.DataFrame(results_list, columns=["t", "p", "effect_size"])

    significant_results = results_df[results_df["p"] < 0.05]

    with open(f"results/ttest_simulation_{file_name}_effect_size.txt", "w") as f:
        f.write(f"Number of significant results: {len(significant_results)}\n")
        for effect_size_name, effect_size in effect_size_dict.items():
            significant_results_effect_size = significant_results[significant_results["effect_size"] > effect_size]
            f.write(
                f"Number of significant results with effect size > {effect_size}: {len(significant_results_effect_size)}\n")
    fig, ax = plt.subplots(1, 1, figsize=(4, 3))

    sns.histplot(significant_results["effect_size"], ax=ax, kde=True, stat='count', color='blue')

    ax.set_title("Effect Size Distribution of Significant Results")
    ax.set_xlabel("Effect Size")
    fig.tight_layout()
    fig.savefig(f"figures/ttest_simulation_{file_name}_effect_size_hist.pdf")

    results_df.to_csv(f"results/ttest_simulation_{file_name}.csv", index=False)


def main():
    sns.set_theme()
    sns.set_style("darkgrid")
    random.seed(42)
    np.random.seed(42)

    mt_results = data.get_mt_results()
    ts_results = data.get_ts_results()

    effect_size_dict = {
        "small": 0.2,
        "medium": 0.5,
        "large": 0.8,
        "very_large": 1.2,
    }
    with open("results/ttest_sample_size.txt", "w") as f:
        for effect_size in effect_size_dict.values():
            sample_size = calculate_ttest_sample_size(0.05, effect_size, 0.8)
            f.write(f"Required Sample Size for effect size {effect_size}: {math.ceil(sample_size)}\n")

    perform_ttest_simulation(mt_results, n=10 ** 4, file_name="mt", effect_size_dict=effect_size_dict)
    perform_ttest_simulation(ts_results, n=10 ** 4, file_name="ts", effect_size_dict=effect_size_dict)


if __name__ == "__main__":
    main()
