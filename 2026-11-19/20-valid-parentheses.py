# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Result: Accepted 103/103, 1 ms, 19.4 MB | Submission: https://leetcode.com/submissions/detail/2199068575/
# Date: 2026-11-19

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
