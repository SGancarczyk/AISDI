from time import time
from graphcreating import graph_creating
from readfromtxt import read_from_txt
import random


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


class Quicksort:
    def __init__(self, data):
        self._data = data

    def Partition(self, data, left, right):
        # choosing pivot_position by random
        pivot_position = random.randint(0, right)
        pivot = data[pivot_position]
        swap(data, pivot_position, right)
        leftwall = left
        for i in range(left, right-1):
            if data[i] < pivot:
                swap(data, leftwall, i)
                leftwall += 1
        swap(data, right, leftwall)
        return leftwall

    def Quicksort(self, data, left, right):
        if left < right:
            pivot_position = self.Partition(data, left, right)
            self.Quicksort(data, left, pivot_position-1)
            self.Quicksort(data, pivot_position+1, right)

    def Quicksort_runtime(self, data: list):
        start_time = time()
        self.Quicksort(data, 0, len(data)-1)
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
