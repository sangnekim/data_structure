class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0) #0번 항목은 사용하지 않음

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def Parent(self,i):
        return self.heap[i//2]

    def Left(self, i):
        return self.heap[i*2]

    def Right(self, i):
        return self.heap[i*2 + 1]

    def display(self, msg = '힙 트리 '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size() #노드 n의 위치
        while (i != 1 and n > self.Parent(i)): #부모보다 큰 동안 계속 업힙
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1] # 삭제할 루트를 복사해 둠
            last = self.heap[self.size()] # 마지막 노드
            while (child <= self.size()): # 마지막 노드 이전까지
                #만약 오른쪽 노드가 더 크면 child를 1 증가(기본은 왼쪽 노드)
                if child < self.size() and self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child]: # 더 큰 자식이 더 작으면 삽입 위치 찾음. down-heap 종료
                    break
                self.heap[parent] = self.heap[child] #down-heap
                parent = child
                child *= 2

            self.heap[parent] = last #맨 마지막 노드를 parent 위치에 복사
            self.heap.pop(-1) #맨 마지막 노드 삭제
            return hroot
