"""
    link: https://github.com/keon/algorithms/blob/master/algorithms/arrays/top_1.py

    arr = [1, 2, 3, 3, 3, 4, 5] => [3]

    note:
        adade  bishtarin tekrar ro bar migardoone
"""


def top_1(arr):
    values = {}  # adad va tekraresh ro zakhire mikonim
    result = []  # add bishtarin tekrar
    f_val = 0    # meghdare bishtarin tekrar

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    f_val = max(values.values())

    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue

    return result


print(top_1([1, 2, 3, 3, 3, 4, 5]))
