"""
LeetCode 217. Contains Duplicate — Easy
Date: 2026-11-17 (Sprint extra problem)
Problem: https://leetcode.com/problems/contains-duplicate/
Submission: https://leetcode.com/submissions/detail/2197708516/
Result: Accepted 80/80 testcases, Runtime 10 ms, Memory 33.3 MB
Solved by: pratikey (https://leetcode.com/u/pratikey/)

Approach: A duplicate exists iff the set of nums is smaller than the list.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
