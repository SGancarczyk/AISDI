import matplotlib.pyplot as plt


def graph_creating(data: dict, save_name):
    # Arguement is dict, where keys represents size of tested data,
    #  and values represents program runtime
    sizes = data.keys()
    times = data.keys()
    plt.plot(sizes, times, marker='o')
    plt.title('Sorting time depending on the number of items')
    plt.xlabel('Data range (words)')
    plt.ylabel('Operating time (seconds)')
    plt.grid(True)
    plt.savefig(f'{save_name}.png')
    plt.show()
