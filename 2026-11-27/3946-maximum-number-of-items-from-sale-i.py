# Maximum Number of Items From Sale I
# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/
# LeetCode 3946 (Daily Challenge 2026-11-27), Medium
# Submission: https://leetcode.com/submissions/detail/2204289574/
# Result: Accepted 764/764, 1490 ms, 19.7 MB
# Date: 2026-11-27
#
# Idea: for a set S of item types bought at least once, free copies are
# sum of g(i) over i in S, where g(i) counts j != i with factor_i | factor_j.
# Leftover budget is best spent on extra copies of the cheapest item.
# So total(S) = sum_{i in S} (1 + g(i)) + (budget - price(S)) // p_min.
# Maximise sum of values with a 0/1 knapsack DP over total price.

from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        factors = [f for f, _ in items]
        prices = [p for _, p in items]

        # g(i): number of j != i such that factor_i divides factor_j
        g = [0] * n
        for i in range(n):
            fi = factors[i]
            cnt = 0
            for j in range(n):
                if j != i and factors[j] % fi == 0:
                    cnt += 1
            g[i] = cnt

        p_min = min(prices)
        NEG = -10 ** 9
        dp = [NEG] * (budget + 1)
        dp[0] = 0
        for i in range(n):
            v = 1 + g[i]
            c = prices[i]
            for spent in range(budget, c - 1, -1):
                if dp[spent - c] != NEG:
                    if dp[spent - c] + v > dp[spent]:
                        dp[spent] = dp[spent - c] + v

        ans = 0
        for spent in range(budget + 1):
            if dp[spent] != NEG:
                total = dp[spent] + (budget - spent) // p_min
                if total > ans:
                    ans = total
        return ans
