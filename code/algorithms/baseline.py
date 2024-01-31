# Author: Liesbet Ooghe
# 
# Baseline algorithm. Amino acids are created one by one and given a random
# direction. Once the whole protein is done, t

import random

def baseline_random_algorithm(protein):
    """
    Changes the direction of each amino of the inputted protien randomly to any of
    {-2, -1, 1, 2} and changes the coordinates.
    
    in: an protein class objects
    out: the amino class objects direction and coordinates have been changed

    """
    for amino in protein.aminos.values():

        # the last amino in the protein gets direction 0
        if amino.i == protein.i_list[-1]:
            amino.change_direction(0)
            amino.change_coordinates()

        else:
            amino.change_direction(random.choice([-2, -1, 1, 2]))
            amino.change_coordinates()