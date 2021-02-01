class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1 #반시계 방향으로 회전
            if self.front < 0:
                self.front = MAX_QSIZE -1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear-1 #반시계 방향으로 회전
            if self.rear < 0:
                self.rear = MAX_QSIZE - 1
            return item

    def getRear(self):
        return self.items[self.rear]
