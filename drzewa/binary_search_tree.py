from random import randint
from time import time # noqa
from graphcreating import graph_creating_tree

test_data = [randint(1, 30000) for _ in range(10000)]


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if root.key == key:
        return root
    if root.key < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


def search(root, key):

    # Base Cases: root is null or key
    # is present at root
    if root is None or root.key == key:
        return root

    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


# This function deletes a given key x from the
def del_node(root, x):

    # Base case
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.key > x:
        root.left = del_node(root.left, x)
    elif root.key < x:
        root.right = del_node(root.right, x)

    else:
        # If root matches with the given key

        # Cases when root has 0 children or
        # only right child
        if root.left is None:
            return root.right

        # When root has only left child
        if root.right is None:
            return root.left

        # When both children are present
        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)

    return root


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.key, end=" ")
        in_order(root.right)


def display_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.key))
        if node.left or node.right:
            if node.left:
                display_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                display_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


def create_tree(size, data):
    r = Node(data[0])
    for i, digit in enumerate(data[:size]):
        if i == 0:
            continue
        r = insert(r, digit)
    return r


def runtime(size):
    start_time = time()
    create_tree(size, test_data)
    return time() - start_time


def benchmarks():
    results = {}
    for i in range(1000, 10001, 1000):
        results[i] = runtime(i)
    graph_creating_tree(results, 'binary_search_tree_graph')


def is_valid(root):
    if root.left:
        if root.left.key >= root.key:
            return False
        if not is_valid(root.left):
            return False
    if root.right:
        if root.right.key <= root.key:
            return False
        if not is_valid(root.right):
            return False
    return True


if __name__ == "__main__":
    # benchmarks()
    values = [3,4,2,6,4,1,3,7,8]
    t1 = create_tree(len(values), values)
    del_node(t1, 1)
    del_node(t1, 3)
    display_tree(t1)