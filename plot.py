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

def x_as(output):
    x_as = []
    for line in output:
        x_as.append(line[2][0])
    return x_as

def y_as(output):
    y_as = []
    for line in output:
        y_as.append(line[2][1])
    return y_as
        

if __name__ == "__main__":
    filename = sys.argv[1]
    filepath = "output/" + filename
    output = get_output(filepath)
    output = add_coordinates(output)
    x_as = x_as(output)
    y_as = y_as(output)
    plt.grid(False)
    plt.axis('off')
    location = 0
    plt.plot(x_as, y_as, marker = 'H')
    plt.show()