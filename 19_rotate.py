"""
    rotate('hello', 2) => llohe
    rotate('hello', 5) => hello
    rotate('hello', 7) => llohe
"""


def rotate(s, k):
    double_s = s + s  # hellohello
    if k <= len(s):  # k = 2
        return double_s[k: k + len(s)]  # 2:7
    else:  # k = 7
        return double_s[k - len(s): k]  # 2:7


print(rotate('hello', 7))
