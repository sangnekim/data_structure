class CircularLinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail == None

    def clear(self):
        self.tail = None

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node #node의 링크가 자신을 가리키도록 함
            self.tail = node #tail이 node를 가리기키도록 함
        else:
            node.link = self.tail.link #node의 링크가 front를 가리키도록함
            self.tail.link = node #tail의 링크가 node을 가리키도록 함
            self.tail = node #tail이 node를 가리키도록 함

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count

    def display(self, msg = 'CircularLinkedQueue:'):
        print(msg, end = '')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end = ' ')
                node = node.link
            print(node.data, end = ' ')
        print()
