# bubble sort implemented
from graphcreating import graph_creating
from time import time
from readfromtxt import read_from_txt


def bubblesort(list: list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


def bubblesort_runtime(data):
    start_time = time()
    bubblesort(data)
    endtime = time()
    return endtime - start_time


def bubblesort_test(data):
    runtimes = {}
    print(data)
    for i in range(1000, 10000, 1000):
        o_data = data[:i]
        runtimes[i] = bubblesort_runtime(o_data)
    print(runtimes)
    graph_creating(runtimes, 'bubblesort_runtimes')


data = read_from_txt('pan-tadeusz.txt')
bubblesort_test(data)
