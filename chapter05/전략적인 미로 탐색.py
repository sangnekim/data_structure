import math
(ox,oy) = (5,4) #출구의 위치

#거리(d)를 계산하기 위한 함수
def dist(x,y):
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)

#거리에 따라 우선순위를 정하므로 상속받아서 오버라이딩
class PriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__()

    def findMaxIndex(self): #오버라이딩
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i][2] > self.items[highest][2]:
                    highest = i
            return highest

def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1, -dist(0,1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end = '->')
        x,y,_ = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1):
                q.enqueue((x,y-1, -dist(x,y-1)))
            if isValidPos(x, y+1):
                q.enqueue((x,y+1, -dist(x,y+1)))
            if isValidPos(x-1, y):
                q.enqueue((x-1,y, -dist(x-1,y)))
            if isValidPos(x+1, y):
                q.enqueue((x+1,y, -dist(x+1,y)))
        print('우선순위큐: ', q.items)
    return False
