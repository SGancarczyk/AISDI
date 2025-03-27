from time import time
from graphcreating import graph_creating
from readfromtxt import read_from_txt


class Insertionsort:
    def __init__(self, data):
        self._data = data

    def insertionsort(self, mrange):
        data = self._data
        for i in range(1, mrange):
            j = i
            while j > 0 and data[j - 1] > data[j]:
                data[j], data[j-1] = data[j-1], data[j]
                j -= 1

    def insertionsort_runtime(self, range):
        start_time = time()
        self.insertionsort(range)
        endtime = time()
        return endtime - start_time

    def insertionsort_test(self):
        runtimes = {}
        for i in range(1000, 10000, 1000):
            runtimes[i] = self.insertionsort_runtime(i)
        graph_creating(runtimes, 'insertionsort_runtimes')


data = read_from_txt('pan-tadeusz.txt')
i_sort_1 = Insertionsort(data)
i_sort_1.insertionsort_test()
