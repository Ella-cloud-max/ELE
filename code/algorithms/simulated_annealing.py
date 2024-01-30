# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:21:32 2024

@author: Eric van Huizen
"""

from code.classes.protein import Protein
from code.algorithms import randomise
from hill_climb import create_options, try_direction
from math import e as e
from typing import Any
import random
import copy


def simulated_annealing(protein, start_temperature, temp_decreasing_interval, no_progress_limit) -> tuple['Protein', int]:
    Zc = protein.count_score()
    T = start_temperature
    iterate_counter = 0
    current_protein = copy.deepcopy(protein)
    best_solution = (copy.deepcopy(current_protein), Zc)
    no_progress_counter = 0
    while iterate_counter < 1000:
        if iterate_counter%temp_decreasing_interval == 0 and iterate_counter != 0:
            T = T * 0.5
        id_list, directions_list, mutation_list = create_options(current_protein)
        index_list: list[int] = []
        index_list = list(range(len(id_list)))

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
    
        if no_progress_counter >= no_progress_limit:
            return best_solution
        if len(index_list) == 0:
            return best_solution
    return best_solution

def setup_simulated_annealing(protein_file_name, loop_amount, start_temperature, temp_decreasing_interval, no_progress_limit) -> 'Protein':
    protein = Protein(f"proteins/{protein_file_name}")
    randomise.random_assignment_protein(protein)
    counter = 0
    best_protein = copy.deepcopy(protein)
    while counter < loop_amount:
        current_solution, current_solution_score = simulated_annealing(protein, start_temperature, temp_decreasing_interval, no_progress_limit)
        if current_solution_score < best_protein.count_score():
            best_protein = copy.deepcopy(current_solution)
        counter += 1
        print(f"protein {counter}, score {current_solution_score}")
        if counter != loop_amount:
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
    return best_protein
