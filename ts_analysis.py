import math
import pandas as pd

SEARCH_RESULTS_FILE_NAME = "results/text-simplification/evaluation_results_test.en_references.tsv_nts_search_test_translation_20220607-024145.csv"

def float_formatter(x):
    if math.isnan(x):
        return ""
    return "%1.2f" % x

def main():
    search_results_df = pd.read_csv(SEARCH_RESULTS_FILE_NAME)
    search_results_df = search_results_df[search_results_df["Hypothesis"] == '1']

    search_results_df = search_results_df.sort_values(["Variant", "Epoch"])

    bleu_results = search_results_df[search_results_df["Metric"] == "BLEU"]
    sari_results = search_results_df[search_results_df["Metric"] == "SARI"]
    best_performing_validation = search_results_df[["Variant", "Perplexity"]].groupby("Variant").min(
        "Perplexity").reset_index()

    final_bleu_results = bleu_results[["Variant", "Epoch", "Perplexity", "Score"]].merge(best_performing_validation,
                                                                                on=["Variant", "Perplexity"],
                                                                                how="inner").sort_values(["Variant"])
    final_sari_results = sari_results[["Variant", "Epoch", "Perplexity", "Score"]].merge(best_performing_validation,
                                                                                on=["Variant", "Perplexity"],
                                                                                how="inner").sort_values(["Variant"])


    final_bleu_results.to_csv("results/text-simplification/bleu_results.csv", index=False)


if __name__ == "__main__":
    main()