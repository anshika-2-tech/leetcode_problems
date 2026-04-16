class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [0] * k
        self.k = k
        self.front = 0
        self.rear = -1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.front = (self.front - 1) % self.k
        self.q[self.front] = value
        
        if self.count == 0:
            self.rear = self.front
        
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        
        if self.count == 0:
            self.front = self.rear
        
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.rear = (self.rear - 1) % self.k
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k





