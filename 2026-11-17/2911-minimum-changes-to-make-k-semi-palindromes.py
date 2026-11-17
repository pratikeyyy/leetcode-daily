"""
LeetCode 2911. Minimum Changes to Make K Semi-palindromes — Hard
Daily Challenge: 2026-11-17
Problem: https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/description/?envType=daily-question&envId=2026-11-17
Submission: https://leetcode.com/submissions/detail/2197708187/
Result: Accepted 558/558 testcases, Runtime 3982 ms, Memory 19.5 MB
Solved by: pratikey (https://leetcode.com/u/pratikey/)

Approach: Precompute cost[i][j] = min changes to make s[i:j] a semi-palindrome,
trying every divisor d of the substring length and, for each residue class mod d,
counting mismatched mirror pairs. Then DP over partitions: dp[p][i] = min cost
to split s[:i] into p semi-palindromic parts.
"""

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # cost[i][j]: min changes to make s[i:j] a semi-palindrome
        cost = [[INF] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i + 2, n + 1):  # length >= 2 (len 1 has no valid divisor)
                L = j - i
                best = INF
                for d in range(1, L):
                    if L % d != 0:
                        continue
                    changes = 0
                    for r in range(d):
                        idx = list(range(i + r, j, d))
                        m = len(idx)
                        for t in range(m // 2):
                            if s[idx[t]] != s[idx[m - 1 - t]]:
                                changes += 1
                    best = min(best, changes)
                cost[i][j] = best

        # dp[p][i]: min cost to partition s[:i] into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(p * 2, n + 1):  # each part needs >= 2 chars
                for j in range((p - 1) * 2, i - 1):
                    if dp[p - 1][j] < INF and cost[j][i] < INF:
                        dp[p][i] = min(dp[p][i], dp[p - 1][j] + cost[j][i])
        return dp[k][n]
