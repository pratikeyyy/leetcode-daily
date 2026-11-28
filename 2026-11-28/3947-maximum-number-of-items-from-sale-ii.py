# Maximum Number of Items From Sale II
# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/
# LeetCode 3947 (Daily Challenge 2026-11-28), Medium
# Submission: https://leetcode.com/submissions/detail/2204888944/
# Result: Accepted 875/875, 265 ms, 58.5 MB
# Date: 2026-11-28
#
# Idea: buying k_i copies of item i gives min(k_i, d_i) free copies, where
# d_i = number of other items j with factor_i dividing factor_j (each pair
# (i, j) gives at most one free copy, and different i's don't interfere).
# So total = sum_i (k_i + min(k_i, d_i)): the first d_i copies of item i are
# worth 2 each, further copies worth 1 each. Extra copies beyond d_i are
# best bought as the cheapest item. Take the "doubled" slots in increasing
# price order while price < 2 * cheapest price (each such slot never hurts
# the total), then spend the rest on cheapest singles.

from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        maxf = max(f for f, _ in items)
        cnt = [0] * (maxf + 1)
        for f, _ in items:
            cnt[f] += 1
        # total[f] = number of items whose factor is a multiple of f
        total = [0] * (maxf + 1)
        for f in range(1, maxf + 1):
            s = 0
            for m in range(f, maxf + 1, f):
                s += cnt[m]
            total[f] = s
        p_min = min(p for _, p in items)
        slots = {}
        for f, p in items:
            d = total[f] - 1
            if d > 0:
                slots[p] = slots.get(p, 0) + d
        cost = 0
        doubled = 0
        limit = 2 * p_min
        for p in sorted(slots):
            if p >= limit:
                break
            take = min(slots[p], (budget - cost) // p)
            doubled += take
            cost += take * p
            if cost == budget:
                break
        return 2 * doubled + (budget - cost) // p_min
