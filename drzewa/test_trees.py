import pytest
from bst_tree import Tree, create_tree, is_valid # noqa
from avl_tree import TreeAVL, AVL_create_tree # noqa


@pytest.fixture
def sample_data():
    return [20, 4, 15, 70, 50, 100]


def test_bst_insert_and_search(sample_data):
    tree = create_tree(sample_data)
    for val in sample_data:
        assert tree.search(val) is not None
    assert tree.search(999) is None


def test_bst_delete(sample_data):
    tree = create_tree(sample_data)
    tree.del_node(70)
    assert tree.search(70) is None


def test_bst_validity(sample_data):
    tree = create_tree(sample_data)
    assert is_valid(tree.root)


def test_avl_insert_and_search(sample_data):
    avl = AVL_create_tree(sample_data)
    inorder = avl.inorder()
    for val in sample_data:
        assert val in inorder


def test_avl_delete(sample_data):
    avl = AVL_create_tree(sample_data)
    avl.delete(70)
    assert 70 not in avl.inorder()
