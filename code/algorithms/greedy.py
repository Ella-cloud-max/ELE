import random
from code.classes.amino import Amino
from code.classes.protein import Protein

def reset_aminos(amino: Amino) -> None:
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

def get_best_possibilities(amino: Amino, protein: Protein) -> list[int]:
    """
    Returns a sublist of the list of all possible directions the inputted
    amino can have containing only the directions that decrease the score the
    most.

    pre: the list of possible directions the amino can have, a sublist of
    [-2, -1, 1, 2]
    post: the list of best directions the amino can have, a sublist of the in-list
    """

    best_possibilities: list[int] = []
    minimum_score: int = 0
    
    for possibility in amino.get_possibilities():
        amino.previous_amino.change_direction(possibility)
        amino.change_coordinates()
        if protein.count_score(amino) == minimum_score:
            best_possibilities.append(possibility)
        elif protein.count_score(amino) < minimum_score:
            best_possibilities: list[int] = [possibility]
            minimum_score: int = protein.count_score(amino)
    
    return best_possibilities

def greedy_random_algorithm(protein: Protein) -> None:
    """
    A greedy-random algorithm has the following heuristic: every amino is
    placed so that the score decreases as much as possible. If there are
    multiple options for which this true, one is chosen at random.

    post: the directions and coordinates of the amino class objects within the
    protein have been changed, and the protein is certainly valid (no
    overlapping aminos)
    """

    # first amino is given random direction
    protein.aminos[protein.i_list[0]].change_direction(random.choice([-2, -1, 1, 2]))

    while protein.get_empty_amino() != None:
        amino: Amino = protein.get_empty_amino()
        possibilities: list[int] = amino.get_possibilities()

        # if there are no possible directions, amino is surrounded
        if len(possibilities) == 0:
            reset_aminos(amino)
        
        else:

            # for P-type amino, score cannot change so there are no best
            # possibilities
            if amino.soort == "H":
                possibilities: list[int] = get_best_possibilities(amino, protein)

            amino.previous_amino.change_direction(random.choice(possibilities))
            amino.change_coordinates()
