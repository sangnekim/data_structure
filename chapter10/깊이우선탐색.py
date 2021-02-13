def dfs(graph, start, visited = set()):
    if start not in visited:
        visited.add(start)
        print(start, end = ' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)
