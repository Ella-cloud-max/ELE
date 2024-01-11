import csv
import sys
import matplotlib.pyplot as plt

def get_output(file):
    output = []
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            if line[0] == "H" or line[0] == "P":
                output.append(line)
    return output

def add_coordinates(output):
    for index, line in enumerate(output):
        #line.append([0,0])
        if index == 0:
            line.append([0,0])
        else:
            old = output[index-1]
            if int(old[1]) == 2:
                new_y = old[2][1] + 1
                line.append([old[2][0], new_y])
            if int(old[1]) == -2:
                new_y = old[2][1] - 1
                line.append([old[2][0], new_y])
            if int(old[1]) == 1:
                new_x = old[2][0] + 1
                line.append([new_x, old[2][1]])
            if int(old[1]) == -1:
                new_x = old[2][0] - 1
                line.append([new_x, old[2][1]])
    return output

def coord_line(output):
    x_as = []
    y_as = []
    for line in output:
        x_as.append(line[2][0])
        y_as.append(line[2][1])
    return x_as, y_as

def coord_types(output, type_letter):
    x_as = []
    y_as = []
    for line in output:
        if line[0] == type_letter:
            x_as.append(line[2][0])
            y_as.append(line[2][1])
    return x_as, y_as

def coord_stars(x_as, y_as):
    assert len(x_as) == len(y_as)
    for index in range(len(x_as)):
        print(index)

if __name__ == "__main__":
    filename = sys.argv[1]
    filepath = "output/" + filename
    output = get_output(filepath)
    output = add_coordinates(output)
    x_as, y_as = coord_line(output)
    coord_stars(x_as, y_as)
    x_as_H, y_as_H = coord_types(output, "H")
    x_as_P, y_as_P = coord_types(output, "P")
    plt.grid(False)
    plt.axis('off')
    location = 0
    plt.plot(x_as, y_as, c = "black")
    plt.scatter(x_as_H, y_as_H, c = "red", zorder = 3, label = "H")
    plt.scatter(x_as_P, y_as_P, c = "blue", zorder = 3, label = "P")
    plt.legend()
    plt.show()
