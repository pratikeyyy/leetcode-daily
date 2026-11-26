# 169. Majority Element
# https://leetcode.com/problems/majority-element/
# Result: Accepted 59/59, 10 ms, 21.4 MB
# Submission: https://leetcode.com/submissions/detail/2204030372/
# Date: 2026-11-26
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Boyer-Moore voting algorithm
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert s.majorityElement([1]) == 1
    print("All samples pass")
