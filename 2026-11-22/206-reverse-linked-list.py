# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy | Date: 2026-11-22
# Result: Accepted (28/28 testcases, 0 ms, 20.3 MB)
# Submission: https://leetcode.com/submissions/detail/2201008101/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
