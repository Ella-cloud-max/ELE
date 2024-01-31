import matplotlib.pyplot as plt

def histogram(list1, output_file):
    bins = [x + 0.5 for x in set(sorted(list1))]
    bins.append(min(bins) - 1)
    bins = sorted(bins)

    plt.hist(list1, bins)
    plt.xlim(min(list1) - 1.5, max(list1) + 1.5)
    plt.savefig(f"output/{output_file}_histogram.png")