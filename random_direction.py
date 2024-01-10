# heeft problemen met opgesloten aminos

import random
import sys

# "1" betekent een positieve stap in de eerste dimensie (X-as richting).
# "-1" betekent een negatieve stap in de eerste dimensie (X-as richting).
# "2" betekent een positieve stap in de tweede dimensie (Y-as richting).
# "-2" betekent een negatieve stap in de tweede dimensie (Y-as richting).

class Amino():
    def __init__(self, type, previous):
        self.type = type                      # H or P
        self.coordinates = [0, 0]
        self.direction = 0                    # -2, -1, 1 or 2 (see explanation above)
        self.previous_amino = previous      # variable holds class of previous amino

    def __repr__(self):
        return f"{self.type}, {self.coordinates}, {self.direction}, {self.previous_amino}"

    # changes coordinates of amino based on direction which is chosen at random
    def move_amino(self):

        # direction of {-2, -1, 1, 2} is chosen at random
        self.direction = random.randint(-2, 2)
        while self.direction == 0:
            self.direction = random.randint(-2, 2)

        # this is for very first amino, as None-object does not have coordinates.
        if self.previous_amino == None:
            if abs(self.direction) == 1:
                self.coordinates = [self.direction, 0]
            elif abs(self.direction) == 2:
                self.coordinates = [0, (self.direction / 2)]

        # for any amino other than first, coordinates are coordinates of previous amino plus movement in direction
        else:
            if abs(self.direction) == 1:
                self.coordinates = [self.previous_amino.coordinates[0] + self.direction, self.previous_amino.coordinates[1]]
            elif abs(self.direction) == 2:
                self.coordinates = [self.previous_amino.coordinates[0], self.previous_amino.coordinates[1] + (self.direction / 2)]

        self.check_coordinates()

        return self

    # checks whether coordinates of amino are not same as any previous amino's
    def check_coordinates(self):
        check_previous = self.previous_amino
        while check_previous != None:

            # if a previous amino is placed on coordinates, restart function move_amino (and change direction to change coordinates)
            if check_previous.coordinates == self.coordinates:
                self.move_amino()

            else:
                check_previous = check_previous.previous_amino
        
# returns list of input file containing protein (each amino is an item in list)
def get_protein(file):
    return [*str(*open(file))]

# goes through list of protein and moves each amino based on previous amino
def make_structure(protein_list, output_file):
    previous_amino = None
    for i in range(len(protein_list)):
        current_amino = Amino(protein_list[i], previous_amino)
        
        if i == len(protein_list) - 1:
            output_file.write(f"{current_amino.type}, {current_amino.direction}\n")
            return current_amino
        
        previous_amino = current_amino.move_amino()
        output_file.write(f"{previous_amino.type}, {previous_amino.direction}\n")

def count_score(amino):
    score = 0
    while amino != None:
        print(amino)
        if amino.type == "H":
            check_previous = amino.previous_amino
            while check_previous != None:
                print(check_previous)
                if ((check_previous.coordinates[0] - amino.coordinates[0]) + (check_previous.coordinates[1] - amino.coordinates[1])) == 1 and check_previous != amino.previous_amino:
                    score -= 1
                check_previous = check_previous.previous_amino
        amino = amino.previous_amino
    return score

if __name__ == "__main__":

    protein_list = get_protein(f"proteins/{sys.argv[1]}")

    output_file = open(f"output/{sys.argv[2]}", "w")
    output_file.write("amino,fold\n")

    final_amino = make_structure(protein_list, output_file)

    print(count_score(final_amino))

    output_file.close()
