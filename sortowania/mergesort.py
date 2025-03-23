import random
lst = [random.randint(1, 100) for i in range(100)]


def merge(lst1, lst2):
    # Merges two sorted(asc) lists
    merged_lst = []
    while len(lst1) and len(lst2):  # The loop ends at the end of one of the lists
        if lst1[0] < lst2[0]:
            merged_lst.append(lst1[0])  # Appending smaller item to merged list
            lst1.pop(0)  # Removing sorted item from original list
        else:
            merged_lst.append(lst2[0])
            lst2.pop(0)
    merged_lst.extend(lst1)  # Extending merged list with sorted list(one is empty)
    merged_lst.extend(lst2)
    return merged_lst


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        # calling merge and merge_sort function recursively
        # splitting given list to single element lists(sorted)
        # then merging them
        return merge(merge_sort(lst[:len(lst)//2]), merge_sort(lst[len(lst)//2:]))


print(merge_sort(lst))