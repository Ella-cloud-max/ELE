import random

# must have amino as input for continuity to other algorithm
def random_assignment(protein):
    for amino in protein.aminos.values():
        directions = [-1, 1, -2, 2]
        if amino.i == protein.i_list[-1]:
            amino.direction = 0
            amino.change_coordinates()
            return
        elif amino.i != 0:
            directions.remove(amino.previous_amino.direction * -1)
        amino.change_direction(random.choice(directions))
        amino.change_coordinates()

def random_reconfigure_amino(protein, change_amino):
    change_amino.change_direction(random.choice([-2, -1, 1, 2]))
    change_amino.change_coordinates()
    for amino in protein.aminos.values():
        if amino.i > change_amino.i:
            change_amino.change_coordinates()
