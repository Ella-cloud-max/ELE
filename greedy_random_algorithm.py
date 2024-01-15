from random_algorithm import randomise
from score import count_score
import random

def greedy_and_random_direction(amino):
    if amino.type == "P":
        return randomise()

    options = {-2: 0,
               -1: 0,
               1: 0,
               2: 0}

    for item in options:
        if abs(item) == 1:
            amino.coordinates = [amino.previous_amino.coordinates[0] + item, amino.previous_amino.coordinates[1]]
        elif abs(item) == 2:
            amino.coordinates = [amino.previous_amino.coordinates[0], amino.previous_amino.coordinates[1] + (item / 2)]

        options[item] = count_score(amino)
        print(item, options[item])

    best_score = 0

    for item in options:
        if options[item] < best_score and amino.check_coordinates():
            best_score = options[item]

    best_options = []
    print(best_score)
    for item in options:
        print(options[item])
        if options[item] == best_score:
            best_options.append(item)
    print(best_options)
    return random.choice(best_options)
