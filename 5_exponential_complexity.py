"""
    exponential Time   O(n^n)

    note:
        dar in algorithm tamame halat ejra mishan,
        dar in algorithm dar ejraye badi 2 barabar zaman tool mikeshe.  algorithm subsets O(3^n)
"""

from itertools import chain, combinations


def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


print(list(subsets(['a', 'b', 'c'])))
