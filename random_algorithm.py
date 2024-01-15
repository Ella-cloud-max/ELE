import random

# must have amino as input for continuity to other algorithm
def randomise(amino):
    direction = random.randint(-2, 2)
    while direction == 0:
        direction = random.randint(-2, 2)
    return direction
    