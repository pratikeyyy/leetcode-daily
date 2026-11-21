# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Difficulty: Easy | Date: 2026-11-21
# Result: Accepted (210/210 testcases, 18 ms, 31.1 MB)
# Submission: https://leetcode.com/submissions/detail/2200309747/
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for x in nums[1:]:
            cur = x if cur < 0 else cur + x
            if cur > best:
                best = cur
        return best


