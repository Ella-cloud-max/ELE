from code.classes import protein, amino
from code.algorithms import randomise
from code.algorithms import depth_first
from code.visualisation import visualisation

if __name__ == "__main__":

    input_file = "proteins/protein1.csv"

    # Try depth first algorithms
    test_protein = protein.Protein(input_file)
    depth = depth_first.DepthFirst(test_protein)

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

    test_protein.print_output("output_L.csv")

