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


def create_options(protein):
    aminos = protein.aminos
    directions_list: list = []
    score_list: list = []
    id_list: list = []
    aminos_id = protein.i_list
    for i in range(1, len(aminos_id) - 1):
        direction_options: list[int] = [-1, 1, -2, 2]
        if i != aminos_id[-1]:
            direction_options.remove(aminos[i].direction)
        direction_options.remove(aminos[i].previous_amino.direction * -1)
        # print(f"id is {i}, options are {direction_options}")
        for option in direction_options:
            protein_copy = copy.deepcopy(protein)
            aminos_copy = protein_copy.aminos
            old_direction = aminos_copy[i].direction
            aminos_copy[i].direction = option


            # print(f"id is {i}")
            # print(f"aminos i direction is {aminos_copy[i].direction}")
            # print(f"aminos i + 1 direction is {aminos_copy[i + 1].direction}")
            protein_copy.rotate(i, old_direction)
            protein_copy.change_coordinates(i)
            if len(protein_copy.get_coordinates()) == protein_copy.size:
                score_list.append(protein_copy.count_score())
                id_list.append(i)
                directions_list.append(option)

    # print(f"list of id {id_list}")
    # print(f"list of directions {directions_list}")
    # print(f"list of scores {score_list}")
    return (id_list, directions_list, score_list)


def mutate_structure(amino_id, protein, direction):
    None

def loop(protein) -> tuple[Any]:
    Zc = protein.count_score()
    T = 20
    iterate_counter = 0
    current_protein = copy.deepcopy(protein)
    best_solution = (copy.deepcopy(current_protein), Zc)
    no_progress_counter = 0
    while iterate_counter < 1000:
        print(f"iteration is {iterate_counter}")
        # print(f"direction last amino {current_protein.aminos[current_protein.size - 1].direction}")
        # print(current_protein.get_coordinates())
        if iterate_counter%200 == 0 and iterate_counter != 0:
            T = T * 0.5
        id_list, directions_list, score_list = create_options(current_protein)
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
                print(f"Id is {amino_id}, old direction is {current_protein.aminos[amino_id].direction}, new direction is {new_direction}")
                Zc = Zn
                amino_change = current_protein.aminos[amino_id]
                old_direction = amino_change.direction
                amino_change.direction = new_direction
                current_protein.rotate(amino_id, old_direction)
                current_protein.change_coordinates(amino_id)
                
                if Zc <= best_solution[1]:
                    best_solution = (copy.deepcopy(current_protein), Zc)
                break
            elif random.random() > pow(e, x):
            # elif random.random() > pow(2, x):
                print(f"Id is {amino_id}, old direction is {current_protein.aminos[amino_id].direction}, new direction is {new_direction}")
                Zc = Zn
                amino_change = current_protein.aminos[amino_id]
                old_direction = amino_change.direction
                amino_change.direction = new_direction
                current_protein.rotate(amino_id, old_direction)
                current_protein.change_coordinates(amino_id)
                if Zc < best_solution[1]:
                    best_solution = (copy.deepcopy(current_protein), Zc)
                break
            else:
                index_list.remove(choice)
        # if Zc >= best_solution[1]:
        #     no_progress_counter += 1
        # else:
        #     no_progress_counter = 0
        # if no_progress_counter > 100:
        #     return best_solution
        if len(index_list) == 0:
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
        current_solution = loop(protein)
        if current_solution[1] < best_protein.count_score():
            best_protein = copy.deepcopy(current_solution[0])
        counter += 1
        print(f"protein {counter}, score {current_solution[0].count_score()}")
        if counter != 10:
            randomise.random_assignment(protein)
            while protein.check_viability() == False:
                randomise.random_assignment(protein)
    id_list, directions_list, score_list = create_options(best_protein)
    score = min(score_list)
    index = score_list.index(score)
    amino_id = id_list[index]
    new_direction = directions_list[index]
    amino_change = best_protein.aminos[amino_id]
    old_direction = amino_change.direction
    amino_change.direction = new_direction
    best_protein.rotate(amino_id, old_direction)
    best_protein.change_coordinates(amino_id)
    
    best_protein.print_output("output_Eric.csv")
    print(best_protein.count_score())
    print_folded_protein("output/output_Eric.csv")
    
