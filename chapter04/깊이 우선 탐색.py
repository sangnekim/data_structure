def isValidPos(x,y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def DFS():
    stack = Stack()
    stack.push((0,1)) #시작위치 삽입
    print('DFS: ')

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end= '->')
        (x,y) = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.' #현재위치를 지나왔다고 '.'표시
            if isValidPos(x, y-1):
                stack.push((x,y-1)) #상
            if isValidPos(x, y+1):
                stack.push((x, y+1)) #하
            if isValidPos(x-1, y):
                stack.push((x-1, y)) #좌
            if isValidPos(x+1, y):
                stack.push((x+1, y)) #우
        print(' 현재 스택: ', stack)
    return False
