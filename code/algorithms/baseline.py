import random

def baseline_random_algorithm(protein):
    """
    Changes the direction of each amino of the inputted protein randomly to any
    of {-2, -1, 1, 2} and changes the coordinates (according to the direction
    of the previous amino).
    
    pre: a protein class objects
    post: the directions and coordinates of the amino class objects within the
    protein have been changed.
    """

    for amino in protein.aminos.values():

        # the last amino in the protein gets direction 0
        if amino.i == protein.i_list[-1]:
            amino.change_direction(0)
            amino.change_coordinates()

        else:
            amino.change_direction(random.choice([-2, -1, 1, 2]))
            amino.change_coordinates()