# Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/
# LeetCode 412, Easy
# Submission: https://leetcode.com/submissions/detail/2204889023/
# Result: Accepted 8/8, 0 ms, 19.5 MB
# Date: 2026-11-28
#
# Idea: count 1..n; multiples of 15 -> "FizzBuzz", of 3 -> "Fizz",
# of 5 -> "Buzz", else the number itself.

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
