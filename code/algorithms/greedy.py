import random

def reset_aminos(amino):
    """
    Resets the inputted amino and previous aminos until an amino has more than
    two possible directions to go to and is not an H-type amino. This function
    is called upon when the inputted amino is surrounded, and allows the
    protein to go in a different direction to prevent this.

    pre: an amino class object that is surrounded by others
    post: the amino class object and a number of previous aminos have been reset
    """

    while len(amino.get_possibilities()) <= 2 or amino.soort == "H":
        amino.reset_position()
        amino = amino.previous_amino
    amino.reset_position()
    amino.previous_amino.reset_position()
    # amino.previous_amino.reset_position()

def get_best_possibilities(amino, protein):
    """
    Returns a sublist of the list of all possible directions the inputted
    amino can have containing only the directions that decrease the score the
    most.

    pre: the list of possible directions the amino can have, a sublist of
    [-2, -1, 1, 2]
    post: the list of best directions the amino can have, a sublist of the in-list
    """

    best_possibilities = []
    minimum_score = 0
    
    for possibility in amino.get_possibilities():
        amino.previous_amino.change_direction(possibility)
        amino.change_coordinates()
        if protein.count_score(amino) == minimum_score:
            best_possibilities.append(possibility)
        elif protein.count_score(amino) < minimum_score:
            best_possibilities = [possibility]
            minimum_score = protein.count_score(amino)
    
    return best_possibilities

def greedy_random_algorithm(protein):
    """
    A greedy-random algorithm has the following heuristic: every amino is
    placed so that the score decreases as much as possible. If there are
    multiple options for which this true, one is chosen at random.
    """

    # the first amino is given a random direction
    protein.aminos[protein.i_list[0]].change_direction(random.choice([-2, -1, 1, 2]))

    while protein.get_empty_amino() != None:
        amino = protein.get_empty_amino()
        possibilities = amino.get_possibilities()
        if len(possibilities) == 0:
            reset_aminos(amino)
        else:
            if amino.soort == "H":
                possibilities = get_best_possibilities(amino, protein)

            amino.previous_amino.change_direction(random.choice(possibilities))
            amino.change_coordinates()
