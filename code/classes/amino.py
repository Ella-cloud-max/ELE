from typing import Any

# "1" betekent een positieve stap in de eerste dimensie (X-as richting).
# "-1" betekent een negatieve stap in de eerste dimensie (X-as richting).
# "2" betekent een positieve stap in de tweede dimensie (Y-as richting).
# "-2" betekent een negatieve stap in de tweede dimensie (Y-as richting).

class Amino():
    def __init__(self, i: int, soort: str, direction: int, coordinates: list[int], previous: Any) -> None:
        self.i: int = i
        self.soort: str = soort                      # H or P
        self.direction: int = direction                    # -2, -1, 1 or 2 (see explanation above)
        self.coordinates: list[int] = coordinates    # [n, m]
        self.previous_amino = previous               # variable holds class of previous amino
    
    def __repr__(self) -> str:
        return f"{self.i}, {self.soort}, {self.direction}, {self.coordinates}"

    def change_direction(self, direction):
        self.direction = direction

    def change_coordinates(self) -> None:
        """ Change coordinates of amino based on the direction of the previous amino """
        if self.previous_amino == None:
            return

        if abs(self.previous_amino.direction) == 1:
            self.coordinates = [self.previous_amino.coordinates[0] + self.previous_amino.direction, self.previous_amino.coordinates[1]]
        elif abs(self.previous_amino.direction) == 2:
            self.coordinates = [self.previous_amino.coordinates[0], self.previous_amino.coordinates[1] + (int(self.previous_amino.direction / 2))]

    def get_possibilities(self) -> list[int]:
        """ Get a list of the possible directions an amino can go to """
        previous = self.previous_amino
        previous_coordinates = self.previous_amino.coordinates
        unsave_coordinates = []
        while previous != None:
            unsave_coordinates.append(previous.coordinates)
            previous = previous.previous_amino
        
        available_options = set([-2, -1, 1, 2])
        unavailable_options = set()
        for i in available_options:
            if abs(i) == 1 and [previous_coordinates[0] + i, previous_coordinates[1]] in unsave_coordinates:
                unavailable_options.add(i)
            elif abs(i) == 2 and [self.previous_amino.coordinates[0], self.previous_amino.coordinates[1] + (i/2)] in unsave_coordinates:
                unavailable_options.add(i)
        options = list(available_options - unavailable_options)
        return options
