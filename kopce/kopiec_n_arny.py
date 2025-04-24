from time import time
from grapcreatorn import graph_creating_heap, graph_creating_pop


class heap:
    def __init__(self, T, n):
        self.arny = n
        self.nodes = T
        self.build_max_heap()

    def __len__(self):
        return len(self.nodes)

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def add(self, element):
        self.nodes.append(element)
        self.heapify_up(len(self)-1)

    def heapify_up(self, element_index):
        if element_index == 0:
            return
        parent = (element_index - 1) // self.arny
        if self.nodes[element_index] <= self.nodes[parent]:
            return
        else:
            self.swap(element_index, parent)
            self.heapify_up(parent)

    def pop_root(self):
        if len(self) < 1:
            return
        else:
            self.swap(0, len(self)-1)
            del self.nodes[-1]
            self.max_heapify(len(self), 0)

    def max_heapify(self, heap_size, i):
        largest = i
        for k in range(1, self.arny+1):
            child_index = self.arny * i + k
            if child_index < heap_size and self.nodes[child_index] > self.nodes[largest]:
                largest = child_index
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(heap_size, largest)

    def build_max_heap(self):
        heap_size = len(self)
        for i in range(heap_size//self.arny, -1, -1):
            self.max_heapify(heap_size, i)

    def __str__(self):
        output = ""
        i = 1
        levels = 0
        while i < len(self.nodes):
            i *= self.arny
            levels += 1

        index = 0
        level = 0
        while index < len(self.nodes):
            count = self.arny ** level
            level_nodes = self.nodes[index:index + count]

            margin = " " * (max(1, (self.arny **
                                    (levels - level)) // self.arny))
            between = " " * (max(1, (self.arny **
                                     (levels - level + 1)) // self.arny))

            line = margin + between.join(str(x) for x in level_nodes)
            output += line + "\n"

            index += count
            level += 1

        return output


def generate_numbers():
    import random
    return [random.randint(1, 300000) for _ in range(100000)]


def heap_create_runtime(data, n):
    start_time = time()
    h1 = heap(data, n)
    end_time = time()
    return end_time - start_time


def heap_create_test(data, n):
    runtimes = {}
    for i in range(10000, 100001, 10000):
        mdata = data[:i]
        runtimes[i] = heap_create_runtime(mdata, n)
    return runtimes


def heap_pop_runtime(h1, how_much):
    start_time = time()
    for _ in range(how_much):
        h1.pop_root()
    end_time = time()
    return end_time - start_time


def heap_pop_test(data, n):
    runtimes = {}
    for i in range(10000, 100001, 10000):
        mheap = heap(data[:], n)
        runtimes[i] = heap_pop_runtime(mheap, i)
    return runtimes


def main():
    a = generate_numbers()
    h1 = heap([], 2)
    create2 = heap_create_test(a, 2)
    pop2 = heap_pop_test(a, 2)
    create5 = heap_create_test(a, 5)
    pop5 = heap_pop_test(a, 5)
    create7 = heap_create_test(a, 7)
    pop7 = heap_pop_test(a, 7)
    graph_creating_heap(create2, create5, create7, "Final create")
    graph_creating_pop(pop2, pop5, pop7, "Final Pop")
    h1.pop_root(2)

main()
