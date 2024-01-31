import sys

from code.classes import protein, amino
from code.algorithms import baseline, randomise, depth_first, breadth_first,\
    hill_climb, simulated_annealing
from code.visualisation import visualisation
import code.algorithms.greedy as greedy
import pickle

# Use example: python3 main.py greedy protein1


def baseline_func(input_file):
    # ------------- baseline random algorithm -------------
    test_protein = protein.Protein(input_file)
    baseline.baseline_random_algorithm(test_protein)

    while test_protein.check_validity() == False:
        baseline.baseline_random_algorithm(test_protein)
    
    return test_protein

def random_plus_func(input_file):
    # ------------- adaptations to random algo -------------
    test_protein = protein.Protein(input_file)
    randomise.random_assignment_protein(test_protein)

    while test_protein.check_validity() == False:
        randomise.random_assignment_protein(test_protein)
    
    return test_protein


def greedy_func(input_file):
    # ------------- greedy-random algorithm -----------
    test_protein = protein.Protein(input_file)
    greedy.greedy_random_algorithm(test_protein)

    return test_protein

def depth_first_func(input_file):
    # ------------- depth-first algorithm -------------
    test_protein = protein.Protein(input_file)
    depth = depth_first.DepthFirst(test_protein)

    # Run the algoritm for x amount of seconds
    depth.run("depthfirst_output.csv")

    return depth.protein

def breadth_first_func(input_file):
    # ------------- depth-first algorithm -------------
    test_protein = protein.Protein(input_file)
    breadth = breadth_first.BreadthFirst(test_protein)

    # Run the algoritm for x amount of seconds
    breadth.run("breadthfirst_output.csv")

    return breadth.protein

def hill_climb_func(input_file: str) -> 'protein':
    # ------------- depth-first algorithm -------------
    current_protein = protein.Protein(input_file)
    hill_climb.setup_hill_climb(current_protein)
    return current_protein

def simulated_annealing_func(input_file: str, temperature: int,
                             cooling_rate_interval: int,
                             no_progress_limit: int) -> 'protein':
    # ------------- depth-first algorithm -------------
    current_protein = protein.Protein(input_file)
    simulated_annealing.setup_simulated_annealing(current_protein, temperature,
                                                  cooling_rate_interval,
                                                  no_progress_limit)
    return current_protein

if __name__ == "__main__":
    
    algorithm = f"{sys.argv[1]}"
    input_file = f"proteins/{sys.argv[2]}.csv"
    
    
    if algorithm == "baseline":
        test_protein = baseline_func(input_file)
    elif algorithm == "random":
        test_protein = random_plus_func(input_file)
    elif algorithm == "greedy":
        test_protein = greedy_func(input_file)
    elif algorithm == "depth":
        test_protein = depth_first_func(input_file)
    elif algorithm == "breadth":
        test_protein = depth_first_func(input_file)
    elif algorithm == "hill_climb":
        test_protein = hill_climb_func(input_file)
    elif algorithm == "simulated_annealing":
        start_temperature = int(sys.argv[3])
        cooling_rate_interval = int(sys.argv[4])
        no_progress_limit = int(sys.argv[5])
        test_protein = simulated_annealing_func(input_file, start_temperature,
                                                cooling_rate_interval,
                                                no_progress_limit)
 
    if sys.argv[3] == "experiment":
        result = pickle.dumps(test_protein)
        sys.stdout.buffer.write(result)
    else:
        output_file = f"{sys.argv[3]}.csv"
        test_protein.print_output(output_file)
        visualisation.print_folded_protein(f"output/{output_file}")
