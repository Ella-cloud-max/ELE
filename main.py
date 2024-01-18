import sys

from code.classes import protein, amino
from code.algorithms import randomise
from code.algorithms import depth_first
from code.visualisation import visualisation


if __name__ == "__main__":

    input_file = f"{sys.argv[1]}"

    # ------------- random algorithm -------------
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

    # ------------- depth-first algorithm -------------
    input_file = "proteins/protein1.csv"
    test_protein2 = protein.Protein(input_file)
    depth = depth_first.DepthFirst(test_protein2)

    # Run the algoritm for x amount of seconds
    depth.run(5)

    print(f"Value of the configuration after Depth First: "
         f"{depth.protein.count_score()}")

    depth.protein.print_output("output_ella.csv")
    visualisation.print_folded_protein("output/output_ella.csv")

    # Try random algorithm
    test_protein = protein.Protein(input_file)
    random_protein = randomise.randomise(test_protein)

    while test_protein.check_viability() == False:
        random_protein = randomise.randomise(test_protein)
