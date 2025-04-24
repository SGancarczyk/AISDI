from binary_search_tree import create_tree, is_valid, insert, search, del_node
import pytest


def test_create_tree():
    values = [3,4,2,6,4,1,3,7,8]
    t1 = create_tree(len(values), values)
    assert t1.key == 3
    assert t1.left.key == 2
    assert t1.right.key == 4


def test_is_valid():
    values = [3,4,2,6,4,1,3,7,8]
    t1 = create_tree(len(values), values)
    assert is_valid(t1)


def test_is_valid_false():
    values = [3,4,2,6,4,1,3,7,8]
    t1 = create_tree(len(values), values)
    t1.left.key = 0
    assert not is_valid(t1)


def test_search():
    values = [3,4,2,6,4,1,3,7,8]
    t1 = create_tree(len(values), values)
    assert search(t1, 6)
    assert search(t1, 8)
    assert not search(t1, 10)


def test_insert():
    values = [3,4,2,6,4,1,3,7,8]
    t1 = create_tree(len(values), values)
    insert(t1, 10)
    assert search(t1, 10)
    assert is_valid(t1)


def test_del():
    values = [3,4,2,6,4,1,3,7,8]
    t1 = create_tree(len(values), values)
    del_node(t1, 1)
    del_node(t1, 3)
    assert not search(t1, 1)
    assert not search(t1, 3)
    assert is_valid(t1)
    