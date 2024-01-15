import csv
import sys
import matplotlib.pyplot as plt
from typing import Any

def get_output(file: str) -> list[list[Any]]:
    """ Import the aminos and directions from the file and add coordinates """
    output = []
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            if line[0] == "H" or line[0] == "P":
                output.append(line)
    output_coords = add_coordinates(output)
    return output_coords

def add_coordinates(output: list[list[Any]]) -> list[list[Any]]:
    """ Add coordinates to a list of amninos and directions """
    for index, line in enumerate(output):
        # the first amino has location 0,0
        if index == 0:
            line.append((0,0))
            line.append(index)
        else:
            # the next amino depends upon the previous amino
            previous = output[index-1]
            
            # up
            if int(previous[1]) == 2:
                line.append((previous[2][0], previous[2][1] + 1))
                line.append(index)
            
            # down
            elif int(previous[1]) == -2:
                line.append((previous[2][0], previous[2][1] - 1))
                line.append(index)
            
            # right
            elif int(previous[1]) == 1:
                line.append((previous[2][0] + 1, previous[2][1]))
                line.append(index)
            
            # left
            elif int(previous[1]) == -1:
                line.append((previous[2][0] - 1, previous[2][1]))
                line.append(index)
    return output

def coord_stars(coordinates_H: list[list[Any]]) -> list[tuple[int, int]]:
    """ Create a list of the H-bond coordinates """
    # make a dict of the coordinates and their index in the overall structure
    just_coords = {}
    for coordinate in coordinates_H:
        just_coords[coordinate[2]] = coordinate[3]

    star_coordinates = []
    for coordinate in coordinates_H:
        # check if to there is a H amino to the right
        # and that the H aminos aren't connected yet
        possibility_right = (coordinate[2][0] + 1, coordinate[2][1])
        if possibility_right in just_coords and abs(just_coords[possibility_right] - coordinate[3]) != 1:
            star_coordinates.append((coordinate[2][0] + 0.5, coordinate[2][1]))
        
        # check if there is a H amino above
        # and that the H aminos aren't connected yet
        possibility_up = (coordinate[2][0], coordinate[2][1] + 1)
        if possibility_up in just_coords and abs(just_coords[possibility_up] - coordinate[3]) != 1:
            star_coordinates.append((coordinate[2][0], coordinate[2][1] + 0.5))
    return star_coordinates

def coord_types(output: list[list[Any]], soort: str) -> list[list[Any]]:
    """ Get a list of coordinates of all aminos of a specific type """
    output_coord = []
    for line in output:
        if line[0] == soort:
            output_coord.append(line)
    return output_coord

def create_plot(output):
    """ Create a plot of the protein """
    # coordinates to the connections between amino
    x_as = [x[2][0] for x in output]
    y_as = [x[2][1] for x in output]
    
    # coordinates for all the H amino
    coord_H = coord_types(output, "H")
    x_as_H = [x[2][0] for x in coord_H]
    y_as_H = [x[2][1] for x in coord_H]

    # coordinates for all the P amino
    coord_P = coord_types(output, "P")
    x_as_P = [x[2][0] for x in coord_P]
    y_as_P = [x[2][1] for x in coord_P]
    
    # coordinates for all the H-bonds
    stars = coord_stars(coord_H)
    x_stars = [x[0] for x in stars]
    y_stars = [x[1] for x in stars]

    # Create a plot
    plt.grid(False)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')

    # Add the H and P amino to the plot
    plt.scatter(x_as_H, y_as_H, c = "red", zorder = 3, label = "H")
    plt.scatter(x_as_P, y_as_P, c = "blue", zorder = 3, label = "P")

    # Add the connections between the amino to the plot
    plt.plot(x_as, y_as, c = "black")

    # Add the H-bonds to the plot as stars
    plt.scatter(x_stars, y_stars, c = "hotpink", zorder = 3, label = "star", marker= "*")

    # Show the plot
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # import the output file
    filename = sys.argv[1]
    filepath = "output/" + filename
    output = get_output(filepath)
    create_plot(output)

   
