# 3411. Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/
# Result: Accepted 865/865, 32 ms, 19.2 MB
# Submission: https://leetcode.com/submissions/detail/2202300672/
# Date: 2026-11-24
from math import gcd
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if prod == l * g:
                    ans = max(ans, j - i + 1)
        return ans
