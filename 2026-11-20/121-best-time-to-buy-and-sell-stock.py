# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy | Date: 2026-11-20
# Result: Accepted (213/213 testcases, 19 ms, 28.5 MB)
# Submission: https://leetcode.com/submissions/detail/2199717210/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > best:
                best = p - min_price
        return best
