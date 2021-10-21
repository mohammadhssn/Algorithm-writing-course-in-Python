"""
    Link: https://github.com/TheAlgorithms/Python/blob/master/maths/two_sum.py

    two_sum([2, 7, 11, 15], 9)
    [0, 1]

    two_sum([2, 7, 11, 15], 17)
    [0, 3]
"""


def tow_sum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1
    while p1 < p2:
        s = numbers[p1] + numbers[p2]
        if s == target:
            return p1, p2
        elif s > target:
            p2 = p2 - 1
        else:
            p1 = p1 - 1


print(tow_sum([2, 7, 11, 15], 17))
