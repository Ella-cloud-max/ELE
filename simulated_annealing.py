# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:21:32 2024

@author: Eric van Huizen
"""

from import_csv import import_structure
from code.classes.amino import Amino
from code.classes.protein import Protein
from code.algorithms import randomise
from code.visualisation.visualisation import *
from math import e as e
from typing import Any
import sys
import random
import copy
import time

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

def simulated_annealing(protein) -> tuple[Any]:
    Zc = protein.count_score()
    T = 20
    iterate_counter = 0
    current_protein = copy.deepcopy(protein)
    best_solution = (copy.deepcopy(current_protein), Zc)
    no_progress_counter = 0
    while iterate_counter < 1000:
        # print(iterate_counter)
        if iterate_counter%200 == 0 and iterate_counter != 0:
            T = T * 0.5
        id_list, directions_list, mutation_list = create_options(current_protein)
        index_list: list[int] = []
        [index_list.append(x) for x in range(len(id_list))]

        while len(index_list) != 0:
            choice = random.choice(index_list)
            amino_id = id_list[choice]
            new_direction = directions_list[choice]
            mutation_option = mutation_list[choice]

            trial = try_direction(current_protein, new_direction, mutation_option, amino_id)
            if trial[0]:
                x = (Zc - trial[1])/T
                Zn = trial[1]
            if trial[0] and Zn <= Zc:
                Zc = Zn
                current_protein = trial[2]
                
                if Zc < best_solution[1]:
                    best_solution = (copy.deepcopy(current_protein), Zc)
                break
            elif trial[0] and random.random() > pow(e, x):
                Zc = trial[1]
                current_protein = trial[2]

                if Zc < best_solution[1]:
                    best_solution = (copy.deepcopy(current_protein), Zc)
                break
            else:
                index_list.remove(choice)
        iterate_counter += 1
        if  Zn >= best_solution[1]:
            no_progress_counter += 1
        elif Zn < best_solution[1]:
            no_progress_counter = 0
    
        if no_progress_counter >= 100:
            return best_solution
        if len(index_list) == 0:
            return best_solution
    
    return best_solution


if __name__ == "__main__":
    start_time = time.time()
    counter = 0
    loop_amount = int(sys.argv[2])
    # to create random protein
    protein = Protein(f"proteins/{sys.argv[1]}")
    randomise.random_assignment_protein(protein)
    while protein.check_validity() == False:
        randomise.random_assignment_protein(protein)
    best_protein = copy.deepcopy(protein)
    while counter < loop_amount:
        current_solution, current_solution_score = simulated_annealing(protein)
        if current_solution_score < best_protein.count_score():
            best_protein = copy.deepcopy(current_solution)
        counter += 1
        print(f"protein {counter}, score {current_solution_score}")
        if counter != loop_amount:
            randomise.random_assignment_protein(protein)
            while protein.check_validity() == False:
                randomise.random_assignment_protein(protein)
    id_list, directions_list, mutation_list = create_options(best_protein)
    score_list = []
    protein_list = []
    for i in range(len(id_list)):
        trial = try_direction(best_protein, directions_list[i], mutation_list[i], id_list[i])
        if trial[0]:
            score_list.append(trial[1])
            protein_list.append(trial[2])
    score = min(score_list)
    if score < best_protein.count_score():
        index = score_list.index(score)
        best_protein = protein_list[index]
    protein_name = sys.argv[1]
    best_protein.print_output("output_" + protein_name)
    print_folded_protein("output/output_" + protein_name)
    end_time = time.time()
    print(f"Time duration is {end_time - start_time}")
