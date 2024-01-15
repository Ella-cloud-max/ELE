# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:21:32 2024

@author: Eric van Huizen
"""

from amino import Amino
from score import count_score
from random_algorithm import randomise
from main import get_protein
import sys

def make_structure(protein_list, algorithm, output_file):
    

if __name__ == "__main__":
    protein_list = get_protein(f"proteins/{sys.argv[1]}")

    output_file = open(f"output/{sys.argv[2]}", "w")
    output_file.write("amino,fold\n")

    final_amino = make_structure(protein_list, randomise, output_file)

    output_file.write(f"score,{count_score(final_amino)}")
    output_file.close()