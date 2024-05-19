#641. Design Circular Deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.deque = [0] * k
        self.front = 0
        self.rear = 0
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.size
        self.deque[self.front] = value
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.size
        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size
