import sys
from code.classes.protein import Protein
import random

def greedy(protein):
    amino = protein.aminos[protein.i_list[0]]
    amino.direction = random.choice([-2, -1, 1, 2])

    while True:
        amino = protein.get_empty_amino()
        if amino == None:
            protein.print_output("output_greedy.csv")
            return

        if amino.soort == "P":
            possibilities = amino.get_possibilities()
            if len(possibilities) == 0:
                while len(amino.get_possibilities()) <= 2 or amino.soort == "H":
                    amino.reset_position()
                    amino = amino.previous_amino
                amino.reset_position()
                amino.previous_amino.reset_position()
                continue
            amino.previous_amino.change_direction(random.choice(possibilities))
            amino.change_coordinates()
            continue

        good_possibilities = []
        possibilities = amino.get_possibilities()
        if len(possibilities) == 0:
            while len(amino.get_possibilities()) <= 2 or amino.soort == "H":
                amino.reset_position()
                amino = amino.previous_amino
            amino.reset_position()
            amino.previous_amino.reset_position()
            continue

        minimum_score = 0
        for item in possibilities:
            amino.previous_amino.change_direction(item)
            amino.change_coordinates()
            if protein.count_score(amino) < minimum_score:
                minimum_score = protein.count_score(amino)

        for item in possibilities:
            amino.previous_amino.change_direction(item)
            amino.change_coordinates()
            if protein.count_score(amino) == minimum_score:
                good_possibilities.append(item)

        amino.previous_amino.change_direction(random.choice(good_possibilities))
        amino.change_coordinates()
