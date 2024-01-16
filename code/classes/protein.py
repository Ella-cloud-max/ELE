from .amino import Amino

class Protein():
    def __init__(self, input_file):
        self.i_list = []
        self.aminos = self.make_aminos(input_file)
        self.score = 0
    
    def make_aminos(self, input_file):
        aminos = {}

        structure = [*str(*open(input_file))]
        
        aminos[0] = Amino(0, structure[0], 0, [0, 0], None)
        self.i_list.append(0)
        for i in range(1, len(structure)):
            aminos[i] = Amino(i, structure[i], 0, [0, 0], aminos[i-1])
            self.i_list.append(i)
        return aminos

    def check_viability(self):
        check_amino = self.aminos[self.i_list[-1]]
        while check_amino != None:
            check_previous = check_amino.previous_amino
            while check_previous != None:
                if check_amino.coordinates == check_previous.coordinates:
                    return False
        return True

    def count_score(self):
        count_amino = self.aminos[self.i_list[-1]]
        while count_amino != None:
            if count_amino.soort == "H":
                check_previous = count_amino.previous_amino
                while check_previous != None:
                    if (abs(check_previous.coordinates[0] - count_amino.coordinates[0]) + abs(check_previous.coordinates[1] - count_amino.coordinates[1])) == 1 and check_previous.soort == "H" and abs(check_previous.i - count_amino.i) != 1:
                        self.score -= 1
                    check_previous = check_previous.previous_amino
            count_amino = count_amino.previous_amino
        return self.score

    def print_output(self, output_file):
        output_file = open(f"output/{output_file}", "w")
        output_file.write("amino,fold\n")
        for amino in self.aminos.values():
            output_file.write(f"{amino.soort},{amino.direction}\n")
        output_file.write(f"score,{self.count_score()}")
        output_file.close()
