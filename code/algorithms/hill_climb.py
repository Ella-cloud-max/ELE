from code.classes.protein import Protein
import random
from code.algorithms import randomise
from typing import Any
from copy import deepcopy


def create_pull_options(protein: 'Protein') -> tuple[list[int], list[int],
                                                     list[str]]:
    """
    Creates the mutation options created by pull move mutation.

    pre: input is a protein class object
    post: returns a tuple which contains a list of id's, list of directions
          and a list of the strings 'pull'
    """
    directions_list: list = []
    id_list: list = []
    mutation_list: list[str] = []
    aminos_id = protein.i_list

    for i in range(len(aminos_id) - 1):
        options = protein.aminos[i].get_pull_options()
        for option in options:
            id_list.append(i)
            directions_list.append(option)
            mutation_list.append("pull")
    return (id_list, directions_list, mutation_list)


def create_rotate_options(protein: 'Protein') -> tuple[list[int], list[int],
                                                       list[str]]:
    """
    Creates the mutation options for a rotate move

    pre: input is a protein class object
    post: returns a tuple which contains a list of id's, list of directions
          and a list of the strings 'rotate'
    """
    directions_list: list[int] = []
    id_list: list[int] = []
    mutation_list: list[str] = []
    aminos_id = protein.i_list

    for i in range(1, len(aminos_id) - 1):
        options = protein.aminos[i].get_rotate_options()
        for option in options:
            id_list.append(i)
            directions_list.append(option)
            mutation_list.append("rotate")
    return (id_list, directions_list, mutation_list)


def create_change_direction_options(protein: 'Protein')\
            -> tuple[list[int], list[int], list[str]]:
    """
    Creates the mutation options for a rotate move where the direction of
    the aminos after it stay the same

    pre: input is a protein class object
    post: returns a tuple which contains a list of id's, list of directions
        and a list of the strings 'change direction'
    """
    directions_list: list = []
    id_list: list = []
    mutation_list: list[str] = []
    aminos_id = protein.i_list

    for i in range(1, len(aminos_id) - 1):
        options = protein.aminos[i].get_rotate_options()
        for option in options:
            id_list.append(i)
            directions_list.append(option)
            mutation_list.append("change direction")
    return (id_list, directions_list, mutation_list)


def create_options(protein: 'Protein') -> tuple[list[int], list[int],
                                                list[str]]:
    """
    Combines the mutation option lists

    pre: input is a protein class object
    post: returns a tuple which contains a list of id's, list of directions and
        a list of the strings
    """

    id_list, directions_list, mutation_list = create_pull_options(protein)
    rotate_options = create_rotate_options(protein)
    change_direction_options = create_change_direction_options(protein)
    id_list = id_list + rotate_options[0] + change_direction_options[0]
    directions_list = directions_list + rotate_options[1] + \
        change_direction_options[1]
    mutation_list = mutation_list + rotate_options[2] + \
        change_direction_options[2]
    return (id_list, directions_list, mutation_list)


def mutate_direction_rotate(amino_id: int, current_protein: 'Protein',
                            new_direction: int) -> None:
    """
    Changes the direction of the amino-acid to the given new direction,
    which id is given as parameter

    pre: input is a protein class object
    """
    amino_change = current_protein.aminos[amino_id]
    old_direction = amino_change.direction
    amino_change.direction = new_direction
    current_protein.rotate(amino_id, old_direction)
    current_protein.change_coordinates(amino_id)


def mutate_direction_pull(amino_id: int, current_protein: 'Protein',
                          new_direction: int) -> None:
    """
    Swaps the direction of the given amino-acid with
    the direction of the next amino

    pre: input is a protein class object
    """
    amino_change = current_protein.aminos[amino_id]
    if amino_id != 0 and amino_id != current_protein.size - 2:
        amino_change.next_amino.direction = amino_change.direction
    amino_change.direction = new_direction
    current_protein.change_coordinates(amino_id)


def try_direction(protein: 'Protein', new_direction: int, mutation_option: str,
                  amino_id: int) -> tuple[bool, int, Any]:
    """
    The given mutation direction is tested on validity

    pre: input is a protein class object, integer new direction and string
    post: returns a tuple containing a boolean value,
          protein or none and the score
    """
    copy_protein = deepcopy(protein)
    if mutation_option == "rotate":
        mutate_direction_rotate(amino_id, copy_protein, new_direction)
    elif mutation_option == "pull":
        mutate_direction_pull(amino_id, copy_protein, new_direction)
    else:
        copy_protein.aminos[amino_id].direction = new_direction
        copy_protein.change_coordinates(amino_id)
    if copy_protein.check_validity():
        return (True, copy_protein.count_score(), copy_protein)
    return (False, 1, None)


def hill_climb(protein: 'Protein') -> tuple['Protein', int]:
    """
    Executes the hill climb algorithm

    pre: input is a protein class object
    post: returns a tuple containing the best protein and the score
    """
    current_protein = (deepcopy(protein), protein.count_score())
    while True:
        id_list, directions_list, mutation_list = \
            create_options(current_protein[0])
        index_list: list[int] = []
        index_list = list(range(len(id_list)))

        while len(index_list) != 0:
            choice = random.choice(index_list)
            amino_id = id_list[choice]
            new_direction = directions_list[choice]
            mutation_option = mutation_list[choice]
            trial = try_direction(current_protein[0], new_direction,
                                  mutation_option, amino_id)
            if trial[0] and trial[1] < current_protein[1]:
                current_protein = (trial[2], trial[1])
                break
            else:
                index_list.remove(choice)
        if len(index_list) == 0:
            return current_protein
    return current_protein


def setup_hill_climb(protein: 'Protein') -> 'Protein':
    """
    Initialise hill climb function and create a random structure
    of the loaded protein

    pre: input is a str that contains the name of the csv file of the protein
         and an integer that limits the amount of iterations
    post: returns the best protein found, as a protein class object
    """
    randomise.random_assignment_protein(protein)
    counter = 0
    best_protein = deepcopy(protein)
    while True:
        current_solution, current_solution_score = hill_climb(protein)
        if current_solution_score < best_protein[0].count_score():
            best_protein = deepcopy(current_solution)
        counter += 1
        print(f"protein {counter}, score {current_solution_score}")
        randomise.random_assignment_protein(protein)
    return best_protein
