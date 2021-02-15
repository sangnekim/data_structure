INF = 9999
def printA(A): #현재의 A행렬을 화면에 출력하는 함수
    vsize = len(A)
    print('======================================')
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF):
                print('INF', end = '')
            else:
                print("%4d"%A[i][j], end = '')
        print("")

def shortest_path_floyd(vertex, adj):
    vsize = len(vertex) #정점의 개수
    A = list(adj) #2차원 배열의 복사
    for i in range(vsize):
        A[i] = list(adj[i])

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
        printA(A)
