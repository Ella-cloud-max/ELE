import random

# must have amino as input for continuity to other algorithm
def randomise(protein):
    for amino in protein.aminos.values():
        if amino.i == protein.i_list[-1]:
            amino.direction = 0
            return
        amino.direction = random.choice([-2, -1, 1, 2])
        amino.change_coordinates()