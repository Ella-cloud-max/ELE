import random

def baseline_random_amino(protein, amino):
    """The baseline random algorithm"""
    if amino.i == protein.i_list[-1]:
        amino.direction = 0
    else:
        amino.change_direction(random.choice([-2, -1, 1, 2]))
    amino.change_coordinates()

def baseline_random_protein(protein):
    """This function applies the baseline random algorithm
    to the whole protein."""
    for amino in protein.aminos.values():
        baseline_random_amino(protein, amino)