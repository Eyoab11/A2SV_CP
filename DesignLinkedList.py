#707. Design Linked List
class LinkedList:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = LinkedList(0)
        self.right = LinkedList(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1 

        

    def addAtHead(self, val: int) -> None:
        node, next, prev = LinkedList(val), self.left.next, self.left
        prev.next , next.prev = node, node
        
        node.next, node.prev = next, prev
        

    def addAtTail(self, val: int) -> None:
        node, next, prev = LinkedList(val), self.right , self.right.prev
        prev.next , next.prev = node, node
        
        node.next, node.prev = next, prev
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, next, prev = LinkedList(val), cur, cur.prev
            prev.next, next.prev = node, node
            node.next, node.prev = next, prev

        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0 and cur != self.right:
            next, prev = cur.next, cur.prev
            prev.next, next.prev = next, prev
            

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
