"""
Names: Ella, Erik, en Liesbet
Project: Protein Pow(d)er
"""

from code.classes.amino import Amino
from score import count_score
from code.algorithms.randomise import randomise
from visualisation import print_folded_protein
import sys

# vgm is dit overbodig,, want str(*open(file)) is ook gewoon een lijst van characters eigenlijk
def get_protein(file):
    """
    input: a file with a string of the compisition (pattern of Hydrophobe and Polar) of a protein
    output: a list of characters made from the string
    """
    return [*str(*open(file))]

# goes through list of protein and moves each amino based on previous amino
def make_structure(protein_list, algorithm, output_file):
    previous_amino = Amino(0, protein_list[0], 0, [0, 0], None)
    for i in range(1, len(protein_list)):

        current_amino = Amino(i, protein_list[i], 0, previous_amino.coordinates, previous_amino)

        current_amino.move_amino(algorithm)
        output_file.write(f"{previous_amino.soort},{previous_amino.direction}\n")

        previous_amino = current_amino
    output_file.write(f"{previous_amino.soort},{previous_amino.direction}\n")
    return previous_amino

if __name__ == "__main__":

    protein_list = get_protein(f"proteins/{sys.argv[1]}")

    output_file = open(f"output/{sys.argv[2]}", "w")
    output_file.write("amino,fold\n")
    final_amino = make_structure(protein_list, randomise, output_file)
    score = count_score(final_amino)
    output_file.write(f"score,{score}")
    output_file.close()

    # N = 1000
    # lowest_score = [0, 0]
    # for i in range(N):
    #     output_file = open(f"output_repetitions/output_{i}", "w")
    #     output_file.write("amino,fold\n")
    #     final_amino = make_structure(protein_list, randomise, output_file)
    #     score = count_score(final_amino)
    #     output_file.write(f"score,{score}")
    #     output_file.close()
    #     if score < lowest_score[1]:
    #         lowest_score = [i, score]
    #         print_folded_protein(f"output_repetitions/output_{i}")
    #     output_file.close()