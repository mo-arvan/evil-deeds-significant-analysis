import os
import subprocess
import itertools
import json
import pandas as pd

# Directory containing the files to choose from
directory_path = "results/text-simplification/nts_test_selected"

# Get a list of files in the directory
file_list = os.listdir(directory_path)

# Check if there are at least two files in the directory
if len(file_list) < 2:
    print("Not enough files in the directory.")
    exit(1)

# Generate all possible pair combinations of files
file_combinations = list(itertools.combinations(file_list, 2))

# Define the command to run
reference_files = [
    f"results/text-simplification/references/test_references_{i}"
    for i in range(9)  # Create paths from 0 to 8
]

results = []
for file_pair in file_combinations:
    file_a = os.path.join(directory_path, file_pair[0])
    file_b = os.path.join(directory_path, file_pair[1])

    # Construct the command as a list of arguments
    command = [
        "sacrebleu",
        *reference_files,
        "-i",
        file_a,
        file_b,
        "-m",
        "bleu",
        "-lc",
        "--paired-bs",
        "--paired-bs-n",
        "1000",
        "--force",
        # "-f"
        # "latex",
    ]

    # Run the command and capture the output
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        results.append(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running the command: {e}")
        exit(1)

# Parse JSON results into a list of dictionaries
parsed_results = [json.loads(result) for result in results]

# Create a DataFrame using pandas
data = []
for idx, result in enumerate(parsed_results):
    system_a = result[0]["system"]
    system_b = result[1]["system"]
    bleu_a = result[0]["BLEU"]
    bleu_b = result[1]["BLEU"]

    data.append(
        {
            "Pair Number": idx + 1,
            "System A": system_a,
            "System B": system_b,
            "BLEU Score A": bleu_a["score"],
            "BLEU p-value A": bleu_a.get("p_value", ""),
            "BLEU Mean A": bleu_a["mean"],
            "BLEU CI A": bleu_a["ci"],
            "BLEU Score B": bleu_b["score"],
            "BLEU p-value B": bleu_b.get("p_value", ""),
            "BLEU Mean B": bleu_b["mean"],
            "BLEU CI B": bleu_b["ci"],
        }
    )

df = pd.DataFrame(data)

# Define the CSV file path
csv_file_path = "results/permuate_paired_bootstrap_ts.csv"

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)
