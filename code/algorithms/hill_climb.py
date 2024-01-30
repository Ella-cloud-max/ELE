# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:55:16 2024

@author: Eric van Huizen
"""

import random
from code.algorithms import randomise
from typing import Any
import copy


def create_pull_options(protein):
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

def create_rotate_options(protein):
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

def create_change_direction_options(protein):
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

def create_options(protein):
    id_list, directions_list, mutation_list = create_pull_options(protein)
    rotate_options = create_rotate_options(protein)
    change_direction_options = create_change_direction_options(protein)
    id_list = id_list + rotate_options[0] + change_direction_options[0]
    directions_list = directions_list + rotate_options[1] + change_direction_options[1]
    mutation_list = mutation_list + rotate_options[2] + change_direction_options[2]
    return (id_list, directions_list, mutation_list)

def mutate_direction_rotate(amino_id, current_protein, new_direction):
    amino_change = current_protein.aminos[amino_id]
    old_direction = amino_change.direction
    amino_change.direction = new_direction
    current_protein.rotate(amino_id, old_direction)
    current_protein.change_coordinates(amino_id)

def mutate_direction_pull(amino_id, current_protein, new_direction):
    amino_change = current_protein.aminos[amino_id]
    if amino_id != 0 and amino_id != current_protein.size - 2:
        amino_change.next_amino.direction = amino_change.direction
    amino_change.direction = new_direction
    current_protein.change_coordinates(amino_id)

def try_direction(protein, new_direction, mutation_option, amino_id):
    copy_protein = copy.deepcopy(protein)
    if mutation_option == "rotate":
        mutate_direction_rotate(amino_id, copy_protein, new_direction)
    elif mutation_option == "pull":
        mutate_direction_pull(amino_id, copy_protein, new_direction)
    else:
        copy_protein.aminos[amino_id].direction = new_direction
        copy_protein.change_coordinates(amino_id)
    if copy_protein.check_viability():
        return (True, copy_protein.count_score(), copy_protein)
    return (False, 1)

def hill_climb(protein) -> tuple[Any]:
    current_protein = (copy.deepcopy(protein), protein.count_score())
    while True:
        id_list, directions_list, mutation_list = create_options(current_protein[0])
        index_list: list[int] = []
        [index_list.append(x) for x in range(len(id_list))]
        while len(index_list) != 0:
            choice = random.choice(index_list)
            amino_id = id_list[choice]
            new_direction = directions_list[choice]
            mutation_option = mutation_list[choice]
            trial = try_direction(current_protein[0], new_direction, mutation_option, amino_id)
            if trial[0] and trial[1] < current_protein[1]:
                current_protein = (trial[2], trial[1])
                break
            else:
                index_list.remove(choice)
        if len(index_list) == 0:
            return current_protein
    return current_protein

def setup_hill_climb(protein_file_name, loop_amount):
    protein = Protein(f"proteins/{protein_file_name}")
    randomise.random_assignment_protein(protein)
    counter = 0
    best_protein = copy.deepcopy(protein)
    while counter < loop_amount:
        current_solution, current_solution_score = hill_climb(protein)
        if current_solution_score < best_protein[0].count_score():
            best_protein = copy.deepcopy(current_solution)
        counter += 1
        print(f"protein {counter}, score {current_solution_score}")
        if counter != loop_amount:
            randomise.random_assignment_protein(protein)
    
    return best_protein
