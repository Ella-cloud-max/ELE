# u(p), d(own), l(eft), r(ight)


class Protein():
    def __init__(self, type, previous):
        self.type = type
        self.coordinates = [0, 0]
        self.previous_protein = previous
    
    def move_protein(self, new_coords):
        self.coordinates = new_coords

def get_protein(file):
    protein = [*str(*open(file))]
    return protein
    
# def build(protein):
#     first_protein = Protein(protein[0], None)
#     for i in range(len())
#     current_protein = Protein

if __name__ == "__main__":

    filename = "proteinen/HHPHHHPH.csv"
    protein = get_protein(filename)

    # build()
    
    
