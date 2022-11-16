def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '0']),
         '1': set(['2', '0']),
         '2': set(['3','0']),
         '3': set(['3','2']),
         }

dfs(graph, '3')
