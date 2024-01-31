import subprocess
import time
import sys
import pickle
from code.visualisation import visualisation, histogram

algorithm = sys.argv[1]
input_protein = sys.argv[2] 
output_file = sys.argv[1] + "_" + sys.argv[2]

start = time.time()
n_runs = 0
list_scores = []
best_protein = None
min_score = 0

while time.time() - start < 100:
    print(f"run: {n_runs}")
    result = subprocess.Popen(["timeout", "10", "python3.11", "main.py", algorithm, f"{input_protein}", "experiment"], stdout=subprocess.PIPE)
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

best_protein.print_output(f"experiment/experiment_{output_file}.csv")
visualisation.print_folded_protein(f"output/experiment/experiment_{output_file}.csv")

histogram.histogram(list_scores, output_file)
