from random import randint
from time import time


def measure_time(create_func, search_func=None, delete_func=None):
    sizes = list(range(1000, 10001, 1000))
    build_times = []
    search_times = []
    delete_times = []

    data = [randint(1, 30000) for _ in range(10000)]

    for n in sizes:
        sub_data = data[:n]

        # Mierzenie czasu tworzenia
        start = time()
        tree = create_func(sub_data)
        build_times.append(time() - start)

        # Mierzenie czasu wyszukiwania
        if search_func:
            start = time()
            for key in sub_data:
                search_func(tree, key)
            search_times.append(time() - start)

        # Mierzenie czasu usuwania (tylko dla BST)
        if delete_func:
            start = time()
            for key in sub_data:
                delete_func(tree, key)
            delete_times.append(time() - start)

    return sizes, build_times, search_times, delete_times


def bst_search(tree, key):
    return tree.search(key)


def bst_delete(tree, key):
    tree.del_node(key)


def avl_search(tree, key):
    # AVL stores root in tree.root
    node = tree.root
    while node:
        if node.key == key:
            return node
        elif key < node.key:
            node = node.left
        else:
            node = node.right
    return None
