# 2124. Check if All A's Appears Before All B's
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Difficulty: Easy | Date: 2026-11-22
# Result: Accepted (216/216 testcases, 0 ms, 19.1 MB)
# Submission: https://leetcode.com/submissions/detail/2201007884/

class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s
