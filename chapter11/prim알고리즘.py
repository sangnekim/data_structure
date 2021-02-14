INF = 9999
#현재 트리에 인접한 정점들 중에서 가장 가까운 정점을 찾는 함수
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

#Prim의 최소 비용 신장 트리 프로그램
def MSTPrim(vertex, adj):
    vsize = len(vertex)
    dist = [INF]*vsize
    selected = [False]*vsize
    dist[0] = 0

    for i in range(vsize):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end = ' ')
        for v in range(visze):
            if (adj[u][v] != None):
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

    print()
