# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy | Date: 2026-11-19
# Result: Accepted (492/492 testcases, 8 ms, 19.5 MB)
# Submission: https://leetcode.com/submissions/detail/2199038625/
# Note: Replacement problem for skipped 2914 (max 6 attempts reached 2026-11-19).
# Next unsolved slug from the sprint curated list (217, 242 already solved).

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome("0P") is False
    assert sol.isPalindrome("ab_a") is True
    print("125: all sample tests passed")
