INF = 9999
#최소 dist 정점을 찾는 함수
def choose_vertex(dist, found):
    min = INF
    minpos = -1
    for i in range(len(dist)): #모든 정점 중에서
        if dist[i] < min and found[i] == False: #방문하지 않은 최소 dist 정점
            min = dist[i]
            minpos = i
    return minpos # 최소 dist 정점의 인덱스 반환

def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx) # 정점의 수
    dist = list(adj[start]) #dist 배열 생성 및 초기화
    path = [start] * vsize #path 배열 생성 및 초기화
    found = [False] * vsize #found 배열 생성 및 초기화
    found[start] = True #시작정점: 이미 찾아짐
    dist[start] = 0 #시작정점의 거리: 0

    for i in range(vsize):
        print('Step%2d: '%(i+1), dist) #단계별 dist[]출력용
        u = choose_vertex(dist, found) #최소 dist 정점 u 탐색
        found[u] = True

        for w in range(vsize): #모든 정점에 대해
            if not found[w]: # 아직 찾아지지 않았으면
                if dist[u] + adj[u][w] < dist[w]: #갱신 조건 검사
                    dist[w] = dist[u] + adj[u][w] #dist 갱신
                    path[w] = u #이전 정점 갱신

    return path #찾아진 최단 경로 반환
