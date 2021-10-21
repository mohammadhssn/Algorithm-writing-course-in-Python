"""
    [1, 44, 556, -14, 5, 0, 2, -5] => -14
"""


def remove_min(stack):
    storage_stack = []
    if len(stack) == 0:
        return stack

    min = stack.pop()  # -5
    stack.append(min)  # [1, 44, 556, -4, 5, 0, 2, -5]

    for i in range(len(stack)):
        val = stack.pop()
        if val < min:
            min = val
        storage_stack.append(val)

    for i in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != min:
            stack.append(val)

    return stack, min


print(remove_min([1, 44, 556, -14, 5, 0, 2, -5]))
