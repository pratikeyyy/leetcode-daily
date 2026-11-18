# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy | Date: 2026-11-18
# Result: Accepted (56/56 testcases, 5 ms, 19.4 MB)
# Submission: https://leetcode.com/submissions/detail/2198500445/

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagram("a", "a") is True
    assert sol.isAnagram("ab", "a") is False
    print("242: all sample tests passed")
