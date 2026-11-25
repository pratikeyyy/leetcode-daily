# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Result: Accepted 80/80, 16 ms, 33.1 MB (already solved before sprint; re-submitted, count unchanged)
# Submission: https://leetcode.com/submissions/detail/2202956897/
# Date: 2026-11-25
from typing import List


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
