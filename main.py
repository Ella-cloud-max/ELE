import sys

from code.classes import protein, amino
from code.algorithms import randomise
from code.visualisation import visualisation

if __name__ == "__main__":

    input_file = f"{sys.argv[1]}"

    test_protein = protein.Protein(input_file)
    
    randomise.random_assignment(test_protein)

    while test_protein.check_viability() == False:
        randomise.random_assignment(test_protein)
    
    test_protein.print_output(f"{sys.argv[2]}")
    visualisation.print_folded_protein(f"output/{sys.argv[2]}")

    for test_amino in test_protein.aminos.values():
        if test_amino.i == test_protein.i_list[-1]:
            continue
        randomise.random_reconfigure_amino(test_protein, test_amino)

        while test_protein.check_viability() == False:
            randomise.random_configure_amino(test_protein, test_amino)
        
        test_protein.print_output(f"{sys.argv[2]}_2")
        visualisation.print_folded_protein(f"output/{sys.argv[2]}_2")
