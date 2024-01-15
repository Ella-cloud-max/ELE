# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:21:32 2024

@author: Eric van Huizen
"""

from amino import Amino
from score import count_score
from random_algorithm import randomise
from main import get_protein
from import_csv import import_structure 
import sys    


if __name__ == "__main__":
    
    amino_acids: dict = import_structure(f"output/{sys.argv[1]}")
    last_amino_id = amino_acids.items()
    print(last_amino_id)
    score = count_score(last_amino_id)
    print(score)