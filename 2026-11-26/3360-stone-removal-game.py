# 3360. Stone Removal Game
# https://leetcode.com/problems/stone-removal-game/
# Result: Accepted 53/53, 0 ms, 19.1 MB
# Submission: https://leetcode.com/submissions/detail/2203607035/
# Date: 2026-11-26
class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        alice_turn = True
        while n >= take:
            n -= take
            take -= 1
            alice_turn = not alice_turn
        # player whose turn it is cannot move and loses
        return not alice_turn
