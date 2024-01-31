from code.classes import protein, amino
from code.algorithms import randomise
from code.visualisation import visualisation
import code.algorithms.greedy as greedy
import matplotlib.pyplot as plt
import time

start = time.time()
list_scores = []
best_protein = None
min_score = 0
for N in range(40):
    print(N)
    input_file = "proteins/protein4.csv"

    test_protein = protein.Protein(input_file)
    greedy.greedy(test_protein)
    
    score = test_protein.count_score()
    list_scores.append(score)
    if score < min_score:
        best_protein = test_protein
        min_score = score


length = time.time() - start

print(length)

best_protein.print_output("repetition/protein4.csv")
visualisation.print_folded_protein(f"output/repetition/protein4.csv")

bins = [x + 0.5 for x in set(sorted(list_scores))]
bins.append(min(bins) - 1)
bins = sorted(bins)

plt.hist(list_scores, bins)
plt.xlim(min(list_scores) - 1.5, max(list_scores) + 1.5)
plt.show()
