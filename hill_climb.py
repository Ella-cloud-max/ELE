# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:55:16 2024

@author: Eric van Huizen
"""

import random
from code.classes.amino import Amino
from code.classes.protein import Protein
from code.algorithms import randomise
from code.visualisation.visualisation import print_folded_protein
from typing import Any
import copy
import time
import sys

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

def create_options(protein):
    id_list, directions_list, mutation_list = create_pull_options(protein)
    options = create_rotate_options(protein)
    id_list += options[0]
    directions_list += options[1]
    mutation_list += options[2]
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
    else:
        mutate_direction_pull(amino_id, copy_protein, new_direction)
    if copy_protein.check_validity():
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

if __name__ == "__main__":
    start_time = time.time()
    counter = 0
    loop_amount = int(sys.argv[2])
    # to create random protein
    protein = Protein(f"proteins/{sys.argv[1]}")
    randomise.random_assignment_protein(protein)
    while protein.check_validity() == False:
        randomise.random_assignment_protein(protein)
    best_protein = (copy.deepcopy(protein), protein.count_score())
    while counter < loop_amount:
        random_score = protein.count_score()
        current_solution = hill_climb(protein)
        if current_solution[1] < best_protein[0].count_score():
            best_protein = (copy.deepcopy(current_solution[0]), random_score)
        counter += 1
        print(f"protein {counter}, score {current_solution[0].count_score()}")
        if counter != loop_amount:
            randomise.random_assignment_protein(protein)
            while protein.check_validity() == False:
                randomise.random_assignment_protein(protein)
    protein_name = sys.argv[1]
    best_protein[0].print_output("output_" + protein_name)
    print(f"This is the best protein found, the random score was {best_protein[1]}")
    print_folded_protein("output/output_" + protein_name)
    end_time = time.time()
    print(f"Time duration is {end_time - start_time}")