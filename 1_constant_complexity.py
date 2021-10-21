"""
    constant Time  O(1)

    note:
        (Tedade voorody tasiry dar ejraye algorithm nadarad)
"""

nums = [1, 345, 56, 24354, 545645, 232, 454, 6, 786]


def show(list):
    if list[0] % 2 == 0:
        return f'{list[0]}Even'
    return 'Odd'


print(show(nums))
