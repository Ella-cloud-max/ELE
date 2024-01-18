# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:21:32 2024

@author: Eric van Huizen
"""

from import_csv import import_structure
from code.classes.amino import Amino
from code.classes.protein import Protein
import sys


def create_options(protein):
    directions_list = []
    score_list = []
    id_list = []
    direction_options = [-1, 1, -2, 2]
    current_structure = protein
    aminos_id = protein.i_list

    for i in range(1, len(aminos_id) - 1):
        # code voor het maken van de opties
        continue

    return (id_list, directions_list, score_list)

def mutate_structure(amino_id, protein, direction):
    None

def acceptatiekans(protein):
    Zc = protein.count_score
    T = 0.2 * Zc
    iterate_counter = 0
    best_solution = (protein, Zc)
    if iterate_counter%5 == 0 and iterate_counter != 0:
        T = T * 0.5



if __name__ == "__main__":

    # protein = Protein(f"output/{sys.argv[1]}")
    protein = Protein("output/output_E.csv")
    last_amino_id = protein.i_list[-1]
    last_amino = protein.aminos[last_amino_id]
