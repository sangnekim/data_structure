class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def clear(self):
        self.front = self.rear = None

    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count

    def display(self, msg = 'DoublyLinkedDeque:'):
        print(msg, end = '')
        node = self.front
        while not node == None:
            print(node.data, end = ' ')
            node = node.next
        print()

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next #front를 다음 노드로 옮김
            if self.front == None: #노드가 하나뿐
                self.rear = None #rear도 None
            else:
                self.front.prev = None #front의 이전노드 None으로 변경
            return data
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data
