import subprocess
import time
import sys
from code.algorithms import baseline
from code.classes import protein

input_file = f"proteins/protein1.csv"
start = time.time()
n_runs = 0
list_scores = []

while time.time() - start < 100:
    print(f"run: {n_runs}")
    test_protein = protein.Protein(input_file)
    result = subprocess.run(["timeout", "5", "python3", "main.py", "proteins/protein1.csv"], capture_output=True)
    list_scores.append(result.stdout)
    n_runs += 1

print(list_scores)