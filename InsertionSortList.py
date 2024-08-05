#147. Insertion Sort List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        prev = head
        cur = head.next

        while cur:
            if prev.val <= cur.val:
                prev = cur
                cur = cur.next
                continue
            
            node = dummyNode
            while cur.val > node.next.val:
                node = node.next
            prev.next = cur.next
            cur.next = node.next
            node.next = cur
            cur = prev.next
        return dummyNode.next

        


