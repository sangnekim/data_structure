import collections

def bfs(graph, start):
    visited = set([start])
    queue = collections.deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex, end = ' ')
        nbr = graph[vertex] - visited
        for v in nbr:
            visited.add(v)
            queue.append(v)
