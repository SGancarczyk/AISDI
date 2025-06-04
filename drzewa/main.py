import matplotlib.pyplot as plt
from bst_tree import create_tree
from avl_tree import AVL_create_tree
from benchmark import measure_time, bst_search, bst_delete, avl_search

sizes, bst_build, bst_search_t, bst_delete = measure_time(
    create_tree, bst_search, bst_delete)
_, avl_build, avl_search_t, _ = measure_time(AVL_create_tree, avl_search)

# Wykres tworzenia drzew
plt.figure(figsize=(10, 6))
plt.plot(sizes, bst_build, label='BST', marker='o')
plt.plot(sizes, avl_build, label='AVL', marker='s')
plt.title("Czas tworzenia drzew BST i AVL")
plt.xlabel("Rozmiar danych")
plt.ylabel("Czas (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("wykres_tworzenie.png")
plt.show()

# Wykres wyszukiwania w drzewach
plt.figure(figsize=(10, 6))
plt.plot(sizes, bst_search_t, label='BST', marker='o')
plt.plot(sizes, avl_search_t, label='AVL', marker='s')
plt.title("Czas wyszukiwania w drzewach BST i AVL")
plt.xlabel("Rozmiar danych")
plt.ylabel("Czas (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("wykres_wyszukiwanie.png")
plt.show()

# Wykres usuwania z drzew BST
plt.figure(figsize=(10, 6))
plt.plot(sizes, bst_delete, label='BST', marker='o')
plt.title("Czas usuwania w drzewie BST")
plt.xlabel("Rozmiar danych")
plt.ylabel("Czas (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("wykres_usuwanie.png")
plt.show()

print("\nWyświetlanie drzewa BST (dla 10 pierwszych elementów):")
bst_tree = create_tree(list(range(10)))
bst_tree.display(bst_tree.root)

print("\nWyświetlanie drzewa AVL (dla 10 pierwszych elementów):")
avl_tree = AVL_create_tree(list(range(10)))
avl_tree.display(avl_tree.root)
