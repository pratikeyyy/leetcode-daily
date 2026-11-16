"""
LeetCode 2243. Calculate Digit Sum of a String — Easy
Daily Challenge: 2026-11-16
Problem: https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/?envType=daily-question&envId=2026-11-16
Submission: https://leetcode.com/problems/calculate-digit-sum-of-a-string/submissions/2197161757/?envType=daily-question&envId=2026-11-16
Result: Accepted 121/121 testcases, Runtime 0 ms (Beats 100%), Memory 19.15 MB (Beats 79.32%)
Solved by: pratikey (https://leetcode.com/u/pratikey/)

Approach: Repeatedly split s into groups of size k, replace each group by the sum of its digits, and continue until len(s) <= k.
"""

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        return s if len(s) <= k else self.digitSum("".join(str(sum(int(c) for c in s[i:i+k])) for i in range(0, len(s), k)), k)
