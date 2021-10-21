"""
    Link: https://github.com/keon/algorithms/blob/master/algorithms/search/search_range.py

    [5,7,7,8,8,8,10], target = 8
    Output: [3,5]

    [5,7,7,8,8,8,10], target = 11
    Output: [None, None]

    [5,7,7,8,8,8,10], target = 10
"""


def search_range(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            break

    for j in range(len(nums) - 1, - 1, - 1):
        if target == nums[j]:
            return [mid, j]
    return [None, None]


print(search_range([5, 7, 7, 8, 8, 8, 10], 7))
