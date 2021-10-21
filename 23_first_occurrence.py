"""
    Link: https://github.com/keon/algorithms/blob/master/algorithms/search/first_occurrence.py

    [2, 2, 3, 3, 3, 4, 5], 3 => 2
"""


def first_occurrence(array, element):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if low == mid:
            break
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid

    if array[low] == element:
        return low


print(first_occurrence([2, 2, 3, 3, 3, 4, 5], 3))
