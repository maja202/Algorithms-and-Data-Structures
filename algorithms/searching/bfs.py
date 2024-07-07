from collections import deque

def bfs(graph, start):
    visited = set()
    to_visit = deque([start])
    
    visited.add(start)
    
    while to_visit:
        node = to_visit.popleft()
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                to_visit.append(neighbor)

        
graph = {
    0: [1, 2], 
    1: [2], 
    2: [3], 
    3: [1, 2]
}
bfs(graph, 0)
