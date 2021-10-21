"""
    polynomial Time    O(n^n)

    note:
        mesle algorithm bubble sort O(n^2)
"""

num = [12, 2, 4, 67, 24, 56, 55]


def bubble_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped:
            break
    return lst


print(bubble_sort(num))
