from .amino import Amino
from typing import Any, Union

class Protein():
    def __init__(self, input_file: str) -> None:
        self.i_list: list[int] = []
        self.aminos = self.make_aminos(input_file)
        self.score = 0
    
    def make_aminos(self, input_file: str) -> dict[int, Any]:
        """ Add aminos to a protein """
        aminos = {}
        structure = [*str(*open(input_file))]
        
        aminos[0] = Amino(0, structure[0], 0, [0, 0], None)
        self.i_list.append(0)
        for i in range(1, len(structure)):
            aminos[i] = Amino(i, structure[i], 0, [0, 0], aminos[i-1])
            self.i_list.append(i)
        return aminos
    
    def get_empty_amino(self) -> Any:
        """ Get the first amino that does not have coordinates yet""" 
        for amino in self.aminos.values():
            if amino.coordinates == [0, 0] and amino.i != 0:
                return amino

        return None

    def check_viability(self) -> bool:
        """ Check that no aminos have the same coordinates """
        check_amino = self.aminos[self.i_list[-1]]
        while check_amino != None:
            check_previous = check_amino.previous_amino
            while check_previous != None:
                if check_amino.coordinates == check_previous.coordinates:
                    return False
                check_previous = check_previous.previous_amino
            check_amino = check_amino.previous_amino
        return True

    def count_score(self) -> Union[bool, int]:
        """ Count and update the score of the protein """
        if not self.check_viability():
            return False
        
        self.score = 0
        count_amino = self.aminos[self.i_list[-1]]
        while count_amino != None:
            # Check if there are H*H or H*C bonds (also does -1 if there is a C*C bond)
            if count_amino.soort == "H" or count_amino.soort == "C":
                check_previous = count_amino.previous_amino
                while check_previous != None:
                    if (abs(check_previous.coordinates[0] - count_amino.coordinates[0]) + abs(check_previous.coordinates[1] - count_amino.coordinates[1])) == 1 \
                        and (check_previous.soort == "H" or check_previous.soort == "C") \
                        and abs(check_previous.i - count_amino.i) != 1:
                        self.score -= 1
                    check_previous = check_previous.previous_amino
            
            # Check if there are C*C bonds (minus an extra -4)
            if count_amino.soort == "C":
                check_previous = count_amino.previous_amino
                while check_previous != None:
                    if (abs(check_previous.coordinates[0] - count_amino.coordinates[0]) + abs(check_previous.coordinates[1] - count_amino.coordinates[1])) == 1 \
                        and check_previous.soort == "C" \
                        and abs(check_previous.i - count_amino.i) != 1:
                        self.score -= 4
                    check_previous = check_previous.previous_amino
            
            count_amino = count_amino.previous_amino
        return self.score

    def print_output(self, output_file_name: str) -> None:
        """ Print the output of a protein to a file"""
        output_file = open(f"output/{output_file_name}", "w")
        output_file.write("amino,fold\n")
        for amino in self.aminos.values():
            output_file.write(f"{amino.soort},{amino.direction}\n")
        output_file.write(f"score,{self.count_score()}")
        output_file.close()
