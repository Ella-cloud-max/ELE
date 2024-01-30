import sys
from code.classes.protein import Protein
import random

def get_possibilities2(amino) -> list[int]:
    """ Get a list of the possible directions an amino can go to. """
    available_options = set([-2, -1, 1, 2])
    if amino.previous_amino == None:
        options = list(available_options)
        return options
    previous = amino.previous_amino
    previous_coordinates = amino.previous_amino.coordinates
    unsave_coordinates = []
    while previous != None:
        unsave_coordinates.append(previous.coordinates)
        previous = previous.previous_amino

    unavailable_options = set()
    for i in available_options:
        if abs(i) == 1 and (previous_coordinates[0] + i, previous_coordinates[1]) in unsave_coordinates:
            unavailable_options.add(i)
        elif abs(i) == 2 and (amino.previous_amino.coordinates[0], amino.previous_amino.coordinates[1] + (i/2)) in unsave_coordinates:
            unavailable_options.add(i)
    options = list(available_options - unavailable_options)
    return options

def greedy(protein):
    amino = protein.aminos[protein.i_list[0]]
    amino.direction = random.choice([-2, -1, 1, 2])
    while True:
        amino = protein.get_empty_amino()
        if amino == None:
            protein.print_output("output_greedy.csv")
            return
        if amino.soort == "P":
            possibilities = get_possibilities2(amino)
            if len(possibilities) == 0:
                while len(get_possibilities2(amino)) <= 2 or amino.soort == "H":
                    amino.reset_position()
                    amino = amino.previous_amino
                amino.reset_position()
                amino.previous_amino.reset_position()
                continue
            amino.previous_amino.direction = random.choice(possibilities)
            amino.change_coordinates()
            continue

        good_possibilities = []
        possibilities = get_possibilities2(amino)
        if len(possibilities) == 0:
            while len(get_possibilities2(amino)) <= 2 or amino.soort == "H":
                amino.reset_position()
                amino = amino.previous_amino
            amino.reset_position()
            amino.previous_amino.reset_position()
            continue
        minimum_score = 0
        for item in possibilities:
            amino.previous_amino.change_direction(item)
            amino.change_coordinates()
            if protein.count_score_amino(amino) < minimum_score:
                minimum_score = protein.count_score_amino(amino)
        for item in possibilities:
            amino.previous_amino.change_direction(item)
            amino.change_coordinates()
            if protein.count_score_amino(amino) == minimum_score:
                good_possibilities.append(item)
        amino.previous_amino.change_direction(random.choice(good_possibilities))
        amino.change_coordinates()
