import subprocess
import time
import sys
from code.algorithms import baseline
from code.classes import protein
import matplotlib.pyplot as plt
import pickle, codecs
from unidecode import unidecode
from code.visualisation import visualisation

input_protein = sys.argv[1]  

start = time.time()
n_runs = 0
list_scores = []
best_protein = None
min_score = 0

while time.time() - start < 100:
    print(f"run: {n_runs}")
    result = subprocess.Popen(["timeout", "5", "python3", "main.py", "greedy", f"{input_protein}"], stdout=subprocess.PIPE)
    output, _ = result.communicate()

    if output == "":
        n_runs += 1
        continue

    test_protein = pickle.loads(output)
    score = test_protein.count_score()
    list_scores.append(score)
    if score < min_score:
        best_protein = test_protein
        min_score = score

    n_runs += 1

best_protein.print_output(f"experiment_best_{input_protein}.csv")
visualisation.print_folded_protein(f"output/experiment_best_{input_protein}.csv")

bins = [x + 0.5 for x in set(sorted(list_scores))]
bins.append(min(bins) - 1)
bins = sorted(bins)

plt.hist(list_scores, bins)
plt.xlim(min(list_scores) - 1.5, max(list_scores) + 1.5)
plt.savefig("ella.png")
