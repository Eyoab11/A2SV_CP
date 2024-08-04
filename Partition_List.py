86. Partition List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = ListNode(), ListNode()
        lefttail, righttail= left, right

        while head:
            if head.val < x:
                lefttail.next = head
                lefttail = lefttail.next
            else:
                righttail.next = head
                righttail = righttail.next
            head = head.next
        lefttail.next = right.next
        righttail.next = None
        return left.next




         
