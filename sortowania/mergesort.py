from graphcreating import graph_creating
from time import time
from readfromtxt import read_from_txt
import random # noqa


class Mergesort:
    def __init__(self, data):
        self._data = data

    def merge(self, lst1, lst2):
        # Merges two sorted(asc) lists
        merged_lst = []
        # The loop ends at the end of one of the lists
        while len(lst1) and len(lst2):
            if lst1[0] < lst2[0]:
                # Appending smaller item to merged list
                merged_lst.append(lst1[0])
                # Removing sorted item from original list
                lst1.pop(0)
            else:
                merged_lst.append(lst2[0])
                lst2.pop(0)
        # Extending merged list with sorted list(one is empty)
        merged_lst.extend(lst1)
        merged_lst.extend(lst2)
        return merged_lst

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        else:
            # calling merge and merge_sort function recursively
            # splitting given list to single element lists(sorted)
            # then merging them
            return self.merge(self.merge_sort(lst[:len(lst)//2]),
                              self.merge_sort(lst[len(lst)//2:]))

    def mergesort_runtime(self, data: list):
        start_time = time()
        self.merge_sort(data)
        endtime = time()
        return endtime - start_time

    def mergesort_test(self):
        runtimes = {}
        for i in range(1000, 10000, 1000):
            o_data = self._data[:i]
            runtimes[i] = self.mergesort_runtime(o_data)
        graph_creating(runtimes, 'mergesort_runtimes')


data = read_from_txt('pan-tadeusz.txt')
m_sort_1 = Mergesort(data)
m_sort_1.mergesort_test()


'''tests = [random.randint(1, 100) for i in range(100)]
m_sort_2 = Mergesort(tests)
print(m_sort_2.merge_sort(tests))'''
