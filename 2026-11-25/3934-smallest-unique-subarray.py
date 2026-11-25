# 3934. Smallest Unique Subarray
# https://leetcode.com/problems/smallest-unique-subarray/
# Result: Accepted 719/719, 2208 ms, 39.8 MB
# Submission: https://leetcode.com/submissions/detail/2202956788/
# Date: 2026-11-25
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MASK = (1 << 64) - 1
        B = 9113823

        def exists_unique(L: int) -> bool:
            # 64-bit polynomial rolling hash; count occurrences of every
            # length-L subarray. Unique exists iff some hash occurs once.
            powB = pow(B, L - 1, 1 << 64)
            h = 0
            for i in range(L):
                h = ((h * B) + nums[i] + 1007) & MASK
            cnt = {h: 1}
            for i in range(1, n - L + 1):
                h = ((h - (nums[i - 1] + 1007) * powB) * B
                     + nums[i + L - 1] + 1007) & MASK
                c = cnt.get(h)
                if c is None:
                    cnt[h] = 1
                elif c == 1:
                    cnt[h] = 2
            return any(v == 1 for v in cnt.values())

        # Monotone: any extension of a unique subarray is unique, so the
        # predicate "a unique subarray of length L exists" is monotone in L.
        lo, hi, ans = 1, n, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if exists_unique(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
