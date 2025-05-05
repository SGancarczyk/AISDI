import matplotlib.pyplot as plt


def graph_creating_heap(data1: dict, data2: dict, data3: dict, save_name):
    # Arguement is dict, where keys represents size of tested data,
    #  and values represents program runtime
    sizes1, times1 = list(data1.keys()), list(data1.values())
    sizes2, times2 = list(data2.keys()), list(data2.values())
    sizes3, times3 = list(data3.keys()), list(data3.values())
    plt.plot(sizes1, times1, marker='o', label="Typ kopca 2-arny")
    plt.plot(sizes2, times2, marker='o', label="Typ kopca 5-arny")
    plt.plot(sizes3, times3, marker='o', label="Typ kopca 7-arny")
    plt.title('Creation of heap time depending on the number of items')
    plt.xlabel('Data range (numbers)')
    plt.ylabel('Operating time (seconds)')
    plt.grid(True)
    plt.legend()
    plt.savefig(f'{save_name}.png')
    plt.show()


def graph_creating_pop(data1: dict, data2: dict, data3: dict, save_name):
    # Arguement is dict, where keys represents size of tested data,
    #  and values represents program runtime
    sizes1, times1 = list(data1.keys()), list(data1.values())
    sizes2, times2 = list(data2.keys()), list(data2.values())
    sizes3, times3 = list(data3.keys()), list(data3.values())
    plt.plot(sizes1, times1, marker='o', label="Typ kopca 2-arny")
    plt.plot(sizes2, times2, marker='o', label="Typ kopca 5-arny")
    plt.plot(sizes3, times3, marker='o', label="Typ kopca 7-arny")
    plt.title('Pop root depending on the number of items')
    plt.xlabel('Data range (numbers)')
    plt.ylabel('Operating time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{save_name}.png')
    plt.show()
