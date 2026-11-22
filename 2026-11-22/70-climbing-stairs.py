# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy | Date: 2026-11-22
# Result: Accepted (45/45 testcases, 0 ms, 19.2 MB)
# Submission: https://leetcode.com/submissions/detail/2201090498/

class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci-style DP: ways(n) = ways(n-1) + ways(n-2)
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
