# 1352. Product of the Last K Numbers
# https://leetcode.com/problems/product-of-the-last-k-numbers/
# Difficulty: Medium | Date: 2026-11-23
# Result: Accepted (35/35 testcases, 116 ms, 33.8 MB)
# Submission: https://leetcode.com/submissions/detail/2201631623/
    def __init__(self):
        # prefix[i] = product of all numbers added since the last zero
        # (prefix[0] = 1 is a sentinel so division works).
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # A zero wipes every product that includes it; restart.
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            # The last k numbers include a zero.
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]
