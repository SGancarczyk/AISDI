from random import randint
from time import time # noqa
from graphcreating import graph_creating_tree

test_data = [randint(1, 30000) for _ in range(10000)]


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key == node.key:
            return
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)

        return self._search(node.right, key)
    
    def del_node(self, x):

        if self.root is None:
            return
        else:
            self._del_node(self.root, x)
    
    def _del_node(self, node, x):
        # If key to be searched is in a subtree
        if node.key > x:
            node.left = self._del_node(node.left, x)
        elif node.key < x:
            node.right = self._del_node(node.right, x)

        else:
            # If root matches with the given key

            # Cases when root has 0 children or
            # only right child
            if node.left is None:
                return node.right

            # When root has only left child
            if node.right is None:
                return node.left

            # When both children are present
            succ = self.get_successor(node)
            node.key = succ.key
            node.right = self._del_node(node.right, succ.key)
        return node

    def get_successor(self, curr):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')

    def print_tree(self, order="inorder"):
        if order == "inorder":
            self.inorder(self.root)
        elif order == "preorder":
            self.preorder(self.root)
        elif order == "postorder":
            self.postorder(self.root)
        print()

    def display(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left is not None or node.right is not None:  
                if node.left:
                    self.display(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.display(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


def create_tree(data):
    t = Tree()
    for digit in data:
        t.insert(digit)
    return t


def runtime(size):
    start_time = time()
    tree = create_tree(test_data[:size])
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
    values = [3, 4, 2, 6, 4, 1, 3, 7, 8, 10, 50]
    t1 = create_tree(values)
    t1.del_node(3)
    t1.del_node(6)
    t1.insert(6)
    t1.del_node(7)
    t1.display(t1.root)
    # Drukowanie drzewa w porządku inorder (lewy, korzeń, prawy)
    t1.print_tree("inorder")   # Wydrukuje: 3 5 7 10 15 20
