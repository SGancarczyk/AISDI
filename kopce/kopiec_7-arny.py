from time import time
from graphcreator import graph_creating_heap, graph_creating_pop


class heap:
    def __init__(self, T):
        self.nodes = T
        self.build_max_heap()

    def __len__(self):
        return len(self.nodes)

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def add(self, element):
        self.nodes.append(element)
        self.heapify_up(len(self) - 1)

    def heapify_up(self, element_index):
        if element_index == 0:
            return
        parent = (element_index - 1) // 7
        if self.nodes[element_index] <= self.nodes[parent]:
            return
        else:
            self.swap(element_index, parent)
            self.heapify_up(parent)

    def pop_root(self):
        if len(self) < 1:
            return
        else:
            self.swap(0, len(self) - 1)
            del self.nodes[-1]
            self.max_heapify(len(self), 0)

    def max_heapify(self, heap_size, i):
        largest = i
        for k in range(1, 8):
            child_index = 7 * i + k
            if child_index < heap_size and self.nodes[child_index] > self.nodes[largest]:
                largest = child_index
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(heap_size, largest)

    def build_max_heap(self):
        heap_size = len(self)
        for i in range(heap_size // 7, -1, -1):
            self.max_heapify(heap_size, i)

    def __str__(self):
        output = ""
        i = 1
        levels = 0
        while i < len(self):
            i *= 7
            levels += 1
        index = 0
        level = 0
        while index < len(self):
            count = 7 ** level
            level_nodes = self.nodes[index:index + count]


            spaces = " " * max(0, (7 ** (levels - level)) - 1)
            between = " " * max(0, (7 ** (levels - level + 1)) - 1)

            line = spaces + between.join(str(x) for x in level_nodes)
            output += line + "\n"

            index += count
            level += 1

        return output


def generate_numbers():
    import random
    return [random.randint(1, 300000) for _ in range(100000)]


def heap_create_runtime(data):
    start_time = time()
    h1 = heap(data)
    end_time = time()
    return end_time - start_time


def heap_create_test(data):
    runtimes = {}
    for i in range(10000, 100001, 10000):
        mdata = data[:i]
        runtimes[i] = heap_create_runtime(mdata)
    graph_creating_heap(runtimes, "Kopiec 7-arny create")


def heap_pop_runtime(h1, how_much):
    start_time = time()
    for _ in range(how_much):
        h1.pop_root()
    end_time = time()
    return end_time - start_time


def heap_pop_test(data):
    runtimes = {}
    for i in range(10000, 100001, 10000):
        mheap = heap(data[:])
        runtimes[i] = heap_pop_runtime(mheap, i)
    graph_creating_pop(runtimes, "Kopiec 7-arny pop_root")


def main():
    a = generate_numbers()
    heap_create_test(a)
    heap_pop_test(a)


main()