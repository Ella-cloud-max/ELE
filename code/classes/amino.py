# "1" betekent een positieve stap in de eerste dimensie (X-as richting).
# "-1" betekent een negatieve stap in de eerste dimensie (X-as richting).
# "2" betekent een positieve stap in de tweede dimensie (Y-as richting).
# "-2" betekent een negatieve stap in de tweede dimensie (Y-as richting).

class Amino():
    def __init__(self, i: int, soort: str, direction: int, coordinates: list[int], previous) -> None:
        self.i: int = i
        self.soort: str = soort                      # H or P
        self.direction: int = direction                    # -2, -1, 1 or 2 (see explanation above)
        self.coordinates: list[int] = coordinates    # [n, m]
        self.previous_amino = previous               # variable holds class of previous amino

    def __repr__(self) -> str:
        return f"{self.i}, {self.soort}, {self.direction}, {self.coordinates}, previous:{self.previous_amino}"

    # changes coordinates of amino based on direction which is chosen at random
    def change_coordinates(self) -> None:

        if self.previous_amino == None:
            return

        if abs(self.previous_amino.direction) == 1:
            self.coordinates = [self.previous_amino.coordinates[0] + self.previous_amino.direction, self.previous_amino.coordinates[1]]
        elif abs(self.previous_amino.direction) == 2:
            self.coordinates = [self.previous_amino.coordinates[0], self.previous_amino.coordinates[1] + (self.previous_amino.direction / 2)]

    # # checks whether coordinates of amino are not same as any previous amino's
    # def check_coordinates(self, algorithm) -> bool:
    #     check_previous = self.previous_amino
    #     save_coordinates = []
    #     while check_previous != None:
    #         save_coordinates.append(check_previous.coordinates)            
    #         check_previous = check_previous.previous_amino
        
    #     if self.coordinates in save_coordinates:
    #         return False

        # for i in [-2, -1, 1, 2]:
        #     if abs(i) == 1 and [self.coordinates[0] + i, self.coordinates[1]] in save_coordinates:
        #         self.neighbours += 1
        #     elif abs(i) == 2 and [self.coordinates[0], self.coordinates[1] + i] in save_coordinates:
        #         self.neighbours += 1

        # print(self.i, self.soort, self.neighbours)

        # if self.neighbours == 4:
        #     check_previous = self.previous_amino
        
        # return True