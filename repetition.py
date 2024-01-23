from code.classes import protein, amino
from code.algorithms import randomise
from code.visualisation import visualisation
import matplotlib.pyplot as plt
import time

start = time.time()
list_scores = []
for N in range(100000):
    input_file = "proteins/protein.csv"

    test_protein = protein.Protein(input_file)
    
    random_protein = randomise.random_assignment_protein(test_protein)
    while test_protein.check_viability() == False:
        random_protein = randomise.random_assignment_protein(test_protein)
    
    list_scores.append(test_protein.count_score())

length = time.time() - start

print(length)

plt.hist(list_scores, [-3.5, -2.5, -1.5, -0.5, 0.5])
plt.xlim(min(list_scores) - 1.5, max(list_scores) + 1.5)
plt.show()