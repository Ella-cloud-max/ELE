import random

# "1" betekent een positieve stap in de eerste dimensie (X-as richting).
# "-1" betekent een negatieve stap in de eerste dimensie (X-as richting).
# "2" betekent een positieve stap in de tweede dimensie (Y-as richting).
# "-2" betekent een negatieve stap in de tweede dimensie (Y-as richting).

output_file = open("output/output_random.csv", "a")

class Protein():
    def __init__(self, type, previous):
        self.type = type                      # H of P
        self.coordinates = [0, 0]
        self.direction = 0
        self.previous_protein = previous

    def __repr__(self):
        return f"{self.type}, {self.coordinates}, {self.direction}, {self.previous_protein}"

    def move_protein(self):
        if self.previous_protein == None:
            if abs(self.direction) == 1:
                self.coordinates = [self.direction, 0]
            elif abs(self.direction) == 2:
                self.coordinates = [0, (self.direction / 2)]
        else:
            if abs(self.direction) == 1:
                # print(self.previous_protein.coordinates)
                self.coordinates = [self.previous_protein.coordinates[0] + self.direction, self.previous_protein.coordinates[1]]
            elif abs(self.direction) == 2:
                # print(self.previous_protein.coordinates)
                self.coordinates = [self.previous_protein.coordinates[0], self.previous_protein.coordinates[1] + (self.direction / 2)]
        
        self.check_protein()

    def check_protein(self):
        check_previous = self.previous_protein
        while check_previous != None:
            if check_previous.coordinates == self.coordinates:
                one_protein(self)
            else:
                check_previous = check_previous.previous_protein
        

def get_protein(file):
    protein = [*str(*open(file))]
    return protein

def one_protein(current_protein):
    current_protein.direction = random.randint(-2, 2)
    while current_protein.direction == 0:
        current_protein.direction = random.randint(-2, 2)

    # print(current_protein.direction)
    current_protein.move_protein()
    # print(current_protein.coordinates)


    return current_protein

def build(proteins_list):
    previous_protein = None
    for i in range(len(proteins_list)):
        current_protein = Protein(proteins_list[i], previous_protein)
        
        if i == len(proteins_list) - 1:
            output_file.write(f"{current_protein.type}, {current_protein.direction}\n")
            return
        previous_protein = one_protein(current_protein)
        output_file.write(f"{previous_protein.type}, {previous_protein.direction}\n")

        


if __name__ == "__main__":

    filename = "proteinen/protein4.csv"
    proteins_list = get_protein(filename)
    output_file.write("amino,fold\n")

    build(proteins_list)

    output_file.close()
