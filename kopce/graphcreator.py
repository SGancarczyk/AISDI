import matplotlib.pyplot as plt


def graph_creating_heap(data: dict, save_name):
    # Arguement is dict, where keys represents size of tested data,
    #  and values represents program runtime
    sizes = data.keys()
    times = data.values()
    plt.plot(sizes, times, marker='o')
    plt.title('Creation of heap time depending on the number of items')
    plt.xlabel('Data range (numbers)')
    plt.ylabel('Operating time (seconds)')
    plt.grid(True)
    plt.savefig(f'{save_name}.png')
    plt.show()


def graph_creating_pop(data: dict, save_name):
    # Arguement is dict, where keys represents size of tested data,
    #  and values represents program runtime
    sizes = data.keys()
    times = data.values()
    plt.plot(sizes, times, marker='o')
    plt.title('Pop root depending on the number of items')
    plt.xlabel('Data range (numbers)')
    plt.ylabel('Operating time (seconds)')
    plt.grid(True)
    plt.savefig(f'{save_name}.png')
    plt.show()
