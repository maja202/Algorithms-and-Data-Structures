def dfs_iterative(graph, start):
    visited = set()
    to_visit = [start]
    result = []
    
    while to_visit:
        node = to_visit.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            to_visit.extend(reversed(list(graph[node])))
        
    print(result)
    
            visited: 0

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs_iterative(graph, '0')
