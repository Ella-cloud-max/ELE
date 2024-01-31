import matplotlib.pyplot as plt

def histogram(list1, output_file):
    title = output_file.replace("_", " ").title()
    bins = [x + 0.5 for x in set(sorted(list1))]
    bins.append(min(bins) - 1)
    bins = sorted(bins)

    plt.hist(list1, bins, edgecolor='black')
    plt.xlim(min(list1) - 1.5, max(list1) + 1.5)
    plt.xlabel("Stability Score")
    plt.ylabel("Iterations")
    plt.title(title)
    plt.savefig(f"output/experiment/histogram_{output_file}.png")