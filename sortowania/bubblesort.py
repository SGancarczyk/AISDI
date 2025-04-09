# bubble sort implemented
from graphcreating import graph_creating
from time import time
from readfromtxt import read_from_txt


class Bubblesort:
    def __init__(self, data):
        self._data = data

    def bubblesort(self, data):
        for i in range(len(data)):
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

    def bubblesort_runtime(self, data: list):
        start_time = time()
        self.bubblesort(data)
        endtime = time()
        return endtime - start_time

    def bubblesort_test(self):
        runtimes = {}
        for i in range(1000, 10000, 1000):
            o_data = self._data[:i]
            runtimes[i] = self.bubblesort_runtime(o_data)
        graph_creating(runtimes, 'bubblesort_runtimes')


data = read_from_txt('pan-tadeusz.txt')
b_sort_1 = Bubblesort(data)
b_sort_1.bubblesort_test()
