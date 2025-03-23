from time import time
from graphcreating import graph_creating
from readfromtxt import read_from_txt


class Insertionsort:
    def __init__(self, data):
        self._data = data

    def insertionsort():
        # To be implemented
        pass

    def insertionsort_runtime(self, data: list):
        start_time = time()
        self.insertionsort(data)
        endtime = time()
        return endtime - start_time

    def insertionsort_test(self):
        runtimes = {}
        for i in range(1000, 10000, 1000):
            o_data = self._data[:i]
            runtimes[i] = self.insertionsort_runtime(o_data)
        graph_creating(runtimes, 'insertionsort_runtimes')


data = read_from_txt('pan-tadeusz.txt')
i_sort_1 = Insertionsort(data)
i_sort_1.insertionsort_test()
