# 3331. Find Subtree Sizes After Changes
# https://leetcode.com/problems/find-subtree-sizes-after-changes/
# Difficulty: Medium | Date: 2026-11-21
# Result: Accepted (632/632 testcases, 1001 ms, 60.2 MB)
# Submission: https://leetcode.com/submissions/detail/2200309647/
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = [-1] * n
        last = {}  # char -> nearest ancestor node with that char on current path
        # stack entries: (node, entering, prev_last_for_this_char)
        stack = [(0, True, None)]
        while stack:
            node, entering, prev = stack.pop()
            c = s[node]
            if entering:
                old = last.get(c)
                if node != 0 and old is not None:
                    new_parent[node] = old
                else:
                    new_parent[node] = parent[node]
                last[c] = node
                stack.append((node, False, old))
                for ch in reversed(children[node]):
                    stack.append((ch, True, None))
            else:
                if prev is None:
                    last.pop(c, None)
                else:
                    last[c] = prev

        # build final tree and compute subtree sizes (iterative post-order)
        fchildren = [[] for _ in range(n)]
        for i in range(1, n):
            fchildren[new_parent[i]].append(i)
        size = [1] * n
        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            for ch in fchildren[node]:
                stack.append(ch)
        for node in reversed(order):
            for ch in fchildren[node]:
                size[node] += size[ch]
        return size
