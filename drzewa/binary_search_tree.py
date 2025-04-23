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


# Note that it is not a generic inorder successor
# function. It mainly works when the right child
# is not empty, which is  the case we need in BST
# delete.
def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


# This function deletes a given key x from the
# given BST and returns the modified root of the
# BST (if it is modified).
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


# Utility function to do inorder traversal
def print_tree(root):  # zjebane do poprawy
    if root is not None:
        print_tree(root.left)
        print(root.key, end=" ")
        print_tree(root.right)


def Test_Insertion():
    pass


def Test_SearchTree():
    pass


def Test_NotInTree():
    pass


def create_tree(size):
    r = Node(test_data[0])
    for i, digit in enumerate(test_data[:size]):
        if i == 0:
            continue
        r = insert(r, digit)
    return r


def runtime(size):
    start_time = time()
    create_tree(size)
    return time() - start_time


def benchmarks():
    results = {}
    for i in range(1000, 10001, 1000):
        results[i] = runtime(i)
    graph_creating_tree(results, 'binary_search_tree_graph')


# Driver code
if __name__ == "__main__":
    benchmarks()
