from time import time
from graphcreating import graph_creating
from readfromtxt import read_from_txt
import random


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


class Quicksort:
    def __init__(self, data):
        self.mdata = data

    def Partition(self, left, right: int):
        # choosing pivot_position by random
        data = self.mdata
        pivot_position = random.randint(left, right)
        pivot = data[pivot_position]
        swap(data, pivot_position, right)
        leftwall = left
        for i in range(left, right):
            if data[i] <= pivot:
                swap(data, leftwall, i)
                leftwall += 1
        swap(data, right, leftwall)
        return leftwall

    def Quicksort(self, left, right):
        if left < right:
            pivot_position = self.Partition(left, right)
            self.Quicksort(left, pivot_position-1)
            self.Quicksort(pivot_position+1, right)

    def Quicksort_runtime(self, range):
        start_time = time()
        self.Quicksort(0, range)
        endtime = time()
        return endtime - start_time

    def Quicksort_test(self):
        runtimes = {}
        for i in range(1000, 10000, 1000):
            runtimes[i] = self.Quicksort_runtime(i)
        graph_creating(runtimes, 'Quicksort_runtimes')


data = read_from_txt('pan-tadeusz.txt')
q_sort_1 = Quicksort(data)
q_sort_1.Quicksort_test()
with open("quick_sort_odp.txt", "w") as file:
    for word in q_sort_1.mdata:
        file.write(word)
        file.write(" ")
