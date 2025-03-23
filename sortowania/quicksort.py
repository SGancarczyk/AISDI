from time import time
from graphcreating import graph_creating
from readfromtxt import read_from_txt


class Quicksort:
    def __init__(self, data):
        self._data = data

    def Quicksort(self, data):
        # To be implemented
        pass

    def Quicksort_runtime(self, data: list):
        start_time = time()
        self.Quicksort(data)
        endtime = time()
        return endtime - start_time

    def Quicksort_test(self):
        runtimes = {}
        for i in range(1000, 10000, 1000):
            o_data = self._data[:i]
            runtimes[i] = self.Quicksort_runtime(o_data)
        graph_creating(runtimes, 'Quicksort_runtimes')


data = read_from_txt('pan-tadeusz.txt')
q_sort_1 = Quicksort(data)
q_sort_1.Quicksort_test()
