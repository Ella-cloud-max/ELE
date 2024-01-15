from amino import Amino


def count_score(amino: 'Amino') -> int:
    """
    Input is the last amino-acid from the chain
    
    pre: amino class object
    post: returns the score as an integer
    """
    score = 0
    while amino != None:
        if amino.soort == "H":
            check_previous = amino.previous_amino
            while check_previous != None:
                if (abs(check_previous.coordinates[0] - amino.coordinates[0]) + abs(check_previous.coordinates[1] - amino.coordinates[1])) == 1 and check_previous.soort == "H" and abs(check_previous.i - amino.i) != 1:
                    score -= 1
                check_previous = check_previous.previous_amino
        amino = amino.previous_amino
    return score