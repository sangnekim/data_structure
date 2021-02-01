def isValidPos(x,y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def BFS():
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS: ')

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end = '->')
        x,y = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] ='.'
            if isValidPos(x, y-1):
                que.enqueue((x, y-1)) #상
            if isValidPos(x, y+1):
                que.enqueue((x, y+1)) #하
            if isValidPos(x-1, y):
                que.enqueue((x-1, y)) #좌
            if isValidPos(x+1, y):
                que.enqueue((x+1, y)) #우
    return False
