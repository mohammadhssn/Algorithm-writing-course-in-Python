"""
    linear Time  O(n)

    note:
        dar in algorithm har che tedade voroody ziyad beshe tedade Operation ha ham ziyad mishe.
"""

nums = [1, 34, 556, 2, 45, 5, 67, 22]


def show(lst):  # bozorg tarin add dakhel list
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i
    return max_num


print(show(nums))
