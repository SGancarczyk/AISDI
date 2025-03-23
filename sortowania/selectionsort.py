from time import time
from graphcreating import graph_creating
from readfromtxt import read_from_txt


class Selectionsort:
    def __init__(self, data: list):
        self._data = data

    def selectionsort(self, data):
        for i in range(len(data)):
            min_index = i + self.mini(data[i:])
            data[i], data[min_index] = data[min_index], data[i]
        return data

    def mini(self, lst):
        # Returns index of minimal element in list
        min_index = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i
        return min_index

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
