import os
import re
from deepsig import aso
import numpy as np
import pandas as pd
# 2023-06-02 03:56:07 | INFO | fairseq_cli.generate | Generate test with beam=5: BLEU4 = 34.76, 68.2/42.6/28.6/19.6 (BP=0.974, ratio=0.975, syslen=127816, reflen=131156)


file_name_result_list = []

path = "results/rethinking/"

bleu_pattern = r"BLEU4 = (\d+\.\d+)"

for f in os.listdir(path):
    dir_path = os.path.join(path, f)
    if os.path.isdir(dir_path):
        with open(dir_path + "/generated.result", "r") as file:
            last_line = file.readlines()[-1]

            bleu = re.findall(bleu_pattern, last_line)[0]

            file_name_result_list.append((f, float(bleu)))


sorted_file_name_result_list = sorted(file_name_result_list, reverse=True, key=lambda x: x[1])

with open("results/rethinking_result.txt", "w") as file:
    for result in sorted_file_name_result_list:
        file.write(str(result) + "\n")


results_df = pd.DataFrame(sorted_file_name_result_list, columns=["model", "bleu"])

results_df.to_csv("results/rethinking_result.csv", index=False)

