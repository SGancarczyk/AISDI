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
        self.heapify_up(len(self)-1)

    def heapify_up(self, element_index):
        if element_index == 0:
            return
        parent = (element_index-1)//2
        if self.nodes[element_index] <= self.nodes[parent]:
            return
        else:
            self.swap(element_index, parent)
            self.heapify_up(parent)
    
    def pop_root(self):
        self.swap(0, len(self)-1)
        del self.nodes[-1]
        self.max_heapify(len(self), 0)

    def max_heapify(self, heap_size, i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        if left < heap_size and self.nodes[left] > self.nodes[i]:
            largest = left

        if right < heap_size and self.nodes[right] > self.nodes[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.max_heapify(heap_size, largest)

    def build_max_heap(self):
        heap_size = len(self)
        for i in range(heap_size//2, -1, -1):   # for all the parents 
            self.max_heapify(heap_size, i)

    def __str__(self):
        output = ""
        i = 1
        levels = 0
        while (i < len(self)):
            i *= 2
            levels += 1
        index = 0
        level = 0
        while index < len(self):
            count = 2 ** level
            level_nodes = self.nodes[index:index + count]

            # Oblicz margines na początku linii, żeby wyśrodkować
            spaces = " " * ((2 ** (levels - level)) - 1)

            # Odstępy między elementami tego poziomu
            between = " " * ((2 ** (levels - level + 1)) - 1)

            line = spaces + between.join(str(x) for x in level_nodes)
            output += line + "\n"

            index += count
            level += 1

        return output


def main():
    a = [1, 4, 2, 1, 6, 5, 7, 2, 7, 10, 3]
    h1 = heap(a)
    h1.add(12)
    h1.add(8)
    h1.add(4)
    h1.add(5)
    h1.add(9)
    h1.pop_root()
    h1.pop_root()
    print(h1)


main()