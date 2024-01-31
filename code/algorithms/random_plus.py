import random
from code.classes.amino import Amino
from code.classes.protein import Protein

def random_assignment_amino(amino: Amino) -> None:
    """
    Assigns inputted amino with a random direction that cannot be the opposite
    direction of the pervious amino. Slight improvement on baseline.

    post: the amino object's direction and coordinates have changed
    """
    directions: list[int] = [-1, 1, -2, 2]
    if amino.i != 0:
        directions.remove(amino.previous_amino.direction * -1)
    amino.change_direction(random.choice(directions))
    amino.change_coordinates()

def random_assignment_protein(protein: Protein) -> None:
    """
    Applies function random_assignment_amino to every amino in a protein class
    object.

    post: the directions and coordinates of the amino class objects within the
    protein have been changed, and the protein is certainly valid (no
    overlapping aminos)
    """
    while protein.check_validity() == False:
        for amino in protein.aminos.values():
            if amino.i == protein.i_list[-1]:
                amino.direction: int = 0
                amino.change_coordinates()
            else:
                random_assignment_amino(amino)
