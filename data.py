import pandas as pd


def get_mt_results():
    """
    Get the BLEU scores for machine translation experiments
    :return:
    """
    return pd.read_csv('results/text-simplification/search.csv')["BLEU"].to_numpy()


def get_ts_results():
    """
    Get the BLEU scores for text simplification experiments
    :return:
    """
    return pd.read_csv('results/rethinking/rethinking_result.csv')["bleu"].to_numpy()
