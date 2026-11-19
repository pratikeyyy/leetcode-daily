# 2567. Minimum Score by Changing Two Elements
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Result: Accepted 70/70, 38 ms, 31.1 MB | Submission: https://leetcode.com/submissions/detail/2199068496/
# Date: 2026-11-19
from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # Change 2 smallest, 2 largest, or 1 smallest + 1 largest
        return min(
            nums[-1] - nums[2],
            nums[-3] - nums[0],
            nums[-2] - nums[1],
        )
