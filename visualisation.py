# USE: python3 visualisation.py example_output.csv

import csv
import sys

def get_output(file):
    output = []
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            if line[0] == "H" or line[0] == "P":
                output.append(line)
    return output

def empty_square(size):
    square = []
    for x in range(0, size):
        square.append(list(" " * size))
    return square

def add_proteins(vis, output):
    mid = len(output) * 2
    vis[mid][mid] = output[0][0]
    now_line = mid
    now_col = mid
    for index, line in enumerate(output):
        direction = int(line[1])
        if direction == 1:
            vis[now_line][now_col + 1] = "-" 
            vis[now_line][now_col + 2] = output[index+1][0]
            now_col += 2
        elif direction == -1:
            vis[now_line][now_col - 1] = "-"   
            vis[now_line][now_col - 2] = output[index+1][0]  
            now_col -= 2
        elif direction == 2:
            vis[now_line - 1][now_col] = "|"
            vis[now_line - 2][now_col] = output[index+1][0]
            now_line -= 2
        elif direction == -2:
            vis[now_line + 1][now_col] = "|"
            vis[now_line + 2][now_col] = output[index+1][0]
            now_line += 2
    return vis 

def delete_empty(square):
    empty = list(" " * len(square))
    nice_square = square.copy()
    for line in square:
        if line == empty:
            nice_square.remove(line)

    return nice_square


def print_nice(square):
    square = delete_empty(square)
    for line in square:
        for item in line:
            print(item, end=" ")
        print()

def print_folded_protein(output):
    vis = empty_square(len(output) * 2 * 2)
    print_nice(add_proteins(vis, output))
    
if __name__ == "__main__":
    filename = sys.argv[1]
    filepath = "output/" + filename
    output = get_output(filepath)
    print_folded_protein(output)
    