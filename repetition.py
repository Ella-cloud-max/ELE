from code.classes import protein, amino
from code.algorithms import randomise
from code.visualisation import visualisation
import greedy
import matplotlib.pyplot as plt
import time

start = time.time()
list_scores = []
for N in range(500):
    input_file = "proteins/protein4.csv"

    test_protein = protein.Protein(input_file)
    greedy.greedy(test_protein)
    
    list_scores.append(test_protein.count_score())

length = time.time() - start

print(length)

bins = [x + 0.5 for x in set(sorted(list_scores))]
bins.append(min(bins) - 1)
bins = sorted(bins)

plt.hist(list_scores, bins)
plt.xlim(min(list_scores) - 1.5, max(list_scores) + 1.5)
plt.show()
