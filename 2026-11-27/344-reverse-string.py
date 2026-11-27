# Reverse String
# https://leetcode.com/problems/reverse-string/
# LeetCode 344, Easy
# Submission: https://leetcode.com/submissions/detail/2204289699/
# Result: Accepted 477/477, 1 ms, 23.4 MB
# Date: 2026-11-27
#
# Idea: two pointers swapping from both ends, in place, O(1) extra space.

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
