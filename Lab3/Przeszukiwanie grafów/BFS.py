from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            neighbours = graph[vertex]
            queue.extend(neighbours)

graph = {
    '0': ['1', '3'],
    '1': ['4'],
    '2': ['4', '5'],
    '3': ['1'],
    '4': ['3'],
    '5': ['5']
}

start_vertex = '2'
bfs(graph, start_vertex)