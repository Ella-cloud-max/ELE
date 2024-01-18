# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:21:32 2024

@author: Eric van Huizen
"""

from import_csv import import_structure
from code.classes.amino import Amino
from code.classes.protein import Protein
from math import e as e
import sys
import random
import copy


def create_options(protein):
    aminos = protein.aminos
    coordinates_list: list = []
    score_list: list = []
    id_list: list = []
    aminos_id = protein.i_list

    for i in range(1, len(aminos_id) - 1):
        protein_copy = copy.deepcopy(protein)
        aminos_copy = protein_copy.aminos
        center = aminos_copy[i].coordinates
        options_set = set()
        options_set.add((center[0] - 1, center[1]))
        options_set.add((center[0] + 1, center[1]))
        options_set.add((center[0], center[1] - 1))
        options_set.add((center[0], center[1] + 1))
        options_list = list(options_set - protein.coordinates_set)
        for option in options_list:
            coordinates_list.append(option)
            aminos_copy[i].coordinates = option
            score_list.append(protein_copy.count_score())
            id_list.append(i)

    return (id_list, coordinates_list, score_list)


def mutate_structure(amino_id, protein, direction):
    None

def loop(protein):
    Zc = protein.count_score()
    T = 0.2 * 30
    iterate_counter = 0
    current_protein = copy.deepcopy(protein)
    best_solution = (current_protein, Zc)
    while iterate_counter < 1:
        if iterate_counter%5 == 0 and iterate_counter != 0:
            T = T * 0.5
        id_list, coordinate_list, score_list = create_options(protein)
    
        index_list: list[int] = []
        [index_list.append(x) for x in range(len(score_list))]
        
        while len(index_list) != 0:
            choice = random.choice(index_list)
            amino_id = id_list[choice]
            Zn = score_list[choice]
            new_coordinate = coordinate_list[choice]
            x = (Zc-Zn)/T
            if Zn <= Zc:
                Zc = Zn
                amino_change = current_protein.aminos[amino_id]
                current_protein.coordinates_set.pop(amino_change.coordinates)
                current_protein.coordinates_set.
                amino_change.coordinates = new_coordinate
                if Zc < best_solution[1]:
                    best_solution = (copy.deepcopy(current_protein), Zc)
                break
            elif random.random() < pow(e, x):
                Zc = Zn
                amino_change = current_protein.aminos[amino_id]
                amino_change.coordinates = new_coordinate
                if Zc < best_solution[1]:
                    best_solution = (copy.deepcopy(current_protein), Zc)
                break
            else:
                index_list.remove(choice)
        if len(index_list) == 0:
            return best_solution
        iterate_counter += 1
    return best_solution



if __name__ == "__main__":

    # protein = Protein(f"output/{sys.argv[1]}")
    protein = Protein("output/output_E.csv")
    last_amino_id = protein.i_list[-1]
    last_amino = protein.aminos[last_amino_id]
    # print(protein.count_score())
    protein_copy = copy.deepcopy(protein)
    test = protein_copy.aminos[7]
    test.coordinates = [0, 5]
    test.previous_amino.direction = 2
    # print(protein.count_score())
    # print(protein_copy.count_score())
    print(loop(protein)[1])

