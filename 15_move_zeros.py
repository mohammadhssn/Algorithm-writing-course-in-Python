"""
    Link: https://github.com/keon/algorithms/blob/master/algorithms/arrays/move_zeros.py

    [1, 3, 0, False, 0, 'b', 44, 67] => [1, 3, False, 'b', 44, 67, 0 ,0]
"""


def move_zeros(seq):
    result = []
    zeros = 0

    for i in seq:
        if i == 0 and type(i) != bool:
            zeros += 1
        else:
            result.append(i)
    result.extend([0] * zeros)
    return result


print(move_zeros([1, 3, 0, False, 0, 'b', 44, 67]))
