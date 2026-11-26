# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Result: Accepted 77/77, 0 ms, 19.1 MB
# Submission: https://leetcode.com/submissions/detail/2203607813/
# Date: 2026-11-26
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
