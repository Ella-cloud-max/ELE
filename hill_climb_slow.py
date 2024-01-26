# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:55:16 2024

@author: Eric van Huizen
"""

from iteratief2 import create_rotate_options, create_pull_options, mutate_direction_pull, mutate_direction_rotate
import random
from code.classes.amino import Amino
from code.classes.protein import Protein
from code.algorithms import randomise
from code.visualisation.visualisation import *
from typing import Any
import copy
import time

def loop(protein) -> tuple[Any]:
    current_protein = (copy.deepcopy(protein), protein.count_score())
    while True:
        id_list, directions_list, score_list, mutation_list = create_rotate_options(current_protein[0])
        pull_options = create_pull_options(current_protein[0])
        id_list += pull_options[0]
        directions_list += pull_options[1]
        score_list += pull_options[2]
        mutation_list += pull_options[3]
        index_list: list[int] = []
        [index_list.append(x) for x in range(len(score_list))]

        while len(index_list) != 0:
            choice = random.choice(index_list)
            amino_id = id_list[choice]
            new_score = score_list[choice]
            new_direction = directions_list[choice]
            mutation_option = mutation_list[choice]
            if new_score < current_protein[1]:
                if mutation_option == "rotate":
                    mutate_direction_rotate(amino_id, current_protein[0], new_direction)
                else:
                    mutate_direction_pull(amino_id, current_protein[0], new_direction)
                current_protein = (current_protein[0], current_protein[0].count_score())
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
    while protein.check_viability() == False:
        randomise.random_assignment_protein(protein)
    best_protein = copy.deepcopy(protein)
    while counter < loop_amount:
        current_solution = loop(protein)
        # current_solution[0].print_output("output_Eric.csv")
        # print_folded_protein("output/output_Eric.csv")
        if current_solution[1] < best_protein.count_score():
            best_protein = copy.deepcopy(current_solution[0])
        counter += 1
        print(f"protein {counter}, score {current_solution[0].count_score()}")
        if counter != loop_amount:
            randomise.random_assignment_protein(protein)
            while protein.check_viability() == False:
                randomise.random_assignment_protein(protein)

    best_protein.print_output("output_Eric.csv")
    print("This is the best protein found")
    print_folded_protein("output/output_Eric.csv")
    end_time = time.time()
    print(f"Time duration is {end_time - start_time}")