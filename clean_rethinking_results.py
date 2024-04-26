import os
import subprocess

# Define the base directory where you want to start your search
base_directory = "results/rethinking/evaluation_logs"

# Loop through all subdirectories in the base directory
for root, dirs, files in os.walk(base_directory):
    for directory in dirs:
        # Check if the directory name starts with "model-save-dir-"
        if directory.startswith("model-save-dir-"):
            # Construct the path to the generated.result file
            result_file_path = os.path.join(root, directory, "generated.result")

            # Check if the file exists
            if os.path.isfile(result_file_path):
                # Define the command
                # from: https://github.com/takase/rethink_perturbations
                command = (
                    f"cat generated.result | grep '^H' | sed 's/^H\\-//g' | "
                    "sort -t ' ' -k1,1 -n | cut -f 3- > clean.result"
                )

                # Execute the command using subprocess
                subprocess.run(command, shell=True, cwd=os.path.dirname(result_file_path))
                print(f"Processed {result_file_path} and created clean.result")

print("Done processing all applicable files.")