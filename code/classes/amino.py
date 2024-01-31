from typing import Any

# "1" betekent een positieve stap in de eerste dimensie (X-as richting).
# "-1" betekent een negatieve stap in de eerste dimensie (X-as richting).
# "2" betekent een positieve stap in de tweede dimensie (Y-as richting).
# "-2" betekent een negatieve stap in de tweede dimensie (Y-as richting).


class Amino():
    def __init__(self, i: int, soort: str, direction: int,
                 coordinates: tuple[int, int], previous: Any) -> None:
        self.i: int = i
        self.soort: str = soort
        self.direction: int = direction
        self.coordinates: tuple[int, int] = coordinates
        self.previous_amino = previous
        self.next_amino: Any = None

    def __repr__(self) -> str:
        return f"{self.i}, {self.soort}, {self.direction}, {self.coordinates}"

    def change_direction(self, direction: int):
        """
        Changes the direction of the amino.

        in: direction is an int of {-2, -1, 1, 2}
        out: self.direction is direction
        """

        self.direction = direction

    def change_coordinates(self) -> None:
        """
        Changes coordinates of amino based on the direction of
        the previous amino
        """

        if self.previous_amino is None:
            return
        if abs(self.previous_amino.direction) == 1:
            self.coordinates = (self.previous_amino.coordinates[0] +
                                self.previous_amino.direction,
                                self.previous_amino.coordinates[1])
        elif abs(self.previous_amino.direction) == 2:
            self.coordinates = (self.previous_amino.coordinates[0],
                                self.previous_amino.coordinates[1] +
                                (int(self.previous_amino.direction / 2)))

    def get_possibilities(self) -> list[int]:
        """
        Get a list of the possible directions an amino can go to.

        out: a list of integers, a subset of [-2, -1, 1, 2]
        """

        available_options = set([-2, -1, 1, 2])
        if self.previous_amino is None:
            options = list(available_options)
            return options
        previous = self.previous_amino
        previous_coordinates = self.previous_amino.coordinates
        unsave_coordinates = []
        while previous is not None:
            unsave_coordinates.append(previous.coordinates)
            previous = previous.previous_amino

        unavailable_options = set()
        for i in available_options:
            if abs(i) == 1 and (previous_coordinates[0] + i,
                                previous_coordinates[1]) in unsave_coordinates:
                unavailable_options.add(i)
            elif abs(i) == 2 and (self.previous_amino.coordinates[0],
                                  self.previous_amino.coordinates[1] +
                                  (i/2)) in unsave_coordinates:
                unavailable_options.add(i)
        options = list(available_options - unavailable_options)
        return options

    def get_rotate_options(self) -> list[int]:
        """
        Creates a list containing the directions for the rotate mutation

        post: returns a list of direction integers
        """
        direction_options: list[int] = [-1, 1, -2, 2]
        if self.direction != 0:
            direction_options.remove(self.direction)
        if self.i != 0:
            direction_options.remove(self.previous_amino.direction * -1)
        return direction_options

    def get_pull_options(self) -> list[int]:
        """
        Creates a list containing the directions for the pull mutation

        post: returns a list of direction integers
        """
        direction_options: list[int] = [-1, 1, -2, 2]
        if self.i == 0:
            direction_options.remove(self.direction)
            direction_options.remove(self.next_amino.direction * -1)
        elif self.next_amino.direction == 0:
            direction_options.remove(self.direction)
            direction_options.remove(self.previous_amino.direction * -1)
        else:
            direction_options = [self.next_amino.direction]
            if self.direction == direction_options[0]:
                direction_options.remove(self.direction)
        return direction_options

    def reset_position(self) -> None:
        """
        Sets the direction and the coordinates to zero
        """
        self.direction = 0
        self.coordinates = (0, 0)
