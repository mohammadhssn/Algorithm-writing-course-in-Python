"""
    Link: https://github.com/keon/algorithms/blob/master/algorithms/search/linear_search.py

    [1, 3, 5, 23, 34, 54, 55] , 23 => 3
"""


def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i

    return -1


print(linear_search([1, 3, 5, 23, 34, 54, 55], 23))
