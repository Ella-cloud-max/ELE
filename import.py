# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:21:52 2024

@author: Eric van Huizen
"""

from amino import Amino
from score import count_score
from random_algorithm import randomise
import sys
import csv

def import_structure(file):
    reader = csv.reader(file)
    next(reader)    # skip header
    soort, direction = next(reader) # first line
    amino_id = 0
    previous_amino = Amino(amino_id, soort, direction, [0, 0], None)
    while line != :
        soort, direction = next(reader)
        amino_id += 1
        if direction == 0:
            coordinates = previous_amino.coordinates
            coordinates = [coordinates[0] + 1, coordinates[1] + 1]
        elif abs(direction) == 1:
            coordinates = previous_amino.coordinates
            coordinates[0] = coordinates[0] + direction
        else:
            coordinates
        current_amino = Amino(amino_id, soort, direction, coordinates,
                              previous_amino)


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     exit()
    # input_file = open(f"output/{sys.argv[1]}", "r")
    input_file = open("output/output_l.csv", "r")
    import_structure(input_file)
    input_file.close()