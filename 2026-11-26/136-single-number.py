# 136. Single Number
# https://leetcode.com/problems/single-number/
# Result: Accepted 61/61, 1 ms, 21.3 MB
# Submission: https://leetcode.com/submissions/detail/2203831300/
# Date: 2026-11-26
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result
