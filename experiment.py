import subprocess
import time
import sys
from code.algorithms import baseline
from code.classes import protein

input_file = f"proteins/protein1.csv"
start = time.time()
n_runs = 0

while time.time() - start < 100:
    print(f"run: {n_runs}")
    test_protein = protein.Protein(input_file)
    subprocess.run(["timeout", "60", f"{baseline.baseline_random_protein(test_protein)}"])
    n_runs += 1