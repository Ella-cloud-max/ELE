from code.classes import protein, amino
from code.algorithms import randomise

if __name__ == "__main__":

    input_file = "proteins/protein2.csv"

    test_protein = protein.Protein(input_file)
    
    random_protein = randomise.randomise(test_protein)

    while test_protein.check_viability() == False:
        random_protein = randomise.randomise(test_protein)
    
    test_protein.print_output("output_L.csv")

