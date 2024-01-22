# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:21:32 2024

@author: Eric van Huizen
"""

from import_csv import import_structure
from code.classes import protein, amino
import sys

def score(structure):
    return -6

def create_options(amino_sctructure):
    directions_list = []
    score_list = []
    direction_options = [[-1, 1, -2, 2]]
    
    return (directions_list, score_list)

def acceptatiekans(amino_structure):
    Zc = score(amino_structure)
    T = 0.2 * Zc
    iterate_counter = 0
    best_solution = (amino_structure, Zc)
    if iterate_counter%5 == 0 and iterate_counter != 0:
        T = T * 0.5
    


if __name__ == "__main__":
    
    # amino_acids: dict = import_structure(f"output/{sys.argv[1]}")
    amino_acids: dict = import_structure(f"output/output_L.csv")
    last_amino_id = len(amino_acids.items()) - 1
    last_amino = amino_acids[last_amino_id]