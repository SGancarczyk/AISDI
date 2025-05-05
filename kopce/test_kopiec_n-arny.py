import pytest
from kopiec_n_arny import heap


def is_valid_heap(h: heap):
    n = len(h.nodes)
    for i in range(n):
        for k in range(1, h.arny + 1):
            child = h.arny * i + k
            if child < n:
                if h.nodes[i] < h.nodes[child]:
                    return False
    return True


def test_build_max_heap():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    h = heap(data, 2)  
    assert is_valid_heap(h)
    assert h.nodes[0] == 9


def test_add():
    h = heap([], 2)
    h.add(10)
    h.add(5)
    h.add(15)
    assert h.nodes[0] == 15
    assert is_valid_heap(h)


def test_pop_root():
    data = [10, 3, 15, 7, 2, 8, 12]
    h = heap(data, 2)
    original_size = len(h.nodes)
    max_element = h.nodes[0]
    h.pop_root()
    assert len(h.nodes) == original_size - 1
    assert is_valid_heap(h)
    assert max_element >= h.nodes[0]
