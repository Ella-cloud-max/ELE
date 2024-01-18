from code.classes import protein, amino
from code.algorithms import randomise
from code.visualisation import visualisation

score = 0
for N in range(10000):
    input_file = "proteins/protein1.csv"

    test_protein = protein.Protein(input_file)
    
    random_protein = randomise.random_assignment(test_protein)
    while test_protein.check_viability() == False:
        random_protein = randomise.random_assignment(test_protein)
    
    test_protein.print_output(f"repetitions/output_{N}")

    if test_protein.count_score() < score:
        score = test_protein.score
        visualisation.print_folded_protein(f"output/repetitions/output_{N}")