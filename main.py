# heeft problemen met opgesloten aminos

from amino import Amino
from score import count_score
from random_algorithm import randomise
import sys

# returns list of input file containing protein (each amino is an item in list)
def get_protein(file):
    return [*str(*open(file))]

# goes through list of protein and moves each amino based on previous amino
def make_structure(protein_list, algorithm, output_file):
    previous_amino = Amino(0, protein_list[0], None)
    for i in range(1, len(protein_list)):
        current_amino = Amino(i, protein_list[i], previous_amino)
        current_amino.coordinates = current_amino.previous_amino.coordinates

        current_amino.move_amino(algorithm)
        output_file.write(f"{previous_amino.type},{previous_amino.direction}\n")

        previous_amino = current_amino
    output_file.write(f"{previous_amino.type},{previous_amino.direction}\n")
    return previous_amino

if __name__ == "__main__":

    protein_list = get_protein(f"proteins/{sys.argv[1]}")

    output_file = open(f"output/{sys.argv[2]}", "w")
    output_file.write("amino,fold\n")

    final_amino = make_structure(protein_list, randomise, output_file)

    output_file.write(f"score,{count_score(final_amino)}")
    output_file.close()
