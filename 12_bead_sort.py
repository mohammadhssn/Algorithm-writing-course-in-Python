"""
    Link: https://github.com/TheAlgorithms/Python/blob/master/sorts/bead_sort.py

        [1, 5, 77, 43, 2, 3, 55] => [1, 2, 3, 4, 43, 55, 77]
        1(1, 5)  2(5, 77)  3(77, 43)
                            77 -= 77 -43
                            43 +=  77 - 43
"""


def bead_sort(sequence):
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("Sequence must be list of non-negative integers")

    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower

    return sequence


print(bead_sort([1, 5, 77, 43, 2, 3, 55]))
