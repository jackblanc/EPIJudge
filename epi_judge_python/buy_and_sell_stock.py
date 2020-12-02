from typing import List

from test_framework import generic_test

# [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] = 30

# Brute force, O(n^2)
# def buy_and_sell_stock_once(prices: List[float]) -> float:
#     maximum = float('-inf')
#     for i in range(len(prices)):
#         for j in range(i, len(prices)):
#             if prices[j] - prices[i] > maximum:
#                 maximum = prices[j] - prices[i]
#
#     return maximum


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
