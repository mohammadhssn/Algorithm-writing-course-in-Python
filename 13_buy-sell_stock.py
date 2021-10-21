"""
    buy-sell stock
        [7, 1, 5, 3, 6, 4] = 5
        [8, 5, 4, 3, 2, 1] = 0
"""


def max_profit(prices):
    cur_max, max_so_dar = 0, 0
    for i in range(1, len(prices)):                             # 1 2 3 4 5
        cur_max = max(0, cur_max + prices[i] - prices[i - 1])   # 0 // 4 // 2 // 5 // 3
        max_so_dar = max(max_so_dar, cur_max)                   # 4 // 4 // 5 // 5
    return max_so_dar


print(max_profit([8, 5, 4, 3, 2, 1]))
