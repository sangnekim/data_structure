class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None #공백상태 검사

    def clear(self):
        self.top = None #스택 초기화

    def push(self, item):
        n = Node(item, self.top) #새로운 노드 n을 생성한 후 n의 링크가 시작노드(top)을 가리키게 함
        self.top = n #시작노드(top)이 n을 가리키게 함

    def pop(self):
        if not self.isEmpty():
            n = self.top #변수 n이 시작노드를 가키리도록 함
            self.top = n.link #top이 다음노드를 가리키도록 함
            return n.data #n이 가리키는 노드의 데이터를 반환

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def size(self):
        node = self.top #시작 노드
        count = 0
        while not node == None:
            node = node.link #다음 노드로 이동
            count += 1 #count 증가
        return count

    def display(self, msg = 'LinkedStack: '):
        print(msg, end = '')
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()
