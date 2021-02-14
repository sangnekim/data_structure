# 그래프의 모든 정점에 대해 부모 노드의 인덱스를 저장하기 위해 전역변수로 사용
parent = []
set_size = 0

def init_set(nSets):
    global set_size, parent
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)

def find(id):
    while (parent[id] >= 0):
        id = parent[id]
    return id

def union(s1, s2):
    global set_size
    parent[s1] = s2
    set_size = set_size -1

#kruskal의 최소 비용 신장 트리 프로그램
def MSTkruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = []

    for i in range(vsize - 1): #모든 간선을 리스트에 넣음
        for j in range(i+1, vsize):
            if adj[i][j] != None:
                eList.append((i,j,adj[i][j]))

    #간선 리스트를 가중치의 내림차순으로 정렬
    eList.sort(key = lambda e: e[2], reverse= True)

    edgeAccepted = 0
    while edgeAccepted < vsize - 1:
        e = eList.pop(-1) #가장 작은 가중치를 가진 간선
        uset = find(e[0]) #두 정점이 속한 집합 번호
        vset = find(e[1])

        if uset != vset:
            print('간선 추가: (%s,%s,%d)'%(vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            edgeAccepted += 1
