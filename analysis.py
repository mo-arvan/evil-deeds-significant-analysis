import os
import re
from deepsig import aso
import numpy as np
# 2023-06-02 03:56:07 | INFO | fairseq_cli.generate | Generate test with beam=5: BLEU4 = 34.76, 68.2/42.6/28.6/19.6 (BP=0.974, ratio=0.975, syslen=127816, reflen=131156)


result_list = []

path = "results/rethinking/"

bleu_pattern = r"BLEU4 = (\d+\.\d+)"

for f in os.listdir(path):
    dir_path = os.path.join(path, f)
    if os.path.isdir(dir_path):
        with open(dir_path + "/generated.result", "r") as file:
            last_line = file.readlines()[-1]

            bleu = re.findall(bleu_pattern, last_line)[0]

            result_list.append(float(bleu))


sorted_result = sorted(result_list, reverse=True)

top_half = sorted_result[:len(sorted_result) // 2]
bottom_half = sorted_result[len(sorted_result) // 2:]

seed = 1234
np.random.seed(seed)
min_eps = aso(top_half, bottom_half, seed=seed)  # min_eps = 0.225, so A is better

print("Top half: ", min_eps)