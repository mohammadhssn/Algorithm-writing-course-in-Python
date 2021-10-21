"""
    Link: https://github.com/keon/algorithms/blob/master/algorithms/search/search_insert.py

    search insert
    [1, 2, 3, 4] --- 3 => 2
    [1, 2, 3, 4] --- 4 => 3
    [1, 2, 3, 4] --- 0 => 0
"""


def search_insert(arr, val):
    low = 0                 # 0
    high = len(arr) - 1     # 3
    mid = high // 2         # 3 / 2 = 1

    while low <= high:      # 0 <= 3 -- 2 <= 3 -- 3 <= 3 -- 3 <= 3 -- 3 <= 2
        if val > arr[mid]:  # 4 > 2  -- 4 > 3  -- 4 > 4  -- 4 > 4
            mid += 1        # mid 2  -- mid 3
            low = mid       # low 2  -- low 3
        else:
            mid -= 1        # mid 3 -- 2
            high = mid      # high 3 -- 2

    return low      # 2


print(search_insert([1, 2, 3, 4], 4))