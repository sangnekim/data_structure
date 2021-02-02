class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg = 'LinkedList: '):
        print(msg, end = '')
        node = self.head
        while not node == None:
            print(node.data, end = ' ')
            node = node.link
        print()

    def getNode(self, pos): # pos번째 노드 반환
        if pos < 0:
            return None
        node = self.head #node는 head부터 시작
        while pos > 0 and node != None: # pos번 반복
            node = node.link # node를 다음 노드로 이동
            pos -=1 #남은 반복 횟수 줄임
        return node #최종 노드 반환

    def getEntry(self, pos): # pos번째 노드의 데이터 반환
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def replace(self, pos, elem): # pos번째 노드의 데이터를 변경
        node = self.getNode(pos)
        if node != None:
            node.data = elem

    def find(self, data): # 데이터로 data를 갖는 노드 반환
        node = self.head
        while node is not None: #모든 노드에서 찾음
            if node.data == data: #찾아지면 바로 반환
                return node
            node = node.link
        return node #찾아지지 않으면 None 반환

    def insert(self, pos, elem):
        before = self.getNode(pos - 1) # before 노드를 찾음
        if before == None:
            self.head = Node(elem, self.head) #맨 앞에 삽입함
        else:
            node = Node(elem, before.link) # 노드 생성 + 새로운 노드가 before 다음 노드를 가리키게 함
            before.link = node #before노드가 새로운 노드를 가리키게 함

    def delete(self, pos):
        before = self.getNode(pos - 1) # before 노드를 찾음
        if before == None:
            if self.head is not None: #공백이 아니면
                self.head = self.head.link # head를 다음으로 이동
        elif before.link != None: #중간에 있는 노드 삭제
            before.link = before.link.link # before이 다음 다음 노드를 가리키게 함
