# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:21:52 2024

@author: Eric van Huizen
"""
import sys
import csv
from code.classes.amino import Amino
from code.classes.protein import Protein


def import_structure(file_directory: str) -> dict:
    """
    Imports the amino acids from a file that contains a known solution

    pre: string which is the directory to the file
    post: outputs a dictionary containing the amino-acids
    """

    file = open(file_directory, "r")
    aminos: dict = {}
    reader = csv.reader(file)
    next(reader)    # skip header
    soort, direction = next(reader) # first line
    direction = int(direction)
    amino_id = 0
    coordinates = [0, 0]
    aminos[amino_id] = Amino(amino_id, soort, direction, coordinates, None)
    for soort, direction in reader:
        if soort == "score":
            break
        direction = int(direction)
        amino_id += 1
        previous_direction = aminos[amino_id - 1].direction
        if previous_direction == 0:
            coordinates = [coordinates[0] + 1, coordinates[1] + 1]
        elif abs(previous_direction) == 1:
            coordinates = [coordinates[0] + previous_direction, coordinates[1]]
        else:
            if previous_direction > 0:
                coordinates = [coordinates[0], coordinates[1] + 1]
            else:
                coordinates = [coordinates[0], coordinates[1] - 1]

        aminos[amino_id] = Amino(amino_id, soort, direction, coordinates,
                              aminos[amino_id - 1])
    file.close()
    return aminos