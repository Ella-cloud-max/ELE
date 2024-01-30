import sys

from code.classes import protein, amino
from code.algorithms import baseline, randomise, depth_first
from code.visualisation import visualisation
import code.algorithms.greedy as greedy

def baseline(input_file):
    # ------------- baseline random algorithm -------------

    print("BASELINE")

    test_protein = protein.Protein(input_file)
    baseline.baseline_random_protein(test_protein)

    while test_protein.check_validity() == False:
        baseline.baseline_random_protein(test_protein)

    test_protein.print_output("random_baseline.csv")
    visualisation.print_folded_protein(f"output/main/random_baseline.csv")

def random_plus(input_file):
    # ------------- adaptations to random algo -------------

    print("RANDOM+")

    test_protein = protein.Protein(input_file)
    randomise.random_assignment_protein(test_protein)

    while test_protein.check_validity() == False:
        randomise.random_assignment_protein(test_protein)

    test_protein.print_output("main/random_improved.csv")
    visualisation.print_folded_protein(f"output/main/random_improved.csv")

def greedy_func(input_file):
    # ------------- greedy-random algorithm -----------

    test_protein = protein.Protein(input_file)
    greedy.greedy(test_protein)

    return test_protein.count_score()
    # test_protein.print_output("main/greedy_random.csv")
    # visualisation.print_folded_protein(f"output/main/greedy_random.csv")

def depth_first(input_file):
    # ------------- depth-first algorithm -------------

    print("DEPTH-FIRST")

    test_protein = protein.Protein(input_file)
    depth = depth_first.DepthFirst(test_protein)

    # Run the algoritm for x amount of seconds
    depth.run("depthfirst_output.csv")

    print(f"Value of the configuration after Depth First: "
            f"{depth.protein.count_score()}")

    depth.protein.print_output("output_ella.csv")
    visualisation.print_folded_protein("output/output_ella.csv")


if __name__ == "__main__":

    input_file = f"{sys.argv[1]}"
    score = greedy_func(input_file)

    print(score, end = '')
    