# heeft problemen met opgesloten aminos

from amino import Amino
import sys

# returns list of input file containing protein (each amino is an item in list)
def get_protein(file):
    return [*str(*open(file))]

# goes through list of protein and moves each amino based on previous amino
def make_structure(protein_list, output_file):
    previous_amino = Amino(0, protein_list[0], None)
    for i in range(1, len(protein_list)):
        current_amino = Amino(i, protein_list[i], previous_amino)
        current_amino.coordinates = current_amino.previous_amino.coordinates

        current_amino.move_amino()
        output_file.write(f"{previous_amino.type},{previous_amino.direction}\n")

        previous_amino = current_amino
    output_file.write(f"{previous_amino.type},{previous_amino.direction}\n")

def count_score(amino):
    score = 0
    while amino != None:
        if amino.type == "H":
            check_previous = amino.previous_amino
            while check_previous != None:
                if (abs(check_previous.coordinates[0] - amino.coordinates[0]) + abs(check_previous.coordinates[1] - amino.coordinates[1])) == 1 and check_previous != amino.previous_amino and check_previous.type == "H":
                    score -= 1
                check_previous = check_previous.previous_amino
        amino = amino.previous_amino
    return score

if __name__ == "__main__":

    protein_list = get_protein(f"proteins/{sys.argv[1]}")

    output_file = open(f"output/{sys.argv[2]}", "w")
    output_file.write("amino,fold\n")

    final_amino = make_structure(protein_list, output_file)

    # print(count_score(final_amino))

    output_file.close()
