# Problem: Add Two Numbers
# URL: https://leetcode.com/problems/add-two-numbers/
#
# Problem outline:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get the overflow (tens digit) and quotient (ones digit) of the sum of the two one digits
        overflow, quotient = divmod(l1.val + l2.val, 10)
        head_node = ListNode(quotient)
        current_node = head_node

        l1 = l1.next
        l2 = l2.next

        # iterate till end of both numbers
        while not (l1 is None and l2 is None):
            first = l1 if l1 is not None else ListNode()
            second = l2 if l2 is not None else ListNode()
            overflow, quotient = divmod(first.val + second.val + overflow, 10)
            new_node = ListNode(quotient)
            current_node.next = new_node
            current_node = new_node
            l1 = first.next
            l2 = second.next

        # to append 1 if there is still an overflow
        if overflow == 1:
            current_node.next = ListNode(1)

        return head_node