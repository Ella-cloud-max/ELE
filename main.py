import sys

from code.classes import protein, amino
from code.algorithms import randomise
from code.algorithms import depth_first
from code.visualisation import visualisation
from code.algorithms import baseline
import greedy



if __name__ == "__main__":

    input_file = f"{sys.argv[1]}"

    # ------------- baseline random algorithm -------------

    test_protein = protein.Protein(input_file)
    baseline.baseline_random_protein(test_protein)

    while test_protein.check_viability() == False:
        baseline.baseline_random_protein(test_protein)
    
    test_protein.print_output("main/random_baseline.csv")
    visualisation.print_folded_protein(f"output/main/random_baseline.csv")

    # ------------- adaptations to random algo -------------
    
    test_protein = protein.Protein(input_file)
    randomise.random_assignment_protein(test_protein)

    while test_protein.check_viability() == False:
        randomise.random_assignment_protein(test_protein)
    
    test_protein.print_output("main/random_improved.csv")
    visualisation.print_folded_protein(f"output/main/random_improved.csv")

    # ------------- greedy-random algorithm -----------

    test_protein = protein.Protein(input_file)
    greedy.greedy(test_protein)
    test_protein.print_output("main/greedy_random.csv")
    visualisation.print_folded_protein(f"output/main/greedy_random.csv")

    # ------------- depth-first algorithm -------------

    test_protein = protein.Protein(input_file)
    depth = depth_first.DepthFirst(test_protein)

    # Run the algoritm for x amount of seconds
    depth.run(5)

    print(f"Value of the configuration after Depth First: "
         f"{depth.protein.count_score()}")

    depth.protein.print_output("output_ella.csv")
    visualisation.print_folded_protein("output/output_ella.csv")