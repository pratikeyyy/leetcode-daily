# 3041. Maximize Consecutive Elements in an Array After Modification
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/
# Difficulty: Hard | Date: 2026-11-20
# Result: Accepted (668/668 testcases, 652 ms, 59.8 MB)
# Submission: https://leetcode.com/submissions/detail/2199717166/
from typing import List
from collections import Counter

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        vals = sorted(set(cnt) | {x + 1 for x in cnt})
        NEG = -10 ** 9
        A = {}  # longest chain ending at v, last element is value v used as-is
        B = {}  # longest chain ending at v, last element is value v-1 bumped to v
        ans = 0
        for v in vals:
            if cnt.get(v, 0) >= 1:
                prev = max(A.get(v - 1, NEG), B.get(v - 1, NEG))
                A[v] = prev + 1 if prev > NEG // 2 else 1
            if cnt.get(v - 1, 0) >= 1:
                bv = 1  # single bumped element forms chain [v]
                if cnt.get(v - 1, 0) >= 2 and A.get(v - 1, NEG) > NEG // 2:
                    bv = max(bv, A[v - 1] + 1)  # spare v-1 element
                if B.get(v - 1, NEG) > NEG // 2:
                    bv = max(bv, B[v - 1] + 1)  # chain ending at v-1 used no v-1 element
                B[v] = bv
            ans = max(ans, A.get(v, 0), B.get(v, 0))
        return ans
