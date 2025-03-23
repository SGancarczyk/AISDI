from time import time
from graphcreating import graph_creating
from readfromtxt import read_from_txt


class Selectionsort:
    def __init__(self, data: list):
        self._data = data

    def selectionsort(self, data):
        for i in range(len(data)):
            minimum = data[i]
            for j in range(i, len(data)):
                if data[j] < minimum:
                    minimum = data[j]
                    indeks = j
            pom = data[indeks]
            data[indeks] = data[i]
            data[i] = pom

    def selectionsort_runtime(self, data: list):
        start_time = time()
        self.selectionsort(data)
        endtime = time()
        return endtime - start_time

    def selectionsort_test(self):
        runtimes = {}
        for i in range(1000, 10000, 1000):
            o_data = self._data[:i]
            runtimes[i] = self.selectionsort_runtime(o_data)
        graph_creating(runtimes, 'selectionsort_runtimes')


data = read_from_txt('pan-tadeusz.txt')
s_sort_1 = Selectionsort(data)
s_sort_1.selectionsort_test()
