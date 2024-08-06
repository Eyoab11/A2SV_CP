#92. Reverse Linked List II

# Partially done by myself got a little help from YouTube
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        for i in range(left - 1):
            prev = cur
            cur = cur.next
        
        prevNode = None
        for j in range(right - left + 1):
            node = cur.next
            cur.next = prevNode
            prevNode = cur
            cur = node
        prev.next.next = cur
        prev.next = prevNode
        return dummy.next
        

