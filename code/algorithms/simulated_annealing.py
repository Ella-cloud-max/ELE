from code.classes.protein import Protein
<<<<<<< HEAD
from code.algorithms import randomise
=======
from code.algorithms import random_plus
from hill_climb import create_options, try_direction
>>>>>>> 4e3aeb0f34808e59ccad526df2b42b98174638f7
from math import e as e
import random
from copy import deepcopy


def simulated_annealing(protein: 'Protein', start_temperature: int,
                        cooling_rate_interval: int,
                        no_progress_limit: int) -> tuple['Protein', int]:
    """
    Executes the simulated annealing algorithm

    pre: input is a protein class object, an integer start temperature,
    post: returns a tuple containing a protein class object and the score
    """

    current_score = protein.count_score()
    T = float(start_temperature)
    iterate_counter = 0
    current_protein = deepcopy(protein)
    best_solution = (deepcopy(current_protein), current_score)
    no_progress_counter = 0
    while iterate_counter < 1000:
        if iterate_counter % cooling_rate_interval == 0 and \
                iterate_counter != 0:
            T = T * 0.5
        id_list, directions_list, mutation_list = create_options(
                                                    current_protein)
        index_list: list[int] = []
        index_list = list(range(len(id_list)))

        while len(index_list) != 0:
            choice = random.choice(index_list)
            amino_id = id_list[choice]
            new_direction = directions_list[choice]
            mutation_option = mutation_list[choice]
            trial = try_direction(current_protein, new_direction,
                                  mutation_option, amino_id)
            if trial[0]:
                x = (current_score - trial[1])/T
                new_score = trial[1]
            if trial[0] and new_score <= current_score:
                current_score = new_score
                current_protein = trial[2]

                if current_score < best_solution[1]:
                    best_solution = (deepcopy(current_protein), current_score)
                break
            elif trial[0] and random.random() > pow(e, x):
                current_score = trial[1]
                current_protein = trial[2]

                if current_score < best_solution[1]:
                    best_solution = (deepcopy(current_protein), current_score)
                break
            else:
                index_list.remove(choice)

        iterate_counter += 1
        if new_score >= best_solution[1]:
            no_progress_counter += 1
        elif new_score < best_solution[1]:
            no_progress_counter = 0

        if no_progress_counter >= no_progress_limit:
            return best_solution
        if len(index_list) == 0:
            return best_solution
    return best_solution


def setup_simulated_annealing(protein: 'Protein', start_temperature: int,
                              cooling_rate_interval: int,
                              no_progress_limit: int) -> 'Protein':
    """
    Initialise simulated annealing, create a random structure of
    the loaded protein and try to improve the output of simulated annealing

    pre: input is the protein file name, iteration limit, starting temperature,
        cooling rateinterval and limit for the having no progress
    post: returns a protein class object
    """
    protein = Protein(f"proteins/{protein_file_name}")
    random_plus.random_assignment_protein(protein)
    counter = 0
    best_protein = deepcopy(protein)
    while True:
        current_solution, current_solution_score = simulated_annealing(
                protein, start_temperature, cooling_rate_interval,
                no_progress_limit)
        if current_solution_score < best_protein.count_score():
            best_protein = deepcopy(current_solution)
        counter += 1
        print(f"protein {counter}, score {current_solution_score}")
        random_plus.random_assignment_protein(protein)
    id_list, directions_list, mutation_list = create_options(best_protein)
    score_list = []
    protein_list = []
    for i in range(len(id_list)):
        trial = try_direction(best_protein, directions_list[i],
                              mutation_list[i], id_list[i])
        if trial[0]:
            score_list.append(trial[1])
            protein_list.append(trial[2])
    score = min(score_list)
    if score < best_protein.count_score():
        index = score_list.index(score)
        best_protein = protein_list[index]
    return best_protein
