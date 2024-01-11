import random

# "1" betekent een positieve stap in de eerste dimensie (X-as richting).
# "-1" betekent een negatieve stap in de eerste dimensie (X-as richting).
# "2" betekent een positieve stap in de tweede dimensie (Y-as richting).
# "-2" betekent een negatieve stap in de tweede dimensie (Y-as richting).

class Amino():
    def __init__(self, i, type, previous):
        self.i = i
        self.type = type                      # H or P
        self.coordinates = [0, 0]
        self.direction = 0                    # -2, -1, 1 or 2 (see explanation above)
        self.previous_amino = previous      # variable holds class of previous amino

    def __repr__(self):
        return f"{self.i}, {self.type}, {self.coordinates}, {self.direction}"

    # changes coordinates of amino based on direction which is chosen at random
    def move_amino(self):

        self.previous_amino.direction = random.randint(-2, 2)
        while self.previous_amino.direction == 0:
            self.previous_amino.direction = random.randint(-2, 2)

        # for any amino other than first, coordinates are coordinates of previous amino plus movement in direction
        if abs(self.previous_amino.direction) == 1:
            self.coordinates = [self.previous_amino.coordinates[0] + self.previous_amino.direction, self.previous_amino.coordinates[1]]
        elif abs(self.previous_amino.direction) == 2:
            self.coordinates = [self.previous_amino.coordinates[0], self.previous_amino.coordinates[1] + (self.previous_amino.direction / 2)]

        self.check_coordinates()

    # checks whether coordinates of amino are not same as any previous amino's
    def check_coordinates(self):
        check_previous = self.previous_amino
        while check_previous != None:

            # if a previous amino is placed on coordinates, restart function move_amino (and change direction to change coordinates)
            if check_previous.coordinates == self.coordinates:
                self.move_amino()

            else:
                check_previous = check_previous.previous_amino