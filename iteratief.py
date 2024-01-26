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


def create_pull_options(protein):
    aminos = protein.aminos
    directions_list: list = []
    score_list: list = []
    id_list: list = []
    mutation_list: list[str] = []
    aminos_id = protein.i_list

    for i in range(len(aminos_id) - 1):
        protein_copy = copy.deepcopy(protein)
        aminos_copy = protein_copy.aminos
        direction_options: list[int] = [-1, 1, -2, 2]
        if i == 0:
            direction_options.remove(aminos_copy[i].direction)
            direction_options.remove(aminos_copy[i].next_amino.direction * -1)
        elif i == aminos_id[-2]:
            direction_options.remove(aminos_copy[i].direction)
            direction_options.remove(aminos_copy[i].previous_amino.direction * -1)
        else:
            direction_options = [aminos_copy[i].next_amino.direction]
            if aminos_copy[i].direction == direction_options[0]:
                direction_options.remove(aminos_copy[i].direction)
        # print(f"id is {i}, options are {direction_options}")
        for option in direction_options:
            # print(aminos_copy[i].direction)

            if i != 0 and i != aminos_id[-2]:
                aminos_copy[i + 1].direction = aminos_copy[i].direction
            aminos_copy[i].direction = option

            protein_copy.change_coordinates(i)
            if len(protein_copy.get_coordinates()) == protein_copy.size:
                score_list.append(protein_copy.count_score())
                id_list.append(i)
                directions_list.append(option)
                mutation_list.append("pull")

    return (id_list, directions_list, score_list)

def mutate_direction_pull(amino_id, current_protein, new_direction):
    amino_change = current_protein.aminos[amino_id]
    if amino_id != 0 and amino_id != protein.size - 2:
        amino_change.next_amino.direction = amino_change.direction
    amino_change.direction = new_direction
    current_protein.change_coordinates(amino_id)


def loop(protein) -> tuple[Any]:
    Zc = protein.count_score()
    T = 20
    iterate_counter = 0
    current_protein = copy.deepcopy(protein)
    best_solution = (copy.deepcopy(current_protein), Zc)
    no_progress_counter = 0
    while iterate_counter < 1000:
        # print(f"iteration is {iterate_counter}")
        if iterate_counter%200 == 0 and iterate_counter != 0:
            T = T * 0.5
        id_list, directions_list, score_list, mutation_list = create_pull_options(current_protein)
        index_list: list[int] = []
        [index_list.append(x) for x in range(len(score_list))]

        while len(index_list) != 0:
            choice = random.choice(index_list)
            amino_id = id_list[choice]
            Zn = score_list[choice]
            new_direction = directions_list[choice]
            x = (Zc-Zn)/T
            # x = Zc - Zn
            if Zn <= Zc:
                Zc = Zn
                mutate_direction_pull(amino_id, current_protein, new_direction)
                if Zc < best_solution[1]:
                    best_solution = (copy.deepcopy(current_protein), Zc)
                break
            elif random.random() > pow(e, x):
                Zc = Zn
                mutate_direction_pull(amino_id, current_protein, new_direction)
                if Zc < best_solution[1]:
                    best_solution = (copy.deepcopy(current_protein), Zc)
                break
            else:
                index_list.remove(choice)

        if Zn >= best_solution[1]:
            no_progress_counter += 1
        elif Zn < best_solution[1]:
            no_progress_counter = 0
        if no_progress_counter >= 200:
            return best_solution

        iterate_counter += 1
    return best_solution



if __name__ == "__main__":
    counter = 0
    # to create random protein
    protein = Protein(f"proteins/{sys.argv[1]}")
    randomise.random_assignment(protein)
    while protein.check_viability() == False:
        randomise.random_assignment(protein)
    best_protein = copy.deepcopy(protein)
    while counter < 10:
        current_solution = copy.deepcopy(loop(protein)[0])
        if current_solution.count_score() < best_protein.count_score():
            best_protein = copy.deepcopy(current_solution)
        counter += 1
        print(f"protein {counter}, score {current_solution.count_score()}")
        print(f"best protein {counter}, score {best_protein.count_score()}")
        randomise.random_assignment(protein)
        while protein.check_viability() == False:
            randomise.random_assignment(protein)
        
    best_protein.print_output("output_Eric.csv")
    print(best_protein.count_score())
    print_folded_protein("output/output_Eric.csv")
    
