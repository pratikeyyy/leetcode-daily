# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy | Date: 2026-11-23
# Result: Accepted (29/29 testcases, 49 ms, 22.6 MB)
# Submission: https://leetcode.com/submissions/detail/2201631716/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's tortoise and hare: if the fast pointer ever meets
        # the slow one, the list has a cycle.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
