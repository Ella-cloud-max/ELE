import subprocess
import time
import sys
from code.algorithms import baseline
from code.classes import protein
import matplotlib.pyplot as plt

start = time.time()
n_runs = 0
list_scores = []

while time.time() - start < 100:
    print(f"run: {n_runs}")
    result = subprocess.run(["timeout", "5", "python3", "main.py", "proteins/protein1.csv"], capture_output=True, text = True)
    print(result.stdout)
    if result.stdout == "":
        n_runs += 1
        continue
    list_scores.append(int(result.stdout))
    n_runs += 1

bins = [x + 0.5 for x in set(sorted(list_scores))]
bins.append(min(bins) - 1)
bins = sorted(bins)

plt.hist(list_scores, bins)
plt.xlim(min(list_scores) - 1.5, max(list_scores) + 1.5)
plt.show()