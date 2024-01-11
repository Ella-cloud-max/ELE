# USE: python3 visualisation.py example_output.csv

import csv
import sys

def get_output(file: str) -> list[list[str]]:
    ''' Read the amino and directions from the file '''
    output = []
    with open(file) as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == "H" or line[0] == "P":
                output.append(line)
    return output

def get_stability(file: str) -> str:
    ''' Read the stability from the file '''
    with open(file) as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == "score":
                return line[1]
    return "?"

def create_empty_square(size: int) -> list[list[str]]:
    ''' Create an empty square big enough for the protein '''
    square = []
    size += 2 #nu gedaan omdat er anders problemen zijn met add_stars index out of reach
    for x in range(0, size):
        square.append(list(" " * size))
    return square

def add_proteins(empty_square: list[list[str]], output: list[list[str]]) -> list[list[str]]:
    ''' Add the proteins and connections into the empty square '''
    mid = len(output) * 2
    empty_square[mid][mid] = output[0][0]
    now_line = mid
    now_col = mid
    for index, line in enumerate(output):
        direction = int(line[1])
        if direction == 1:
            empty_square[now_line][now_col + 1] = "-" 
            empty_square[now_line][now_col + 2] = output[index+1][0]
            now_col += 2
        elif direction == -1:
            empty_square[now_line][now_col - 1] = "-"   
            empty_square[now_line][now_col - 2] = output[index+1][0]  
            now_col -= 2
        elif direction == 2:
            empty_square[now_line - 1][now_col] = "|"
            empty_square[now_line - 2][now_col] = output[index+1][0]
            now_line -= 2
        elif direction == -2:
            empty_square[now_line + 1][now_col] = "|"
            empty_square[now_line + 2][now_col] = output[index+1][0]
            now_line += 2
    return empty_square 

def add_stars(square: list[list[str]]) -> list[list[str]]:
    ''' Add stars into the places there is a H-bond '''
    for index_line, line in enumerate(square):
        for index_item, item in enumerate(line):
            if item == "H":
                if line[index_item + 2] == "H" and line[index_item + 1] != "-":
                    line[index_item + 1] = "*"
                elif square[index_line - 2][index_item] == "H" and square[index_line - 1][index_item] != "|":
                    square[index_line - 1][index_item] = "*"
    return square

def delete_empty(square: list[list[str]]) -> list[list[str]]:
    ''' Delete the empty lines and columns from the square '''
    empty_line = list(" " * len(square))
    nice_square = square.copy()
    for line in square:
        if line == empty_line:
            nice_square.remove(line)
    
    empty_col = list(range(len(nice_square[0])))
    for index, item in enumerate(nice_square[0]):
        for index_line in range(len(nice_square)):
            if nice_square[index_line][index] != " ":
                try:
                    empty_col.remove(index)
                except ValueError:
                    pass
    
    for i in range(len(nice_square)):
        for index in sorted(empty_col, reverse=True):
            del nice_square[i][index]
    
    return nice_square

def count_stars(square: list[list[str]]) -> int:
    ''' Count the number of stars in the square '''
    stars = 0
    for line in square:
        for item in line:
            if item == "*":
                stars -= 1
    return stars

def fill_square(empty_square: list[list[str]], output: list[list[str]]) -> list[list[str]]:
    ''' Fill the empty square with the proteins, stars and delete the empty lines '''
    protein_square = add_proteins(empty_square, output)
    complete_square = add_stars(protein_square)
    pretty_square = delete_empty(complete_square)
    return pretty_square

def print_folded_protein(filepath: str) -> None:
    ''' Print the folded protein, the stability score, and the expected stability '''
    output = get_output(filepath)   #get list of amino and directions
    empty_square = create_empty_square(len(output) * 2 * 2)
    square = fill_square(empty_square, output) # fill the square with the amino and stars
    for line in square:
        for item in line:
            print(item, end=" ")
        print()
    print(f"The counted stability is {count_stars(square)}") # print the amount of stars in the square
    print(f"The stability from the file is {get_stability(filepath)}") # print the amount of stars there should be according to the file

if __name__ == "__main__":
    filename = sys.argv[1]
    filepath = "output/" + filename
    print_folded_protein(filepath)