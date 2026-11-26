# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Result: Accepted 75/75, 3 ms, 20.4 MB
# Submission: https://leetcode.com/submissions/detail/2204120871/
# Date: 2026-11-26
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Two pointers: j tracks where the next non-zero goes.
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0], nums
    nums = [0]
    s.moveZeroes(nums)
    assert nums == [0], nums
    nums = [1, 2, 3]
    s.moveZeroes(nums)
    assert nums == [1, 2, 3], nums
    nums = [0, 0, 1]
    s.moveZeroes(nums)
    assert nums == [1, 0, 0], nums
    print("All samples pass")
